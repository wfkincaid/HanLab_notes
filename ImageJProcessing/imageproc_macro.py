import re
import subprocess
import os
from pathlib import Path
import pandas as pd

# imagej_path = "C:/Users/WarrenKincaid/Downloads/ij154-win-java8/ImageJ/ImageJ.exe"
# proc_directory = "C:/Users/WarrenKincaid/git/notebook_wk_hanlab/ImageJProcessing/"

def modify_macro(
    filenumber,
    time_stamp,
    trial_number,
    save_configs = None,
    selectIm_color_configs = None,
    macro_file = f"Modsplat_autothreshold_updated_um_thrshd.ijm",
):
    """
    Primer
    
    This function modifies a text-based .ijm macro file to be run in imageJ
    
    It opens a defined image file in the local saved Candice's 

    ----

    Args -
        filenumber: digit(s); Candice filename file number, #/## in "_T000#" or "_T00##"
        time_stamp: digit(s); time in minutes of image corresponding with the file's image number ('filenumber')
        trial_number: digit(s); trial number in file name used as other folder for all files
        save_configs: None; this becomes set to a dictionary for each saveAs instance, eg:
            [
                {'suffix': '_edit1'},           # 1st saveAs
                {'suffix': '_edit2'},           # 2nd saveAs
                {'suffix': '_edit3'},           # 3rd saveAs
            ]
        selectim_configs = None; this becomes set to a dictionary
        macro_file = original macro name to be opened, edited and saved under
        modified name, currently set to the base macro .ijm file for the
        initial automated processing of an image to reach an image which is
        successfully color split, despeckled, masked with the 'Intermodes'
        threshold, and watershed along with the scale initially set for the
        necessary ice crystal grey-fill selection step
                
        Requires path to macro file being modified
    """
    with open(macro_file, "r") as file:
        macro_content = file.read()
            
    file_num_str = f"{int(filenumber):04d}"
    time_stamp_str = str(time_stamp)

    if trial_number == 1:
        trial_folders = r"Tre_PVA_Images/03_13_24_trial1/"
        process_number = r"405"
    if trial_number == 2:
        trial_folders = r"Tre_PVA_Images/12_12_23_trial2/"
        process_number = r"337"
    if trial_number == 3:
        trial_folders = r"Tre_PVA_Images/03_13_24_trial3/"
        process_number = r"406"

    open_counter = 0of save_configs is None:
        save_configs = [
                {'suffix': f'_{time_stamp_str}min_setscale'},                       # 1st saveAs
                {'suffix': f'_{time_stamp_str}min_setred'},                         # 2nd saveAs
                {'suffix': f'_{time_stamp_str}min_setred_contrast'},                 # 3rd saveAs
                {'suffix': f'_{time_stamp_str}min_setred_contrast_trshdmosaic'},     # 4th saveAs 
                {'suffix': f'_{time_stamp_str}min_trhd-im_ws'},                      # 5th saveAs
            ]

    open_pattern = r'(open\(\s*".*?ImageJProcessing\/)(.*?_trial\d+\/)(.*?Process\_)(\d+)(\_T)(\d+)(\.\w+"\);)'

    def open_replace(match):
        nonlocal open_counter
        open_counter += 1
        
        format_prefix = match.group(1)
        trial_dir_outer = match.group(2)
        trial_dir_inner = match.group(3)
        proc_number = match.group(4)
        T_literal = match.group(5)
        T_number = match.group(6)
        file_ext = match.group(7)

        original_line = match.group(0)
        print(f"\nProcessing open() line: {original_line[:80]}...")
        print(f"    Found trial: {trial_dir_outer[6:]}")
        print(f"    Which has process number: {proc_number}")
        print(f"    and T number: {T_number}")
        print(f"    Replacing with trial number: {trial_folders[6:]}...")
        print(f"    Which has process number: {process_number}")
        print(f"    And the new T number: {file_num_str}")
        
        return f'{format_prefix}{trial_folders}{trial_dir_inner}{process_number}{T_literal}{file_num_str}{file_ext}'
    
    modified_macro = re.sub(open_pattern, open_replace, macro_content)
    
    if save_configs is None:
        save_configs = [
                {'suffix': f'_{time_stamp_str}min_setscale'},                       # 1st saveAs
                {'suffix': f'_{time_stamp_str}min_setred'},                         # 2nd saveAs
                {'suffix': f'_{time_stamp_str}min_setred_contrast'},                 # 3rd saveAs
                {'suffix': f'_{time_stamp_str}min_setred_contrast_trshdmosaic'},     # 4th saveAs 
                {'suffix': f'_{time_stamp_str}min_trhd-im_ws'},                      # 5th saveAs
            ]
    
    save_counter = 0
    saveAs_pattern = r'(saveAs\s*\(\s*"[^"]+"\s*,\s*".*?ImageJProcessing\/)(.*?_trial\d+\/)(.*?T)(\d+)([^"]*?)(.\w+"\);)'

    def saveAs_replace(match):
        nonlocal save_counter
        save_counter += 1
        
        config_idx = min(save_counter - 1, len(save_configs) - 1)
        config = save_configs[config_idx]

        save_command_prefix = match.group(1)
        trial_dir = match.group(2)
        T_dir_outer = match.group(3)
        T_number = match.group(4)
        original_insertions = match.group(5)
        ext_closing = match.group(6)
        
        original_line = match.group(0)
        new_number = file_num_str
        extension_instance = config['suffix']
        print(f"\nProcessing saveAs() instance #{save_counter}, line: {original_line[:80]}...")
        print(f"    Original trial number: {trial_dir[6:]}")
        print(f"    with T number of: {T_number}")
        print(f"    Replacing with trial: {trial_folders[6:]}")
        print(f"    and T number: {new_number}")
        print(f"    Original suffixes: '{original_insertions}'")
        print(f"    Replacing with: '{extension_instance}'")

        return f'{save_command_prefix}{trial_folders}{T_dir_outer}{new_number}{extension_instance}{ext_closing}'
    
    modified_macro = re.sub(saveAs_pattern, saveAs_replace, modified_macro)

    if selectIm_color_configs is None:
        selectIm_color_configs = [
                {'suffix': f'_{time_stamp_str}min_setscale-1.tif (red)"'}, # red generated 1st
                {'suffix': f'_{time_stamp_str}min_setscale-1.tif (green)"'}, # green generated 2nd
                {'suffix': f'_{time_stamp_str}min_setscale-1.tif (blue)"'}, # blue generated 3rd
            ]
    
    selectIm_counter = 0
    selectIm_pattern = r'(selectImage\(\s*"T)(\d+)(\_\d+min\_setscale\-1\.tif\s*\(\w+\)")(\s*\);)'

    def selectIm_replace(match):
        nonlocal selectIm_counter
        selectIm_counter += 1

        config_idx = min(selectIm_counter - 1, len(selectIm_color_configs) - 1)
        config = selectIm_color_configs[config_idx]

        select_command = match.group(1)
        T_number = match.group(2)
        filename_color_strclose = match.group(3)
        line_close = match.group(4)

        original_line = match.group(0)
        new_number = file_num_str
        color_suffix_instance = config['suffix']
        print(f"\nProcessing selectImage() instance #{selectIm_counter}, line: {original_line[:80]}...")
        print(f"    Found number: {T_number}")
        print(f"    Replacing with: {new_number}")
        print(f"    Original suffixes: '{filename_color_strclose}'")
        print(f"    Replacing with: '{color_suffix_instance}'")

        return f'{select_command}{new_number}{color_suffix_instance}{line_close}'

    modified_macro = re.sub(selectIm_pattern, selectIm_replace, modified_macro)

    selectIm_th_counter = 0
    selectIm_th_pattern = r'(selectImage\(\s*"T)(\d+)(\_\d+min\_setred_contrast\.tif")(\s*\);)'
    
    def selectIm_th_replace(match):
        nonlocal selectIm_th_counter
        selectIm_th_counter += 1

        selectIm_command = match.group(1)
        T_number = match.group(2)
        filename_ext = match.group(3)
        line_close = match.group(4)
        
        original_line = match.group(0)
        new_number = file_num_str
        new_extension = f'_{time_stamp_str}min_setred_contrast.tif"'
        print(f"\nProcessing selectImage() line: {original_line[:30]}")
        print(f"    Found T number: {T_number}")
        print(f"    Replacing with: {new_number}")
        print(f"    Found this extension: {filename_ext}")
        print(f"    Replacing with: {new_extension}")
        
        return f'{selectIm_command}{new_number}{new_extension}{line_close}'
    
    modified_macro =  re.sub(selectIm_th_pattern, selectIm_th_replace, modified_macro)

    print(f"\n{'='*50}\n")
    print(f"Modified macro summary:")
    print(f"    Trial folders used: {trial_folders[6:]}")
    print(f"    File number used: {file_num_str}")
    print(f"    Time stamp used: {time_stamp_str}min")
    print(f"    Number of selectImage (color) instances modified: {selectIm_counter}")
    print(f"    Number of saveAs instances modified: {save_counter}")
    print(f"\n{'='*50}\n")
    
    output_file = macro_file.replace('.ijm', f'_{time_stamp_str}min.ijm')
    output_path = f'{trial_folders}{output_file}'
    print(f"The local path for the modified macro is:\n {output_path}\n")
    # This path needs to be the same as the output path used below
    with open(output_path, "w") as file:
        file.write(modified_macro)
    
    print(f"Modified {selectIm_counter} selectImage instances")
    print(f"Modified {save_counter} saveAs instances")
    
    return modified_macro

