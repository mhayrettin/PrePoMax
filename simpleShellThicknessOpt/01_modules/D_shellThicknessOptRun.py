#libs
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
from A_INP_FILE_GENERATOR_MODULE import INPFileGenerator
from B_AUTOMATED_MULTI_RUN_MODULE import CalculiXRunner
from C_getResultsFromFRD import get_node_deformations as getNodeDef

#init parameters
base_file_path = r'simpleShellThicknessOpt\02_baseModelFile\shell_7_parts_base_static.inp'
resultsDirectory = r'simpleShellThicknessOpt\03_results'
ccx_executable = r'C:\\Users\\CalculiX\\bin\\ccx\\ccx213.exe'
number_of_cores = 4

#thickness starters
thicknessStarter = ['1', '1', '1', '1', '1', '1', '1']
currentThicknesses = thicknessStarter
defHistory = []
thicknessHistory = []

#increments and Step Sizes
increment_step = .5  # Define how much to increment each thickness value
maxIterations = 100  # Number of iterations
deformationLimit = 2  # Deformation limit in mm
maxDef = deformationLimit + 1   # just for initialization of while loop > deformationLimit

#INP Generator Initialization
inpGeneratorClass = INPFileGenerator(base_file_path, resultsDirectory, ccx_executable, number_of_cores)

#OPTIMIZATION LOOP
while maxDef > deformationLimit and len(defHistory) < maxIterations:
    currentThicknesses = [str(float(currentThicknesses[i]) + increment_step) for i in range(7)]
    file_name = inpGeneratorClass.generate_new_inp_file(new_values = currentThicknesses, file_index = len(defHistory))
    print(f">> File Generated: {file_name}")
    thicknessHistory.append(float(currentThicknesses[0]))
    calculix_runner = CalculiXRunner(resultsDirectory, ccx_executable, [file_name], number_of_cores)
    calculix_runner.run()
    print(f">> CalculiX Run Completed for {file_name}")

    frd_path = resultsDirectory + '\\' + file_name + '.frd'
    maxDef = getNodeDef(frd_path)['dy'].max()
    defHistory.append(maxDef)
    print("\n**************************************")
    print(f">> Maximum dy deformation for {file_name}")
    print("--------------------------------------")
    print(f">> dyMax = {maxDef}")
    print("**************************************")


#RESULTING THICKNESS AND DEFORMATION
print('\n\n>> All CalculiX runs completed successfully!\n' + 
      f">> Final Thickness:\t{thicknessHistory[-1]}\n" + 
      f">> Final Deformation:\t{defHistory[-1]}\n")


#PLOT
fig, ax1 = plt.subplots()
final_thickness = thicknessHistory[-1]
final_deformation = defHistory[-1]

ax1.annotate(f'Final Deformation: {final_deformation:.2f}', xy=(len(defHistory)-1, final_deformation), 
             xytext=(len(defHistory)-1, final_deformation + 10),
             arrowprops=dict(facecolor='blue', shrink=0.05),
             fontsize=10, color='blue')

ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis

ax2.annotate(f'Final Thickness: {final_thickness:.2f}', xy=(len(thicknessHistory)-1, final_thickness), 
             xytext=(len(thicknessHistory)-1, final_thickness + 0.5),
             arrowprops=dict(facecolor='red', shrink=0.05),
             fontsize=10, color='red')
color = 'blue'
ax1.set_xlabel('Iteration')
ax1.set_ylabel('Deformation', color=color)
ax1.plot(defHistory, color=color)
ax1.set_ylim(0, 25)
ax1.tick_params(axis='y', labelcolor=color)

color = 'red'
ax2.set_ylabel('Thickness', color=color)
ax2.plot(thicknessHistory, color=color)
ax2.tick_params(axis='y', labelcolor=color)
ax2.set_ylabel('Thickness', color=color)
ax1.axhline(y=deformationLimit, color='lightgreen', linestyle='--', label=f'Deformation Limit: {deformationLimit}')
ax1.text(len(defHistory)*.3, deformationLimit*2, f'Deformation Limit: {deformationLimit} [mm]', fontsize=10, color='lightgreen')
ax1.legend()
ax2.plot(thicknessHistory, color=color)

fig.tight_layout()  # to ensure the right y-label is not slightly clipped
plot_path = os.path.join(resultsDirectory, 'AAA_thickness_optimization_plot.png')
fig.savefig(plot_path)
print(f"\n>> Plot saved to {plot_path}")

plt.show()

