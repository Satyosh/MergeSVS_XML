#! /usr/bin/python 

import glob
import linecache as lc
import re

i = 0
k = 1
user=[]
file_handler=[]

# output file name
f = open("marge.xml","w")

# get list of xml files
filelist = glob.glob("./input/*.xml")


# open one file to get master header.
# Which defines the resolution of images.
master_file = open(filelist[0],"r").readlines()
master_header = master_file[0]    # header of xml file
master_footer = master_file[-1]   # footer of xml file

f.write(master_header)

for file in filelist:
    tmp2 = open(file,"r")
    user.append(tmp2.readlines())

for i in range(len(filelist)):
    for j in range(2,len(user[i])):
        target_line= lc.getline(filelist[i],j)
        target_re = re.sub('Annotation Id="[0-9]+"', 'Idnum',target_line)
        Id_tmp = 'Annotation Id="'+str(k)+'"'
        if(re.search('Idnum',target_re)):
            target_Id = target_re.replace("Idnum",Id_tmp)
            k+=1
        else:
            target_Id = target_re

        f.write(target_Id)
        f.write("\n")
lc.clearcache()

f.write(master_footer)
f.close
