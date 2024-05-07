import os

def convert_all_chn_to_txt(folder_path):
    try:
        # List all files in the folder
        files = os.listdir(folder_path)
        
        for file in files:
            if file.endswith('.chn'):
                chn_file_path = os.path.join(folder_path, file)
                txt_file_path = os.path.join(folder_path, file[:-4] + '.txt')
                
                with open(chn_file_path, 'r', encoding='utf-8') as f:
                    chn_content = f.read()
                
                with open(txt_file_path, 'w', encoding='utf-8') as f:
                    f.write(chn_content)
                
                print(f"Converted '{file}' to '{file[:-4]}.txt'")
        
        print("Conversion of all .chn files successful!")
    except Exception as e:
        print("An error occurred:", str(e))

# Example usage:
convert_all_chn_to_txt('chnfiles/')
