from bs4 import BeautifulSoup
import requests
import csv

class Informacion():
    Correo = None
    Contrasenia = None

    def __init__(self, Correo, Contrasenia):
        self.Correo = Correo
        self.Contrasenia = Contrasenia

    def getToken(self):

        params = {
            'user[email]': self.Correo,
            'user[password]': self.Contrasenia,
            'commit': 'Sign in'
        }

        _apiUrl = "https://gis-api.aiesec.org/v1/{palabra1}/{palabra2}?access_token={token}"
        AUTH_URL = "https://auth.aiesec.org/users/sign_in"
        s = requests.Session()
        token_response = s.get(AUTH_URL).text
        soup = BeautifulSoup(token_response, 'html.parser')
        test = soup.find("form")  # , name="authenticity_token").value
        token = soup.find("form").find(attrs={'name': 'authenticity_token'}).attrs[
            'value']  # , name="authenticity_token").value
        params['authenticity_token'] = token
        response = s.post(AUTH_URL, data=params)
        try:
            token = response.history[-1].cookies["expa_token"]
            print(token)
            return token, True
        except KeyError:
            cookies = response.history[-1].cookies
            print("Cuenta inválida, o ha cambiado el modo de autenticación")
            return None, False