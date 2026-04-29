import re
import subprocess
import os
from pathlib import Path
import imagej

imagej_path = "C:/Users/WarrenKincaid/Downloads/ij154-win-java8/ImageJ/ImageJ.exe"
proc_directory = "C:/Users/WarrenKincaid/git/notebook_wk_hanlab/ImageJProcessing/"

def modify_macro(
    filenumber,
    time_stamp,
    trial_number,
    save_configs = None,
    macro_file = "Modsplat_autothreshold_updated.ijm",
):
    """
    Primer
    
    Args -
        filenumber: digit(s); Candice filename file number, #/## in "_T000#" or "_T00##"
        time_stamp: digit(s); time in minutes
        save_configs: List of dicts for each saveAs instance, eg:
            [
                {'suffix': '_edit1'},           # 1st saveAs
                {'suffix': '_edit2'},           # 2nd saveAs
                {'suffix': '_edit3'},           # 3rd saveAs
            ]
        macro_file = original macro name to be opened, edited and saved under modified name
        
        Requires path to macro file being modified
    """
    with open(macro_file, "r") as file:
        macro_content = file.read()
    
    file_num_str = f"{int(filenumber):04d}"
    time_stamp_str = str(time_stamp)

    open_counter = 0
    open_pattern = r'(open\(\s*".*?_T)(\d+)(\.\w+"\);)'

    def open_replace(match):
        nonlocal open_counter
        open_counter += 1
        
        format_prefix = match.group(1)
        T_number = match.group(2)
        file_ext = match.group(3)

        original_line = match.group(0)
        print(f"\nProcessing open() line: {original_line[:80]}...")
        print(f"    Found number: {T_number}")
        print(f"    Replacing with: {file_num_str}")

        return f'{format_prefix}{file_num_str}{file_ext}'
    
    modified_macro = re.sub(open_pattern, open_replace, macro_content)
    
    if save_configs is None:
        save_configs = [
                {'suffix': f'_{time_stamp_str}min_setscale'},           # 1st save
                {'suffix': f'_{time_stamp_str}min_setred'},             # 2nd save
                {'suffix': f'_{time_stamp_str}min_trhd-im_ws'}   # 3rd save
            ]
    
    save_counter = 0
    saveAs_pattern  = r'(saveAs\s*\(\s*"[^"]+"\s*,\s*")(.*?T)(\d+)([^"]*?)(.\w+"\);)'
    
    def saveAs_replace(match):
        nonlocal save_counter
        save_counter += 1
        
        config_idx = min(save_counter - 1, len(save_configs) - 1)
        config = save_configs[config_idx]

        save_command = match.group(1)
        format_prefix = match.group(2)
        T_number = match.group(3)
        original_insertions = match.group(4)
        file_ext = match.group(5)

        original_line = match.group(0)
        new_number = file_num_str
        extension_instance = config['suffix']
        print(f"\nProcessing saveAs() instance #{save_counter}, line: {original_line[:80]}...")
        print(f"    Found number: {T_number}")
        print(f"    Replacing with: {new_number}")
        print(f"    Original suffixes: '{original_insertions}'")
        print(f"    Replacing with: '{extension_instance}'")

        return f'{save_command}{format_prefix}{new_number}{extension_instance}{file_ext}'
    
    modified_macro = re.sub(saveAs_pattern, saveAs_replace, modified_macro)

    print(f"\n{'='*50}\n")
    print(f"Modified macro summary:")
    print(f"    File number used: {file_num_str}")
    print(f"    Time stamp used: {time_stamp_str}min")
    print(f"    Number of saveAs instances modified: {save_counter}")
    print(f"\n{'='*50}\n")
    
    if trial_number == 1:
        trial_folder = "Tre_PVA_Images/03_13_24_trial1/"
    if trial_number == 2:
        trial_folder = "Tre_PVA_Images/12_12_23_trial2/"
    if trial_number == 3:
        trial_folder = "Tre_PVA_Images/03_13_24_trial3/"

    output_file = macro_file.replace('.ijm', f'_{time_stamp_str}min.ijm')
    output_path = f'{trial_folder}{output_file}'
    print(f"The local path for the modified macro is:\n {output_path}\n")
    # This path needs to be the same as the output path used below
    with open(output_path, "w") as file:
        file.write(modified_macro)
    
    print(f"Modified {save_counter} saveAs instances")
    return modified_macro

# I now want to loop this for filenumbers 1, 4, 8, 12, 
filenumbers = [1, 4, 8, 12, 16, 20, 24]
timestamps = [5, 20, 40, 60, 80, 100, 120]
target_pairs = list(zip(filenumbers, timestamps))



New_macro = modify_macro(
    filenumber = 1,
    time_stamp = 5,
    trial_number = 1,
    )

ij = imagej.init(imagej_path, headless=False)

# Full modified_macro_path
new_macro_path = r'C:\Users\WarrenKincaid\git\notebook_wk_hanlab\ImageJProcessing\Tre_PVA_Images\03_13_24_trial1\Modsplat_autothreshold_updated_5min.ijm'



