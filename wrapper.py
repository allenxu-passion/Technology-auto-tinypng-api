# @Author: allenxu
# @Date: 2018.8.7

import os
import glob
import tinify
from multiprocessing import Pool

tinify.key = 'T9bb5AsNDt1CWtvmG3xnWL43EyUNN1wN'

def tinypng(f):
	old_size = os.path.getsize(f)
	file = tinify.from_file(f)
	file.to_file(f)
	new_size = os.path.getsize(f)
	tinified_size = old_size - new_size
	print(f,"tinified size:",tinified_size)
	   
print('start and wait...')
pngs = glob.glob('*.png')
jpgs = glob.glob('*.jpg')
p = Pool(4)
for f in pngs:
	if os.path.basename(f).endswith('.9.png'):
		continue
	p.apply_async(tinypng, args=(f, ))
for f in jpgs:
    p.apply_async(tinypng, args=(f, ))
p.close()
p.join()

print('finish.')