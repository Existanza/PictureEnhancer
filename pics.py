# written for Python version 3.4.1
__author__ = 'Deca'
from PIL import Image
import sys


def save(image, image_name, mode, im_type):
    full_image_name = image_name + '_' + mode + im_type
    image.save(full_image_name)
    print('Saved ' + full_image_name + '.')


def convert_greyscale(image, image_name, im_type):
    out = image.convert('L')
    save(out, image_name, 'greyscale', im_type)


def convert_coloured(image, image_name, im_type):
    rgb2 = (
        3.2406, -1.5372, -0.4986, 0,
        -0.9689, 1.8578, 0.0415, 0,
        0.0557, -0.2040, 1.0570, 0)
    out = image.convert('RGB', rgb2)
    save(out, image_name, 'coloured', im_type)


def convert_shade(image, image_name, im_type):
    im_red = image.copy()
    im_green = image.copy()
    im_blue = image.copy()
    pixels = image.load()
    pixels_red = im_red.load()
    pixels_green = im_green.load()
    pixels_blue = im_blue.load()
    for i in range(image.size[0]):
        for j in range(image.size[1]):
            if i % int(image.size[0]/10) == 0 and i > 0 and j == 0:
                print('. ', end='')
                sys.stdout.flush()
            tmp_tuple = pixels[i, j]
            pixels_red[i, j] = (255, tmp_tuple[1], tmp_tuple[2])
            pixels_green[i, j] = (tmp_tuple[0], 255, tmp_tuple[1])
            pixels_blue[i, j] = (tmp_tuple[0], tmp_tuple[1], 255)
            del tmp_tuple
    print()
    save(im_red, image_name, 'red', im_type)
    save(im_green, image_name, 'green', im_type)
    save(im_blue, image_name, 'blue', im_type)


def load(im_name, im_type):
    try:
        full_im_name = im_name + im_type
        print('\n' + 'Trying to open ' + full_im_name + '\n')
        im = Image.open(full_im_name)
        convert_greyscale(im, im_name, im_type)
        convert_coloured(im, im_name, im_type)
        convert_shade(im, im_name, im_type)
    except FileNotFoundError:
        print(full_im_name + ' hasn\'t been found.')


im_name = input('Insert the image name (only jpg/bmp, localized in the scrypt\'s folder.): ')
if im_name.endswith('.jpg') or im_name.endswith('.bmp'):
    im_type = im_name[len(im_name)-4:]
    im_name = im_name[:-4]
    load(im_name, im_type)
else:
    load(im_name, '.jpg')
    load(im_name, '.bmp')