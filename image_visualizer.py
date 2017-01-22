import dicom
from matplotlib import pyplot as plt
from os import listdir
from os.path import isfile, join, isdir
import numpy as np
from pygaze import eyetracker


src = '/Users/muhammadkhan/Desktop/hackathon-deepcancer/sample_images/'

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

curr_pos = 0
def flip_image(e):
    global curr_pos

    if e.key == "right":
        curr_pos = curr_pos + 1
    elif e.key == "left":
        curr_pos = curr_pos - 1
    else:
        return
    curr_pos = curr_pos % im_array.shape[2]
    ax.cla()
    ax.imshow(im_array[:,:,curr_pos], cmap='gray')
    fig.canvas.draw()

low_bnd = -800
up_bnd = 1200
#for dir_n in range(len(all_dirs)):
dir_n = 0
im_array = np.zeros([512, 512, len(all_dirs[dir_n])]).astype('float32')
for f in all_dirs[dir_n]:
    plan = dicom.read_file(src + '/' + dir_names[dir_n] +  '/' + f)
    im = plan.pixel_array
    im[im < low_bnd] = low_bnd
    im[im > up_bnd] = up_bnd
    im2 = (im - im.min())/(im.max() - im.min())
    #print(plan.InstanceNumber)
    im_array[:, :, plan.InstanceNumber-1] = im.astype('float32')
        
#tracker = eyetracker.EyeTracker(None)
fig = plt.figure()
fig.canvas.mpl_connect('key_press_event', flip_image)
ax = fig.add_subplot(111)
ax.imshow(im_array[:,:,0], cmap='gray')
plt.show()
np.save('data' + str(dir_n), im_array)
