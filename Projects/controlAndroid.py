from ppadb.client import Client
from time import sleep

adb = Client(host='127.0.0.1', port=5037)
devices = adb.devices()

if len(devices) == 0:
    print('no device attached')
    quit()

device = devices[0]

# # instalar apk de um app no celular
# device.install('Telegram.apk')
# print('App instalado')

# print('Abrindo app')
# device.shell('input swipe 500 1500 500 250')
# device.shell('input tap 931 1367')
# sleep(2)

# device.shell('input tap 530 2000')
# sleep(2)

# # Apagar campo de texto
# for i in range(15):
#     device.shell('input keyevent 67')

# numero = '5537988347387'

# print('Digitando número')
# device.shell(f'input text {numero}')
# device.shell('input tap 940 1400')
# device.shell('input tap 870 1486')
# device.shell('input tap 544 1266')

# Inserindo código
code = 748590

sleep(2)
device.shell('input tap 483 653')
device.shell(f'input text {code}')
sleep(2)

# # Desistanlando Telegram X
# print('Desinstalando Telegram X')
# device.uninstall('org.thunderdog.challegram')