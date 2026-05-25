import re
import subprocess
import os
from pathlib import Path
import pandas as pd

# Want script capable of taking "*_grey.tif" from first half of processing

def generate_results_macro(
    filenumber,
    time_stamp,
    trial_number,
    threshold_method = "Intermodes",  # default to Intermodes,
    saveAs_configs = None,
    selectIm_configs = None,
    results_macro_file = f"ModSplat_ResultsMacro.ijm",
):
    """
    Primer
    ----
    Args - 
        filenumber:
        time_stamp:
        trial_number:
        .
        .
        .

    """
    with open(results_macro_file, "r") as file:
        results_macro = file.read()
    
    file_num_str  = f"{int(filenumber):04d}"
    time_stamp_str = str(time_stamp)
    trial_num_str = str(trial_number)

    if trial_number == 1:
        trial_folders = r"Gly_PVA_Images/03_04_24_trial1/"
    if trial_number == 2:
        trial_folders = r"Gly_PVA_Images/03_14_24_trial2/"
    if trial_number == 3:
        trial_folders = r"Gly_PVA_Images/03_14_24_trial3/"
    
    if threshold_method == "Intermodes":
        trhd_str = "im"
    if threshold_method == "Huang2":
        trhd_str = "h2"
    if threshold_method == "Otsu":
        trhd_str = "ot"
    if threshold_method == "RenyiEntropy":
        trhd_str = "re"
    
    open_counter = 0
    open_pattern = r'(open\(\s*".*?ImageProcessing\/)(.*?_trial\d+\/)(.*?\/T)(\d+)(.*?_grey)(\.\w+"\);)'

    def open_result(match):
        nonlocal open_counter
        open_counter += 1

        open_suffix = f"_{time_stamp_str}min_trhd-{trhd_str}_ws_grey"

        open_command = match.group(1)
        trial_dir_outer = match.group(2)
        trial_dir_inner_T = match.group(3)
        T_number = match.group(4)
        original_suffixes = match.group(5)
        file_exten = match.group(6)
        
        original_line = match.group(0)
        print(f"\nProcessing open() line: {original_line[:80]}")
        print(f"    Found trial: {trial_dir_outer[4:]}")
        print(f"    Found T number: {T_number}")
        print(f"    Found threshold method used to be: {original_suffixes[6:]}")
        print(f"    Replacing with trial: {trial_folders[4:]}")
        print(f"    and updated T number: {file_num_str}")
        print(f"    and updating threshold method to be: {threshold_method}")

        return f'{open_command}{trial_folders}{trial_dir_inner_T}{file_num_str}{open_suffix}{file_exten}'
    
    modified_macro = re.sub(open_pattern, open_result, results_macro)
    
    if saveAs_configs is None:
        saveAs_configs = [
                {'filetype': 'Results', 'suffix': f'Summary_T{file_num_str}_{time_stamp_str}min_trial{trial_num_str}'},                         # saveAs instances 1, Summary.csv
                {'filetype': 'Tiff', 'suffix': f'drawing_T{file_num_str}_{time_stamp_str}min_trial{trial_num_str}'},                            # saveAs instances 2, Drawing of Outlines
                {'filetype': 'Results', 'suffix': f'Results_T{file_num_str}_{time_stamp_str}min_trial{trial_num_str}'},                        # saveAs instance 3, Results.csv
                {'filetype': 'Tiff', 'suffix': f'T{file_num_str}_{time_stamp_str}min_trhd-{trhd_str}_ws_grey_trial{trial_num_str}_proc'},       # saveAs instances 4, final image (after threshold and "Analyze Particles..")
                {'filetype': 'Tiff', 'suffix': f'AreaDistribution_T{file_num_str}_{time_stamp_str}min_trial{trial_num_str}'},                   # saveAs instance 5, Area Distribution image
                {'filetype': 'Results', 'suffix': f'AreaDistribution_T{file_num_str}_{time_stamp_str}min_trial{trial_num_str}_list'},           # saveAs instance 6, Area Distribution list
            ] 
    
    saveAs_counter = 0
    saveAs_pattern = r'(saveAs\(")([^"]+)("\s*, \s*".*?ImageJProcessing\/)(.*?_trial\d+\/)(.*?T)(\d+)([^"]*?)(\.\w+"\);)'
    
    def saveAs_results(match):
        nonlocal saveAs_counter
        saveAs_counter += 1

        config_idx = min(saveAs_counter - 1, len(saveAs_configs) - 1)
        config = saveAs_configs[config_idx]

        saveAs_func_prefix = match.group(1)
        saveAs_type = match.group(2)        # "Results" or "Tiff", group itself not including quotes
        base_directory = match.group(3)
        trial_directories = match.group(4)
        autoproc_T_literal = match.group(5)
        T_number = match.group(6)
        original_insertions = match.group(7)
        file_exten = match.group(8)

        original_line = match.group(0)
        filesave_insertion = config['filetype']
        suffixes_insertion = config['suffix']
        print(f"\nProcessing saveAs() instance #{saveAs_counter}, line: {original_line[:80]}")
        print(f"    Original file type: {saveAs_type}")
        print(f"    Original trial number: {trial_directories[4:]}")
        print(f"    Original T number: {T_number}")
        print(f"    Original extensions: {original_insertions}")
        print(f"    Replacing file type with: {filesave_insertion}")
        print(f"    Replacing with trial number: {trial_folders[4:]}")
        print(f"    Replacing with T number: {file_num_str}")
        print(f"    Modifying extensions to be: {suffixes_insertion}")
        
        return f'{saveAs_func_prefix}{filesave_insertion}{base_directory}{trial_folders}{autoproc_T_literal}{file_num_str}{suffixes_insertion}{file_exten}'

    modified_macro = re.sub(saveAs_pattern, saveAs_results, modified_macro)

    selectIm_counter = 0
    selectIm_pattern = r'(selectImage\(\s*"T)(\d+)(.*?_grey)(\.\w+"\);)'

    def selectImage_results(match):
        nonlocal selectIm_counter
        selectIm_counter += 1
        
        selectIm_suffix = f"_{time_stamp_str}min_trhd-{trhd_str}_ws_grey"

        selectImage_prefix = match.group(1)
        T_number = match.group(2)
        original_suffixes = match.group(3)
        file_exten = match.group(4)

        original_line = match.group(0)
        print(f"\nProcessing selectImage() instance #{selectIm_counter}, line: {original_line[:80]}")
        print(f"    Original T number: {T_number}")
        print(f"    at the time and with the threshold method: {original_suffixes}")
        print(f"    Replacing with T number: {file_num_str}")
        print(f"    and with suffixes: {selectIm_suffix}")

        return f'{selectImage_prefix}{file_num_str}{selectIm_suffix}{file_exten}'

    modified_macro = re.sub(selectIm_pattern, selectImage_results, modified_macro)

    print(f"\n{'='*50}\n")
    print(f"Modified macro summary:")
    print(f"    Trial folders used: {trial_folders}")
    print(f"    File number used: {file_num_str}")
    print(f"    Time stamp used: {time_stamp_str}min")
    print(f"    Threshold method used: {threshold_method}")
    print(f"    Number of saveAs instances modified: {saveAs_counter}")
    print(f"\n{'='*50}\n")
    
    output_file = results_macro_file.replace('.ijm', f'_{time_stamp_str}min.ijm')
    output_path = f'{trial_folders}{output_file}'
    print(f"The local path for the modified macro is:\n {output_path}\n")
    # This path needs to be the same as the output path used below
    with open(output_path, "w") as file:
        file.write(modified_macro)
    
    print(f"\nModified {open_counter} open() instances")
    print(f"Modified {saveAs_counter} saveAs instances")
    print(f"Modified {selectIm_counter} selectImage instances")
    
    return modified_macro

# I now want to examine this for filenumbers 1, 4, 8, 12, 20, 24 and their corresponding times for all 3 trials
filenumbers = [1, 4, 8, 12, 16, 20, 24]
timestamps = [5, 20, 40, 60, 80, 100, 120]
trials = [1, 2, 3]

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
    generate_results_macro(
        filenumber = row['filenumber'],
        time_stamp = row['time_stamp'],
        trial_number = row['trial_number'],
    )
    


