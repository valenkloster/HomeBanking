#VARIABLES
cuenta = 0 #cuenta de la persona
opcion = 0 #opcion que elija el usuario
lista = [] #lista que va a almacenar los cbu ingresados

#importo los modulos
from modulos import ver_dinero as vr
from modulos import agregar_dinero as agregar
from modulos import pago_servicios as pago
from modulos import transferir_dinero as transferir

#realizo bucle hasta que el usuario elija la opcion salir
while (opcion != 5):
    print("\nMenu de opciones:\n\t1. Ver dinero en cuenta\n\t2. Agregar dinero\n\t3. Transferir dinero\n\t4. Pago de servicios\n\t5. Salir")
    opcion = int(input("Ingrese una opcion: ")) #guardo la opcion que selecciono
  
    #opcion 1
    if opcion == 1:
        vr.ver_dinero(cuenta)
    #opcion 2
    elif (opcion == 2):
        cuenta = agregar.agregarDinero(cuenta)
    #opcion 3
    elif (opcion == 3):
        cuenta = transferir.transferirDinero(cuenta, lista)        
    #opcion 4
    elif (opcion == 4):
        cuenta = pago.pagoServicios(cuenta)
    #opcion 5
    elif (opcion == 5):
        print("\nAdios!!\n")
    #opcion default
    else:
        print("\n Esa opcion no es valida\n")
