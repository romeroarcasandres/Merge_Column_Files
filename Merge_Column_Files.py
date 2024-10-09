import os
import pandas as pd
from tkinter import Tk, filedialog, simpledialog, messagebox

# Function to prompt the user to select a directory
def select_directory():
    Tk().withdraw()  # Hides the Tkinter GUI window
    directory = filedialog.askdirectory(title="Select the directory with files")
    return directory

# Function to load files based on extension and return a DataFrame
def load_files(directory, extensions):
    all_data = pd.DataFrame()
    
    for file in os.listdir(directory):
        if file.endswith(extensions):
            file_path = os.path.join(directory, file)
            
            if file.endswith('.csv'):
                data = pd.read_csv(file_path)
            elif file.endswith('.txt'):
                data = pd.read_csv(file_path, delimiter='\t')
            elif file.endswith('.xlsx'):
                data = pd.read_excel(file_path)
            
            all_data = pd.concat([all_data, data], ignore_index=True)
    
    return all_data

# Function to prompt the user for the desired output formats using Tkinter
def get_output_formats():
    Tk().withdraw()  # Hides the Tkinter GUI window
    valid_formats = {'xlsx', 'txt', 'csv'}
    
    # First attempt to prompt for formats
    formats_input = simpledialog.askstring(
        "Output Formats", 
        "Enter the desired output formats separated by a comma (e.g., xlsx, txt, csv):"
    )
    
    if formats_input:
        formats = formats_input.replace(" ", "").split(",")  # Remove spaces and split by comma
        selected_formats = [fmt for fmt in formats if fmt in valid_formats]
        
        if selected_formats:
            return selected_formats
        
        # If first input is invalid, show message and re-prompt
        print("The format is not valid. Please select a valid format: xlsx, txt, csv")
        formats_input = simpledialog.askstring(
            "Output Formats", 
            "The format is not valid. Please select a valid format: xlsx, txt, csv"
        )
        
        if formats_input:
            formats = formats_input.replace(" ", "").split(",")
            selected_formats = [fmt for fmt in formats if fmt in valid_formats]
            
            if selected_formats:
                return selected_formats
    
    # Default to csv if invalid formats are entered twice or no input
    messagebox.showerror("Error", "No valid formats selected. Defaulting to .csv")
    return ['csv']

# Function to ask the user whether to remove duplicate rows
def ask_remove_duplicates():
    Tk().withdraw()  # Hides the Tkinter GUI window
    response = messagebox.askyesno("Remove Duplicates", "Do you want to remove identical (duplicated) rows?")
    return response

# Function to save the merged data in multiple formats
def save_files(data, directory, formats):
    for file_format in formats:
        output_path = os.path.join(directory, f"merged_files.{file_format}")
        
        if file_format == 'csv':
            data.to_csv(output_path, index=False)
        elif file_format == 'txt':
            data.to_csv(output_path, sep='\t', index=False)
        elif file_format == 'xlsx':
            data.to_excel(output_path, index=False)
        
        print(f"Merged file saved as: {output_path}")

# Main function
def main():
    # Step 1: Prompt user for directory
    directory = select_directory()
    
    # Step 2: Load and merge files
    extensions = ('.xlsx', '.txt', '.csv')
    merged_data = load_files(directory, extensions)
    
    # Step 3: Ask the user whether to remove duplicated rows
    remove_duplicates = ask_remove_duplicates()
    
    if remove_duplicates:
        merged_data = merged_data.drop_duplicates()  # Remove identical rows
    
    # Step 4: Get output formats from the user (supports multiple formats)
    output_formats = get_output_formats()
    
    # Step 5: Save the merged file in selected formats
    save_files(merged_data, directory, output_formats)

if __name__ == "__main__":
    main()
