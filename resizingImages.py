"""
    here I'll try to save each mile resized in the correct way
"""


import dicom
from matplotlib import pyplot as plt
from os import listdir
from os.path import isfile, join, isdir
import numpy as np

src = '/Users/nripesh/Downloads/sample_images/'

# find the number of files in each folder
dir_names = []
all_dirs = []
dir_length = []
for folder in listdir(src):
    if isdir(join(src, folder)):
        dir_files = []
        for file in listdir(join(src, folder)):
            if isfile(join(src, folder, file)):
                # print(file)
                dir_files.append(file)
        print("number of files in folder: " + str(len(dir_files)))
        all_dirs.append(dir_files)
        dir_length.append(len(dir_files))
        dir_names.append(folder)



def rescale_image(im):
    low_bnd = -800
    up_bnd = 1200

    im[im < low_bnd] = low_bnd
    im[im > up_bnd] = up_bnd
    im2 = (im - im.min()) / (im.max() - im.min())

    return im2


for dir_n in range(0, 0):
# for dir_n in range(len(all_dirs)):
    im_array = np.zeros([512, 512, len(all_dirs[dir_n])]).astype('float32')

    for f in all_dirs[dir_n]:
        plan = dicom.read_file(src + '/' + dir_names[dir_n] +  '/' + f)
        im = rescale_image(plan.pixel_array)
        im_array[:, :, plan.InstanceNumber-1] = im.astype('float32')

        # plt.imshow(im, cmap='gray')
        # plt.show()
        # plt.waitforbuttonpress()

    # plt.imshow(im_array[:, :, 50], cmap='gray')

