from yattag import Doc, indent
from PIL import Image
import os

print("======== PREPARING XML IS PROCESSING ========\n")

def making_xml(link_of_image, name_of_image,name_of_student,label,width): # WIDTH = HEIGHT nen chi can lay 1
    doc, tag, text = Doc().tagtext()

    with tag('annotation'):
        with tag('folder'):
            text('THESIS2019')  #NAME OF FOLDER
        with tag('filename'):
            text(name_of_image)  #NAME OF IMAGE
        with tag('path'):
            text(link_of_image) #LINK OF IMAGE
        with tag('source'):
            with tag('database'):
                text('Unknown')
        with tag('size'):
            with tag('width'):
                text(str(width)) #FIXED
            with tag('height'):
                text(str(height)) #FIXED
            with tag('depth'):
                text(3)
        with tag('segmented'):
                text(0)
        with tag('object'):
            with tag('name'):
                text(label) #LABEL
            with tag('pose'):
                text('Unspecified')
            with tag('truncated'):
                text('1')
            with tag('difficult'):
                text('0')
            with tag('bndbox'):
                with tag('xmin'):
                    text('0')        #FIXED = 0
                with tag('ymin'):
                    text('0')        #FIXED = 0
                with tag('xmax'):
                    text(str(width))    #FIXED  = WIDTH
                with tag('ymax'):
                    text(str(width)) #FIXED = HEIGHT

    result = indent( doc.getvalue(), indentation = ' '*4, newline = '\r\n')
    #print(result)
    name = './_data/students/'+name_of_student+"/seq/"+name_of_image[:-4] + ".xml"
    f= open(name,"w+")
    with open(name, 'w') as myfile:
        myfile.write(result)
files = os.listdir("./_data/students/")
for name in files:
    link = "./_data/students/"+ name +"/seq/"
    images = os.listdir(link)
    number_of_xml = 0
    for image in images:
        if "xml" not in image :
            link_of_image =  link + str(image)
            im = Image.open(link_of_image)
            width, height = im.size
    #print("image : ",str(image), "|" , "width : ",width, " height : ",height)  height = width
            making_xml(link_of_image,str(image),str(name), name, width)
            number_of_xml +=1
    print("Successfully making XML files for :",name,"folder, number of xml :",number_of_xml)
print("\n======== PREPARING XML IS FINISHED ========\n")
