import pandas as pd
import os
import skimage.io
import numpy as np
import cv2
from tqdm import tqdm
from functools import reduce

###############################################

def image_threshold(img, threshold):
    

    img_p, img_h, img_w, img_c = img.shape
    result = []
    for i in range(img_p):
        
        image_patch = img[i,:,:,:]
        image_patch = image_patch.reshape(-1, img_c)
        r_image = image_patch[:, 0]
        g_image = image_patch[:, 1]
        b_image = image_patch[:, 2]
    
        r_idx = np.where(r_image < threshold)[0]
        g_idx = np.where(g_image < threshold)[0]
        b_idx = np.where(b_image < threshold)[0]
        all_idx = reduce(np.intersect1d, (r_idx, g_idx, b_idx))
        result.append(len(all_idx))
    return np.array(result)

###############################################

sz = 256
level = 0

target_dir = "/home/daifishba/Project/PANDA/MIL_data/origin_patches/"

train_images_path = "/home/daifishba/Dataset/PANDA/train_images/"
train_masks_path   = "/home/daifishba/Dataset/PANDA/train_label_masks/"



train_csv = pd.read_csv("train_clean.csv")
train_csv = train_csv[train_csv["data_provider"] == "karolinska"]
train_names = list(train_csv["image_id"])



for name in tqdm(train_names):

    image_path = os.path.join(train_images_path, name +".tiff")
    mask_path = os.path.join(train_masks_path, name +"_mask.tiff")


    img = skimage.io.MultiImage(image_path)[level]
    mask  = skimage.io.MultiImage(mask_path)[level]

    shape = img.shape


    pad0,pad1 = (sz - shape[0]%sz)%sz, (sz - shape[1]%sz)%sz

    img = np.pad(img,[[pad0//2,pad0-pad0//2],[pad1//2,pad1-pad1//2],[0,0]],
                        constant_values=255)

    mask = np.pad(mask,[[pad0//2,pad0-pad0//2],[pad1//2,pad1-pad1//2],[0,0]],
                        constant_values=0)
    img = img.reshape(img.shape[0]//sz,sz,img.shape[1]//sz,sz,3)
    img = img.transpose(0,2,1,3,4).reshape(-1,sz,sz,3)

    mask = mask.reshape(mask.shape[0]//sz,sz,mask.shape[1]//sz,sz,3)
    mask = mask.transpose(0,2,1,3,4).reshape(-1,sz,sz,3)
    mask = mask[:,:,:,0]
    
    '''
    # filter out all white pathes
    p_img = 255 - img # inverse
    p_img = np.sum(p_img.reshape(p_img.shape[0], -1), axis=-1) # [num_pathces, HWC]
    _idx = np.where(p_img >= 1)[0]
    img, mask = img[_idx], mask[_idx]

    ratio = sz*sz*0.5
    num_image_black = image_threshold(img, 50)
    _idx = np.where(num_image_black<ratio)[0]
    img, mask = img[_idx], mask[_idx]

    num_image_white = image_threshold((255-img),15)
    _idx = np.where(num_image_white<ratio)[0]
    img, mask = img[_idx], mask[_idx]
    '''
    


    #cap = cv2.VideoCapture(0)
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    video_path = "/home/daifishba/Project/PANDA/MIL_data/videos/" +name+'.mp4'


    output_video = cv2.VideoWriter(video_path, fourcc, 15.0, (sz,  sz))

    patch_folder = os.path.join(target_dir, name)
    if not os.path.exists(patch_folder):
        os.makedirs(patch_folder)

    frame_index = 1
    label = []

    for index, patch in enumerate(img):
        if np.count_nonzero(mask[index]) > (sz*sz*0.5):


            if np.count_nonzero(mask[index]==2)>np.count_nonzero(mask[index]==1):
                output_path = os.path.join(patch_folder, "img_"+ str(frame_index).zfill(5) + ".png")
                skimage.io.imsave(output_path, patch)
                output_video.write(patch)
                frame_index+=1
                label.append(1)

            else:
                output_path = os.path.join(patch_folder, "img_"+ str(frame_index).zfill(5) + ".png")
                skimage.io.imsave(output_path, patch)
                output_video.write(patch)
                frame_index+=1
                label.append(0)


    txt_path = output_path = os.path.join(patch_folder, "label.txt")
    np.savetxt(txt_path, label, fmt='%i')

    #cap.release()
    output_video.release()


