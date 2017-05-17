from Controlador.MetodosExpa import  MetodosExpa
import csv
from time import gmtime, strftime
import time
class PrimerosEPs:
    Usuario=None
    Clave=None

    def __init__(self, Usuario,Clave):
        self.Usuario=Usuario
        self.Clave=Clave

    def Ejecutar(self,RutaGuardar):
        while True:
            Ahora=strftime("%Y-%m-%d-%H-%M-%S", gmtime())
            Estado,jsonPeople,Codigo=MetodosExpa.getPrimerosEps(self.Usuario,self.Clave)
            if(Estado):
                with open(RutaGuardar + '/' + Ahora + '.csv', 'w') as csvfile:
                    writer = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL,
                                        lineterminator='\n')
                    for people in jsonPeople["data"]:

                        id=people["id"]
                        email=people["email"]
                        url=people["url"]
                        first_name=people["first_name"]
                        full_name=people["full_name"]
                        last_name=people["last_name"]
                        home_lc=people["home_lc"]["name"]
                        profile_photo_url=people["profile_photo_url"]
                        cover_photo_url=people["cover_photo_url"]
                        status=people["status"]
                        phone=people["phone"]


                        data=[
                            str(id)
                            ,str(email)
                            ,str(url)
                            ,str(first_name)
                            ,str(full_name)
                            ,str(last_name)
                            ,str(home_lc)
                            ,str(profile_photo_url)
                            ,str(cover_photo_url)
                            ,str(status)
                            ,str(phone)
                        ]
                        writer.writerow(data)

            else:
                print("Error")
            print("dormir 60 minutos")
            time.sleep((60*60))


