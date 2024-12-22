import pandas as pd

frd_file_path = "dummy.frd"


def get_undeformed_node_coordinates(frd_file):
    """
    Parse undeformed node locations from an .frd file between specific markers and return it as a DataFrame.
    
    Parameters:
        frd_file (str): Path to the .frd file.
    
    Returns:
        pd.DataFrame: DataFrame with node IDs as index and coordinates (x, y, z) as columns.
    """

    node_data = []
    reading_data = True

    # Open and process the .frd file
    with open(frd_file, 'r') as file:
        for line in file:                      
            if reading_data:
                if line.startswith(" -1"):
                    node_id = line[3:13].strip()  # Extract Node ID (10 characters)
                    x_coord = float(line[13:25].strip())  # Extract x-coordinate (12 characters)
                    y_coord = float(line[25:37].strip())  # Extract y-coordinate (12 characters)
                    z_coord = float(line[37:49].strip())  # Extract z-coordinate (12 characters)
                    
                    node_data.append([node_id, x_coord, y_coord, z_coord])
                if line.startswith(" -3"):
                    break
    # Convert the list to a DataFrame
    df = pd.DataFrame(node_data, columns=['Node ID', 'x', 'y', 'z'])
    # Set 'Node ID' as the index
    df.set_index('Node ID', inplace=True)

    return df


def get_node_deformations(frd_file):
    """
    Parse node deformations data from a .frd file and return it as a DataFrame.
    
    Parameters:
        frd_file (str): Path to the .frd file.
    
    Returns:
        pd.DataFrame: DataFrame with node IDs as index and deformations (dx, dy, dz) as columns.
    """
    start_marker = " -4  DISP        4    1"
    nodeDeformations = []
    reading_data = False

    # Open and process the .frd file
    with open(frd_file, 'r') as file:
        for line in file:
            if start_marker in line:
                reading_data = True
                continue  
            if reading_data:
                if line.startswith(" -1"):
                    node_id = line[3:13].strip()  # Extract Node ID (10 characters)
                    dx = float(line[13:25].strip())  # Extract dx (12 characters)
                    dy = float(line[25:37].strip())  # Extract dy (12 characters)
                    dz = float(line[37:49].strip())  # Extract dz (12 characters)

                    nodeDeformations.append([node_id, dx, dy, dz])
                if line.startswith(" -3"):
                    break
    # Convert the parsed data to a pandas DataFrame
    df = pd.DataFrame(nodeDeformations, columns=['Node ID', 'dx', 'dy', 'dz'])
    # Set 'Node ID' as the index
    df.set_index('Node ID', inplace=True)

    return df


def get_node_stress_tensor(frd_file):
    """
    Parse node deformations data from a .frd file and return it as a DataFrame.
    
    Parameters:
        frd_file (str): Path to the .frd file.
    
    Returns:
        pd.DataFrame: DataFrame with node IDs as index and deformations (dx, dy, dz) as columns.
    """

    start_marker = " -4  STRESS      6    1"
    nodeStresses = []
    reading_data = False
    # Open and process the .frd file
    with open(frd_file, 'r') as file:
        for line in file:
            if start_marker in line:
                reading_data = True
                continue 
            if reading_data:
                if line.startswith(" -1"):
                    node_id = line[3:13].strip()  # Extract Node ID (10 characters)
                    sxx = float(line[13:25].strip())  # Extract sxx (12 characters)
                    syy = float(line[25:37].strip())  # Extract syy (12 characters)
                    szz = float(line[37:49].strip())  # Extract szz (12 characters)
                    
                    sxy = float(line[49:61].strip())  # Extract sxx (12 characters)
                    syz = float(line[61:73].strip())  # Extract syy (12 characters)
                    szx = float(line[73:85].strip())  # Extract szz (12 characters)

                    nodeStresses.append([node_id, sxx, syy, szz, sxy, syz, szx])
                if line.startswith(" -3"):
                    break
    # Convert the parsed data to a pandas DataFrame
    df = pd.DataFrame(nodeStresses, columns=['Node ID', 'sxx', 'syy', 'szz', 'sxy', 'syz', 'szx'])
    # Set 'Node ID' as the index
    df.set_index('Node ID', inplace=True)

    return df


def get_node_strain_tensor(frd_file):
    """
    Parse node deformations data from a .frd file and return it as a DataFrame.
    
    Parameters:
        frd_file (str): Path to the .frd file.
    
    Returns:
        pd.DataFrame: DataFrame with node IDs as index and deformations (dx, dy, dz) as columns.
    """

    start_marker = " -4  TOSTRAIN    6    1"
    nodeStresses = []
    reading_data = False
    # Open and process the .frd file
    with open(frd_file, 'r') as file:
        for line in file:
            if start_marker in line:
                reading_data = True
                continue
            if reading_data:
                if line.startswith(" -1"):
                    node_id = line[3:13].strip()  # Extract Node ID (10 characters)
                    exx = float(line[13:25].strip())  # Extract exx (12 characters)
                    eyy = float(line[25:37].strip())  # Extract eyy (12 characters)
                    ezz = float(line[37:49].strip())  # Extract ezz (12 characters)
                    
                    exy = float(line[49:61].strip())  # Extract exx (12 characters)
                    eyz = float(line[61:73].strip())  # Extract eyy (12 characters)
                    ezx = float(line[73:85].strip())  # Extract ezz (12 characters)
                    # Append parsed data
                    nodeStresses.append([node_id, exx, eyy, ezz, exy, eyz, ezx])
                if line.startswith(" -3"):
                    break
    # Convert the parsed data to a pandas DataFrame
    df = pd.DataFrame(nodeStresses, columns=['Node ID', 'exx', 'eyy', 'ezz', 'exy', 'eyz', 'ezx'])
    # Set 'Node ID' as the index
    df.set_index('Node ID', inplace=True)

    return df


