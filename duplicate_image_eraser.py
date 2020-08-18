from matplotlib import image
from matplotlib import pyplot
import os
import hashlib
import glob
import time
images_files= glob.glob("path/*.jpg")

print(len(images_files))

Has=[]
x=0
i=0
ini=time.time()
Ini=time.time()
for filename in images_files:
    x+=1
    i+=1
    if(x==500):
        print(i)
        n=time.time()-ini
        print(f'{n} s')
        print(f'tempo estimado: {(n*((len(images_files)-i)/500))/60} min')
        ini=time.time()
        x=0
    hasher = hashlib.md5()
    with open(filename, 'rb') as f:
        buf = f.read()
        hasher.update(buf)
        a = hasher.hexdigest()
        Has.append([a,filename])
        #print(a)
print(f'{(time.time()-ini)/60} min')
print(f'Tempo total para Hashs: {(time.time()-Ini)/60} min')

print("####################")
x=0
Ini=time.time()
ini=time.time()
for i in range(len(Has)-1):
    x+=1
    if(x==100):
        print(i)
        n=time.time()-ini
        print(f'{n} s')
        print(f'tempo estimado: {(n*((len(Has)-i)/100))/60} min')
        ini=time.time()
        x=0
    if os.path.isfile(Has[i][1]):
        for j in range(i+1,len(Has)):
            #print(os.path.isfile(images_files[j]))
            
            if os.path.isfile(Has[j][1]):
               

                if Has[i][0] == Has[j][0]:
                    os.remove(Has[j][1])
                    # os.remove(Has[j][1][:-4]+".xml")
                    print(f"apagada copia de {Has[i][1]}")
    # print(f'{time.time()-ini} s')
print(f'Tempo total para Varredura: {(time.time()-Ini)/60} min')

    

