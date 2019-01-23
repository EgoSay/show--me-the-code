# @Author  : adair_chan
# @Email   : adairchan.dream@gmail.com
# @Date    : 2019/1/23 上午10:59
# @IDE     : PyCharm

"""
主要利用python的Pillow库实现
官方文档：https://pillow.readthedocs.io/en/stable/
参考链接: https://liam.page/2015/04/22/pil-tutorial-basic-usage/
"""
from PIL import Image, ImageDraw, ImageFont


def insert_num(img_path, num):
    with Image.open(img_path) as img:
        width, height = img.size
        draw = ImageDraw.Draw(img)
        draw.text((4 * width / 5, height / 5), num, fill=(255, 10, 10))
        img.save('1.png')


if __name__ == '__main__':
    img_path = "Mario.png"
    insert_num(img_path, '4')
