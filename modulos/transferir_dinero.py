#importo modulo con funciones auxiliares
#import funciones_aux as fa

from modulos.funciones_auxiliares import funciones_aux as fa

#imprimo un sub-menu de opciones y guardo la opcion seleccionada, luego comparo y llamo a las funciones que se encuentran en el modulo importado
def transferirDinero (cuenta, lista):
    print ("\n\tSUB-MENU DE OPCIONES\n\t\t1. Agendar CBUs\n\t\t2. Transferir dinero")
    opcion = int(input("Ingrese la opcion que desea: "))
    #opcion de agendar cbu
    if (opcion == 1):
        lista = fa.agendar_CBUs (cuenta, lista)
        return cuenta
    #opcion de transferir dinero
    elif (opcion == 2):
            cuenta = fa.transf_dinero (cuenta, lista)
            return cuenta
    #opcion default
    else:
         print("\nOpcion no valida")
         return cuenta