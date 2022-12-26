#!/usr/bin/env python

import argparse
import glob
import io
import os

from PIL import Image, ImageFont, ImageDraw

SCRIPT_PATH = os.path.dirname(os.path.abspath(__file__))

# Default data paths.
DEFAULT_LABEL_FILE = os.path.join(SCRIPT_PATH,'labels/2350-common-hangul.txt')
DEFAULT_SOURCE_FONTS_DIR = os.path.join(SCRIPT_PATH, 'fonts/src_font')
DEFAULT_OUTPUT_DIR = os.path.join(SCRIPT_PATH, 'src-image-data-modified')

LABEL_UNICODE = os.path.join(SCRIPT_PATH, 'labels/2350-unicode.txt')

# Width and height of the resulting image.
IMAGE_WIDTH = 256
IMAGE_HEIGHT = 256

def generate_hangul_images(label_file, src_fonts_dir, output_dir, lbl_unicode):
    """Generate Hangul image files.

    This will take in the passed in labels file and will generate several
    images using the font files provided in the font directory. The font
    directory is expected to be populated with *.ttf (True Type Font) files.
    The generated images will be stored in the given output directory.
    """
    with io.open(label_file, 'r', encoding='utf-8') as f:
        labels = f.read().splitlines()

    image_dir = os.path.join(output_dir, 'images')
    if not os.path.exists(image_dir):
        os.makedirs(os.path.join(image_dir))

    # Get a list of the fonts.
    fonts = glob.glob(os.path.join(src_fonts_dir, '*.ttf'))

    total_count = 0
    prev_count = 0
    font_count = 0
    char_no = 0

    with io.open(lbl_unicode, 'r', encoding='utf-8') as f:
        label_unicode = f.read().splitlines()
    
    for character in labels:
        char_no += 1

        # Print image count roughly every 5000 images.
        if total_count - prev_count > 5000:
            prev_count = total_count
            #print('{} images generated...'.format(total_count))
            print('{} images generated...'.format(char_no))

        for x in range(len(src_fonts_dir)):
            font_count += 1
            
            for font in fonts:
                total_count += 1
                image = Image.new("RGB", (256,256), (255, 255, 255))
                font = ImageFont.truetype(font, 170)
                drawing = ImageDraw.Draw(image)
                w, h = drawing.textsize(character, font=font)
                drawing.text(((IMAGE_WIDTH-w)/2, (IMAGE_HEIGHT-h)/2),character,fill=(0,0,0),font=font)
                #file_string = '{}_{}.png'.format('56',char_no)
                file_string = 'NanumBareunGothic_{}.png'.format(label_unicode)
                file_path = os.path.join(image_dir, file_string)
                image.save(file_path, 'PNG')
        font_count = 0
    char_no = 0

    print('Finished generating {} images.'.format(char_no))


if __name__ == '__main__':

    parser = argparse.ArgumentParser()

    parser.add_argument('--label-file', type=str, dest='label_file', default=DEFAULT_LABEL_FILE, help='File containing newline delimited labels.')
    parser.add_argument('--src-font-dir', type=str, dest='src_fonts_dir', default=DEFAULT_SOURCE_FONTS_DIR, help='Directory of ttf fonts to use.')
    parser.add_argument('--output-dir', type=str, dest='output_dir', default=DEFAULT_OUTPUT_DIR, help='Output directory to store generated images.') 
    parser.add_argument('--label-unicode', type=str, dest='lbl_unicode', default=LABEL_UNICODE, help='File containing newline delimited labels.')

    args = parser.parse_args()

    generate_hangul_images(args.label_file, args.src_fonts_dir, args.output_dir, args.lbl_unicode)