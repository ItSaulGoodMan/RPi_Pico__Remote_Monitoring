import datetime, time
a=["dosta", "je bilo"]
b = 12
file = open("test.txt", "r")
x = file.read()
x = x.split("\n")
pr = float(x[-2])
if(pr>200):
    vremeee = datetime.datetime.now()
    a.append(vremeee)
    b=b+1
    