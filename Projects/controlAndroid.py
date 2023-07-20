from ppadb.client import Client
from time import sleep

adb = Client(host='127.0.0.1', port=5037)
devices = adb.devices()

if len(devices) == 0:
    print('no device attached')
    quit()

device = devices[0]

# instalar apk de um app no celular
device.install('Telegram.apk')

device.shell('input swipe 500 1500 500 250')
device.shell('input tap 931 1367')
sleep(2)

device.shell('input tap 547 1885')
sleep(2)

device.shell('input tap 877 1480')
sleep(2)

device.shell('input tap 533 1270')
sleep(2)

# rodar o tap 15 vezes
for i in range(15):
    device.shell('input tap 873 2041')

numero = '5537988347387'

device.shell(f'input text {numero}')
device.shell('input tap 940 1400')
device.shell('input tap 870 1486')
device.shell('input tap 544 1266')