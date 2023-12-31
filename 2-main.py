countrys = {
    "Russia": "0",
    "Ukraine": "1",
    "Kazakhstan": "2",
    "China": "3",
    "Philippines": "4",
    "Myanmar": "5",
    "Indonesia": "6",
    "Malaysia": "7",
    "Vietnam": "10",
    "Kyrgyzstan": "11",
    "Usa": "12",
    "Israel": "13",
    "HongKong": "14",
    "Poland": "15",
    "England": "16",
    "DCongo": "18",
    "Nigeria": "19",
    "Macao": "20",
    "Egypt": "21",
    "India": "22",
    "Ireland": "23",
    "Cambodia": "24",
    "Laos": "25",
    "Haiti": "26",
    "Ivory": "27",
    "Gambia": "28",
    "Serbia": "29",
    "Yemen": "30",
    "Southafrica": "31",
    "Romania": "32",
    "Colombia": "33",
    "Estonia": "34",
    "Canada": "36",
    "Morocco": "37",
    "Ghana": "38",
    "Argentina": "39",
    "Uzbekistan": "40",
    "Cameroon": "41",
    "Chad": "42",
    "Germany": "43",
    "Lithuania": "44",
    "Croatia": "45",
    "Sweden": "46",
    "Iraq": "47",
    "Netherlands": "48",
    "Latvia": "49",
    "Austria": "50",
    "Belarus": "51",
    "Thailand": "52",
    "Saudiarabia": "53",
    "Mexico": "54",
    "Taiwan": "55",
    "Spain": "56",
    "Algeria": "58",
    "Slovenia": "59",
    "Bangladesh": "60",
    "Senegal": "61",
    "Turkey": "62",
    "Czech": "63",
    "Srilanka": "64",
    "Peru": "65",
    "Pakistan": "66",
    "Newzealand": "67",
    "Guinea": "68",
    "Mali": "69",
    "Venezuela": "70",
    "Ethiopia": "71",
    "Mongolia": "72",
    "Brazil": "73",
    "Afghanistan": "74",
    "Uganda": "75",
    "Angola": "76",
    "Cyprus": "77",
    "France": "78",
    "Papua": "79",
    "Mozambique": "80",
    "Nepal": "81",
    "Belgium": "82",
    "Bulgaria": "83",
    "Hungary": "84",
    "Moldova": "85",
    "Italy": "86",
    "Paraguay": "87",
    "Honduras": "88",
    "Tunisia": "89",
    "Nicaragua": "90",
    "Timorleste": "91",
    "Bolivia": "92",
    "Costarica": "93",
    "Guatemala": "94",
    "Uae": "95",
    "Zimbabwe": "96",
    "Puertorico": "97",
    "Togo": "99",
    "Kuwait": "100",
    "Salvador": "101",
    "Libyan": "102",
    "Jamaica": "103",
    "Trinidad": "104",
    "Ecuador": "105",
    "Swaziland": "106",
    "Oman": "107",
    "Bosnia": "108",
    "Dominican": "109",
    "Qatar": "111",
    "Panama": "112",
    "Mauritania": "114",
    "Sierraleone": "115",
    "Jordan": "116",
    "Portugal": "117",
    "Barbados": "118",
    "Burundi": "119",
    "Benin": "120",
    "Brunei": "121",
    "Bahamas": "122",
    "Botswana": "123",
    "Belize": "124",
    "Caf": "125",
    "Dominica": "126",
    "Grenada": "127",
    "Georgia": "128",
    "Greece": "129",
    "Guineabissau": "130",
    "Guyana": "131",
    "Iceland": "132",
    "Comoros": "133",
    "Saintkitts": "134",
    "Liberia": "135",
    "Lesotho": "136",
    "Malawi": "137",
    "Namibia": "138",
    "Niger": "139",
    "Rwanda": "140",
    "Slovakia": "141",
    "Suriname": "142",
    "Tajikistan": "143",
    "Monaco": "144",
    "Bahrain": "145",
    "Reunion": "146",
    "Zambia": "147",
    "Armenia": "148",
    "Somalia": "149",
    "Congo": "150",
    "Chile": "151",
    "Furkinafaso": "152",
    "Lebanon": "153",
    "Gabon": "154",
    "Albania": "155",
    "Uruguay": "156",
    "Mauritius": "157",
    "Bhutan": "158",
    "Maldives": "159",
    "Guadeloupe": "160",
    "Turkmenistan": "161",
    "Frenchguiana": "162",
    "Finland": "163",
    "Saintlucia": "164",
    "Luxembourg": "165",
    "Saintvincentgrenadines": "166",
    "Equatorialguinea": "167",
    "Djibouti": "168",
    "Antiguabarbuda": "169",
    "Caymanislands": "170",
    "Montenegro": "171",
    "Denmark": "172",
    "Switzerland": "173",
    "Norway": "174",
    "Australia": "175",
    "Eritrea": "176",
    "Southsudan": "177",
    "Saotomeandprincipe": "178",
    "Aruba": "179",
    "Montserrat": "180",
    "Anguilla": "181",
    "Japan": "182",
    "Northmacedonia": "183",
    "Seychelles": "184",
    "Newcaledonia": "185",
    "Capeverde": "186",
    "Southkorea": "190"
}

