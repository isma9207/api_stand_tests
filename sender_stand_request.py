import configuration
import requests
import data

''' 
Hacer una solicitud GET que te regrese a la página de documentación para la API
(API Docs) de Urban Grocers.
'''
'''
def get_docs():
    return requests.get(configuration.URL_SERVICE + configuration.DOC_PATH)

response = get_docs()

print(response.headers) #Muestra los encabezados de respuesta
print(response.status_code) #Muestra el codigo de respuesta
print(response.ok) #Devuelve "True" si el código es 2xx o 3xx
print(response.url) #Muestra la direccion de la solicitud
print(response.request) #Muestra el metodo de la solicitud
print(response.text) #Muestra el cuerpo de la respuesta en formato de texto
print(response.json()) #Pasa los datos de respuesta al diccionario, de lo contrario, se devolverá un error
'''
''' 
Hacer una solicitud GET que te regrese los logs para la API
de Urban Grocers.
'''
'''
def get_logs():
    return requests.get(configuration.URL_SERVICE + configuration.LOG_MAIN_PATH, params={'count': 20})

response = get_logs()

print(response.status_code)
print(response.headers)
'''
'''
Hacer una solicitud GET que reciba los datos de la tabla de la base de datos para la API
de Urban Grocers.
'''

def get_users_table():
    return requests.get(configuration.URL_SERVICE + configuration.USERS_TABLE_PATH)

response = get_users_table()

#print(response.status_code)

'''
Hacer una solicitud POST para crear un nuevo usuario
'''

def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,  # inserta la dirección URL completa
                         json=body,  # inserta el cuerpo de solicitud
                         headers=data.headers)  # inserta los encabezados

response = post_new_user(data.user_body)

#print(response.status_code)
#print(response.json())

'''
Hacer una solicitud POST para buscar los kits por sus productos
'''
'''
def post_products_kits(products_id):
    return requests.post(configuration.URL_SERVICE + configuration.PRODUCTS_KITS_PATH,
                         json=products_id,
                         headers=data.headers)

response = post_products_kits(data.product_ids)

print(response.status_code)
print(response.json())
'''
