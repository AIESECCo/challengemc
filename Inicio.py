from Vista.PrimerosEPs import PrimerosEPs

Usuario=input("Ingrese el usuario de expa: ")
Clave=input("Ingrese la clave del usuario: ")
RutaArchivo=input("Ruta para guardar el archivo: ")
objPrimerosEPs=PrimerosEPs(Usuario,Clave)

objPrimerosEPs.Ejecutar(RutaArchivo)