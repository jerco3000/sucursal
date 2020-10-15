from flask import Flask, request, jsonify
from flask_cors import CORS
from h3 import h3
from flask_mysqldb import MySQL
import random

app = Flask(__name__)
CORS(app)
cors = CORS(app, resources={
	r"/*": {
		"origins": "*"
	}
})

app.config["MYSQL_HOST"] = "pagaqui1-free.ctzubts1isjg.sa-east-1.rds.amazonaws.com"
app.config["MYSQL_PORT"] = 53306
app.config["MYSQL_USER"] = "admin"
app.config["MYSQL_PASSWORD"] = "kfsdppf50uopcx"
app.config["MYSQL_DB"] = "pagaqui"
mysql = MySQL(app)

@app.route("/sucursal",methods=['POST'])
def sucursal(event=None, context=None):
	data = request.get_json()
	lat = data["lat"]
	long = data["long"]

	h3_address_9 = h3.geo_to_h3(float(lat),float(long), 9)
	h3_address_8 = h3.geo_to_h3(float(lat),float(long), 8)

	cur = mysql.connection.cursor()
	#sql = '''SELECT emp_run, suc_empresa_id FROM Sucursales WHERE emp_run=%s and suc_cuadrante_9 = "%s"'''
	sql = '''SELECT e.emp_nombrecorto,s.emp_run,s.suc_empresa_id,s.suc_nombre,e.emp_logo_url,e.emp_color_fondo,s.suc_id FROM Sucursales s JOIN Empresas e ON s.emp_run = e.emp_run WHERE e.emp_run=0 or suc_9_cuadrante1="%s" OR suc_9_cuadrante2="%s" OR suc_9_cuadrante3="%s" OR suc_9_cuadrante4="%s" OR suc_9_cuadrante5="%s" OR suc_9_cuadrante6="%s" OR suc_9_cuadrante7="%s"''' 
	#sql = '''SET @cuadrante= '%s'; SELECT e.emp_nombrecorto,s.emp_run,s.suc_empresa_id,s.suc_nombre,e.emp_logo_url,e.emp_color_fondo FROM Sucursales s JOIN Empresas e ON s.emp_run = e.emp_run WHERE suc_9_cuadrante1=@cuadrante OR suc_9_cuadrante2=@cuadrante OR suc_9_cuadrante3=@cuadrante OR suc_9_cuadrante4=@cuadrante OR suc_9_cuadrante5=@cuadrante OR suc_9_cuadrante6=@cuadrante OR suc_9_cuadrante7=@cuadrante; '''
	data = (h3_address_9, h3_address_9, h3_address_9, h3_address_9, h3_address_9, h3_address_9, h3_address_9)
	#data = (h3_address_9)

	#print (sql % data)
	cur.execute(sql % data)
	rv = cur.fetchall()

	lista = []
	for row in rv:
		#lista.append({'emp_nombrecorto': row[0], 'emp_run' : row[1], 'suc_empresa' : row[2], 'suc_nombre' : row[3], 'emp_logo_url' : row[4], 'emp_color_fondo' : row[5]})
		lista.append({'suc_id' : row[6], 'emp_color_fondo' : row[5],'emp_logo_url' : row[4], 'suc_nombre' : row[3], 'suc_empresa' : row[2], 'emp_run' : row[1], 'emp_nombrecorto': row[0]})
	# ##############################################
	# Si no trae nada, deberia buscar en resolucion 8 tambien si no trae nada en 8, debe volver json con error indicando 
	# que no hay sucursal de esta tienda en esta posicion

	return jsonify(lista)
	#return jsonify(lista)

@app.route("/producto",methods=['POST'])
def producto(event=None, context=None):
        data = request.get_json()
        emp_run = data["emp_run"]
        suc_empresa_id = data["suc_empresa_id"]
        codigo = data["codigo"]

        cur = mysql.connection.cursor()
        sql = '''SELECT emp_run,suc_empresa_id,pp_codigo,pp_nombre, pp_descripcion,pp_url,pp_preciobruto,pp_iva,pp_precioneto from ProductosPrueba where emp_run=%s and suc_empresa_id="%s" and pp_codigo="%s";'''
        data = (emp_run, suc_empresa_id, codigo)

        #print (sql % data)
        cur.execute(sql % data)
        rv = cur.fetchall()

        lista = []
        for row in rv:
                #lista.append({'emp_nombrecorto': row[0], 'emp_run' : row[1], 'suc_empresa' : row[2], 'suc_nombre' : row[3]}]
                lista.append({'emp_run' : row[0], 'suc_empresa_id' : row[1],'pp_codigo' : row[2], 'pp_nombre' : row[3], 'pp_descripcion' : row[4], 'pp_url' : row[5], 'pp_preciobruto' : row[6], 'pp_iva' : row[7], 'pp_precioneto' : row[8], 'pp_cantidad' : 1})
        # ##############################################
        # Si no trae nada, deberia buscar en resolucion 8 tambien si no trae nada en 8, debe volver json con error indicando
        # que no hay sucursal de esta tienda en esta posicion

        return jsonify(lista)
        #return jsonify(lista)

@app.route("/productoDemo",methods=['POST'])
def productoDemo(event=None, context=None):
	data = request.get_json()
	emp_run = data["emp_run"]
	suc_empresa_id = data["suc_empresa_id"]
	codigo = data["codigo"]
	cur = mysql.connection.cursor()
	sql = '''SELECT emp_run,suc_empresa_id,pp_codigo,pp_nombre, pp_descripcion,pp_url,pp_preciobruto,pp_iva,pp_precioneto from ProductosPrueba where emp_run=0 and suc_empresa_id="1"'''
	#data = (emp_run, suc_empresa_id, codigo)
	cur.execute(sql)
	rv = cur.fetchall()
	numero = random.randrange(9)
	lista = []
	lista.append({'emp_run' : emp_run, 'suc_empresa_id' : suc_empresa_id,'pp_codigo' : codigo, 'pp_nombre' : rv[numero][3], 'pp_descripcion' : rv[numero][4], 'pp_url' : rv[numero][5], 'pp_preciobruto' : rv[numero][6], 'pp_iva' : rv[numero][7], 'pp_precioneto' : rv[numero][8], 'pp_cantidad' : 1})
	return jsonify(lista)
	
if __name__ == "__main__":
        app.run(host='0.0.0.0')

#for x in range(15):
#  h3_address = h3.geo_to_h3(-33.480760, -70.575850, x) # lat, log, hex resolution print "{} : {}".format(x,h3_address)
#hex_center_coordinates = h3.h3_to_geo(h3_address) # array of [lat, lng] hex_boundary = h3.h3_to_geo_boundary(h3_address)
#print h3_address

# *** RECORDAR ***
# *** Al añadir rutas aqui, tambien se deben añadir en NGNIX, para que reconozca y funcione el proxy
# *** Las pruebas para ver si funcionan pueden ser ejectudas desde FLASK_APP  recordar llamar a puerto 5000 y http
#
# sudo systemctl restart api-sucursal.service
# sudo systemctl restart nginx.service
# source env/bin/activate
# FLASK_APP=sucursal5 flask run --host=0.0.0.0
# deactivate