# I now want to loop this for filenumbers 1, 4, 8, 12, 20, 24 and their corresponding times
filenumbers = [1, 4, 8, 12, 16, 20, 24]
timestamps = [5, 20, 40, 60, 80, 100, 120]
trials = [1, 2, 3]

# If you just want to generate one macro file
# New_macro = modify_macro(
#    filenumber = 1,
#    time_stamp = 5,
#    trial_number = 1,
#    )

# ij = imagej.init(imagej_path, headless=False)

# Full modified_macro_path - this needs to match the pattern of output_path in the function above?

def create_expt_dataframe(
    file_numbers,
    time_stamps,
    trial_numbers
):
    """
    Create a DataFrame for better tracking for each set of desired filenumbers,
    timestamps, and trials for better experiment tracking
    """
    fnum_list = file_numbers
    ts_list = time_stamps
    trial_list = trial_numbers
    data = []

    for trial in trial_list:
        for fnum, ts in zip(fnum_list, ts_list):
            data.append({
                'trial_number': trial,
                'filenumber': fnum,
                'time_stamp': ts,
                'run_id': f"T{trial}_File{fnum}_{ts}min"
            })

    df = pd.DataFrame(data)
    
    return df

expt_df = create_expt_dataframe(
    file_numbers = filenumbers,
    time_stamps = timestamps,
    trial_numbers = trials,
    )

print(f"\n{'='*50}\n")
print(f"DataFrame looks like:")
print(expt_df.head(10))
print(f"\n{'='*50}\n")

for _, row in expt_df.iterrows():
    modify_macro(
        filenumber = row['filenumber'],
        time_stamp = row['time_stamp'],
        trial_number = row['trial_number'],
    )
