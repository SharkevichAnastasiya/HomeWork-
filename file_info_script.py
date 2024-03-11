import os
import sys
import logging
from collections import namedtuple 

# Настройка логирования 

logging.basicConfig(filename='file_info.log', level=logging.INFO)

# Опредление обьекта namedtuple для хранения данных о файле в каталоге 

FileInfo = namedtuple('FaleInfo', ['name', 'extension', 'is_directory', 'parent_dir'])

def get_file_info(file_path):
   
    try:
        files_info = []
        for item in os.listdir(file_path):
            full_path = os.path.join(file_path, item)
            name, extension = os.path.splitext(item)

            if os.path.isdir(full_path):
                is_directory = True
            else:
                is_directory = False

            parent_dir = os.path.basename(os.path.dirname(full_path))
            file_info = FileInfo(name=name, extension=extension, is_directory=is_directory, parent_dir=parent_dir)
            files_info.append(files_info)
            logging.info(f'Processed: {item}')

        return files_info
    
    except Exception as e:
        logging.error(f'Error processing {file_path}: {str(e)}')
        return []
    
if __name__== "__main__":
    if len(sys.argv) !=2:
        print("Usage: python script.py <directory_path>")
        sys.exit(1)

    directory_path = sys.argv[1]

    if not os.path.exists(directory_path):
        print("Directory does not exist.")
        sys.exit(1)

    files_info = get_file_info(directory_path)

# Запись информации в текстовый файл 
    
    with open('file_info.txt', 'w') as f:
        for file_info in files_info:
            f.write(f"Name: {file_info.name}nExtension: {file_info.extension}nIs Directory: {file_info.is_directory}nParent Directory: {file_info.parent_dir}nn")

    print("File information saved to file_info.txt.")

