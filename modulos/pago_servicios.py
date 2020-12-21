#esta funcion permite seleccionar el servicio a pagar e ingresar el monto 
def pagoServicios (cuenta):
    #imprimo en pantalla las opciones de servicio
    print("1. Luz\n2. Agua\n3. Electricidad\n4. Gas\n5. Cable\n6. Telefono\n7. Internet")
    
    #guardo la opcion deseada
    opcion = int(input("\nIngrese una opcion: "))
    
    #guardo el monto que desea pagar
    monto = float(input("\nIngrese el monto a pagar: "))
    
    #si hay suficiente dinero en la cuenta
    if (monto <= cuenta):
      print("\nServicio pagado correctamente")
      cuenta -= monto #le resto el monto
      return cuenta #retorno cuenta modificada
    #si no hay suficiente dinero en la cuenta
    else:
      print("\nNo hay suficiente dinero en la cuenta") #imprimo mensaje en pantalla
      return cuenta #retorno cuenta
        