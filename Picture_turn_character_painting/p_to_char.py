from PIL import Image

ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")


# RGB值转字符的函数 将256灰度映射到70个字符上
def get_char(r, g, b, alpha=256):
    if alpha == 0:
        return ' '
    length = len(ascii_char)
    gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)

    unit = (256.0 + 1) / length
    return ascii_char[int(gray / unit)]


def pillow():
    im = Image.open('avatar.png')
    # (宽，长)
    im = im.resize((80, 50), Image.NEAREST)
    # <PIL.PngImagePlugin.PngImageFile image mode=RGBA size=200x200 at 0x2604DEFEBE0>
    txt = ''
    for i in range(50):
        for j in range(80):
            # print(*im.getpixel((j, i)))
            # print(im.getpixel((j, i)))
            txt += get_char(*im.getpixel((j, i)))
        txt += '\n'
        # print(txt)


if __name__ == '__main__':
    pillow()
