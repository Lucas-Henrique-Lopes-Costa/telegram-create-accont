from telethon.sync import TelegramClient
from ppadb.client import Client
from time import sleep
import pyautogui
import asyncio
import re
import clipboard

api_id = 10103155
api_hash = "13bddab82f9a0f7188686ee7b5558663"
phone = input('Digite o número de telefone: ')

phone = phone.replace('+', '')

adb = Client(host='127.0.0.1', port=5037)
devices = adb.devices()

if len(devices) == 0:
    print('no device attached')
    quit()

device = devices[0]

# # Desistanlando Telegram X
# print('Desinstalando Telegram X')
# device.uninstall('org.thunderdog.challegram')

# # instalar apk de um app no celular
# device.install('Telegram.apk')
# print('App instalado')

# print('Abrindo app')
# device.shell('input swipe 500 1500 500 250')
# device.shell('input tap 930 1370')
# sleep(2)

# device.shell('input tap 530 2000')
# sleep(2)

# # Apagar campo de texto
# for i in range(15):
#     device.shell('input keyevent 67')

# print('Digitando número')
# device.shell(f'input text {phone}')
# device.shell('input tap 940 1400')
# device.shell('input tap 870 1486')
# device.shell('input tap 544 1266')

# # Inserindo código
# sleep(2)
# device.shell('input tap 483 653')
# device.shell('input tap 483 653')
# sleep(2)

# print('Inserindo código')
# code = input('Digite o código: ')
# device.shell(f'input text {code}')

print("Autendicando...")
sleep(2)

print("Salvando Seção...")
# Função para preencher o número de telefone no Telegram
async def fill_phone_number():
    client = TelegramClient(f"sessions/{phone}", api_id, api_hash)
    await client.start()

# Função para colocar o número de telefone no terminal
def enter_number():
    pyautogui.write(phone)
    pyautogui.press('enter')

# Função para pegar o código recebido no telefone usando ppadb.client
def get_verification_code():
    print("Obtendo o código de verificação...")
    sleep(10)

    # print("Clica na conversa do telegram.")
    device.shell('input tap 735 408')
    
    # sleep(5)

    # print("clica no campo de texto")
    device.shell('input tap 318 1928')
    
    # sleep(5)

    # Copiar

    # Portugues
    # device.shell('input tap 240 1758')
    # code_pattern = r"Código de login: (\d+)"
    
    # Ingles
    device.shell('input tap 318 1928')
    code_pattern = r"Login code: (\d+)"
    
    #sleep(5)

    received_message = clipboard.paste()
    match = re.search(code_pattern, received_message)
    if match:
        verification_code = match.group(1)
        pyautogui.write(verification_code)
        pyautogui.press('enter')
        # print('Código inserido')

async def main():
    # Crie as tarefas assíncronas
    fill_task = asyncio.ensure_future(fill_phone_number())
    enter_task = asyncio.ensure_future(loop.run_in_executor(None, enter_number))
    get_task = asyncio.ensure_future(loop.run_in_executor(None, get_verification_code))

    # Aguarde até que ambas as tarefas sejam concluídas
    await asyncio.gather(fill_task, enter_task, get_task)

    print("Processos concluídos.")

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
