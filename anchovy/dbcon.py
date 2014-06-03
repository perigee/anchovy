import ConfigParser

dbconnection = False


def get_db_con():


def _verify_db():
	config = ConfigParser.ConfigParser()
	config.read('example.cfg')
	dbname = config.get('database', 'dbname')
	dbport = config.get('database', 'dbport')
	dbuser = config.get('database', 'dbuser')
	dbpwd = config.get('database', 'dbpwd')
