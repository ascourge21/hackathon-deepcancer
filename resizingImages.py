"""
    here I'll try to save each mile resized in the correct way
"""


import dicom
from matplotlib import pyplot as plt
from os import listdir
from os.path import isfile, join, isdir
import numpy as np
import cv2

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


def resize_image(im_array):
    dim = [512, 512, 110]
    orig_size = im_array.shape[2]
    ref_slices = np.sort(np.random.choice(range(orig_size), dim[2], False))

    im_resized = np.zeros(dim)
    for ri in range(len(ref_slices)):
        if ri == len(ref_slices)-1:
            im_resized[:, :, ri] = np.mean(im_array[:, :, ref_slices[ri]:orig_size], axis=2)
        else:
            im_new = np.mean(im_array[:, :, ref_slices[ri]:ref_slices[ri + 1]], axis=2)
            im_resized[:, :, ri] = im_new

    return im_resized

count = 0
for dir_n in range(len(all_dirs)):
    # dir_n = list(np.random.choice(20, 1))
    print(count)
    count += 1
    im_array = np.zeros([512, 512, len(all_dirs[dir_n])]).astype('float32')

    for f in all_dirs[dir_n]:
        plan = dicom.read_file(src + '/' + dir_names[dir_n] + '/' + f)
        im = rescale_image(plan.pixel_array)
        im_array[:, :, plan.InstanceNumber-1] = im.astype('float32')

    im_reshaped = resize_image(im_array)
    print(im_array.shape)
    print(im_reshaped.shape)
    print()

    np.save('data_resized' + str(dir_n), im_reshaped)


