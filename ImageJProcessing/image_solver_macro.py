import re
import subprocess
import os
from pathlib import Path
import pandas as pd

# Want script capable of taking "*_grey.tif" from first half of processing
# Rearranging for testing for generating results macros

# First: make experimental df

filenumbers = [1, 4, 8, 12, 16, 20, 24]
timestamps = [5, 20, 40, 60, 80, 100, 120]
solutes = ["Glycerol", "Sucrose"]   #, "Trehalose"]

trials_map = {
    "Glycerol": [1, 2, 3],
    "Sucrose": [1, 2, 3, 4],
}

def create_expt_dataframe(
    cosolutes,
    file_numbers,
    time_stamps,
):
    """
    Create a DataFrame for better tracking for each set of desired filenumbers,
    timestamps, and trials for better experiment tracking
    """
    fnum_list = file_numbers
    ts_list = time_stamps
    cosol_list = cosolutes
    data = []

    for sol in cosolutes:
        if sol in trials_map:
            trials = trials_map[sol]
        for trial in trials:
            for fnum, ts in zip(fnum_list, ts_list):
                data.append({
                    'run_id': f"Solute-{sol}_Trial-{trial}_File-T{int(fnum):04d}_{ts}-min",
                    'cosolute': sol,
                    'trial number': trial,
                    'T number': fnum,
                    'time stamp': ts,
                })

    df = pd.DataFrame(data)
    
    return df

expt_df = create_expt_dataframe(
    cosolutes = solutes,
    file_numbers = filenumbers,
    time_stamps = timestamps,
    )

print(f"\n{'='*50}\n")
print(f"The initial DataFrame looks like:")
print(expt_df.head(10))
print(f"\n{'='*50}\n")

# quit()

def determine_proc_methods(
    df, #default to the intended df
):
    """
    Use for determining thresholds used and if watershed applied per processed file
    """
    copy_df = df.copy()

    # "C:/Users/WarrenKincaid/git/notebook_wk_hanlab/ImageJProcessing/Tre_PVA_Images/03_13_24_trial1/AutoProc/T0001_5min_trhd-im_ws_grey.tif"

    copy_df["trial folder"] = None
    
    trial_folder_map = {
        ("Glycerol", 1): r'Gly_PVA_Images/03_04_24_trial1/',
        ("Glycerol", 2): r'Gly_PVA_Images/03_14_24_trial2/',
        ("Glycerol", 3): r'Gly_PVA_Images/03_14_24_trial3/',
        ("Sucrose", 1): r'Suc_PVA_Images/12_01_23_trial1/',
        ("Sucrose", 2): r'Suc_PVA_Images/03_06_24_trial2/',
        ("Sucrose", 3): r'Suc_PVA_Images/03_06_24_trial3/',
        ("Sucrose", 4): r'Suc_PVA_Images/12_08_23_trial4/',
    }
    #   if copy_df["cosolute"] == "Trehalose":
    #       if copy_df["trial number"] == 1:
    #           trial_folder = r'Tre_PVA_Images\/03_13_24_trial1\/'
    #       if copy_df["trial number"] == 2:
    #           trial_folder = r'Tre_PVA_Images\/12_12_23_trial2\/'
    #       if copy_df["trial number"] == 3:
    #           trial_folder = r'Tre_PVA_Images\/03_13_24_trial3\/'

    #    copy_df["trial folder"] = copy_df["trial number"].map(trial_folder)
    

    threshold_map = {
        r'im': "Intermodes",
        r'id': "IsoData",
        r're': "RenyiEntropy",
        r'ot': "Otsu",
        r'h2': "Huang2",
        r'min': "Minimum",
    }
    
    method_lookup = {abv: method for abv, method in threshold_map.items()}
    
    print(f"\n{'='*50}\n")
    print(f"The current DataFrame looks like:")
    print(copy_df.head(10))
    print(f"\n{'='*50}\n")
    
    exten_data = []

    for (cosolute, trial), folder in trial_folder_map.items():
        mask = (copy_df['cosolute'] == cosolute) & (copy_df['trial number'] == trial)
        copy_df.loc[mask, 'trial folder'] = folder
        
        dir_patterns = [
            r'C:/Users/WarrenKincaid/git/notebook_wk_hanlab/ImageJProcessing/',     # Group 1, base directories 
            folder,                                                                         # Group 2, set above
            r'AutoProc/',                                                                # Group 3, inner trial directory
        ]

        directory = f"{''.join(dir_patterns)}"
        print(f"directory is equal to: \n {directory} \n With type of {type(directory)}")
        directory_pat = re.compile(directory)
        print(f"The pattern for directory is equal to: \n {directory_pat} \n With type of {type(directory_pat)}")
        dir_path = Path(directory)
        
        file_groups = r'(T)(\d+)_(\d+)min_trhd-([^_]+)_(ws|no-ws)_grey\.tif'
        #file_suffix = f"_{time_stamp_str}min_trhd-{trhd_str}_{watershed_str}_grey"
        file_pattern = re.compile(file_groups)
        
        for file_path in dir_path.glob("*.tif"):
            match = file_pattern.search(file_path.name)
            if match is None:
                continue  # Skip unmatched files
            if match:
                original_line = match.group(0)
                T_literal = match.group(1)
                T_number = match.group(2)
                time_number = match.group(3)
                threshold_abbrv = match.group(4)
                watershed_abbrv = match.group(5)
                
                file_num = int(T_number)
                print(f"Found T number is: {file_num}, \nFound time is: {time_number}")
                print(f"Found threshold abbreviation: {threshold_abbrv}")
                print(f"Found watershed abbreviation: {watershed_abbrv}")

                if threshold_abbrv in method_lookup:
                    method = method_lookup[threshold_abbrv]
                    exten_data.append({
                            'run_id': f"Solute-{cosolute}_Trial-{trial}_File-T{int(file_num):04d}_{time_number}-min",
                            'method': method,
                            'threshold': threshold_abbrv,
                            'watershed': watershed_abbrv,
                            })

                print(
                    f"---------\n    For solute: {cosolute},"
                    f"\n        trial: {trial},"
                    f"\n        T number: T{T_number},"
                    f"\n        for time: {time_number}min,"
                    f"\n        Updated threshold method: {method},"
                    f"\n        Updated threshold abv: {threshold_abbrv},"
                    f"\n        Updated watershed note: {watershed_abbrv}"
                )
    exten_df = pd.DataFrame(exten_data)
    print(exten_df.head(10))

    final_df = pd.merge(copy_df, exten_df, on='run_id', how='left')

    return final_df

