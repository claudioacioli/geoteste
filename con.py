import psycopg2

host = '192.168.122.164'
port = 5432
database = 'geo'
username = 'geo'
password = 'geo'

conn = None
try:
	conn = psycopg2.connect(
		user=username, 
		password=password, 
		host=host, 
		port=port, 
		database=database)
	cursor = conn.cursor()
	cursor.execute('select version();')
	record = cursor.fetchone()
	print('Version', record, '\n')
except Exception as ex:
	print(ex)
finally:
	if conn:
		cursor.close()
		conn.close()
		print('POst close')
