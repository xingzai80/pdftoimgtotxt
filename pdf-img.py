import pytesseract
from PIL import Image
import fitz


#  打开PDF文件，生成一个对象
#  这里输入你的pdf文件的路径
doc = fitz.open(r'pdf/01.pdf')


print(doc.pageCount)
counter = (doc.pageCount)
print(counter)
numInit = int(0)
for pg in range(doc.pageCount):
    page = doc[pg]
    print(page)
    rotate = int(0)
    # 每个尺寸的缩放系数为2，这将为我们生成分辨率提高四倍的图像。
    zoom_x = 4.0
    zoom_y = 4.0
    trans = fitz.Matrix(zoom_x, zoom_y).preRotate(rotate)
    pm = page.getPixmap(matrix=trans, alpha=False)
    #  将转换的图片保存在本地
    #  这里设置保存图片的名称
    pm.writePNG(r'img/'+'{:1}.png' .format(pg))



textAll = ""
salt = ">_<xingzai>_<" #加盐做分页入库使用
for pg in range(doc.pageCount):
    strnum = str(numInit)
    print(strnum)
    page = (doc[pg])
    img = Image.open(r'img/'+strnum+'.png')
    text = pytesseract.image_to_string(img, lang='chi_sim')
    text = text.replace(' ', '')
    text = ("".join([s for s in text.splitlines(True) if s.strip()]))
    textAll += text + salt+"页数："+str(numInit+1) +'\r\n\n'
    if numInit == counter -1:
        print("写入全部数据")
        with open('demoall.txt', 'w', encoding='utf8') as f:
            f.write(textAll)
    else:
        numInit = numInit+1
        with open('txt/demo'+strnum+'.txt', 'w', encoding='utf8') as f:
            f.write(text)

