
from flask import Flask, redirect, url_for, render_template,request
import matplotlib
import MySQLdb
import statistics

matplotlib.use('Agg')
import matplotlib.pyplot as plt
import mysql.connector
import time
import datetime 
vremevlaznost = '5'

app = Flask(__name__)






@app.route("/")
def home():
       
        
        
    #while True:

        time.sleep(6)  
        file = open("test.txt", "r")
        x = file.read()
        x = x.split("\n")
        db = mysql.connector.connect(
            host = "localhost",
            user = "root",
            passwd = "Pijanista123!",
            database ="pametnakuca"
            )  
        last10temp = db.cursor(buffered=True)
        avgtemp = db.cursor(buffered=True)
        avgmoisture = db.cursor(buffered=True)
        mycursor = db.cursor(buffered=True)
        mycursor.execute("INSERT INTO parametrikuca (Temperatura,Vlaznost) VALUES(%s,%s)",(x[-7],x[-8]))
        avgtemp.execute("SELECT AVG(Temperatura) AS average FROM (SELECT * FROM pametnakuca.parametrikuca order by ID desc limit 10) as t")
        avgmoisture.execute("SELECT AVG(Vlaznost) AS average FROM (SELECT * FROM pametnakuca.parametrikuca order by ID desc limit 10) as t")
        last10temp.execute("SELECT Temperatura FROM pametnakuca.parametrikuca order by ID desc limit 10")
        
        pokazi = 6
       

        prosvlaz = avgmoisture.fetchall()
        prostemp = avgtemp.fetchall()


        db.commit()
       
        proveratemp = float(x[-7])
        proveravlaznost = float(x[-8])
        proveragas = float(x[-3])
        proverazvuk = float(x[-5])
        proveravatra = float(x[-2])
        


                    
            
        

    
        if(proveravlaznost > 47):
            upozorenjevlaznosti = "UPOZORENJE:VLAZNOST PREVISOKA!"
            bojaa1 = "#ff0000"
            
            
        else:
            upozorenjevlaznosti = "NORMALNA VLAZNOST VAZDUHA"

            bojaa1 = "#0281F8"
            
        if(proveratemp > 26.4):
            upozorenjetemperatura = "UPOZORENJE:PREVISOKA TEMPERATURA!"
            bojaa2 = "#ff0000"
            
        else:
            upozorenjetemperatura = "NORMALNA TEMPERATURA"
            bojaa2 = "#0281F8"

        if(proverazvuk > 600):
            upozorenjezvuk = "PRIMECEN ZVUK!"
            bojaa3 = "#ff0000"
            
            
        else:
            upozorenjezvuk = "NEMA ZVUKA"

            bojaa3 = "#0281F8"

        if(proveragas > 420):
            upozorenjegas = "PRIMECENO PRISUSTVO GASA!"
            bojaa4 = "#ff0000"
            
            
        else:
            upozorenjegas = "NEMA GASA"

            bojaa4 = "#0281F8"    

        if(proveravatra > 0.5):
            upozorenjevatra = "PRIMECENA VATRA!"
            bojaa5 = "#ff0000"
            
            
        else:
            upozorenjevatra = "NEMA VATRE"

            bojaa5 = "#0281F8"        
        
        return render_template("index.html", temperatura=proveratemp, vlaznost=proveravlaznost, upozorenjetemp=upozorenjetemperatura, upozorenjevlaznost=upozorenjevlaznosti, bojavlaznost = bojaa1, bojatemperatura=bojaa2, prostemp1 = prostemp, prosvlaz1 = prosvlaz, pokazi1 = pokazi, zvuk = proverazvuk, bojazvuk = bojaa3, upozorenjezv = upozorenjezvuk, gas = proveragas, bojagas = bojaa4, upozorenjegass = upozorenjegas, vatra = proveravatra, upozorenjevat = upozorenjevatra, bojavatra = bojaa5)
@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        user = request.form["nm"]
        return redirect(url_for("user", usr=int(user)))
    else:
        return render_template("login.html")

@app.route("/<usr>", methods=["POST", "GET"])
def user(usr):
  

    db = mysql.connector.connect(
        host = "localhost",
        user = "root",
        passwd = "Pijanista123!",
        database ="pametnakuca"
            )     #Type what you want to do when the user clicks on the link
    # once it is done with doing that code... it will redirect back to the homepage
    minute = usr * 10
    last10temp1 = db.cursor(prepared=True)
    last10temp1.execute("SELECT Temperatura FROM pametnakuca.parametrikuca order by ID desc limit %s; ",(usr,) )
    #last10temp1.execute("INSERT INTO parametrikuca (Temperatura,Vlaznost) VALUES(%s,%s)",usr,usr)
    data = []
    for row in last10temp1:
        data.append(float(row[0]))
    sumaa = sum(data)
    print(sumaa)

    plt.plot(data)
    plt.savefig('static/figura.png')
    plt.close()

    last10vlaz = db.cursor(prepared=True)
    last10vlaz.execute("SELECT Vlaznost FROM pametnakuca.parametrikuca order by ID desc limit %s; ",(usr,) )
    data2 = []

    for row in last10vlaz:
        data2.append(float(row[0]))
    ooo = [float(i) for i in data2]    
    print(ooo)

    plt.plot(data2)
    
    plt.savefig('static/figura2.png')
    plt.close()
    avgtemp1 = db.cursor(prepared=True)
    avgmoisture = db.cursor(buffered=True)
    navodnici = ' " '
   
    
    avgtemp1.execute("SELECT AVG(Temperatura) AS average FROM (SELECT * FROM pametnakuca.parametrikuca order by ID desc limit %s) as t",("22",))
    prostemp = avgtemp1.fetchall()
    
    
    data3 = []
    for row in avgtemp1:
        data3.append((str[0]))
    g = len(data3)
    prosek=[float(i) for i in data3]
    return render_template("grafik.html")

    
  
if __name__ == "__main__":
    app.run(debug = True)
