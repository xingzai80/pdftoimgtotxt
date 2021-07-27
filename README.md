# pdftoimg And imgtoTxt

#### 介绍
Python使用到第三方库PyMuPDF将pdf转换成图片

再将图片转成文字

#### 安装使用

1. git clone `https://gitee.com/Mr-Format/pdftoimg.git`

2. pip安装第三方库PyMuPDF `pip install PyMuPDF`

3. Python IDE 运行 `pdf-img.py`

4. brew install tesseract //安装tesseract，

5. ```
   https://github.com/tesseract-ocr/tessdata 下载部署语言库  路径为 /usr/local/Cellar/tesseract/4.0.0_1/share/tessdata
   ```

#### 代码

```python
import fitz
#  打开PDF文件，生成一个对象
#  这里输入你的pdf文件的路径
doc = fitz.open(r'pdf/001.pdf')

print(doc.pageCount)

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
    textAll += text + salt+"页数："+str(numInit+1)
    if numInit == counter -1:
        print("写入全部数据")
        with open('demoall.txt', 'w', encoding='utf8') as f:
            f.write(textAll)
    else:
        numInit = numInit+1
        with open('txt/demo'+strnum+'.txt', 'w', encoding='utf8') as f:
            f.write(text)
```

