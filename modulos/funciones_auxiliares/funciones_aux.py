#esta funcion se encargara de agendar el cbu a una lista
def agendar_CBUs (cuenta, lista):
    cbu = int(input("Escriba el CBU que quiere agendar: ")) #el usuario lo ingresa
    lista.append (cbu) #lo agrego a la lista
    print("\nCBU agendado correctamente\n") #imprimo mensaje
    return lista #retorno la lista

#funcion que verifica si la lista se encuentra o no vacia
def is_empty(data_structure):
    if data_structure:
        return False
    else:
        return True

#importo el modulo para utilizar la funcion

############################
#import funciones_aux as fu
############################

#funcion encargada de transferir dinero a un cbu perteneciente a la lista
def transf_dinero (cuenta, lista):
  
  #verifico si la lista de CBUs se encuentra o no vacia
  if (is_empty(lista)):
    print("\nLa lista de CBUs se encuentra vacia")
    return cuenta
  else:
   monto = float(input("Monto a transferir: ")) #guardo el monto que la persona desea transferir
   cbu = int(input("Ingrese el CBU de la persona: ")) #le pido que ingrese el cbu 
    
    #a continuacion recorro la lista
   for cbus in lista:
      #si el monto es menor a 5000 pesos, el cbu ingresado se encuentra en la lista y hay suficiente dinero en la cuenta
      if (monto <= 5000) and (cbu == cbus) and (monto<= cuenta):
        cuenta -= monto #le resto a la cuenta la cantidad que transfirio
        print("\nEl monto fue transferido correctamente") #imprimo mensaje
        return cuenta #retorno cuenta modificada
        
        #si el cbu no se encuentra registrado
      elif (cbu != cbus):
        print("\nEse CBU no se encuentra en la lista")
        return cuenta
         
        #si el monto excede el minimo permitido
      elif (monto > 5000):
        print("\nEl monto ingresado supera los maximos, solo se transferiran $5000")
        cuenta -= 5000 #solo transfiero los 5000
        return cuenta #retorno cuenta modificada
         
        #si no hay suficiente dinero en la cuenta para transferir ese monto
      elif (monto > cuenta):
        print("\nNo hay dinero suficiente en la cuenta") #imprimo mensaje en pantalla
        return cuenta #retorno cuenta
