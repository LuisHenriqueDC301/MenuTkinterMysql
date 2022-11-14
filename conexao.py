import pymysql as MySQLdb
#Conexão com o Bando de Dados(bd.sql)
conexao = MySQLdb.connect(host="localhost", user="root", passwd="",db="Conta",port=3307)
banco = conexao.cursor()
