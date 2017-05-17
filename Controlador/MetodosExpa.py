from Controlador.TokenExpa import Informacion
from urllib.parse import  urlencode
import json
import requests
class MetodosExpa:


    @staticmethod
    def getPrimerosEps( Usuario,Clave):
        objInformacion=Informacion(Usuario,Clave)
        token,Resultado=objInformacion.getToken()
        if(Resultado):
            params = {"access_token": token
                , "page": 1
                , "per_page": 100
                }
            baseUrl = "https://gis-api.aiesec.org/{version}/{routes}?{params}"
            url = baseUrl.format(version='v2', routes="people", params=urlencode(params, True))
            print(url)
            r = requests.get(url)
            if int(r.status_code) == 200:
                return True,json.loads(r.text),r.status_code
            else:
                return False,None,r.status_code
        else:
            return False, None, 500