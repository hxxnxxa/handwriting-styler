#!/usr/bin/env python

import argparse
import glob
import io
import os
from PIL import Image, ImageFont, ImageDraw


# Default data paths.
base_path = os.path.dirname(os.path.abspath(__file__))
lbl_path = os.path.join(base_path, 'labels/2350-unicode.txt')
src_ttf_path = os.path.join(base_path, 'fonts/src_font')
output_path = os.path.join(base_path, 'src-image-data-modified')


# Width and height of the resulting image.
width = 256
height = 256


# Generate Korean images
def generate_hangul_images(lbl, src_fonts_path, output_dir):
    """Generate Hangul image files.

    This will take in the passed in labels file and will generate several
    images using the font files provided in the font directory. The font
    directory is expected to be populated with *.ttf (True Type Font) files.
    The generated images will be stored in the given output directory.
    """


    #Read syllables
    with io.open(lbl, 'r', encoding='utf-8') as f:
        labels = f.read().splitlines()


    # Path of the output image 
    image_dir = os.path.join(output_dir, 'images')
    if not os.path.exists(image_dir):
        os.makedirs(os.path.join(image_dir))
  
  
    # Get a list of the fonts.
    fonts = glob.glob(os.path.join(src_fonts_path, '*.ttf'))

    total_count = 0
    font_count = 0
    char_no = 0

    for character in labels:
        hangul_character = chr(int(character, 16))
        char_no += 1

        print('{} images generated...'.format(c))

        for x in range(len(src_fonts_path)):
            font_count += 1

            for font in fonts:
                total_count += 1
                image = Image.new("RGB", (256,256), (255, 255, 255))
                font = ImageFont.truetype(font, 160)
                drawing = ImageDraw.Draw(image)
                w, h = drawing.textsize(hangul_character, font=font)
                drawing.text(((width-w)/2, (height-h)/2),hangul_character,fill=(0,0,0),font=font)
                file_string = '{}_{}.png'.format('NanumBareunGothic', character)
                file_path = os.path.join(image_dir, file_string)
                image.save(file_path, 'PNG')
        font_count = 0
    char_no = 0
    print('Finished generating {} images.'.format(char_no))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--label-file', type=str, dest='lbl', default=lbl_path, help='File containing newline delimited labels.')
    parser.add_argument('--src-font-dir', type=str, dest='src_fonts_path', default=src_ttf_path, help='Directory of ttf fonts to use.')
    parser.add_argument('--output-dir', type=str, dest='output_dir', default=output_path, help='Output directory to store generated images.') 
    args = parser.parse_args()
    generate_hangul_images(args.lbl, args.src_fonts_path, args.output_dir)