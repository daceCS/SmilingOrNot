import io
import PIL.Image
from tkinter import filedialog
import pandas
import numpy as np

from glob import glob

import cv2 # having trouble? file -> settings -> project -> +opencv-python
import matplotlib.pyplot as plt
import pandas as pd

print("Select an image")

# opens up window explorer to get image
# filename = filedialog.askopenfilename(initialdir="/",
#                                       title="Select a File",
#                                       filetypes=(("Text files",
#                                                   "*.png*"),
#                                                  ("all files",
#                                                   "*.*")))
#
# # opens the image
# with open(filename, "rb") as file:
#     img_binary = file.read()

# img = PIL.Image.open(io.BytesIO(img_binary))
# shows the image
# img.show()

import os

smile_faces = []
for dirname, _, filenames in os.walk('./images'):
    for filename in filenames:
        smile_faces.append(os.path.join(dirname, filename))

print(smile_faces[10])

img_mp1 = plt.imread(smile_faces[30])
img_cv2 = cv2.imread(smile_faces[30])

# pd.Series(img_mp1.flatten()).plot(kind="hist",
#                                   bins=50,
#                                   title='Distribution of Pixel Values')
#
# plt.show()
# fig,ax = plt.subplots(figsize=(10,10))
# ax.imshow(img_mp1)
# plt.show()

# fig, axs = plt.subplots(1, 3, figsize=(15, 5))
# axs[0].imshow(img_mp1[:,:,0], cmap='Reds')
# axs[1].imshow(img_mp1[:,:,0], cmap='Greens')
# axs[2].imshow(img_mp1[:,:,0], cmap='Blues')
# axs[0].axis('off')
# axs[1].axis('off')
# axs[2].axis('off')
# plt.show()

img_gray = cv2.cvtColor(img_mp1, cv2.COLOR_RGB2GRAY)
for i in range(0, len(img_gray)):
    print(img_gray[i])
fig, ax = plt.subplots(figsize=(8,8))
ax.imshow(img_gray,cmap='Greys')
ax.axis('off')
ax.set_title("Grey Image")
plt.show()

