import os
import glob


"""
data_path = 'combine-image-data-AritaBuri/images'
files_list = glob.glob(data_path + '/*')

for f in files_list:
	#new_f = f.replace('', 'NanumBareunGothic_AritaBuri_')
	os.rename(f, new_f)
	print('{} --> {}'.format(f,new_f))
"""


file_path = 'combine-image-data-NanumHandwriting/hangul-images'
file_names = os.listdir(file_path)
font_name = 'NanumBareunGothic_NanumHandwriting_'

print("file_path : ", file_path)
print("file_names : ", file_names)
print("font_name : ", font_name)


for name in file_names:
    src = os.path.join(file_path, name)
    dst = font_name + name + '.png'
    dst = os.path.join(file_path, dst)
    os.rename(src, dst)
