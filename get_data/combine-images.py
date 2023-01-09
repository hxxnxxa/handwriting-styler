# imprts related to creating paths
import io
import os
import argparse


# imports related to preprocess from pix2pix
import tfimage as im
import time
import tensorflow as tf
import numpy as np
import threading
import glob
import shutil


# setting global variable for counter 
index = 0
total_count = 0
font_idx = 0


# Default data paths.
base_path = os.path.dirname(os.path.abspath(__file__))
lbl_path = os.path.join(base_path,'../labels/2350-common-hangul.txt')
output_path = os.path.join(base_path, '../images/combined_sequential-53_230106')
input_path = os.path.join(base_path, '../images/tgt_sequential-56/images')
b_dir = os.path.join(base_path, '../images/tgt_sequential-56/images')


# Remove directory after combining
def remove_dir(path):
    """ param <path> could either be relative or absolute. """
    if os.path.isfile(path) or os.path.islink(path):
        os.remove(path)  # remove the file
    elif os.path.isdir(path):
        shutil.rmtree(path)  # remove dir and all contains
    else:
        raise ValueError("file {} is not a file or dir.".format(path))


# Combine src with src_path
def combine(src, src_path):
    if args.b_dir is None:
        raise Exception("missing b_dir")


    # find corresponding file in b_dir, could have a different extension
    basename, _ = os.path.splitext(os.path.basename(src_path))
    print("basename: ",basename) # 1
    print("1_",basename) # 1
    for ext in [".png", ".jpg"]:
        sibling_path = os.path.join(args.b_dir, basename + ext) # tgt-image-data-modified\Arita-buri\NanumBareunGothic_AC00.png \n tgt-image-data-modified\Arita-buri\NanumBareunGothic_AC00.jpg
        print("sibling_path:", sibling_path)
        if os.path.exists(sibling_path):
            sibling = im.load(sibling_path)
            break
    else:
        raise Exception("could not find sibling image for " + src_path)


    # make sure that dimensions are correct
    height, width, _ = src.shape
    if height != sibling.shape[0] or width != sibling.shape[1]:
        raise Exception("differing sizes")
    

    # convert both images to RGB if necessary
    if src.shape[2] == 1:
        src = im.grayscale_to_rgb(images=src)

    if sibling.shape[2] == 1:
        sibling = im.grayscale_to_rgb(images=sibling)


    # remove alpha channel
    if src.shape[2] == 4:
        src = src[:,:,:3]
    
    if sibling.shape[2] == 4:
        sibling = sibling[:,:,:3]

    return np.concatenate([src, sibling], axis=1)


# Procss with src_path, dst_path, image_dir
def process(src_path, dst_path, image_dir):
    global index
    global total_count

    total_count += 1
    src = im.load(src_path)
    #print("src_path: ",src_path)

    if args.operation == "combine":
        dst = combine(src, src_path)
    else:
        raise Exception("invalid operation")
    im.save(dst, dst_path)


# Initialize
complete_lock = threading.Lock()
start = None
num_complete = 0
total = 0


# Notify completion 
def complete():
    global num_complete, rate, last_complete

    with complete_lock:
        num_complete += 1
        now = time.time()
        elapsed = now - start
        rate = num_complete / elapsed
        if rate > 0:
            remaining = (total - num_complete) / rate
        else:
            remaining = 0

        print("%d/%d complete  %0.2f images/sec  %dm%ds elapsed  %dm%ds remaining" % (num_complete, total, rate, elapsed // 60, elapsed % 60, remaining // 60, remaining % 60))

        last_complete = now


# Generate combined image
def generate_hangul_combined_images(label_file, output_dir):
    if not os.path.exists(args.output_dir):
        os.makedirs(args.output_dir)

    # Set the path of hangul-skeleton-combine images in output directory. It will be used later for 
    # setting up hangul-skeleton-combine images path for hangul-skeleton-combine labels
    image_dir = os.path.join(output_dir, 'hangul-images')
    if not os.path.exists(image_dir):
        os.makedirs(os.path.join(image_dir))

    src_paths = []
    dst_paths = []

    # Check if the directory and images already exsist?
    # If yes then skip those images else create the paths list
    skipped = 0
    for src_path in sorted(im.find(args.input_dir), key=os.path.getmtime):
        name, _ = os.path.splitext(os.path.basename(src_path))
        dst_path = os.path.join(image_dir, name + ".png")
        if os.path.exists(dst_path):
            skipped += 1
        else:
            src_paths.append(src_path)
            dst_paths.append(dst_path)
    
    print("skipping %d files that already exist" % skipped)

    global total
    total = len(src_paths)
    
    print("processing %d files" % total)

    global start
    start = time.time()

    if args.workers == 1:
        with tf.Session() as sess:
            for src_path, dst_path in zip(src_paths, dst_paths):
                process(src_path, dst_path, image_dir)
                complete()



if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--input_dir", type=str, dest='input_dir',default=input_path, required=True, help="path to folder containing images")
    parser.add_argument('--output_dir', type=str, dest='output_dir',default=output_path, help='Output directory to store generated hangul skeleton images and ''label CSV file.')
    parser.add_argument("--operation", required=True, choices=["combine"])
    parser.add_argument("--workers", type=int, default=1, help="number of workers")

    # Combine
    parser.add_argument("--b_dir", type=str, dest='b_dir', default=b_dir, help="path to folder containing B images for combine operation")
    parser.add_argument('--label-file', type=str, dest='label_file',default=lbl_path,help='File containing newline delimited labels.')
    args = parser.parse_args()


    generate_hangul_combined_images(args.label_file, args.output_dir)


    # (Not use) Remove the src and target directories
    #src_head, _ = os.path.split(args.input_dir)
    #trg_head, _ = os.path.split(args.b_dir)
    #print("Removing the directories")
    #remove_dir(src_head)
    #remove_dir(trg_head)
    #print("*** DONE ***")
