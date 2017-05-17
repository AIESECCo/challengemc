from Controlador.MetodosExpa import  MetodosExpa
import csv
from time import gmtime, strftime
class PrimerosEPs:
    Usuario=None
    Clave=None

    def __init__(self, Usuario,Clave):
        self.Usuario=Usuario
        self.Clave=Clave

    def Ejecutar(self,RutaGuardar):
        Ahora=strftime("%Y-%m-%d-%H-%M-%S", gmtime())
        Estado,jsonPeople,Codigo=MetodosExpa.getPrimerosEps(self.Usuario,self.Clave)
        if(Estado):
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

                with open(RutaGuardar+'/'+Ahora+'.csv', 'wb') as csvfile:
                    writer = csv.writer(RutaGuardar, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL,
                                        lineterminator='\n')
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
                    writer.writerow(bytes(data,'UTF-8'))

        else:
            print("Error")



