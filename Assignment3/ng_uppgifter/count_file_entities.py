import os 

def count_directories(dir_path):

    
    no_path = 0
    dir_n = os.scandir(path)

    for entry in dir_n:
        if entry.is_dir():
            print(entry.name)
            no_path += 1
    return no_path


def count_py_file(dir_path):
    
    no_file = 0

    entries = os.scandir(path)

    for entry in entries:
        if entry.is_file():
            print(entry.name)
            no_file +=1
    return no_file
path = os.getcwd()
print(path)
print(f'files: {count_py_file(path)}')
print(f'directories: {count_directories(path)}')




