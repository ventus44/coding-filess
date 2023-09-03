from PIL import Image, ImageEnhance, ImageFilter
import os

path = r"C:\Users\Thanos\Desktop\coding files\face_rec\pic_test.JPG"

save_to = r"C:\Users\Thanos\Desktop\photos"

for filename in os.listdir(path):
    imgae = Image.open(f"{path}/{filename}")

    edit = img.filter(ImageFilter.SHARPEN)

    clean_name = os.path.slitext(filename)[0]
    
    edit.save(f".{save_to}/{clean_name}_editedJPG")