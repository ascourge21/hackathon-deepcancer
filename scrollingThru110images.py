"""
    vissualizing to make notes by radiologist
"""

import numpy as np
from matplotlib import pyplot as plt
from os import listdir
from os.path import isfile, join, isdir

# get list of folder/npy names
src = '/Users/nripesh/Downloads/sample_images/'

# find the number of files in each folder
dir_names = []
all_dirs = []
dir_length = []
for folder in listdir(src):
    if isdir(join(src, folder)):
        dir_names.append(folder)
        print(folder)


# for i in range(20):
data_no = 14
im_array = np.load(dir_names[data_no] + '.npy')

# initial position
curr_pos = 0


def flip_image(e, im_array):
    global curr_pos

    if e.key == "right":
        curr_pos += 1
    elif e.key == "left":
        curr_pos -= 1
    else:
        return
    curr_pos = curr_pos % im_array.shape[2]
    ax.cla()
    ax.imshow(im_array[:, :, curr_pos], cmap='gray')
    fig.canvas.draw()
    print('data_is: ' + dir_names[data_no] + ', current pos is: ' + str(curr_pos))

fig = plt.figure()
fig.canvas.mpl_connect('key_press_event', lambda event: flip_image(event, im_array))
ax = fig.add_subplot(111)
ax.imshow(im_array[:, :, curr_pos], cmap='gray')
plt.show()