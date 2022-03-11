from modules import menus, cliente, producto, vendedor

def value_opt(funcion, name):
    #Recibe el nombre del cuestionario para el inquirer.
    return funcion[name].split('.')[0]

def run():
    #funcion principal
    opt = ''
    while opt != '4':
        opt = value_opt(menus.main_menu(),'opcion')
        if opt == '1':
            clients_opt = value_opt(menus.clients_menu(),'clientes')
            cliente.clients_menu(clients_opt)
        elif opt == '2':
            product_opt = value_opt(menus.products_menu(),'productos')
            producto.products_menu(product_opt)
        elif opt == '3':
            seller_opt = value_opt(menus.seller_menu() ,'vendedores')
            vendedor.seller_menu(seller_opt)
        else:
            print('Nos vemos')
        if opt != 'salir':
            menus.pause()

if __name__ == '__main__':
    run()