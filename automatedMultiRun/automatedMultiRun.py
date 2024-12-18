import subprocess
import os
import time


# DEFINE .INP FILES FOLDER LOCATION
working_directory = "C:\\Users\\ABCDEF\\Desktop\\Analysis\\"

# DEFINE THE PATH TO THE CALCULIX EXECUTABLE
ccx_executable = "C:\\Users\\ABCDEF\\Desktop\\Calculix\\bin\\ccx\\ccx213.exe"

# ADD YOUR .INP FILE NAMES WITHOUT .INP EXTENSIONS.
inp_files = ["StaticAnalysisBase_Moment_MODIFIED_1", 
             "StaticAnalysisBase_Moment_MODIFIED_2", 
             "StaticAnalysisBase_Moment_MODIFIED_3"]

# EDIT FOR NUMBER OF PROCESSORS YOU WANT TO USE FOR RUNS.
numberOfCores = 4



tStartTotal = time.time()

print("\n\n>> Running Operations Starting...")

for input_file in inp_files:
    print(f"\n>> Running CalculiX for input file: {input_file}")

    tStartCycle = time.time()

    command = [ccx_executable, "-i", input_file, "-t", str(numberOfCores)]
    
    try:
        result = subprocess.run(command, cwd=working_directory, check=True, capture_output=True, text=True)
        print(f">> CalculiX ran successfully for {input_file}!")
        print(">> Output:")
        print(result.stdout)  # Standard output from CalculiX
        print(">> Errors (if any):")
        print(result.stderr)  # Standard error output from CalculiX
    except subprocess.CalledProcessError as e:
        print(f">> Error while running CalculiX for {input_file}:")
        print(e.stderr)

    deltaTimeCycle = time.time() - tStartCycle
    print(f'\n>> Elaspsed time for this run = {deltaTimeCycle} [s]')
    
    print("-------------------------------------------------------------------------------------------------------------------\n")  # Print a separator between runs

deltaTimeTotal = time.time() - tStartTotal

print("\n****************************************\n>> All CalculiX run's have completed! <<\n****************************************")
print(f"\n>> Total elapsed time for runs = {deltaTimeTotal} [s] <<\n")