try:
    from telethon.errors import rpcerrorlist, SessionPasswordNeededError, PhoneNumberUnoccupiedError
    from configparser import ConfigParser, NoSectionError, NoOptionError
    from json import load, loads, dump, decoder
    from telethon.sync import TelegramClient
    from ppadb.client import Client
    from os import system, remove
    from random import choice
    from requests import get
    from time import sleep
    from sys import exit
    import clipboard
    import pyautogui
    import requests
    import asyncio
    import re

    adb = Client(host='127.0.0.1', port=5037)
    devices = adb.devices()

    if len(devices) == 0:
        print('no device attached')
        quit()

    device = devices[0]
except Exception as e:
    input(f"Import error: {e}")

# CONFIG
try:
    config = ConfigParser()
    config.read('config.ini')

    # SIM API
    c_country = config.get('sim_api', 'country')
    c_operator = config.get('sim_api', 'operator')
    c_product = config.get('sim_api', 'product')
    c_token = config.get('sim_api', 'active_ru_key')

    # Telegram
    c_api_id = config.get('telegram', 'api_id')
    c_ap_hash = config.get('telegram', 'api_hash')

    # Set the proxy url
    proxy_url = 'geo.iproyal.com'
    port = '32325'
    user = 'leiroz7'
    password = 'arvore11_country-br'
except NoSectionError as e:
    input(
        f'Error!!, in config file \
            {str(e).strip("No section: ")} section not found')
