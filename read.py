'''
Created on Jul 21, 2018

@author: x35fe
'''

import sqlite3 as lite
import sys
import csv
from _datetime import datetime

from flask import Flask, render_template

app = Flask(__name__)

con = lite.connect('test.db')

A = open("input.txt", 'r')



def validate(date_text):
    try:
        datetime.strptime(date_text, '%Y-%m-%d')
        return True
    except ValueError:
        return False
    
    
def validate_id(pid):
    try:
        num = int(pid)
        return True
    except ValueError:
        return False

def validate_lo(lo):
    try:
        num = float(lo)
        if num > 0:
            return True
        else : return False
    except ValueError:
        return False
    
def Validate_la(la):
    try:
        num = float(la)
        if num < 0:
            return True
        else : return False
    except ValueError:
        return False
    
def Validate_ele(elevation):
    try:
        num = int(elevation)
        if num >= 0:
            return True
        else : return False
    except ValueError:
        return False
        
        
    




with con:
 
    cur = con.cursor()    
    #cur.execute("CREATE TABLE PRO(ID INI, DESCRIPTION varchar(255), DATETIME datetime, LONGITUDE float(20,10),LATITUDE float(20,10), ELEVATION INT)")
     #LONGITUDE float(20,10),LATITUDE float(20,10), ELEVATION INT")
     
     
    cur.execute("""SELECT count(*) as tot FROM PRO""")
    data = cur.fetchone()[0]
    if data != 0 :
        print("not empty", cur) 
    else :     
        A = open("input.txt", 'r')
        count = 0
        for line in A:
            if count == 0:
                count += 1
                continue
            else :
                token = line.split()
                
                id = token[0]
                token = token[1:]
                
                string = ""
                while len(token) > 0 :
                    if validate(token[0]):
                        date = datetime.strptime(token[0], '%Y-%m-%d')
                        token = token[1:]
                        break
                    else :
                        string = string + " " +  token[0]
                        token = token[1:]  
                
                string = string[1:]
                longitude = token[0]
                latitude  = token[1]
                elevation = token[2]
                        
            cur.execute("INSERT INTO PRO VALUES (?,?,?,?,?,?)", (int(id), string, date,longitude,latitude,elevation))    

   
@app.route("/")
def index():
    return "Welcome to DataBase!"

@app.route("/hello")
def hello():
    return render_template("test.html")



@app.route("/find/id=<string:pid>")
def find_id(pid):
    
    tmp = lite.connect('test.db')
    strings = []
    
    if validate_id(pid):
        with tmp:
            tp = tmp.cursor()
                
            sql = "SELECT * FROM PRO WHERE ID=?"
            result = tp.execute(sql, pid)    
            #cur.execute("SELECT * FROM PRO where ID=?",1)
            
            for row in tp:
                strings.append(row)
        
        
        return render_template("test.html", **locals())
    else : return "It needs to be an integer!"



@app.route("/find/description=<string:description>")
def find_description(description):
    
    tmp = lite.connect('test.db')
    strings = []
    
    with tmp:
        tp = tmp.cursor()
            
        sql = "SELECT * FROM PRO WHERE DESCRIPTION=?"
        result = tp.execute(sql, (description,))    
        #cur.execute("SELECT * FROM PRO where ID=?",1)
        
        for row in tp:
            print(row)
            strings.append(row)
    
    return render_template("test.html", **locals())


@app.route("/add/id=<string:pid>&description=<string:description>&datetime=<string:datetime>&longitude=<string:longitude>&latitude=<string:latitude>&elevation=<string:elevation>")
def add_new(pid,description,datetime,longitude,latitude,elevation):
    
    tmp = lite.connect('test.db')
    strings = []
    
    if not validate_id(pid):
            return "ID has to be integer!"
    if not validate(datetime):
        return "Date has to be in yyyy-mm-dd form!"
    if not validate_lo(longitude):
        return "longitude has to be a positive float number!"
    if not Validate_la(latitude):
        return "latitude has to be a negative float number!"
    if not Validate_ele(elevation):
        return "elevation has to be an integer"       
    
    with tmp:
        tp = tmp.cursor()
            
        tp.execute("INSERT INTO PRO VALUES (?,?,?,?,?,?)", (int(pid), description,datetime,longitude,latitude,elevation))  
        #cur.execute("SELECT * FROM PRO where ID=?",1)
            
        
        for row in tp:
            print(row)
            strings.append(row)
    
    return render_template("test.html", **locals())
@app.route("/delete/id=<string:pid>&datetime=<string:datetime>")
def delete(pid,datetime):
    
    if not validate_id(pid):
            return "ID has to be integer!"
    if not validate(datetime):
        return "Date has to be in yyyy-mm-dd form!"
    
    
    tmp = lite.connect('test.db')
    strings = []
    
    if not validate_id(pid):
            return "ID has to be integer!"
    if not validate(datetime):
        return "Date has to be in yyyy-mm-dd form!"
    
    
    with tmp:
        tp = tmp.cursor()
            
        tp.execute("DELETE FROM PRO WHERE ID=? and DATETIME=?", (int(pid), datetime))  
        #cur.execute("SELECT * FROM PRO where ID=?",1)
        
        for row in tp:
            print(row)
            strings.append(row)
    
    return render_template("test.html", **locals())


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)














