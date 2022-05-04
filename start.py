import os


# Chiusura vecchi containers se gia in esecuzione ed eliminazione vecchie immagini
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
    

# Creazione delle immagini e dei containers con il docker compose up
try:
    print('---- Creazione delle immagini e dei container')
    os.system('docker-compose up -d --build')
    print('---- Creazione avvenuta')
except:
    print('---- Creazione NON avvenuta')
    exit()


# Avvio di tutti i servizi
processi = os.popen('docker ps').read().split('\n')
processi = processi[:len(processi)-1]
for i in range (len(processi)):
    arr = processi[i].split('   ')
    if arr[1] == 'tecnologie_web-server':
        os.system('docker exec -it ' + arr[0] + ' node /home/index.js')
        print('---- Web Server in ESECUZIONE')

