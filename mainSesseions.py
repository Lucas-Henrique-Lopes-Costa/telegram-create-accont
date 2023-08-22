from telethon.sync import TelegramClient
from ppadb.client import Client
from random import choice
from time import sleep
from json import load, dump
import clipboard
import pyautogui
import asyncio
import re

api_id = 10103155
api_hash = "13bddab82f9a0f7188686ee7b5558663"

phone = input('Digite o número de telefone: ')
phone = phone.replace('+', '')

# Set the proxy url
proxy_url = 'geo.iproyal.com'
port = '32325'
user = 'leiroz7'
password = 'arvore11_country-ph'

adb = Client(host='127.0.0.1', port=5037)
devices = adb.devices()

if len(devices) == 0:
    print('no device attached')
    quit()

device = devices[0]

# Escolhe uma foto aleatória da pasta fotos
with open("data/photos.txt") as f:
    photos = str(f.read()).split("\n")
photo = choice(photos)
print(photo)
device.push(f"photos/{photo}", f"/sdcard/Pictures/{photo}")
print("Foto enviada!")

# Mover para a galeria
print("Open gallery")
device.shell('input tap 520 2200')
device.shell('input tap 130 1500')
sleep(4)

# dar acesso a galeria
print("Give access to gallery")
device.shell(
    'pm grant org.thunderdog.challegram android.permission.READ_CONTACTS')
device.shell(
    'pm grant org.thunderdog.challegram android.permission.READ_EXTERNAL_STORAGE')
device.shell(
    'pm grant org.thunderdog.challegram android.permission.WRITE_EXTERNAL_STORAGE')
device.shell(
    'pm grant org.thunderdog.challegram android.permission.CAMERA')
device.shell(
    'pm grant org.thunderdog.challegram android.permission.RECORD_AUDIO')
device.shell(
    'pm grant org.thunderdog.challegram android.permission.ACCESS_FINE_LOCATION')
device.shell(
    'pm grant org.thunderdog.challegram android.permission.ACCESS_COARSE_LOCATION')
device.shell(
    'pm grant org.thunderdog.challegram android.permission.ACCESS_BACKGROUND_LOCATION')

print("Open folder root")
device.shell('input tap 95 250')
sleep(2)
device.shell('input tap 290 1350')

print("Open Folder")
device.shell('input tap 140 540')
sleep(2)

print("Open photo")
device.shell('input keyevent 62')
device.shell('input keyevent 66')

print("Move to gallery")
device.shell('input tap 286 2035')
sleep(2)
device.shell('input tap 140 690')
sleep(2)
device.shell('input tap 400 1270')
sleep(3)
device.shell('input tap 530 2080')
sleep(4)
device.shell('input tap 600 1580')
sleep(2)

device.shell('input tap 995 70')
sleep(2)
device.shell('input tap 995 70')
sleep(2)
device.shell('input tap 60 60')
sleep(2)
device.shell('input tap 55 240')

print("Set accont...")
device.shell('input tap 66 240')
sleep(2)
device.shell('input tap 270 940')

print("Set photo...")
device.shell('input tap 470 588')
sleep(2)
device.shell('input tap 250 1900')
sleep(2)
device.shell('input tap 500 580')
sleep(2)
device.shell('input tap 180 630')
sleep(2)

# Set username
print("Set username...")
device.shell('input tap 500 970')
sleep(1)
device.shell('input tap 480 1780')
sleep(1)

# Gera um username aleatório com o nome e outros 10 números aleatórios
print("Select user...")
with open("data/names.txt") as f:
    names = str(f.read()).split("\n")
name = choice(names)
username = name + ''.join5511918649652
(choice('0123456789') for i in range(10))

device.shell(f'input text {username}')

# Clica em continuar
device.shell('input tap 950 1340')

# Set bio
print("Set bio...")
device.shell('input tap 480 1380')
sleep(2)
device.shell('input tap 480 1780')
sleep(2)

bio = "Eu estou usando o Telegram"
device.shell(f'input text {bio}')
sleep(3)

# Clica em continuar
device.shell('input tap 950 1340')

# Set two-step verification
print("Set two-step verification...")
device.shell('input tap 500 2050')
sleep(2)
device.shell('input tap 500 980')
sleep(2)
device.shell('input tap 500 1564')
sleep(2)

device.shell(f'input text arvore11')
sleep(2)

# Clica em continuar
device.shell('input tap 950 1340')
sleep(1)

# Skip
device.shell('input tap 78 1340')
sleep(1)

device.shell('input keyevent 62')
device.shell('input keyevent 22')
device.shell('input keyevent 66')

print("Voltando para o telegram...")
device.shell('input tap 75 250')
sleep(1)
device.shell('input tap 75 250')
sleep(1)
device.shell('input tap 75 250')
sleep(1)

# Salvar .section
print("Salvando Seção...")

# Limpar o telegram da memória para salvar
device.shell('input tap 535 2200')
device.shell('input tap 835 2200')
device.shell('input swipe 500 1500 500 250')

# Abrindo novamente
device.shell('input swipe 500 1500 500 250')
device.shell('input tap 930 1370')

sleep(4)

async def fill_phone_number():  # Função para preencher o número de telefone no Telegram no terminal e salvar a seção
    client = TelegramClient(f'sessions/{phone}', api_id, api_hash,
                            proxy=("socks5", proxy_url, port, True, user, password))
    await client.start()


def enter_number():  # Função para colocar o número de telefone no terminal
    pyautogui.write(phone)
    pyautogui.press('enter')


def get_verification_code():  # Função para pegar o código recebido no telefone usando ppadb.client
    print("Obtendo o código de verificação...")
    sleep(10)

    # print("Clica na conversa do telegram.")
    device.shell('input tap 735 408')

    # sleep(5)

    # print("clica no campo de texto")
    device.shell('input tap 318 1928')

    # sleep(5)

    # print("Indentifica o código da mensagem.")
    device.shell('input tap 318 1928')
    code_pattern = r"Login code: (\d+)"

    # sleep(5)

    received_message = clipboard.paste()
    match = re.search(code_pattern, received_message)
    if match:
        verification_code = match.group(1)
        pyautogui.write(verification_code)
        pyautogui.press('enter')


async def main():
    # Crie as tarefas assíncronas
    fill_task = asyncio.ensure_future(fill_phone_number())
    enter_task = asyncio.ensure_future(
        loop.run_in_executor(None, enter_number))
    get_task = asyncio.ensure_future(
        loop.run_in_executor(None, get_verification_code))

    # Aguarde até que ambas as tarefas sejam concluídas
    await asyncio.gather(fill_task, enter_task, get_task)

    # adiciona na lista de phones.json
    with open("data/phones.json", "r") as f:
        data = load(f)
    data['phone_numbers'].append(phone)
    with open("data/phones.json", "r+") as f:
        dump(data, f)

    print("Processos concluídos.")

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
