# `2_DOF_MASS_SPRING` : 2 Degree of Freedom Mass-Spring System with PrePoMax & CalculiX

## What's that?
### `\\01_2_dof_mass_spring_system.inp`
> Solver deck file is in this folder.

## ----------------------------------------------------------------------
## Model Explanation
### There are 2 cubes represent masses and 2 spring elements attached to these cubes. 
![image](https://github.com/user-attachments/assets/cebf6ee5-f1c1-4069-95d3-49a87c07f231)

## `SPRING1` element can be defined in PrePoMax UI. `SPRING2` and `SPRINGA` elements can not be defined in UI so you have to add them as `CalculiX Keyword`. Yellow spring element that named as `k1` here is `SPRING1` which is defined in PPM UI. 
![image](https://github.com/user-attachments/assets/00500bbe-bcd5-4355-99d0-4107aa002b4e)

## Other Spring element which has `SPRING2` or `SPRINGA` element type will be added as CalculiX keywords.
## 1) `Model-->Edit CalculiX Keywords`
![image](https://github.com/user-attachments/assets/901d7c70-0bd8-4693-a217-6026d5af4b84)

## 2) You need to add 3 things here:
![image](https://github.com/user-attachments/assets/6a10cd0a-dc3e-4158-a612-6d1c92a184e3)

### 2.1) Define Spring Element as `Additional Element` with `elementID, node1_ID, node2_ID`:
![image](https://github.com/user-attachments/assets/eddf46e3-7d06-48b1-8ba5-0ff4256f55d0)
Also adding code text:
#### `*Element,TYPE=SPRINGA,ELSET=ESPRING`
#### `999999,18525,18527`

### 2.2) Define your spring as `Additional Element Set` with `elementID`.
![image](https://github.com/user-attachments/assets/464f31af-d35d-4e9b-bdd4-535eddc9f125)

Also adding code text:
#### `*Elset, Elset = ESPRING`
#### `999999`

### 2.3) Define your spring as `Additional Section` with `Stiffness Value`.
![image](https://github.com/user-attachments/assets/c25e5762-888c-4030-babc-c7ecd6049429)

Also adding code text:
#### `*Spring,ELSET=ESPRING`
#### `0.003`

# `IMPORTANT!`
## Let's say your spring stiffness is 5 N/mm. When you add this `5` value as a keyword YOU HAVE TO ADD A GODDAMN POINT AT THE END OF VALUE. Like `5.` My value already has a decimal here, it's `0.003` `N/mm` but if it was `100 N/mm` so i would write `100.` there.


## 3) That's it. Run your model...
## ----------------------------------------------------------------------

## By the way, the inp file i add here has 2 steps.
1) NORMAL_MODES analysis that calculates `undamped natural frequencies` of mass-spring system.
2) MODAL_DYNAMICS analysis that uses results of NORMAL_MODES analysis as input and calculates time domain response of cubes.
3) There is a time domain force applied to the right cube. It's applied like a shock force in a short duration. _like ultra dummy version of hammer test force application_
![image](https://github.com/user-attachments/assets/ccd0e829-f908-4fc2-98fb-5f2f5dd11a04)

# FINALLY:  
## You can get natural frequencies of 2 dof mass-spring system in step 1. There will be 2 eigenvalues and also 2 natural frequencies and also 2 mode shapes. One of the mode shapes will be in-phase the other one will be out-of-phase.
## You can get time domain response of both cubes in step-2. There is a constant damping ratio applied already as `0.01`. Also do not forget to set proper time increments according to your natural frequencies.

## If you encounter anything unexpected or have any suggestions, please don't hesitate to reach out to me.
