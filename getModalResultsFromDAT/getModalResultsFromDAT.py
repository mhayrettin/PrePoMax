import pandas as pd

def parse_eigenvalue_data_from_file(file_path):
    """
    Parses the 'E I G E N V A L U E   O U T P U T' section from a file
    and returns the data as a pandas DataFrame.
    
    Parameters:
        file_path (str): Path to the file containing eigenvalue output data.
    
    Returns:
        pd.DataFrame: A DataFrame containing parsed eigenvalue data.
    """
    with open(file_path, 'r') as file:
        data = file.read()
    
    start_marker = "     E I G E N V A L U E   O U T P U T"
    lines = data.splitlines()
    start_index = next(i for i, line in enumerate(lines) if start_marker in line)
    
    lines = lines[start_index + 6:]
    
    parsed_data = []

    for line in lines:
        if not line.strip():  # Stop if an empty line is encountered
            break
        
        # Parse columns using the specified slicing format
        mode_number = line[0:7].strip()      # First column (7 characters)
        eigenvalue = line[7:23].strip()      # Second column (16 characters)
        freq_real_rad = line[23:39].strip()  # Third column (16 characters)
        freq_hz = line[39:55].strip()        # Fourth column (16 characters)
        freq_imag_rad = line[55:71].strip()  # Fifth column (16 characters)
        
        # Append parsed data as a dictionary
        parsed_data.append({
            "Mode_Number": mode_number,
            "Eigenvalue": eigenvalue,
            "Freq_Real_Rad": freq_real_rad,
            "Freq_Hz": freq_hz,
            "Freq_Imag_Rad": freq_imag_rad,
        })
    
    df = pd.DataFrame(parsed_data)
    
    return df


def parse_participation_factors_from_file(file_path):
    """
    Parses the 'P A R T I C I P A T I O N   F A C T O R S' section from a file
    and returns the data as a pandas DataFrame with meaningful column names.
    
    Parameters:
        file_path (str): Path to the file containing participation factors data.
    
    Returns:
        pd.DataFrame: A DataFrame containing parsed participation factors data.
    """
    with open(file_path, 'r') as file:
        data = file.read()
    
    start_marker = "     P A R T I C I P A T I O N   F A C T O R S"
    lines = data.splitlines()
    start_index = next(i for i, line in enumerate(lines) if start_marker in line)
    
    lines = lines[start_index + 4:]
    
    parsed_data = []

    for line in lines:
        if not line.strip():
            break
        
        mode_number = line[0:7].strip()        
        x_component = line[7:23].strip()       
        y_component = line[23:39].strip()      
        z_component = line[39:55].strip()      
        x_rotation = line[55:71].strip()       
        y_rotation = line[71:87].strip()       
        z_rotation = line[87:103].strip()     
        
        parsed_data.append({
            "PARTICIP_FACT_Mode_Number": mode_number,
            "PARTICIP_FACT_X_Component": x_component,
            "PARTICIP_FACT_Y_Component": y_component,
            "PARTICIP_FACT_Z_Component": z_component,
            "PARTICIP_FACT_X_Rotation": x_rotation,
            "PARTICIP_FACT_Y_Rotation": y_rotation,
            "PARTICIP_FACT_Z_Rotation": z_rotation,
        })
    
    df = pd.DataFrame(parsed_data)
    
    return df


