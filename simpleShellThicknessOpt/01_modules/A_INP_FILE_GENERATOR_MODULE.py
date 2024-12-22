import os

class INPFileGenerator:
    def __init__(self, base_file_path, new_directory, ccx_executable, number_of_cores=4):
        self.base_file_path = base_file_path
        self.new_directory = new_directory
        self.ccx_executable = ccx_executable
        self.number_of_cores = number_of_cores
        self.generated_files = []

    def generate_new_inp_file(self, new_values, file_index):
        # Yeni dosya yolunu oluştur
        new_file_path = os.path.join(self.new_directory, f'shell_7_parts_static_{file_index}.inp')

        # Ana dosyayı oku
        with open(self.base_file_path, 'r') as file:
            lines = file.readlines()

        # Değerleri değiştir
        for i, line in enumerate(lines):
            if "*Shell section, Elset=set_1, Material=ABS, Offset=0" in line:
                lines[i + 1] = new_values[0] + '\n'
            elif "*Shell section, Elset=set_2, Material=ABS, Offset=0" in line:
                lines[i + 1] = new_values[1] + '\n'
            elif "*Shell section, Elset=set_3, Material=ABS, Offset=0" in line:
                lines[i + 1] = new_values[2] + '\n'
            elif "*Shell section, Elset=set_4, Material=ABS, Offset=0" in line:
                lines[i + 1] = new_values[3] + '\n'
            elif "*Shell section, Elset=set_5, Material=ABS, Offset=0" in line:
                lines[i + 1] = new_values[4] + '\n'
            elif "*Shell section, Elset=set_6, Material=ABS, Offset=0" in line:
                lines[i + 1] = new_values[5] + '\n'
            elif "*Shell section, Elset=set_7, Material=ABS, Offset=0" in line:
                lines[i + 1] = new_values[6] + '\n'

        # Yeni dosyayı kaydet
        os.makedirs(self.new_directory, exist_ok=True)
        with open(new_file_path, 'w') as new_file:
            new_file.writelines(lines)

        # Dosya adını ve dizinini yazdır
        print(f"GENERATED! New .inp file ---> {new_file_path}")

        # Oluşturulan dosya adını listeye ekle
        self.generated_files.append(os.path.splitext(os.path.basename(new_file_path))[0])
        
        return self.generated_files[-1]

    def generate_all_files(self, new_values_lists):
        for index, new_values in enumerate(new_values_lists, start=1):
            self.generate_new_inp_file(new_values, index)

        # Tüm işlemlerin tamamlandığını yazdır
        print("\n**************************************************************\nAll new .inp file generation processes completed.\n**************************************************************")
        return self.generated_files
