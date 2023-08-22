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

# Salvar .section
print("Salvando Seção...")


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
