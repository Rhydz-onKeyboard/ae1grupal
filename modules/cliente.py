from models.cliente import Cliente
from modules import menus
from helpers import uuid_generator
from datetime import datetime

lista_clientes = []

def clients_menu(selected_option):
    if selected_option == '1':
        print(lista_clientes)
    elif selected_option == '2':
        cliente = menus.add_client()
        cliente = Cliente(
                        uuid_generator.create(4), 
                        cliente['name'], 
                        cliente['last'], 
                        cliente['email'],
                        datetime.today().strftime('%d-%m-%Y'),
                        cliente['saldo']
                        )
        lista_clientes.append(cliente.get())
        print(f"Se agrego el cliente: \n {cliente.get()}")
    elif selected_option == '3':
        dato_eliminar = menus.list_client_to_delete(lista_clientes)['clientes'][-4:]
        for client in lista_clientes:
            if client['id_cliente'] == dato_eliminar:
                confirm = menus.confirm_remove('cliente')['confirmar']
                if confirm:
                    lista_clientes.remove(client)
                else:
                    print('Regresaras al menu principal')
