import os
import shutil

path = input("Enter your path: ")

files = os.listdir(path)

for i in files:
    file_name , extension = os.path.splitext(i)
    extension_1 = extension[1:]

    folder_path = path+"\\"+extension_1

    if os.path.exists(folder_path):
        shutil.move(path + "\\" +i, path+"\\"+ extension_1 + "\\" +i)
        print("Done")
    else:
        os.makedirs(folder_path)
        shutil.move(path + "\\" +i, path+"\\"+ extension_1 + "\\" +i)
        print("Done")

