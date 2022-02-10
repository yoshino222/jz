#找到地址，然后将地址内map-xxxx.json的文件全都变成map-3xxxx
import os
import re
path="C:/Users/Mybogames/Desktop/test"

#获取目录下的文件列表
def getMapList(localPath):
    files= os.listdir(localPath) #路径文件列表
    s = []
    for file in files:
     if os.path.splitext(file)[1] == '.json':#分离文件名和扩展名
          s.append(file)
    return s


q="map-123"
b=re.findall( r'(/w+)(-)(/d+)', q)
print(b)
#print(getMapList(path))