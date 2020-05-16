from flask import Flask, request, jsonify
from h3 import h3
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config["MYSQL_HOST"] = "pagaqui1-free.ctzubts1isjg.sa-east-1.rds.amazonaws.com"
app.config["MYSQL_PORT"] = 53306
app.config["MYSQL_USER"] = "admin"
app.config["MYSQL_PASSWORD"] = "kfsdppf50uopcx"
app.config["MYSQL_DB"] = "pagaqui"
mysql = MySQL(app)

@app.route("/sucursal", methods=['POST'])
def sucursal(event=None, context=None):
	data = request.get_json()
	lat = data["lat"]
	long = data["long"]

	h3_address_9 = h3.geo_to_h3(float(lat),float(long), 9)
	h3_address_8 = h3.geo_to_h3(float(lat),float(long), 8)

	cur = mysql.connection.cursor()
	#sql = '''SELECT emp_run, suc_empresa_id FROM Sucursales WHERE emp_run=%s and suc_cuadrante_9 = "%s"'''
	sql = '''SELECT e.emp_nombrecorto,s.emp_run,s.suc_empresa_id,s.suc_nombre,e.emp_logo_url,e.emp_color_fondo,s.suc_id FROM Sucursales s JOIN Empresas e ON s.emp_run = e.emp_run WHERE suc_9_cuadrante1="%s" OR suc_9_cuadrante2="%s" OR suc_9_cuadrante3="%s" OR suc_9_cuadrante4="%s" OR suc_9_cuadrante5="%s" OR suc_9_cuadrante6="%s" OR suc_9_cuadrante7="%s"''' 
	data = (h3_address_9, h3_address_9, h3_address_9, h3_address_9, h3_address_9, h3_address_9, h3_address_9)

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

if __name__ == "__main__":
        app.run(host='0.0.0.0')

#for x in range(15):
#  h3_address = h3.geo_to_h3(-33.480760, -70.575850, x) # lat, log, hex resolution print "{} : {}".format(x,h3_address)
#hex_center_coordinates = h3.h3_to_geo(h3_address) # array of [lat, lng] hex_boundary = h3.h3_to_geo_boundary(h3_address)
#print h3_address
