import os, shutil
path = input("Enter the path of the folder you want to organize: ")
file_name = os.listdir(path)
folder_names = ['csv files', 'text files', 'image files', 'pdf files']
for loop in range(0,2):
    if not os.path.exists(path + folder_names[loop]):
        print(path+folder_names[loop])
        os.makedirs((path+folder_names[loop]))
for file in file_name:
    if ".csv" in file and not os.path.exists(path + "csv files/" + file):
        shutil.move(path + file, path + "csv files/" + file)
    elif ".pdf" in file and not os.path.exists(path + "pdf files/" + file):
        shutil.move(path + file, path + "pdf files/" + file)
    elif ".png" in file and not os.path.exists(path + "image files/" + file):
        shutil.move(path + file, path + "image files/" + file)
    else:
        print("This file type is not included")
