"""
 reading dicom

    %% need to think about how to encorporate into existing phillips/seimens/epic interfaces
    %% -600 center, 1500 width
"""

import dicom
from matplotlib import pyplot as plt
from os import listdir
from os.path import isfile, join, isdir
import numpy as np

src = '/Users/nripesh/Downloads/sample_images/'
im1 = 'bf86db180c5768eea526e69e125b06e5.dcm'

# find the number of files in each folder
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

onlyfiles = [f for f in listdir(src) if isfile(join(src, f))]
im_array = np.zeros([512, 512, len(onlyfiles)]).astype('float32')

low_bnd = -800
up_bnd = 1200

for f in onlyfiles:
    plan = dicom.read_file(src + f)

    im = plan.pixel_array
    im[im < low_bnd] = low_bnd
    im[im > up_bnd] = up_bnd
    im2 = (im - im.min())/(im.max() - im.min())

    im_array[:, :, plan.InstanceNumber-1] = im.astype('float32')

    # plt.imshow(im, cmap='gray')
    # plt.show()
    # plt.waitforbuttonpress()

plt.imshow(im_array[:, :, 50], cmap='gray')