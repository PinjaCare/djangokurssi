# Tätä waitressia käytetään jos on Renderiä varten konfiguroitu, että
# käytössä on guvicorn, joka taas ei toimi Windowsissa.

from waitress import serve
from django_pro.wsgi import application

if __name__ == '__main__':
    print("Open browser in https://localhost:8000")
    serve(application, port='8000')