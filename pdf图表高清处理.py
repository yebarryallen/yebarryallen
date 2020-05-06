# -*- coding: utf-8 -*-
"""
Created on Wed May  6 17:40:01 2020

@author: yebarryallen
先要在cmd命令安装 如下
pip install pillow

"""
#锐化
#用法教程：https://zhuanlan.zhihu.com/p/59656703
#https://www.cnblogs.com/Young-shi/p/11478732.html
#https://pillow.readthedocs.io/en/stable/reference/ImageEnhance.html#PIL.ImageEnhance.PIL.ImageEnhance.Contrast
'''
发现先用smooth再用 contrast 效果不错
'''
from PIL import Image
from PIL import ImageFilter
im=Image.open('锐化2.png')
bk=Image.open('timg.jpg')
'''
im_1=im.convert('RGB').filter(ImageFilter.SMOOTH)
im_2=im_1.convert('RGB').filter(ImageFilter.SMOOTH)
im_3=im_2.convert('RGB').filter(ImageFilter.SMOOTH)
im_4=im_3.convert('RGB').filter(ImageFilter.SHARPEN)
'''
smooth=im.convert('RGB').filter(ImageFilter.SMOOTH)
#sharpen=im.convert('RGB').filter(ImageFilter.SHARPEN)
#smoothcover=im.convert('RGB').filter(ImageFilter.UnsharpMask(radius=2, percent=150, threshold=3))



from PIL import ImageEnhance
im2=ImageEnhance.Contrast(smooth).enhance(3)
'''
 这里为处理出来的表格打上背景 使得其更像自己画的一样
'''
im2.thumbnail((497,332),resample=Image.BICUBIC)
#接下来可以进行背景图与高清图的融合
#网址https://blog.csdn.net/zhangziju/article/details/79123275
print(bk.mode,bk.size)
print(im2.mode,im2.size)
#调整背景图的大小 使用box
box = (0,0,424,332)
region = bk.crop(box)
#最后一步 加上背景图
print(bk.mode,bk.size)
print(im2.mode,im2.size)
blend1=Image.blend(im2,region,0.2)



