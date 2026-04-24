import re
import subprocess
import os
from pathlib import Path

def modify_macro(
    filenumber,
    time_stamp,
    open_index = None,
    save_index = 3,
    macro_index = None,
    macro_name = "Modsplat_autothreshold_updated.ijm",
    imagej_path="C:/Users/WarrenKincaid/Downloads/ij154-win-java8/ImageJ/ImageJ.exe",
):
    """
    Primer
    
    Args -
        filenumber: digit(s); Candice filename file number, #/## in "_T000#" or "_T00##"
        time_stamp: digit(s); time in minutes
        open_index = None
        save_index = None
        macro_name = original macro name to be opened, edited and saved under modified name
        
        Requires path to macro file being modified
        Requires path to ImageJ application
    """
    open_counter = 0
    def open_replace(match):
        nonlocal open_counter
        open_counter += 1

        if open_index is not None and open_counter != open_index +1:
            return match.group(0)
        open_command_to_local = match.group(1)
        T_number = match.group(2)
        closing = match.group(3)
        
        open_instance = match.group(0)
        old_number = int(T_number)
        print(f"\nProcessing line: {original_line[:50]}...")
        print(f" Found number: {old_number}")

        file_num_str = str(filenumber).zfill(4)
        
        return f'{open_command_to_local}{file_num_str}{closing}'
    
    open_pattern = r'(open\(\s*".*?_T0*)(\d+)(\.\w+"\))'
    open_replacement = re.sub(open_pattern, open_replace, open_instance) 
  
    save_counter = 0
    def save_replace(match):
        nonlocal save_counter
        save_counter += 1
          
        if save_index is not None and save_counter != save_index + 1:
            return match.group(0)
        save_command = match.group(1)
        path_to_local = match.group(2)
        T_number = match.group(3)
        suffixes = match.group(4)
        closing = match.group(5)
           
        save_instance = match.group(0)
        def path_splitter(path_match):
            before = path_match.group(4)
            after = path_match.group(5)
            return f"{before}{insert_text}{after}"
            
        split_regex = f'(.*?)({split_pattern})(.*)'
        new_path = re.sub(split_regex, path_splitter, full_path)

        return f'{path_to_local}{T_number}{closing}'
        
    with open(macro_path, "r") as file:
        macro_content = file.read()
    modified_content = macro_content
    
    saveAs_pattern = r'(saveAs?\s*\(\s*"[^"]+"\s*,\s*")(.*?T0*)(\d+)([^"]*?)(.\w+"\))'
    saveAs_replacement = r'\1'+r'\2'+ (str(filenumber).zfill(4)+"_"+str(time_stamp)+"min_") +r'\4'+r'\5' #1st instance of saveAs
 
    macro_counter = 0
    def macro_replace(match):
        nonlocal macro_counter
        macro_counter += 1
        
        if macro_index is not None and save_counter != save_index +1:
            return match.group(0)
        basename = match.group(1)
        file_ext = match.group(2)
        new_basename = f"{basename}_{time_stamp}" 
        return f'{new_basename}'+r'\2'

    macro_pattern = r'([^.]*)(.\w+)'
    new_macro_name = re.sub(macro_pattern, match_replace, macro_name)


