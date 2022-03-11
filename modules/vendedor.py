from models.vendedor import Vendedor
from modules import menus

lista_vendedores = []

def seller_menu(selected_option):
    if selected_option == '1':
        print(lista_vendedores)
    elif selected_option == '2':
        vendedor = menus.add_seller()
        vendedor = Vendedor(
                        vendedor['rut'], 
                        vendedor['name'], 
                        vendedor['last'],
                        vendedor['section'],
                        vendedor['commission'],
                        )
        lista_vendedores.append(vendedor.get())
        print(f"Se agrego el producto: \n {vendedor.get()}")
    elif selected_option == '3':
        dato_eliminar = menus.list_seller_to_delete(lista_vendedores)['vendedor'][-10:]
        for seller in lista_vendedores:
            if seller['rut'] == dato_eliminar:
                confirm = menus.confirm_remove('vendedor')['confirmar']
                if confirm:
                    lista_vendedores.remove(seller)
                else:
                    print('Regresaras al menu principal')