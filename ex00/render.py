#importing functions and settings variables
import re
settings=open("settings.py","r")
from settings import name
import os

def execute():

    firstname = "John"
    age = "42"
    profession = "King of the world"

    import sys

    #In case of an input error
    if len(sys.argv)!=2:
        print("You have to put one template file as an argument.")
        return
    if "." not in sys.argv[1]:
        print("You have to put one template file as an argument.")
        return
    if sys.argv[1].split(".")[1]!="template":
        print("You have to put one template file as an argument.")
        return

    #If the file appears to be missing or corrupted
    try:
        template_file=open(sys.argv[1],"r+")
    except:
        print("Error: please check the file!")
        return

    #replacing name
    file_string = template_file.read()
    new_string = re.sub(r"{name}", name, file_string)
    template_file.truncate(0)
    template_file.write(new_string)

    #converting file to html
    os.system("mv "+str(sys.argv[1])+" "+str(sys.argv[1].split(".")[0])+".html")

    #write CV
    myCV=open("myCV.template","r+")
    CV_string=myCV.read()
    new_CV = re.sub(r"firstname", firstname, CV_string)
    new_CV = re.sub(r"name", name, new_CV)
    new_CV = re.sub(r"age", age, new_CV)
    new_CV = re.sub(r"profession", profession, new_CV)
    myCV.truncate(0)
    myCV.write(new_CV)

if __name__=="__main__":
    execute()
