#!/usr/bin/env python
# coding: utf-8

# In[6]:


import os
import glob
import shutil


# In[2]:


if not os.path.exists('clevr'):
    os.makedirs('clevr')


# In[3]:


if not os.path.exists('clevr/train'):
    os.makedirs('clevr/train')


# In[4]:


if not os.path.exists('clevr/val'):
    os.makedirs('clevr/val')


# In[5]:


if not os.path.exists('clevr/train/images'):
    os.makedirs('clevr/train/images')


# In[8]:


if not os.path.exists('clevr/val/images'):
    os.makedirs('clevr/val/images')


# In[7]:


train_src_dir = "CLEVR_v1.0/images/train"
train_dst_dir = "clevr/train/images"
for pngfile in glob.iglob(os.path.join(train_src_dir, "*.png")):
    shutil.copy(pngfile, train_dst_dir)


# In[9]:


val_src_dir = "CLEVR_v1.0/images/val"
val_dst_dir = "clevr/val/images"
for pngfile in glob.iglob(os.path.join(val_src_dir, "*.png")):
    shutil.copy(pngfile, val_dst_dir)


# In[11]:


trq_src_dir = "CLEVR_v1.0/questions/CLEVR_train_questions.json"
trq_dst_dir = "clevr/train/questions.json"
shutil.copy(trq_src_dir, trq_dst_dir)


# In[12]:


vq_src_dir = "CLEVR_v1.0/questions/CLEVR_val_questions.json"
vq_dst_dir = "clevr/val/questions.json"
shutil.copy(vq_src_dir, vq_dst_dir)


# In[13]:


trs_src_dir = "CLEVR_v1.0/scenes/CLEVR_train_scenes.json"
trs_dst_dir = "clevr/train/scenes-raw.json"
shutil.copy(trs_src_dir, trs_dst_dir)

vs_src_dir = "CLEVR_v1.0/scenes/CLEVR_val_scenes.json"
vs_dst_dir = "clevr/val/scenes-raw.json"
shutil.copy(vs_src_dir, vs_dst_dir)


# In[ ]:




