# Merge_Column_Files
This script merges files from a user-selected directory and saves the merged content in multiple formats (CSV, TXT, XLSX). It supports .csv, .txt, and .xlsx file types and allows users to choose output formats as well as the option to remove duplicate rows.

## Overview:
The Merge_Column_Files.py script helps you efficiently merge files within a directory into one, with flexible options for output formats and duplicate row removal. It supports merging files from the following formats:
* CSV
* TXT (tab-separated)
* XLSX (Excel)
  
After merging, the user can choose to save the result in CSV, TXT, and/or XLSX format.

## Requirements
* Python 3
* pandas library (for file handling and data merging)
* tkinter library (for user dialogs and file selection)
* os library (for directory and file path operations)

## Files
Merge_Column_Files.py

## Usage
1. Run the script.
2. A file dialog will prompt you to select a directory containing the files (.csv, .txt, .xlsx) you want to merge.
3. The script reads all compatible files from the directory and merges them into a single dataset.
4. A dialog will ask if you want to remove identical rows (duplicate entries). Choose Yes or No.
5. You can specify one or more output formats (CSV, TXT, XLSX). The dialog allows you to enter these formats in a comma-separated format (e.g., csv, xlsx).
6. The merged file will be saved in the selected formats, in the same directory, with the name merged_files followed by the appropriate file extension(s).

## Example
If you choose to merge .csv and .xlsx files and save the output as csv, the file will be saved as merged_files.csv.

If you select all available formats, the output will be saved as merged_files.csv, merged_files.txt, and merged_files.xlsx.

## Important Notes
* Ensure the files you want to merge are located in the same directory.
* When working with .txt files, the script assumes they are tab-separated.
* If you don't specify any valid output formats, the script defaults to saving as .csv.
* The script supports Excel files with multiple sheets but will only process the first sheet by default.
* The columns will be merged in the order in which the files appear, based on their file names.
* It is recommended that all files have the same number of columns to ensure the output file is consistent and usable.

## License
This project is governed by the CC BY-NC 4.0 license. For comprehensive details, kindly refer to the LICENSE file included with this project.