def get_node_forces(frd_file):
    """
    Parse node deformations data from a .frd file and return it as a DataFrame.
    
    Parameters:
        frd_file (str): Path to the .frd file.
    
    Returns:
        pd.DataFrame: DataFrame with node IDs as index and deformations (dx, dy, dz) as columns.
    """

    start_marker = " -4  FORC        4    1"
    nodeForces = []
    reading_data = False
    # Open and process the .frd file
    with open(frd_file, 'r') as file:
        for line in file:
            if start_marker in line:
                reading_data = True
                continue
            if reading_data:
                if line.startswith(" -1"):
                    node_id = line[3:13].strip()  # Extract Node ID (10 characters)
                    Fx = float(line[13:25].strip())  # Extract Fx (12 characters)
                    Fy = float(line[25:37].strip())  # Extract Fy (12 characters)
                    Fz = float(line[37:49].strip())  # Extract Fz (12 characters)

                    nodeForces.append([node_id, Fx, Fy, Fz])
                if line.startswith(" -3"):
                    break
    # Convert the parsed data to a pandas DataFrame
    df = pd.DataFrame(nodeForces, columns=['Node ID', 'Fx', 'Fy', 'Fz'])
    # Set 'Node ID' as the index
    df.set_index('Node ID', inplace=True)

    return df


def combine_dataframes(
    df_undeformed_node_coordinates, 
    df_node_deformations, 
    df_node_stress_tensor, 
    df_node_strain_tensor, 
    df_node_forces
):
    """
    Combine multiple dataframes if they have the same length.

    Parameters:
    - df_undeformed_node_coordinates: DataFrame of undeformed node coordinates.
    - df_node_deformations: DataFrame of node deformations.
    - df_node_stress_tensor: DataFrame of nodal stress tensor components.
    - df_node_strain_tensor: DataFrame of nodal strain tensor components.
    - df_node_forces: DataFrame of nodal forces.

    Returns:
    - DataFrame: Combined dataframe if lengths are equal.
    - None: If lengths are not equal, prints a message and returns None.
    """
    lengths = [
        len(df_undeformed_node_coordinates),
        len(df_node_deformations),
        len(df_node_stress_tensor),
        len(df_node_strain_tensor),
        len(df_node_forces)
    ]

    if all(length == lengths[0] for length in lengths):
        df_results = pd.concat([
            df_undeformed_node_coordinates,
            df_node_deformations,
            df_node_stress_tensor,
            df_node_strain_tensor,
            df_node_forces
        ], axis=1)

        print("\n---------------------------------------------------------------------\n" + 
              "DataFrames combined successfully!\tDataframe Name = 'df_results'\n" + 
              "---------------------------------------------------------------------" )

        print("\n\n*************************************************************************\n" + 
              f"*\tdf_results contains these informations for : {lengths[0]} nodes.\t*\n" + 
              "*\t\t-Undeformed Node Coordinates; x, y, z\t\t\t*\n" + 
              "*\t\t-Node Deformations; dx, dy, dz\t\t\t\t*\n" + 
              "*\t\t-Nodal Stress Tensor; sxx, syy, szz, sxy, syz, szx\t*\n" + 
              "*\t\t-Nodal Strain Tensor; exx, eyy, ezz, exy, eyz, ezx\t*\n" + 
              "*\t\t-Nodal Forces; Fx, Fy, Fz.\t\t\t\t*\n" + 
              "*************************************************************************\n")
        
        # export_csv(df_results)

        return df_results
    else:
        print("The lengths of the dataframes are not equal. Please check the data.")
        print(f"Lengths: {lengths}")
        return None


def export_csv(df_results):
    """
    Export a dataframe to a CSV file with error handling.

    Parameters:
    - df_results: DataFrame to export.
    """

    output_csv_path = frd_file_path.replace(".frd", ".csv")

    try:
        df_results.to_csv(output_csv_path, index=False)
        print("-----------------------------------------------------------------------------------------\n" + 
              f">>> Combined dataframe successfully exported to: {output_csv_path}\n" + 
              "-----------------------------------------------------------------------------------------\n")
    except Exception as e:
        print(f"\nExport failed: {e}\n")



# RUN FUNCTIONS
# df_undeformed_node_coordinates = get_undeformed_node_coordinates(frd_file_path)
# print('\n>> Undeformed Node Coordinates are packed in: df_undeformed_node_coordinates\n')
# df_node_deformations = get_node_deformations(frd_file_path)
# print('>> Node Deformations(displacements) are packed in: df_node_deformations\n')
# df_node_stress_tensor = get_node_stress_tensor(frd_file_path)
# print('>> Node Stress Tensors are packed in: df_node_stress_tensor\n')
# df_node_strain_tensor = get_node_strain_tensor(frd_file_path)
# print('>> Node Strain Tensors are packed in: df_node_strain_tensor\n')
# df_node_forces = get_node_forces(frd_file_path)
# print('>> Nodal Forces are packed in: df_node_forces\n')

# df_results = combine_dataframes(
#     df_undeformed_node_coordinates,
#     df_node_deformations,
#     df_node_stress_tensor,
#     df_node_strain_tensor,
#     df_node_forces
# )

