import os

os.system('docker-compose down')

image = os.popen('docker image ls').read().split('\n')
image = image[:len(image)-1]
for i in range (len(image)):
    arr = image[i].split(' ')
    l = len(arr)
    for ii in range(len(arr)):
        if arr[l-1-ii] == '':
            arr.pop(l-ii-1)
    #print(arr)

    if (arr[0] == 'tecnologie_web-server'):
        os.system('docker image rm ' + arr[2])