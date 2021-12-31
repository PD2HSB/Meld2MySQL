#!/usr/bin/python3

import pymysql
import sys
import easygui
import configparser

def error(message,boxtitle):
    easygui.msgbox(message,title= boxtitle)
    exit()
    
debug   = 0
lengte  = len(sys.argv)

if lengte != 9:
    error('Please add the following string to PDW:' + "\n" + '"%1" "%2" "%3" "%4" "%5" "%6" "%7" "%8"', "ERROR")
else:
    arg1    = sys.argv[1].replace("'","")
    arg2    = sys.argv[2].replace("'","")
    arg3    = sys.argv[3].replace("'","")
    arg4    = sys.argv[4].replace("'","")
    arg5    = sys.argv[5].replace("'","")
    arg6    = sys.argv[6].replace("'","")
    arg7    = sys.argv[7].replace("'","")
    arg8    = sys.argv[8].replace("'","")

try:
    config  = configparser.ConfigParser()
    config.read('meld2mysql.config')
    dbserver= config['MYSQL']['dbserver']
    dbuser  = config['MYSQL']['dbuser']
    dbpass  = config['MYSQL']['dbpass']
    dbname  = config['MYSQL']['dbname']
    dbtable = config['MYSQL']['dbtable']

except:
    error("Configuratiebestand niet gevonden!","ERROR")

#sql = "INSERT INTO " + dbtable + " ('address', 'time', 'date', 'mode', 'type', 'bitrate', 'message', 'label') VALUES ('" + arg1 + "', '" + arg2 + "', '" + arg3 + "', '" + arg4 + "', '" + arg5 + "', '" + arg6 + "', '" + arg7 + "', '" + arg8 + "')"
#print(sql)



db = pymysql.connect(
    host        = dbserver,
    user        = dbuser,
    password    = dbpass,
    database    = dbname)
cursor = db.cursor()

sql = "INSERT INTO `" + dbtable + "` (`address`, `time`, `date`, `mode`, `type`, `bitrate`, `message`, `label`) VALUES ('" + arg1 + "', '" + arg2 + "', '" + arg3 + "', '" + arg4 + "', '" + arg5 + "', '" + arg6 + "', '" + arg7 + "', '" + arg8 + "')"
print(sql)
try:
    cursor.execute(sql)
    db.commit()
    print("succes")

except:
    db.rollback()
    print("error")

db.close()

#except:
#    easygui.msgbox("Database fout","ERROR")

if debug == 1:
    debugmysql = [dbserver,dbuser,dbpass,dbname,dbtable]
    debugargs  = [arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8]
    easygui.msgbox(str(debugmysql) + "\n" + str(debugargs) ,"")

