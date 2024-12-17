# Extract Results from PrePoMax/CalculiX

## What this code does?
This script helps you to extract and export nodal results from PrePoMax or CalculiX.

## Usage Instructions is Not Needed Actually But..
1. **Generate Result File**  
   After running a simulation with PrePoMax or CalculiX, a result file (`result.frd`) will be generated.

2. **Set the File Path**  
   Provide the path to the `.frd` file in the Python script @line#3 ----> frd_file_path = `"C:\\Users\\RESULT_FILE.frd"`

3. **Run the Script**  
   When you execute the Python code, it will automatically compile nodal results into a pandas DataFrame named "df_results" and also export to `.frd` file path as `.csv` with same name.

## Extractable Data
The following data can be extracted from the result file (`RESULT.frd`) and processed as a pandas DataFrame:

- **Undeformed node coordinates**  
- **Nodal deformations**  
- **Nodal stress tensor components**  
- **Nodal strain tensor components**  
- **Nodal forces**

## If you encounter anything unexpected or have any suggestions, please don't hesitate to reach out to me.
