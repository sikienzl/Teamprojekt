#!/usr/bin/python3

import pymysql as mariadb
import configparser

config = configparser.ConfigParser()
config.read(os.path.dirname(os.path.abspath(__file__)) + '/connect.cfg')

try:
    # CONNECTION-Settings
    conn = mariadb.connect(
        host=config['CONNECTION']['host'],
        user=config['CONNECTION']['user'],
        passwd=config['CONNECTION']['passwd'],
        db=config['CONNECTION']['db'],
        charset=config['CONNECTION']['charset']
    )
    cursor = conn.cursor()
    sql = "INSERT INTO DVD(dvd_id, titel) VALUES (%s, %s)"
    cursor.execute(sql, ('2', 'Verrückte Weihnachten'))
    # write values hard into database
    conn.commit()
    # close all
    cursor.close()
    conn.close()
except Exception as e:
    print(
        'Connection Failed!\nError Code is %s;\nError Content is %s;' %
        (e.args[0], e.args[1]))
