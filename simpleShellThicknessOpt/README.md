# `simpleShellThicknessOpt` : Example shell thickness static loading deformation optimization.

## What are those things?
### `\\01_modules\\A_INP_FILE_GENERATION.py`
> This script changes shell thicknesses of a base analysis .inp file and saves it as `base_i.inp` for each iteration.
### `\\01_modules\\B_AUTOMATED_MULTI_RUN_MODULE.py`
> This script runs your analysis files in CalcuLix (.inp's for this case)
>> Check `main\\automatedMultiRun\\automatedMultiRun.py` if you like. This is so similar to it or maybe exactly same i did not check recently.
### `\\01_modules\\C_getResultsFromFRD.py`
> This parses some nodal results from .FRD result files. Only `dy: deformation along y axis` used for this case.
>> Check `main\\getResultsFromFRD\\getResultsFromFRD.py` if you like. Similar things, i just do not parse stresses etc. for this case because only deformations were needed.
### `\\01_modules\\D_shellThicknessOptRun.py`
> This script gets other needed modules, creates initialization needed, and also contains optimization loop (believe it or not there is an extremely high level optimization algorithm in it...)
## ----------------------------------------------------------------------
## Model Explanation
### As you can see, there is a plate similar to a cantilever beam. One end is fixed and there is a vertical laod applied on the other end.
![image](https://github.com/user-attachments/assets/1c05936b-32a3-4a26-9375-e0009c9a5393)
### There are 7 shell sections on this plate in order to control thicknesses of shell elements to get the desired deformation.
![image](https://github.com/user-attachments/assets/c3ab8e8b-e020-4ee0-ae34-85d33972f4ee)
![image](https://github.com/user-attachments/assets/9bb911d8-7921-41c4-8f0b-faef984c7eef)
### `Material` is not important for us now. I don't even remember what did i assisgned.
## ----------------------------------------------------------------------
### General Loop is very simple here:
![image](https://github.com/user-attachments/assets/9d2ad079-fc67-44cc-a4e5-e8d3cced49f6)
## ----------------------------------------------------------------------
### Final result histories saved as .png file.
![AAA_thickness_optimization_plot](https://github.com/user-attachments/assets/080149fc-c980-4ae4-9f31-a2aeece55b74)
## ----------------------------------------------------------------------
## ----------------------------------------------------------------------
# How to Use:
## You may try changing these basically:
### 1) `thicknessStarter` @line#17.
### 2) `incrementStep` @line#23
### 3) `maxIterations` @line#24
### 3) `deformationLimit` @line#25
## or add any other things you like. Play with it.

## If you encounter anything unexpected or have any suggestions, please don't hesitate to reach out to me.