updated_df = determine_proc_methods(expt_df)

print(f"\n{'='*50}\n")
print(f"The final DataFrame looks like:")
print(updated_df.head(15))
print("........")
print(updated_df.tail(20))
print(f"\n{'='*50}\n")

def generate_results_macro(
    cosolute,
    trial_number,
    filenumber,
    time_stamp,
    trial_folder,
    threshold,
    watershed,
    saveAs_configs = None,
    results_macro_file = f"ModSplat_ResultsMacro_new.ijm",
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
    
    trial_num_str = str(trial_number)
    file_num_str  = f"{int(filenumber):04d}"
    time_stamp_str = str(time_stamp)
    
    open_counter = 0
    open_pattern = r'(open\(\s*".*?ImageJProcessing\/)(.*?_trial\d+\/)(.*?\/T)(\d+)(_\d+min_trhd)(.*?_grey)(\.\w+"\);)'

    def open_result(match):
        nonlocal open_counter
        open_counter += 1

        new_time_suffix = f"_{time_stamp_str}min_trhd"
        new_trhd_suffix = f"-{threshold}_{watershed}_grey"

        open_command = match.group(1)
        trial_dir_outer = match.group(2)
        trial_dir_inner_T = match.group(3)
        T_number = match.group(4)
        time_suffix = match.group(5)
        trhd_suffixes = match.group(6)
        file_exten = match.group(7)
        
        original_line = match.group(0)
        print(f"\nProcessing open() line: {original_line[:80]}")
        print(f"    Found trial: {trial_dir_outer[4:]}")
        print(f"    Found T number: {T_number}")
        print(f"    Found time: {time_suffix[3:]}")
        print(f"    Found threshold method and watershed used to be: {trhd_suffixes[5:]}")
        print(f"    Replacing with trial: {trial_folder}")
        print(f"    and updated T number: {file_num_str}")
        print(f"    and updating time to be: {time_stamp_str}")
        print(f"    and updating threshold and watershed to be: {threshold} and {watershed}")

        return f'{open_command}{trial_folder}{trial_dir_inner_T}{file_num_str}{new_time_suffix}{new_trhd_suffix}{file_exten}'
    
    modified_macro = re.sub(open_pattern, open_result, results_macro)
    
    if saveAs_configs is None:
        saveAs_configs = [
                {'filetype': 'Results', 'suffix': f'Summary_T{file_num_str}_{time_stamp_str}min_trial{trial_num_str}'},                         # saveAs instances 1, Summary.csv
                {'filetype': 'Tiff', 'suffix': f'drawing_T{file_num_str}_{time_stamp_str}min_trhd-{threshold}_{watershed}_trial{trial_num_str}_proc'},                            # saveAs instances 2, Drawing of Outlines
                {'filetype': 'Results', 'suffix': f'Results_T{file_num_str}_{time_stamp_str}min_trial{trial_num_str}'},                        # saveAs instance 3, Results.csv
                {'filetype': 'Tiff', 'suffix': f'T{file_num_str}_{time_stamp_str}min_trhd-{threshold}_{watershed}_trial{trial_num_str}_proc'},       # saveAs instances 4, final image (after threshold and "Analyze Particles..")
                {'filetype': 'Tiff', 'suffix': f'AreaDistribution_T{file_num_str}_{time_stamp_str}min_trial{trial_num_str}'},                   # saveAs instance 5, Area Distribution image
                {'filetype': 'Results', 'suffix': f'AreaDistribution_T{file_num_str}_{time_stamp_str}min_trial{trial_num_str}_list'},           # saveAs instance 6, Area Distribution list
            ] 
    
    saveAs_counter = 0
    saveAs_pattern = r'(saveAs\(")([^"]+)("\s*, \s*".*?ImageJProcessing\/)(.*?_trial\d+\/)(AutoProc\/)([\w-]+)(\.\w+"\);)'
    
    def saveAs_results(match):
        nonlocal saveAs_counter
        saveAs_counter += 1

        config_idx = min(saveAs_counter - 1, len(saveAs_configs) - 1)
        config = saveAs_configs[config_idx]

        saveAs_func_prefix = match.group(1)
        saveAs_type = match.group(2)        # "Results" or "Tiff", group itself not including quotes
        base_directory = match.group(3)
        trial_directories = match.group(4)
        autoproc = match.group(5)
        base_filename_insertion = match.group(6)
        file_exten = match.group(7)

        original_line = match.group(0)
        filesave_insertion = config['filetype']
        suffixes_insertion = config['suffix']
        print(f"\nProcessing saveAs() instance #{saveAs_counter}, line: {original_line[:80]}")
        print(f"    Original file type: {saveAs_type}")
        print(f"    Original trial number: {trial_directories[4:]}")
        print(f"    Original filename: {base_filename_insertion}")
        print(f"    Replacing file type with: {filesave_insertion}")
        print(f"    Replacing with trial number: {trial_folder}")
        print(f"    Replacing with T number: {file_num_str}")
        print(f"    Modifying extensions to be: {suffixes_insertion}")
        
        return f'{saveAs_func_prefix}{filesave_insertion}{base_directory}{trial_folder}{autoproc}{suffixes_insertion}{file_exten}'

    modified_macro = re.sub(saveAs_pattern, saveAs_results, modified_macro)

    selectIm_counter = 0
    selectIm_pattern = r'(selectImage\(\s*"T)(\d+)(.*?_grey)(\.\w+"\);)'

    def selectImage_results(match):
        nonlocal selectIm_counter
        selectIm_counter += 1
        
        selectIm_suffix = f"_{time_stamp_str}min_trhd-{threshold}_{watershed}_grey"

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
    print(f"    Trial folders used: {trial_folder}")
    print(f"    File number used: {file_num_str}")
    print(f"    Time stamp used: {time_stamp_str}min")
    print(f"    Threshold method used: {threshold}")
    print(f"    Note on watershed: {watershed}")
    print(f"    Number of saveAs instances modified: {saveAs_counter}")
    print(f"\n{'='*50}\n")
    
    output_file = results_macro_file.replace('.ijm', f'_{time_stamp_str}min.ijm')
    output_path = f'{trial_folder}{output_file}'
    print(f"The local path for the modified macro is:\n {output_path}\n")
    # This path needs to be the same as the output path used below
    with open(output_path, "w") as file:
        file.write(modified_macro)
    
    print(f"\nModified {open_counter} open() instances")
    print(f"Modified {saveAs_counter} saveAs instances")
    print(f"Modified {selectIm_counter} selectImage instances")
    
    return modified_macro

for _, row in updated_df.iterrows():
    generate_results_macro(
        cosolute = row['cosolute'],
        trial_number = row['trial number'],
        filenumber = row['T number'],
        time_stamp = row['time stamp'],
        trial_folder = row['trial folder'],
        threshold = row['threshold'],
        watershed = row['watershed'],
    )
    


