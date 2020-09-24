import mysql.connector
from config_files import DatabaseConfiguration

mydb = mysql.connector.connect(host=DatabaseConfiguration.DATABASE["HOST_DIRECTION"],
                               user=DatabaseConfiguration.DATABASE["DB_USERNAME"],
                               password=DatabaseConfiguration.DATABASE["PASSWORD"],
                               database=DatabaseConfiguration.DATABASE["DATABASE"])
