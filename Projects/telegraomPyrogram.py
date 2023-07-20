from pyrogram import Client

api_id = '10103155'
api_hash = '13bddab82f9a0f7188686ee7b5558663'

def register_account():
    with Client("my_account", api_id, api_hash) as app:
        phone_number = input("Digite seu número de telefone com o código do país: ")
        app.send_code(phone_number)
        code = input("Digite o código de verificação recebido: ")
        app.sign_up(phone_number, code, first_name=input("Digite seu primeiro nome: "),
                     last_name=input("Digite seu último nome (opcional): "))
        print("Registro concluído com sucesso!")

if __name__ == '__main__':
    register_account()
