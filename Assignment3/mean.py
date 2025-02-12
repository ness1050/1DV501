import statistics
import os 

def mean_(lst):
    lst = []
    x = statistics.mean(A_list)
    return lst

def std_(lst):
    lst = statistics.stdev(A_list)
    return lst

def file_to_int_list(path, separator):
    int_list = []
    
    if path is not dict:
        print("no such file")
    else:
        with open(path, 'r', encoding = "utf-8") as file_:
            for line in file_:
                for i in line.split(separator):
                    int_list.append(int(i))
        return int_list


Path_1 = '/10000_integers/file_10000integers_A.txt'
Path_2 = '/10000_integers/file_10000integers_B.txt'

A_list = file_to_int_list(Path_1,',')
B_List = file_to_int_list(Path_2,':')
print(f'Mean: {mean_(A_list)}')
print(f'Standard_divison: {std_(A_list)}')
print(mean_(B_List))
print(std_(B_List))