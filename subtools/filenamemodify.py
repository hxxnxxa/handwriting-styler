import os
import glob

 # version 1

"""
data_path = 'images/tgt_sequential-56/15'
files_list = glob.glob(data_path + '/*')

for f in files_list:
	new_f = f.replace('15_', '')
	os.rename(f, new_f)
	print('{} --> {}'.format(f,new_f))
"""


 # version 2

"""
file_path = 'images/combine_sequential_55_60/hangul-images'
file_names = os.listdir(file_path)
font_name = '60_'

print("file_path : ", file_path)
print("file_names : ", file_names)
print("font_name : ", font_name)


for name in file_names:
    src = os.path.join(file_path, name)
    dst = font_name + name + '.png'
    dst = os.path.join(file_path, dst)
    os.rename(src, dst)
"""



 # version 3

"""
import typer

def modify(tgt_path: str, ori: str, new: str):
    #data_path = 'images/tgt_sequential-56/' + tgt_path
    data_path = 'images/combine_230106/' + tgt_path
    files_list = glob.glob(data_path + '/*')

    for f in files_list:
        new_f = f.replace(ori,new)

        os.rename(f, new_f)
        print('{} --> {}'.format(f, new_f))

if __name__ == "__main__":
    typer.run(modify)
"""


# version 4

data_path = 'images/combine_230106/1_2'
files_list = glob.glob(data_path + '/*')

for f in files_list:
	new_f = f.replace('15_', '')
	os.rename(f, new_f)
	print('{} --> {}'.format(f,new_f))