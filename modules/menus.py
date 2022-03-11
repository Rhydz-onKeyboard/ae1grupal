import inquirer

def pause():
    key_input = [inquirer.Text( name = 'pausa', message= 'Presione ENTER para continuar')]
    return inquirer.prompt(key_input)

def main_menu():
    print('=================================')
    print('     Seleccione una opcion       ')
    print('=================================')

    questions = [
        {'value': 1, 'name':'Clientes'},
        {'value': 2, 'name':'Productos'},
        {'value': 3, 'name':'Vendedores'},
        {'value': 4, 'name':'Salir'},
    ]

    main_questions = [
        inquirer.List('opcion',
            message='Que desea hacer?',
            choices=[ f"{_['value']}. {_['name']}" for _ in questions],
            carousel=True
        ),
    ]

    return inquirer.prompt(main_questions)

def clients_menu():
    print('=================================')
    print('            Clientes             ')
    print('=================================')

    questions = [
        {'value': 1, 'name':'Mostrar Clientes'},
        {'value': 2, 'name':'Agregar Cliente'},
        {'value': 3, 'name':'Eliminar Cliente'},
        {'value': 4, 'name':'Atras'},
    ]
  
    client_questions = [
        inquirer.List('clientes',
            message='Que desea hacer?',
            choices=[ f"{_['value']}. {_['name']}" for _ in questions],
            carousel=True
        ),
    ]

    return inquirer.prompt(client_questions)

def products_menu():
    print('=================================')
    print('            Productos             ')
    print('=================================')

    questions = [
        {'value': 1, 'name':'Mostrar Productos'},
        {'value': 2, 'name':'Agregar Producto'},
        {'value': 3, 'name':'Eliminar Producto'},
        {'value': 4, 'name':'Atras'},
    ]
  
    products_questions = [
        inquirer.List('productos',
            message='Que desea hacer?',
            choices=[ f"{_['value']}. {_['name']}" for _ in questions],
            carousel=True
        ),
    ]

    return inquirer.prompt(products_questions)

def seller_menu():
    print('=================================')
    print('            Vendedores             ')
    print('=================================')

    questions = [
        {'value': 1, 'name':'Mostrar Vendedores'},
        {'value': 2, 'name':'Agregar Vendedor'},
        {'value': 3, 'name':'Eliminar Vendedor'},
        {'value': 4, 'name':'Atras'},
    ]
  
    seller_questions = [
        inquirer.List('vendedores',
            message='Que desea hacer?',
            choices=[ f"{_['value']}. {_['name']}" for _ in questions],
            carousel=True
        ),
    ]

    return inquirer.prompt(seller_questions)

def add_client():
    new_client = [
        inquirer.Text( name = 'name', message ='Cual es tu nombre?'),
        inquirer.Text( name = 'last', message ='Cual es tu apellido?'),
        inquirer.Text( name = 'email', message ='Escribe tu email'),
        inquirer.Text( name = 'saldo', message ='Cual es tu saldo?'),
        ]
    return inquirer.prompt(new_client)

def add_product():
    new_product = [
        inquirer.Text( name = 'name', message ='Cual es el nombre del producto?'),
        inquirer.Text( name = 'category', message ='A que categoria pertenece?'),
        inquirer.Text( name = 'supplier', message ='Cual es el proveedor?'),
        inquirer.Text( name = 'stock', message ='Cual es el stock que tienes?'),
        inquirer.Text( name = 'value', message ='Cual es valor neto?'),
        ]
    return inquirer.prompt(new_product)

def add_seller():
    new_product = [
        inquirer.Text( name = 'rut', message ='Cual es el rut del vendedor?'),
        inquirer.Text( name = 'name', message ='Cual es el nombre?'),
        inquirer.Text( name = 'last', message ='Cual es el apellido?'),
        inquirer.Text( name = 'section', message ='A que seccion pertenece?'),
        inquirer.Text( name = 'commission', message ='Cual es la comision de venta?'),
        ]
    return inquirer.prompt(new_product)

def list_client_to_delete(clients = []):
    client_to_delete = [inquirer.List('clientes', 
        message = 'Selecciones el cliente a eliminar', 
        choices = [f"El cliente: {_['nombre']} {_['apellido']} - id: {_['id_cliente']}" for _ in clients])
    ]
    return inquirer.prompt(client_to_delete)

def list_product_to_delete(product = []):
    product_to_delete = [inquirer.List('productos', 
        message = 'Selecciones el producto a eliminar', 
        choices = [f"El producto: {_['nombre']} - SKU: {_['SKU']}" for _ in product])
    ]
    return inquirer.prompt(product_to_delete)

def list_seller_to_delete(seller = []):
    seller_to_delete = [inquirer.List('vendedor', 
        message = 'Selecciones el producto a eliminar', 
        choices = [f"El vendedor: {_['nombre']} {_['apellido']} - RUT: {_['rut']}" for _ in seller])
    ]
    return inquirer.prompt(seller_to_delete)


def confirm_remove(text):
    question = [
        inquirer.Confirm('confirmar',
            message = f'Se eliminara el {text}, quieres continuar?'
        )
    ]
    return inquirer.prompt(question)