import subprocess
import time

class CalculiXRunner:
    def __init__(self, working_directory, ccx_executable, inp_files, number_of_cores=4):
        self.working_directory = working_directory
        self.ccx_executable = ccx_executable
        self.inp_files = inp_files
        self.number_of_cores = number_of_cores

    def run(self):
        tStartTotal = time.time()
        # print("\n\n>> Running Operations Starting...")

        for input_file in self.inp_files:
            # print(f"\n>> Running CalculiX for input file: {input_file}")
            tStartCycle = time.time()

            command = [self.ccx_executable, "-i", input_file, "-t", str(self.number_of_cores)]
            try:
                result = subprocess.run(command, cwd=self.working_directory, check=True, capture_output=True, text=True)
                # print(f">> CalculiX ran successfully for {input_file}!")
                # print(">> Output:")
                # print(result.stdout)  # CalculiX standard output
                # print(">> Errors (if any):")
                # print(result.stderr)  # CalculiX error output
            except subprocess.CalledProcessError as e:
                print(f">> Error while running CalculiX for {input_file}:")
                print(e.stderr)

            deltaTimeCycle = time.time() - tStartCycle
            print(f'\n>> Elapsed time for this run = {deltaTimeCycle} [s]')
            # print("-------------------------------------------------------------------------------------------------------------------\n")

        deltaTimeTotal = time.time() - tStartTotal
        # print("\n****************************************\n>> All CalculiX run's have completed! <<\n****************************************")
        # print(f"\n>> Total elapsed time for runs = {deltaTimeTotal} [s] <<\n")
