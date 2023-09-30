import face_recognition
from imgaug import augmenters as iaa
import cv2
import os,sys
from PIL import Image
import numpy as np

number_of_student = 0
number_of_error = 0

print("======== PREPARING PRE_DATA IS PROCESSING ========\n")
if len(sys.argv) == 2:
    path = sys.argv[1]
files = os.listdir("./pre_data")
number_of_student = 0
total_images = 0

if not os.path.isdir("./_data"):
    os.makedirs("./_data")

for name in files:
    number_of_student +=1
    link = "./pre_data" +"/"+ name
    pictures = os.listdir(str(link))
    print("Folder",name,"is processing")
    number_of_images = 0
    for picture in pictures:
        number_of_images +=1
        total_images +=1
        old_name = str(picture)
        image = face_recognition.load_image_file( link + "/" + old_name)
        face_locations = face_recognition.face_locations(image)

        for face_location in face_locations:
            top, right, bottom, left = face_location
            face_image = image[top:bottom, left:right]
            pil_image = Image.fromarray(face_image)
            #pil_image.show()

            new_name = old_name[:-4] + "_seq0.jpg"
            new_folder1 = "./_data/students/" + name + "/default/"
           #print(new_folder1+new_name)
            new_folder2 = "./_data/students/" + name + "/seq/"
            if not os.path.isdir(new_folder1):
               os.makedirs(new_folder1)
            if not os.path.isdir(new_folder2):
               os.makedirs(new_folder2)
            pil_image.save(new_folder1+new_name)
    if number_of_images !=0:
        print("Number of images inside folder",name, ":",number_of_images,"\n")
    else:
        print("Folder",name,"is empty !","\n")
print("Number of students : ", number_of_student, ", total images :",total_images)
print("\n======== PREPARING PRE_DATA IS FINISHED ========\n\n")

print("======== DATA AUGMENTATION IS PROCESSING ========\n")

def after_seq(x):
    if len(sys.argv) == 2:
        path = sys.argv[1]
    files = os.listdir("./_data/students")
    for name in files:
        link = "./_data/students/" + name + "/default/"
        pictures = os.listdir(str(link))
        for picture in pictures:
            imglist = []
            before_seq = str(picture)
            img = cv2.imread(link + "/" + str(picture))
            imglist.append(img)
            images_aug = x.augment_images(imglist)
            #cv2.imshow("new",img)cv2.waitKey(0)cv2.destroyAllWindows()
            after_seq = before_seq[:-9] + "_seq" + str(di) + ".jpg"
            new_folder3 = "./_data/students/" + name + "/seq/"
            if not os.path.isdir(new_folder3):
               os.makedirs(new_folder3)
            cv2.imwrite(new_folder3 + after_seq, images_aug[0])
            #label = new_folder3 + str(name) + ".txt"
            #f= open(label,"w+")
            #with open(label, 'w') as myfile:
                #myfile.write(str(name))

#DATA AUGMENTATION

seq1 = iaa.Sequential(iaa.Crop(px=(8,0,0,32)))

#
seq2 = iaa.Sequential(iaa.Fliplr(0.8))

#
seq3 = iaa.Superpixels(p_replace=0.2)

#add
seq4 = iaa.Add((35, 55), per_channel=0.5)

#gaussian
seq5 = iaa.GaussianBlur(sigma=(0, 4.0))

#sharpen
seq6 = iaa.Sharpen(alpha=1, lightness=1.0)

#additive
seq7 = iaa.AdditiveGaussianNoise(scale=0.1 * 255)

#dropout
seq8 = iaa.Dropout(p=0.1)

#Coarsedropout
seq9 =  iaa.CoarseDropout(p=0.1, size_percent=0.1, min_size=2)

#perspective
seq10 = iaa.PerspectiveTransform(scale=(0.01,0.1))

#perspective2
seq11 = iaa.PerspectiveTransform(scale=(0.1,0.1))

#Elastic
seq12 = iaa.ElasticTransformation(alpha=0.5, sigma=0.2)

list_of_seq = [seq1,seq2,seq3,seq4,seq5,seq6,seq7,seq8,seq9,seq10,seq11,seq12]

number_of_seq = len(list_of_seq)
di = 1
for seq in list_of_seq:
    checking_number = 0
    after_seq(seq)
    di+=1
print("Number of seq :",number_of_seq)


print("Total images after DA:",number_of_seq*total_images)
print("\n======== DATA AUGMENTATION IS FINISHED ========\n\n")
