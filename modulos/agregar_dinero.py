#esta funcion va a permitir agregar un monto de dinero a la cuenta
def agregarDinero (cuenta):
    monto = float(input("\n\nIngrese el monto de dinero que desea agregar: ")) #la persona ingresa el monto

    #verifico que cumpla con las condiciones
    if (monto <= 1000):
     cuenta += monto #lo añado a la cuenta
     print("\nDinero agregado a la cuenta\n") #imprimo mensaje en pantalla
     return cuenta #retorno la cuenta modificada

     #si no cumple con el velos maximo 
    else:
      print("\nLo siento, el monto maximo de transaccion es $1000") #imprimo mensaje en pantalla
      return cuenta #retorno cuenta