except NoOptionError as e:
    input(
        f'Error!!, in config file \
             {str(e).strip("No section: ")} section not found')


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class AccountMaker:
    def __init__(self, token, country, operator, product, api_id, api_hash):
        self.color = bcolors
        self.country = int(countrys[str(country).capitalize()])
        self.token = token
        self.operator = operator
        self.product = product
        self.api_id = api_id
        self.api_hash = api_hash
        self.buy_param = (('api_key', self.token), ('action', 'getNumber'), (
            'service', self.product), ('operator', self.operator), ('country', self.country))
        self.balance_param = (('api_key', self.token),
                              ('action', 'getBalance'))
        self.url = 'https://sms-activate.ru/stubs/handler_api.php'
        self.counter = 60

    def create_account(self):
        balance = float(
            str(get(self.url, params=self.balance_param).text).split(":")[-1])
        try:
            print(self.color.OKGREEN +
                  f"\nBalance : {balance}\n"+self.color.ENDC)

            self.country = choice([32, 12, 73])

            # Faça a mudança de senha, para romenia, estados unidos, filipinas e brazil
            password = ""
            if self.country == 32:
                password = "arvore11_country-ro"
                # # Realiza a requisição HTTP utilizando o proxy
                # response = requests.get('http://httpbin.org/ip', proxies=dict(
                #     http=f'socks5://{user}:{password}@{proxy_url}:{port}', https=f'socks5://{user}:{password}@{proxy_url}:{port}'))

                # # Verifica o resultado
                # if response.status_code == 200:
                #     print("Requisição bem-sucedida!")
                #     ip = response.json()['origin']
                #     response = requests.get(f'http://ip-api.com/json/{ip}')
                #     # com base no ip retorna a cidade e pais
                #     print(self.color.OKCYAN +
                #           f"Country: {response.json()['country']} | City: {response.json()['city']}"+self.color.ENDC)
                # else:
                #     print(
                #         f"Erro na requisição. Código de status: {response.status_code}")
            elif self.country == 12:
                password = "arvore11_country-us"
                # # Realiza a requisição HTTP utilizando o proxy
                # response = requests.get('http://httpbin.org/ip', proxies=dict(
                #     http=f'socks5://{user}:{password}@{proxy_url}:{port}', https=f'socks5://{user}:{password}@{proxy_url}:{port}'))

                # # Verifica o resultado
                # if response.status_code == 200:
                #     print("Requisição bem-sucedida!")
                #     ip = response.json()['origin']
                #     response = requests.get(f'http://ip-api.com/json/{ip}')
                #     # com base no ip retorna a cidade e pais
                #     print(self.color.OKCYAN +
                #           f"Country: {response.json()['country']} | City: {response.json()['city']}"+self.color.ENDC)
                # else:
                #     print(
                #         f"Erro na requisição. Código de status: {response.status_code}")
            elif self.country == 4:
                password = "arvore11_country-ph"
                # # Realiza a requisição HTTP utilizando o proxy
                # response = requests.get('http://httpbin.org/ip', proxies=dict(
                #     http=f'socks5://{user}:{password}@{proxy_url}:{port}', https=f'socks5://{user}:{password}@{proxy_url}:{port}'))

                # # Verifica o resultado
                # if response.status_code == 200:
                #     print("Requisição bem-sucedida!")
                #     ip = response.json()['origin']
                #     response = requests.get(f'http://ip-api.com/json/{ip}')
                #     # com base no ip retorna a cidade e pais
                #     print(self.color.OKCYAN +
                #           f"Country: {response.json()['country']} | City: {response.json()['city']}"+self.color.ENDC)
                # else:
                #     print(
                #         f"Erro na requisição. Código de status: {response.status_code}")
            elif self.country == 73:
                password = "arvore11_country-br"
                # # Realiza a requisição HTTP utilizando o proxy
                # response = requests.get('http://httpbin.org/ip', proxies=dict(
                #     http=f'socks5://{user}:{password}@{proxy_url}:{port}', https=f'socks5://{user}:{password}@{proxy_url}:{port}'))

                # # Verifica o resultado
                # if response.status_code == 200:
                #     print("Requisição bem-sucedida!")
                #     ip = response.json()['origin']
                #     response = requests.get(f'http://ip-api.com/json/{ip}')
                #     # com base no ip retorna a cidade e pais
                #     print(self.color.OKCYAN +
                #           f"Country: {response.json()['country']} | City: {response.json()['city']}"+self.color.ENDC)
                # else:
                #     print(
                #         f"Erro na requisição. Código de status: {response.status_code}")

            print(self.color.OKCYAN +
                  f"Password: {password}"+self.color.ENDC)

            response = str(
                get(self.url, params=self.buy_param).text).split(":")

            # Se não retornar, ele muda de pais, e tenta novamente
            if len(response) >= 3:
                phone = response[2]
                id = response[1]
            else:
                print(
                    self.color.FAIL + f"Failed to get number in {list(countrys.keys())[list(countrys.values()).index(str(self.country))]}, changing country..."+self.color.ENDC)
                self.create_account()

            print(self.color.OKCYAN +
                  f"Number: {phone} | Number ID: {id}\n" + self.color.ENDC)

            # Desistanlando Telegram X
            print('Desinstalando Telegram X')
            device.uninstall('org.thunderdog.challegram')

            # instalar apk de um app no celular
            device.install('Telegram.apk')
            print('App instalado')

            # Preparando Ambiete
            print(self.color.OKBLUE+"Ambiente Preparado..."+self.color.ENDC)

            # Abrir o app
            print(self.color.OKBLUE+"Abrindo Telegram..."+self.color.ENDC)
            device.shell('input swipe 500 1500 500 250')
            device.shell('input tap 930 1370')
            sleep(3)

            print(self.color.OKBLUE+"Iniciando Telegram..."+self.color.ENDC)
            device.shell('input tap 530 2000')
            sleep(2)

            try:
                print(self.color.OKBLUE+"Inserindo número..."+self.color.ENDC)

                # Apagar campo de texto
                for i in range(15):
                    device.shell('input keyevent 67')

                self.code_sent(id)
                return self.get_code(id, phone)
            except rpcerrorlist.PhoneNumberBannedError:
                self.cancel_order(phone=phone, id=id, ban=True)
                return self.create_account()
            except rpcerrorlist.FloodWaitError:
                self.cancel_order(phone=phone, id=id, flood=True)
                return self.create_account()
            except rpcerrorlist.PhoneNumberInvalidError:
                self.cancel_order(phone=phone, id=id, flood=True)
                return self.create_account()
        except KeyboardInterrupt:
            print(self.color.FAIL+"\nSaindo...\n"+self.color.ENDC)
            sleep(2)
            return main()
        except IndexError:
            input(response)
            return main()

    def code_sent(self, id):
        params = (('api_key', self.token), ('action', 'setStatus'),
                  ('status', '1'), ('id', id))
        get(self.url, params=params)

    def get_code(self, id, phone):
        params = (('api_key', self.token),
                  ('action', 'getStatus'), ('id', id),)

        print(self.color.OKBLUE+"Digitando número..."+self.color.ENDC)
        device.shell(f'input text {phone}')
        device.shell('input tap 940 1400')
        device.shell('input tap 870 1486')
        device.shell('input tap 544 1266')

        print(self.color.OKBLUE+"Aguardando o SMS....."+self.color.ENDC)

        while True:
            if self.counter == 0:
                self.cancel_order(id, phone)
                return self.create_account()
            response = str(get(self.url, params=params).text)
            if response != "STATUS_WAIT_CODE":
                try:
                    code = response.split(":")[-1]
                    print(self.color.OKGREEN +
                          f"\nCódigo recebido: {code}\n"+self.color.ENDC)

                    sleep(5)
                    device.shell('input tap 483 653')
                    sleep(2)
                    device.shell('input tap 800 1200')

                    print(self.color.OKBLUE+"Inserindo código..."+self.color.ENDC)
                    device.shell(f'input text {code}')
                    sleep(2)

                    print("Autendicando...")

                    # Pega um nome aleatório
                    with open("data/names.txt") as f:
                        names = str(f.read()).split("\n")
                    name = choice(names)
                    device.shell(f'input text {name}')
                    sleep(2)

                    # Clica em continuar
                    print("Clicando em continuar...")
                    device.shell('input tap 950 1340')
                    sleep(2)

                    # Aceita os termos
                    print("Aceita os termos...")
                    device.shell('input tap 870 1695')
                    sleep(2)

                    # Find Contancts
                    print("Negando...")
                    device.shell('input tap 634 1318')
                    sleep(2)

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

                    async def fill_phone_number():  # Coloca o  no terminal e salvar a seção
                        client = TelegramClient(f'sessions/{phone}', self.api_id, self.api_hash,
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

                    self.save_number(phone)
                    self.finish(id)
                    self.wait()
                    return self.create_account()
                except IndexError:
                    input(response)
                    return main()
                except SessionPasswordNeededError:
                    print(
                        self.color.FAIL+"\nThis account was taken by someone else and the password was added, sorry you won't get your money back :(\n" + self.color.ENDC)
                    self.wait()
                    return self.create_account()
                except PhoneNumberUnoccupiedError:
                    with open("data/names.txt") as f:
                        names = str(f.read()).split("\n")
                    print(self.color.OKGREEN+f"\nSucesso!!!\n"+self.color.ENDC)
                    self.save_number(phone)
                    self.finish(id)
                    self.wait()
                    return self.create_account()
                except Exception as e:
                    input(e.__class__.__name__)
            else:
                sleep(5)
                self.counter -= 5
                continue

    def cancel_order(self, id, phone, ban=False, flood=False):
        params = (('api_key', self.token), ('action', 'setStatus'),
                  ('status', '-1'), ('id', id))
        if ban:
            print(self.color.FAIL +
                  '\n[*] Number blocked by telegram, canceling number..'+self.color.ENDC)
            # Apagando App
            print(self.color.OKBLUE+"Desinstalando Telegram..."+self.color.ENDC)
            device.uninstall('org.thunderdog.challegram')
        elif flood:
            print(self.color.FAIL +
                  '\n[*] Number has a waiting time, Number is canceling..'+self.color.ENDC)
            print(self.color.OKBLUE+"Desinstalando Telegram..."+self.color.ENDC)
            device.uninstall('org.thunderdog.challegram')
        else:
            print(self.color.FAIL +
                  "\n[*] Failed to get code within specified time, Canceling number.."+self.color.ENDC)
            print(self.color.OKBLUE+"Desinstalando Telegram..."+self.color.ENDC)
            device.uninstall('org.thunderdog.challegram')
        if get(self.url, params=params).text == "ACCESS_CANCEL":
            self.wait()
        try:
            remove(f"sessions/{phone}.session")
        except:
            pass
        return

    def save_number(self, number):
        with open("data/phones.json", "r") as f:
            data = load(f)
        data['phone_numbers'].append(number)
        with open("data/phones.json", "r+") as f:
            dump(data, f)

    def finish(self, id):
        params = (('api_key', self.token), ('action', 'setStatus'),
                  ('status', '6'), ('id', id))
        get(self.url, params=params)

    def wait(self):
        print(self.color.WARNING +
              "\nWaiting for 10 seconds for new account..."+self.color.ENDC)
        sleep(10)


def banner():
    print(bcolors.WARNING+"""
[+] Telegram Tools
[+] Producer Lucas Henrique
"""+bcolors.ENDC)


def menu():
    print(bcolors.OKCYAN+"""\n
*************************** MENU ********************** ********
*                                                             *
* [1] Account Builder
*                                                             *
***************************************************************
"""+bcolors.ENDC)


def main():
    try:
        system("cls")
        banner()
        menu()
        op = input(bcolors.OKGREEN+"\nOpção :> "+bcolors.ENDC)
        if str(op) == "1":
            maker = AccountMaker(token=c_token, country=c_country, operator=c_operator,
                                 product=c_product, api_id=c_api_id, api_hash=c_ap_hash)
            system("cls")
            banner()
            maker.create_account()
        elif str(op).lower() == "q":
            exit()
        else:
            input("Incorrect operation")
            return main()
    except KeyboardInterrupt:
        print("\nSaindo...")
        exit()


if __name__ == "__main__":
    try:
        system("cls")
        banner()
        main()
    except KeyboardInterrupt:
        print("\nSaindo...")
        exit()
