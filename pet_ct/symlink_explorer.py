import time
import os

for filename in os.listdir('/data2/fdg-pet-ct/models'):
# for filename in os.listdir('/data/fdg-pet-ct/models_wetlab'):
# for filename in os.listdir('/data4/fdg-pet-ct/models'):
    try:
        t = time.ctime(int(filename[:10]))
    except:
        t = time.ctime(int(filename[41:41+10]))
    if 'Jul 30' in t:
        print(filename)
        print(t)
        print('--')