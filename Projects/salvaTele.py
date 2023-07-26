from telethon.sync import TelegramClient
from time import sleep
from ppadb.client import Client
import pyautogui
import asyncio
import re
import clipboard

# Credenciais da API do Telegram
api_id = 10103155
api_hash = "13bddab82f9a0f7188686ee7b5558663"
phone = "5537988347387"

# Função para preencher o número de telefone no Telegram
async def fill_phone_number():
    client = TelegramClient(f"sessions/{phone}", api_id, api_hash)
    await client.start()

# Função para colocar o número de telefone no terminal
def enter_number():
    pyautogui.write(phone)
    pyautogui.press('enter')
    sleep(3)

# Função para pegar o código recebido no telefone usando ppadb.client
def get_verification_code():
    print("Obtendo o código de verificação...")
    sleep(5)
    
    adb = Client(host='127.0.0.1', port=5037)
    devices = adb.devices()

    if len(devices) == 0:
        print('no device attached')
        quit()

    device = devices[0]

    # print("Dispositivo conectado.")
    # clica na conversa do telegram
    device.shell('input tap 735 408')
    # sleep(5)

    # clica no campo de texto
    # print("clica no campo de texto")
    device.shell('input tap 318 1928')
    # sleep(5)

    # clica em copiar
    # print("clica em copiar")
    device.shell('input tap 318 1928')

    received_message = clipboard.paste()
    
    # Use regex para encontrar o código na mensagem
    code_pattern = r"Login code: (\d+)"
    match = re.search(code_pattern, received_message)
    if match:
      verification_code = match.group(1)
      pyautogui.write(verification_code)
      pyautogui.press('enter')

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
