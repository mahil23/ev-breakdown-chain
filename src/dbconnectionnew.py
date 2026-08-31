import os
import pymysql
from dotenv import load_dotenv
from src.env_utils import get_required_env

# Load environment variables
load_dotenv()

DB_HOST = get_required_env('DB_HOST')
DB_PORT = int(get_required_env('DB_PORT'))
DB_USER = get_required_env('DB_USER')
DB_PASSWORD = get_required_env('DB_PASSWORD')
DB_NAME = get_required_env('DB_NAME')



def iud(qry,val):
    con=pymysql.connect(host=DB_HOST,port=DB_PORT,user=DB_USER,password=DB_PASSWORD,db=DB_NAME)
    cmd=con.cursor()
    cmd.execute(qry,val)
    id=cmd.lastrowid
    con.commit()
    con.close()

    return id

def selectone(qry,val):
    con=pymysql.connect(host=DB_HOST,port=DB_PORT,user=DB_USER,password=DB_PASSWORD,db=DB_NAME,cursorclass=pymysql.cursors.DictCursor)
    cmd=con.cursor()
    cmd.execute(qry,val)
    res=cmd.fetchone()

    return res

def selectall(qry):
    con=pymysql.connect(host=DB_HOST,port=DB_PORT,user=DB_USER,password=DB_PASSWORD,db=DB_NAME,cursorclass=pymysql.cursors.DictCursor)
    cmd=con.cursor()
    cmd.execute(qry)
    res=cmd.fetchall()
    return res
def selectall2(qry,val):
    con=pymysql.connect(host=DB_HOST,port=DB_PORT,user=DB_USER,password=DB_PASSWORD,db=DB_NAME,cursorclass=pymysql.cursors.DictCursor)
    cmd=con.cursor()
    cmd.execute(qry,val)
    res=cmd.fetchall()
    return res