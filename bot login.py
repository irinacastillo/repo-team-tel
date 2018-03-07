login = str(input("ingrese su ID: "))
list(login)
if not login.isnumeric():            
    print ('esta mtricula: ', login, 'es invalida')
elif len(list(login)) == 8:
    print('la matricula', login, 'es valida')
else:
    print ('su matricula', login, 'es invalida')

while login == True:
    if login:
        continue
    else:
        break

archivo = input('dirreccion del archivo: ')
if not result_irina.csv.csv():
    print ('archivo no encontrado')
    
pass

with open ('d:/result_irina.csv.csv', 'r') as archivo:
    lineas = archivo.read().splitlines()
    lineas.pop(0)
    for i in lineas:
        linea = i.split(',')
        print (linea)
    


