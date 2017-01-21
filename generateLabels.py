"""
    will search through the large database to find the smaller dataset's labels
"""

from os import listdir, getcwd
from os.path import isfile, join, isdir

src = '/Users/nripesh/Downloads/sample_images/'

# find the number of files in each folder
dir_names = []
all_dirs = []
dir_length = []
for folder in listdir(src):
    if isdir(join(src, folder)):
        dir_names.append(folder)
        print(folder)


# get list of all data
with open(getcwd() + "/stage1_labels.csv") as f:
    content = f.readlines()

folders = []
labels = []
for i in range(1, len(content)):
    x = content[i].strip().split(',')
    folders.append(x[0])
    labels.append(x[1])


# go through and see if dir_names can be found
file = open("labels.txt", 'w')
for i in range(len(dir_names)):
    dir = dir_names[i]
    found = False
    for j in range(len(folders)):
        if folders[j] == dir:
            print("found")
            file.write(dir + ", " + labels[j] + '\n')
            found = True
    if not found:
        print("not found")

file.close()