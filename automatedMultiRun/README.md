# `automatedMultiRun.py` : Automated analysis runs for multiple .inp files.

## What this code does?
This script helps you to run multiple analyses sequentially.

## Usage Instructions
1. **Generate `.inp` Files**  
   Generate your analysis files by exporting as `.inp` files. 'analysis_1.inp, analysis_2.inp, analysis_3.inp etc.`

2. **Set Working Directory**  
   Set the path to `.inp` files in the Python script @line#7 ----> `working_directory = "C:\\Users\\ABCDEF\\Desktop\\Analysis\\"`

3. **Set CalculiX Executable Path**  
   Set the path to `ccxVERSION.exe` executable in the Python script @line#10 ----> `ccx_executable = "C:\\Users\\ABCDEF\\Desktop\\Calculix\\bin\\ccx\\ccx213.exe"`

4. **Add Files to Run List**  
   Add .inp file names to list in the Python script @line#13 ---->
   `inp_files = ["analysis_1", "analysis_2", "analysis_3"]"`

5. **Specify Number of Processors You Want to Use**  
   Edit variable 'numberOfCores' in the Python script @line#18 `numberOfCores = 4`

6. **Run the Script**
   When you run the script, it will send `.inp` files one by one to `Calculix` folder.
   You will be able to see elapsed time for each run and also total time for all analysis.

7. **See Result Files**
   Result files are going to be created in the working directory you set @step#2.

**optional**
   You can also use `getResultsFromFRD.py` script to work easily with `nodal stress\strain\force\displacement` results.
   https://github.com/mhayrettin/PrePoMax_CalculiX_OpenSource/tree/main/getResultsFromFRD

## If you encounter anything unexpected or have any suggestions, please don't hesitate to reach out to me.