def parse_effective_modal_mass_from_file(file_path):
    """
    Parses the 'E F F E C T I V E   M O D A L   M A S S' section from a file
    and returns the data as a pandas DataFrame with meaningful column names.
    
    Parameters:
        file_path (str): Path to the file containing effective modal mass data.
    
    Returns:
        pd.DataFrame: A DataFrame containing parsed effective modal mass data.
    """
    with open(file_path, 'r') as file:
        data = file.read()
    
    start_marker = "     E F F E C T I V E   M O D A L   M A S S"
    lines = data.splitlines()
    start_index = next(i for i, line in enumerate(lines) if start_marker in line)
    
    lines = lines[start_index + 4:]
    
    parsed_data = []

    for line in lines:
        if line.strip().startswith("TOTAL"):
            mode_number = "TOTAL"
            x_component = line[7:23].strip()
            y_component = line[23:39].strip()
            z_component = line[39:55].strip()
            x_rotation = line[55:71].strip()
            y_rotation = line[71:87].strip()
            z_rotation = line[87:103].strip()
            
            parsed_data.append({
                "EFF_MOD_MASS_Mode_Number": mode_number,
                "EFF_MOD_MASS_X_Component": x_component,
                "EFF_MOD_MASS_Y_Component": y_component,
                "EFF_MOD_MASS_Z_Component": z_component,
                "EFF_MOD_MASS_X_Rotation": x_rotation,
                "EFF_MOD_MASS_Y_Rotation": y_rotation,
                "EFF_MOD_MASS_Z_Rotation": z_rotation,
            })
            break
        
        if not line.strip():
            break
        
        mode_number = line[0:7].strip()          # First column (7 characters)
        x_component = line[7:23].strip()         # Second column (16 characters)
        y_component = line[23:39].strip()        # Third column (16 characters)
        z_component = line[39:55].strip()        # Fourth column (16 characters)
        x_rotation = line[55:71].strip()         # Fifth column (16 characters)
        y_rotation = line[71:87].strip()         # Sixth column (16 characters)
        z_rotation = line[87:103].strip()        # Seventh column (16 characters)
        
        parsed_data.append({
            "EFF_MOD_MASS_Mode_Number": mode_number,
            "EFF_MOD_MASS_X_Component": x_component,
            "EFF_MOD_MASS_Y_Component": y_component,
            "EFF_MOD_MASS_Z_Component": z_component,
            "EFF_MOD_MASS_X_Rotation": x_rotation,
            "EFF_MOD_MASS_Y_Rotation": y_rotation,
            "EFF_MOD_MASS_Z_Rotation": z_rotation,
        })
    
    df = pd.DataFrame(parsed_data)
    
    return df


def parse_total_effective_mass_from_file(file_path):
    """
    Parses the 'T O T A L   E F F E C T I V E   M A S S' section from a file
    and returns the data as a pandas DataFrame with meaningful column names.
    
    Parameters:
        file_path (str): Path to the file containing effective modal mass data.
    
    Returns:
        pd.DataFrame: A DataFrame containing parsed effective modal mass data.
    """
    with open(file_path, 'r') as file:
        data = file.read()
    
    start_marker = "     T O T A L   E F F E C T I V E   M A S S"
    lines = data.splitlines()
    start_index = next(i for i, line in enumerate(lines) if start_marker in line)
    
    lines = lines[start_index + 4:]
    
    parsed_data = []

    for line in lines:
        if not line.strip():
            break
        
        mode_number = line[0:7].strip()  
        x_component = line[7:23].strip() 
        y_component = line[23:39].strip()
        z_component = line[39:55].strip()
        x_rotation = line[55:71].strip() 
        y_rotation = line[71:87].strip() 
        z_rotation = line[87:103].strip()
        
        parsed_data.append({
            "totalEffectiveMass": "totalEffectiveMass",
            "totalEffMass_X_Component": x_component,
            "totalEffMass_Y_Component": y_component,
            "totalEffMass_Z_Component": z_component,
            "totalEffMass_X_Rotation": x_rotation,
            "totalEffMass_Y_Rotation": y_rotation,
            "totalEffMass_Z_Rotation": z_rotation,
        })
    
    df = pd.DataFrame(parsed_data)
    
    return df




def concatenate_dataframes(df1, df2, df3, df4):
    """
    Concatenate three DataFrames along the columns axis.
    
    Parameters:
        df1 (pd.DataFrame): First DataFrame.
        df2 (pd.DataFrame): Second DataFrame.
        df3 (pd.DataFrame): Third DataFrame.
        df4 (pd.DataFrame): Fourth DataFrame.
    
    Returns:
        pd.DataFrame: A new DataFrame resulting from the concatenation.
    """
    concatenated_df = pd.concat([df1, df2, df3, df4], axis=1)
    
    export_csv(concatenated_df)

    return concatenated_df


def export_csv(df_results):
    """
    Export a dataframe to a CSV file with error handling.

    Parameters:
    - df_results: DataFrame to export.
    """

    output_csv_path = file_path.replace(".dat", "_modalResults.csv")

    try:
        df_results.to_csv(output_csv_path, index=False)
        print("-----------------------------------------------------------------------------------------\n" + 
              f">>> Modal Result Dataframe successfully exported to: {output_csv_path}\n" + 
              "-----------------------------------------------------------------------------------------\n")
    except Exception as e:
        print(f"\nExport failed: {e}\n")


file_path = r"C:\\Users\\Analysis-1.dat"

eigenvalue_df = parse_eigenvalue_data_from_file(file_path)
participation_factors_df = parse_participation_factors_from_file(file_path)
effective_modal_mass_df = parse_effective_modal_mass_from_file(file_path)
total_effective_mass_df = parse_total_effective_mass_from_file(file_path)

modalResult_df = concatenate_dataframes(eigenvalue_df, participation_factors_df, effective_modal_mass_df, total_effective_mass_df)
