from PIL import Image, ImageFilter
import os

# size_300 = (900,900)
# for f in os.listdir('.'):
#     if f.endswith('.jpg'):
#         i = Image.open(f)
#         fn, fext = os.path.splitext(f)
        
#         i.thumbnail(size_300)
#         i.save('size/{}.png'.format(fn))

image1 = Image.open('yeet_bw.jpg')
image1.filter(ImageFilter.GaussianBlur(15)).save('yeet_bwblurred.jpg')