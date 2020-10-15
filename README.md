# sucursal

API en AWS entrega diferentes funciones.

1º /sucursal {"lat": "xxxx", "long", "yyy"}  devuelve listado de sucursales e informacion de las empresas cercanas.
2º /producto 
3º /transbank ??
4º /retail  avisa el retail de la transaccion finalizada.

pipenv --threepipenv shellpip install flaskFLASK_APP=hello.py flask runflask run --host=0.0. 0.0virtualenv envsource env/bin/activatedeativatevirtualenv -p python3 myenvsudo apt-get install sou    =====which cc/usr/bin/ccwhich make/usr/bin/makewhich cmake/usr/bin/cmakewhich git/usr/bin/gitpip3 install h3====pip3 install flaskpip3 installsudo pip3 install mysqlclientsudo pip3 install flask-mysqldbsudo pip3 install flask-mysqlhttps://www.youtube.com/watch?v=rDbxCeTzw_k1º Hay que crear nuevo entorno virtual2º hay que instalar todos los modulos localmente con "-t" , confirmar en video.        pip3 install xx -t .3º ¿que pasa con la H3 ejecutable en C, se podra instalar local?4º terminar de video el video para ver como subir y hacer prueba.crear pack para aws lambdapip3 install boto3 -t ./zip -r ../sucursal.zip .unzip -l sucursal.zipsudo apt-get install libmysqlclient-devsudo apt-get install libmariadbclient-devsudo pip3 install mysqlclientsudo pip3 install flask-mysqldbsudo pip3 install flask-mysqlflask gunicorn en aws:https://www.digitalocean.com/community/tutorials/como-preparar-aplicaciones-de-flask-con-gunicorn-y-nginx-en-ubuntu-18-04-eshttps://medium.com/@thucnc/deploy-a-python-flask-restful-api-app-with-gunicorn-supervisor-and-nginx-62b20d62691fhay que crear archivo wsgi:(env) ubuntu@ip-172-31-81-34:~/sucursal$ cat wsgi.pyfrom sucursal import appif __name__ == "__main__":    app.run()gunicorn --bind 0.0.0.0:5000 wsgi:appgunicorn -w 4 wsgi:appCORS
https://flask-cors.readthedocs.io/en/latest/

Browser no deja acceder a la 

https://stackoverflow.com/questions/25594893/how-to-enable-cors-in-flask


CODIGO USADO:

from flask import Flask, request, jsonify
from flask_cors import CORS
from h3 import h3
from flask_mysqldb import MySQL

app = Flask(__name__)
CORS(app)
cors = CORS(app, resources={
        r"/*": {
                "origins": "*"
        }
})


** hay que ver quizas como bloquear un poco, porque con este metodo acepta conexiones de todas partes, quizas
no se pueda activar dado que las peticiones vienen desde JAVASCRIPT...

*OJO:

Para el tema del GPS, se debe utilizar HTTPS para el dominio de la WEB, en local funciona porque LOCALHOST lo permite CHROME, pero si se trata de solicitar la posicion GPS desde una web sin HTTPS NO FUNCIONA...

OBLIGADO A INSTALAR EN AMAZON/DOCKER UN PROXY APACHE/ u otro adelante para que conteste HTTPS!!!

https://www.digitalocean.com/community/tutorials/como-preparar-aplicaciones-de-flask-con-gunicorn-y-nginx-en-ubuntu-18-04-es

/etc/systemd/system

sudo systemctl start api-sucursal.service
sudo systemctl stop api-sucursal.service

sudo systemctl start nginx.service
sudo systemctl restart nginx.service
sudo systemctl stop nginx.service
