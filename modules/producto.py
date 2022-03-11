from models.producto import Producto
from modules import menus
from helpers import uuid_generator

lista_productos = []

def products_menu(selected_option):
    if selected_option == '1':
        print(lista_productos)
    elif selected_option == '2':
        producto = menus.add_product()
        producto = Producto(
                        uuid_generator.create(4), 
                        producto['name'], 
                        producto['category'], 
                        producto['supplier'],
                        producto['stock'],
                        producto['value'],
                        )
        lista_productos.append(producto.get())
        print(f"Se agrego el producto: \n {producto.get()}")
    elif selected_option == '3':
        dato_eliminar = menus.list_product_to_delete(lista_productos)['productos'][-4:]
        for product in lista_productos:
            if product['SKU'] == dato_eliminar:
                confirm = menus.confirm_remove('producto')['confirmar']
                if confirm:
                    lista_productos.remove(product)
                else:
                    print('Regresaras al menu principal')