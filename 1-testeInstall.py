from ppadb.client import Client

adb = Client(host='127.0.0.1', port=5037)
devices = adb.devices()

if len(devices) == 0:
    print('no device attached')
    quit()

device = devices[0]

# Desistanlando Telegram X
print('Desinstalando Telegram X')
device.uninstall('org.thunderdog.challegram')

# instalar apk de um app no celular
device.install('Telegram.apk')
print('App instalado')

# abrir app
device.shell('input swipe 500 1500 500 250')
device.shell('input tap 930 1370')
