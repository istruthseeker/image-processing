import distutils.util
from distutils import dir_util
import shutil
import os

print("\n======== PREPARING IMAGES IS PROCESSING ========\n")

link = "./_data/students/"
files = os.listdir("./_data/students")

if not os.path.isdir("./input/image/test"):
    os.makedirs("./input/image/test")
    print("Test folder is made.")
if not os.path.isdir("./input/image/train"):
    os.makedirs("./input/image/train")
    print("Train folder is made.")

IMAGES = './input/image'
for name in files:
    distutils.dir_util.copy_tree(link + str(name)+"/seq/",IMAGES)
    print(name," folder is copied.")


#10% for testing and 90% for training

files = os.listdir("./_data/students/")
number_of_test = number_of_train = 0
for name in files:
    seq = os.listdir("./_data/students/"+name+"/seq")
    for file in seq:
        link_of_image = "./_data/students/"+name+"/seq/"+file
        if "1_seq1" in file:
            shutil.copy2(link_of_image, "./input/image/test")
            number_of_test +=1
        else:
            shutil.copy2(link_of_image, "./input/image/train")
            number_of_train +=1
print("\nNumber of testing image :",number_of_test,", Number of training images :",number_of_train,"\nPercent of tesing image :",number_of_test/(number_of_test+number_of_train)*100,"%")
print("\n======== PREPARING IMAGES IS FINISHED ========\n")
