import math

#constantes
G = 6.67*math.pow(10, -11) #constante gravitacional universal(Nm2/kg2)
mb = 5.972*math.pow(10, 24) #massa terra (kg)

#getting acelaration from sensor

a = 8.69 #tempory change when acess to sensores is available

#igualando a lei da gravitação universal com a segunda lei de newton
#we can igualat the distance(ISS, EARTH)

r = math.sqrt(G*(mb/a)) #calculo do raio da orbita

v = math.sqrt(G*(mb/r)) #calculo da velocidade em km/s
vs = v/1000 #convert to km/s
vh = vs*3600 #convert to km/h

print("a velocidade neste momento é")
print("%.2f" % vs , "km/s ou","%.2f" % vh , "km/h")
