# //单张图片转文字
import pytesseract
from PIL import Image

img = Image.open(r'img/1.png')
text = pytesseract.image_to_string(img,lang='chi_sim')
with open('demo.txt', 'w', encoding='utf8') as f:
    f.write(text)
print(text)