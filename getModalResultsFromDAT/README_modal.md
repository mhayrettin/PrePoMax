# `getModalResultsFromDAT.py` : Extract Modal Results from PrePoMax/CalculiX and export as .csv file.

## What this code does?
This script helps you to extract and export modal results from PrePoMax or CalculiX dat file.

## Usage Instructions is Not Needed Actually But..
1. **Generate Result File**  
   After running a simulation with PrePoMax or CalculiX, a dat file (`result.dat`) will be generated.

2. **Set the File Path**  
   Provide the path to the `.dat` file in the Python script @line#3 ----> `file_path = r"C:\\Users\\Analysis-1.dat"`

3. **Run the Script**  
   When you execute the Python code, it will automatically compile modal results into a pandas DataFrame named "modalResult_df" and also export to `.dat` file path as `_modalResults.csv` with same name.

## Extractable Data
The following data can be extracted from the result file (`Analysis-1.dat`) and processed as a pandas DataFrame:

- **Eigenvalue Output**  
- **Participation Factors**  
- **Effective Modal Mass**  
- **Total Effective Mass**  

## If you encounter anything unexpected or have any suggestions, please don't hesitate to reach out to me.
