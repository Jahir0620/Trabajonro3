print("##### 1.CREACION #####")

print("## 1.1 ##")
d={1:"jahir",2:"arrascue"}
print(d)
print("## 1.2 ##")
a=dict({"año":2019})
print(a)
print("## 1.3 ##")
b={4:"rojo",5:"verde",6:"amarillo"}
print(b)
print("## 1.4 ##")
c={7:"lapiz",8:"lapicero",9:"corrector"}
print(c[8])
print("## 1.5 ##")
d=dict({"cumpleaños":"6/09"})
print(d)
print("## 1.6 ##")
e={10:"leon",11:"tigre",12:"lobo"}
print(e[10],e[11],e[12])
print("## 1.7 ##")
f={13:"tallo",14:"hoja",15:"raiz"}
print(f[15])
print(f)
print("## 1.8 ##")
g={16:"fernando",17:"diaz"}
print(g)
print("## 1.9 ##")
h={18:"teclado",19:"mouse",20:"monitor"}
print(h[18],h[19],h[20])
print("## 1.10 ##")
i={21:"programacion",22:2}
print(i[21],i[22])

print("##### 2.PERTENENCIA DE CLAVE #####")
print("## 2.1 ##")
j={1:"jahir",2:"arrascue",3:"acosta"}
item=int(input("ingrese opcion:"))
if item in j:
    print(True)
else:
    print(False)

print("## 2.2 ##")
k={4:"rojo",5:"verde",6:"amarillo"}
item=int(input("ingrese opcion:"))
if item in k:
    print(True)
else:
    print(False)

print("## 2.3 ##")
l={7:"lapiz",8:"lapicero",9:"corrector"}
item=int(input("ingrese opcion:"))
if item in l:
    print(True)
else:
    print(False)
print("## 2.4 ##")
m={10:"leon",11:"tigre",12:"lobo"}
item=int(input("ingrese opcion:"))
if item in m:
    print(True)
else:
    print(False)
print("## 2.5 ##")
n={13:"tallo",14:"hoja",15:"raiz"}
item=int(input("ingrese opcion:"))
if item in n:
    print(True)
else:
    print(False)
print("## 2.6 ##")
o={16:"fernando",17:"diaz"}
item=int(input("ingrese opcion:"))
if item in o:
    print(True)
else:
    print(False)
print("## 2.7 ##")
p={18:"teclado",19:"mouse",20:"monitor"}
item=int(input("ingrese opcion:"))
if item in p:
    print(True)
else:
    print(False)
print("## 2.8 ##")
q={1:"inca",2:"casinelli",3:"coca"}
item=int(input("ingrese opcion:"))
if item not in q:
    print(True)
else:
    print(False)
print("## 2.9 ##")
r={1:"polo",2:"camisa",3:"short"}
item=int(input("ingrese opcion:"))
if item not in r:
    print(True)
else:
    print(False)
print("## 2.10 ##")
s={1:"gloria",2:"kirma",3:"nestle"}
item=int(input("ingrese opcion:"))
if item not in s:
    print(True)
else:
    print(False)

print("##### 4.COMPARACION #####")

print("## 4.1 ##")
not1={"jahir":12,"juan":10,"hugo":12}
not2={"shamir":9,"cris":12,"tomas":10}
print("not1==not2",not1==not2)

print("## 4.2 ##")
nom1={"name1":"aldo","name2":"jahir"}
nom2={"name3":"jahir","name4":"aldo"}
print("nom1==nom2",nom1==nom2)

print("## 4.3 ##")
ap1={1:"arrascue",2:"acosta"}
ap2={3:"arrascue",4:"acosta"}
print("ap1==ap2",ap1==ap2)

print("## 4.4 ##")
col1={5:"rojo",6:"verde",7:"azul"}
col2={8:"verde",9:"amarillo",10:"rojo"}
print("col1==col2",col1==col2)

print("## 4.5 ##")
dias1={"dia1":"lunes","dia2":"miercoles","dia3":"viernes"}
dias2={"dia4":"martes","dia5":"jueves","dia6":"sabado"}
print("dias1==dias2",dias1==dias2)

print("## 4.6 ##")
año1={1:1999,2:1988,3:1978}
año2={4:1999,5:1988,6:1978}
print("año1==año2",año1==año2)

print("## 4.7 ##")
util1={"num1":"lapiz","num2":"borrador","num3":"tajador"}
util2={"num4":"lapiz","num5":"borrador","num6":"tajador"}
print("util1==util2",util1==util2)

print("## 4.8 ##")
rop1={1:"polo",2:"casaca",3:"short"}
rop2={4:"calzoncillos",5:"casaca",6:"short"}
print("rop1==rop2",rop1==rop2)

print("## 4.9 ##")
anim1={1:"leon",2:"pantera",3:"oso"}
anim2={4:"pantera",5:"leon",6:"oso"}
print("anim1==anim2",anim1==anim2)

print("## 4.10 ##")
frut1={"fruta3":"manzana","fruta4":"pera","fruta5":"uva"}
frut2={"fruta6":"manzana","fruta7":"pera","fruta8":"uva"}
print("frut1==frut2",frut1==frut2)

print("##### 5.INDEXACION #####")

print("## 5.1 ##")
continente={1:"asia",2:"america",3:"africa",4:"europa",5:"oceania"}
print("el valor de la clave 3 es:",continente[3])

print("## 5.2 ##")
animales={1:"perro",2:"gato",3:"oso"}
print("el valor de la clave 1 es:",animales[1])

print("## 5.3 ##")
distrito={1:"olmos",2:"motupe",3:"jayanca",4:"pacora",5:"illimo"}
print("el valor de la clave 4 es:",distrito[4])

print("## 5.4 ##")
calzados={0:"zaptos",1:"zapatillas",2:"sandalias"}
print("el valor de la clave inicial es:",calzados[0])

print("## 5.5 ##")
marca_cel={1:"huawei",2:"samsumg",3:"alcatel",4:"lg"}
print("el valor de la clave 1 es:",marca_cel[1])

print("## 5.6 ##")
tiendas={1:"curacao",2:"metro",3:"saga falabella",4:"marathon"}
print("el valor de la clave 3 es:",tiendas[3])

print("## 5.7 ##")
abarrotes={1:"arroz",2:"azucar",3:"huevos",4:"sal"}
print("el valor de la clave 1 es:",abarrotes[1])

print("## 5.8 ##")
combustible={1:"petroleo",2:"kerosene",3:"gasolina",4:"glp"}
print("el valor de la clave 3 es:",combustible[3])

print("## 5.9 ##")
raperos={1:"aczino",2:"wos",3:"sub",4:"jazze",5:"cacha",6:"papo"}
print("el valor de la clave 4 es:",raperos[4])

print("## 5.10 ##")
deportes={1:"futbol",2:"voley",3:"basquetball",4:"surf"}
print("el valor de la clave 3 es:",deportes[3])

print("##### 7.LONGITUD #####")

print("## 7.1 ##")
msg={1:"Jahir" ,3:"Arrascue",2:"kevin", 4:"acosta"}
print(len(msg))

print("## 7.2 ##")
txt={"Jahir":"nombre1" ,"Arrascue":"apelli1","kevin":"nombre2"}
print(len(txt))

print("## 7.3 ##")
y={"juan":1}
print(len(y))

print("## 7.4 ##")
tx={1:"ElGuason",2:"batman"}
print(len(tx))

print("## 7.5 ##")
mar={1:"huawei",2:"samsumg",3:"lg"}
print(len(mar))

print("## 7.6 ##")
comedor={"silla":1,"mesa":2,"mueble":3}
print(len(comedor))

print("## 7.7 ##")
col={"juan":"ana","pedro":"sofia","jahir":"maria"}
print(len(col))

print("## 7.8 ##")
continentes={1:"america",2:"africa",3:"europa"}
print(len(continente))

print("## 7.9 ##")
prom={"anita":15,"juancito":10,"pedrito":20}
print(len(prom))

print("## 7.10 ##")
cuadernos={1:"stanford",2:"justus"}
print(len(cuadernos))

print("##### 8.ITERACION #####")
print("## 8.1 ##")
devic={"arduino":1,"laptop":2,"tablet":3}
for k,v in devic.items():
    print(k,v)

print("## 8.2 ##")
cooloores={"manzana":"roja","platano":"amarillo","pera":"verde"}
for k,v in cooloores.items():
    print(k,v)

print("## 8.3 ##")
cap={"peru":"lima","argentina":"buenos aires","inglaterra":"londres"}
for k,v in cap.items():
    print(k,v)

print("## 8.4 ##")
paices={"perú":"alianza","argentina":"boca juniors","colombia":"caracas"}
for k,v in paices.items():
    print(k,v)

print("## 8.5 ##")
pais={"brasil":"flamengo","uruguay":"peñarol","chile":"u de chile"}
for k,v in pais.items():
    print(k,v)

print("## 8.6 ##")
cursos={"mate":16,"progra":15,"circuitos":12}
for k,v in cursos.items():
    print(k,v)

print("## 8.7 ##")
granja={"gallina":"universitario","mono":"alianza","pavo":"cristal"}
for k,v in granja.items():
    print(k,v)

print("## 8.8 ##")
carnivoros={"leon":"africa","cocodrilo":"europa","tigre":"europa"}
for k,v in carnivoros.items():
    print(k,v)

print("## 8.9 ##")
universidad={"UNPRG":"la pedro es la pedro","usat":"dice ser la mejor","vallejo":"plata como cancha"}
for k,v in universidad.items():
    print(k,v)

print("## 8.10 ##")
transport={"moto":"honda","carro":"hiunday","avion":"air"}
for k,v in transport.items():
    print(k,v)

print("##### 9.BUSQUEDA #####")

print("## 9.1 ##")
a={1:"avion",2:"carro",3:"moto"}
print(a.get(2))

print("## 9.2 ##")
uni={"jahir":"UNPRG","jhans":"SIPAN","karen":"USAT"}
print(uni.get("jahir"))

print("## 9.3 ##")
dep={1:"futbol",2:"voley",3:"basquet"}
print(dep.get(3))

print("## 9.4 ##")
cas={"aldo":"departamento","kevin":"condominio","karolina":"mini"}
print(cas.get("kevin"))

print("## 9.5 ##")
sex={"anibal":"masculino","nick":"masculino","karla":"femenino"}
print(sex.get("karla"))

print("## 9.6 ##")
carreras={1:"civil",2:"electronico",3:"mecanico"}
print(carreras.get(1))

print("## 9.7 ##")
carr={"avion":1,"carro":2,"moto":3}
print(carr.get("moto"))

print("## 9.8 ##")
nota={"jahir":20,"jhans":15,"karen":18}
print(nota.get("jahir"))

print("## 9.9 ##")
not2={"fabrizio":14,"kike":12,"junito":14}
print(not2.get("kike"))

print("## 9.10 ##")
uni={"jahir":"UNPRG","jhans":"SIPAN","karen":"USAT"}
print(uni.get("jhans"))

print("##### 13.ELIMINACION #####")

print("## 13.1 ##")
mon={1:"peso",2:"euro",3:"dolar"}
del mon[1]
print(mon)

print("## 13.2 ##")
fig={"circulo":1,"cuadrado":2,"rombo":3}
del fig["rombo"]
print(fig)

print("## 13.3 ##")
cur={1:"matematica",2:"comunicacion",3:"lenguaje"}
del cur[1]
print(cur)

print("## 13.4 ##")
colors={1:"rojo",2:"verde",3:"azul"}
del colors[2]
print(colors)

print("## 13.5 ##")
fruti={1:"fresa",2:"manzana",3:"uva"}
del fruti[3]
print(fruti)

print("## 13.6 ##")
comedr={"mesa":"comedor", "silla":"sentarse","mantel":"para la mesa"}
del comedr["mesa"]
print(comedr)

print("## 13.7 ##")
marcas={"nike":1,"adidas":2,"puma":3}
del marcas["nike"]
print(marcas)

print("## 13.8 ##")
elemn={"maar":"peces" ,"tierra":"seres humanos","fuego":"volcan"}
del elemn["fuego"]
print(elemn)

print("## 13.9 ##")
utiles={1:"cuaderno",2:"lapiz",3:"lapicero"}
del utiles[2]
print(utiles)

print("## 13.10 ##")
reptiles={1:"cocodrilo" ,2:"iguana",3:"pacaso"}
del reptiles[1]
print(reptiles)

print("##### 14.REEMPLAZO #####")

print("## 14.1 ##")
crs={11:"matematica",12:"comunicacion",13:"lenguaje"}
crs[11]="civica"
print(crs)

print("## 14.2 ##")
vegetales={1:"esparrago",2:"lechuga",3:"repollo"}
vegetales[2]="tomate"
print(vegetales)

print("## 14.3 ##")
tuberculos={1:"papas",2:"yuca",3:"camote"}
tuberculos[3]="recacha"
print(tuberculos)

print("## 14.4 ##")
mar_mot={1:"honda",2:"wanxin",3:"yamaha"}
mar_mot[2]="zonchens"
print(mar_mot)

print("## 14.5 ##")
mar_car={1:"hyunday",2:"4x4",3:"kia"}
mar_car[1]="toyota"
print(mar_car)

print("## 14.6 ##")
sonid={1:"auriculares",2:"parlante",3:"audifonos"}
sonid[1]="mp3"
print(sonid)

print("## 14.7 ##")
tel={1:"lg",2:"sony",3:"samsumg"}
tel[2]="panasonyc"
print(tel)

print("## 14.8 ##")
met={1:"hierro",2:"magnesio",3:"plata"}
met[3]="acero"
print(met)

print("## 14.9 ##")
personajes={1:"goku",2:"cel",3:"vegeta"}
personajes[1]="krilin"
print(personajes)

print("## 14.10 ##")
gaseosas={1:"inca",2:"coca",3:"casinelli"}
gaseosas[2]="oro"
print(gaseosas)

print("##### 15.AGREGADO #####")

print("## 15.1 ##")
crs={1:"matematica",2:"comunicacion",3:"lenguaje"}
crs.setdefault(4,"razonamiento verbal")
print(crs)

print("## 15.2 ##")
vegetales={1:"esparrago",2:"lechuga",3:"repollo"}
vegetales.setdefault(4,"cebolla")
print(vegetales)

print("## 15.3 ##")
tuberculos={1:"papas",3:"yuca",4:"camote"}
tuberculos.setdefault(2,"oyuco")
print(tuberculos)

print("## 15.4 ##")
mar_mot={2:"honda",3:"wanxin",4:"yamaha"}
mar_mot.setdefault(1,"zonzhen")
print(mar_mot)

print("## 15.5 ##")
mar_car={1:"hyunday",2:"4x4",3:"kia"}
mar_car.setdefault(4,"lamboryini")
print(mar_car)

print("## 15.6 ##")
sonid={2:"auriculares",3:"parlante",4:"audifonos"}
sonid.setdefault(1,"cable usb")
print(sonid)

print("## 15.7 ##")
tel={1:"lg",3:"sony",4:"samsumg"}
tel.setdefault(2,"huawei")
print(tel)

print("## 15.8 ##")
met={1:"hierro",2:"magnesio",3:"plata"}
met.setdefault(4,"carbon")
print(met)

print("## 15.9 ##")
personajes={2:"goku",3:"cel",4:"vegeta"}
personajes.setdefault(1,"krilim")
print(personajes)

print("## 15.10 ##")
gaseosas={1:"inca",2:"coca",3:"casinelli"}
gaseosas.setdefault(4,"oro")
print(gaseosas)



print("##### 17.ANULACION #####")

print("## 17.1 ##")
fig={1:"circulo",2:"cuadrado",3:"rombo"}
fig.clear()
print(fig)

print("## 17.2 ##")
colors={1:"rojo",2:"verde",3:"azul"}
colors.clear()
print(colors)

print("## 17.3 ##")
fruti={"fresa":1,"manzana":2,"uva":3}
fruti.clear()
print(fruti)

print("## 17.4 ##")
comedr={"mesa":1, "silla":2,"mantel":3}
comedr.clear()
print(comedr)

print("## 17.5 ##")
mar={1:"nike",2:"adidas",3:"puma"}
mar.clear()
print(mar)

print("## 17.6 ##")
elemn={1:"maar" ,2:"tierra",3:"fuego"}
elemn.clear()
print(elemn)

print("## 17.7 ##")
utiles={1:"cuaderno",2:"lapiz",3:"lapicero"}
utiles.clear()
print(utiles)

print("## 17.8 ##")
distrit={1:"olmos",2:"motupe",3:"olmos",4:"pacora",5:"illimo"}
distrit.clear()
print(distrit)

print("## 17.9 ##")
tends={1:"metro",2:"saga falabella",3:"marathon"}
tends.clear()
print(tends)

print("## 17.10 ##")
continen={1:"asia",2:"africa",3:"europa",4:"oceania"}
continen.clear()
print(continen)


print("##### 19.INSERCION #####")

print("## 19.1 ##")
granja={1:"gallina",2:"pato",3:"pavo"}
granja[1]="cuy"
print(granja)

print("## 19.2 ##")
universidad={1:"UNPRG",2:"usat",3:"vallejo"}
universidad[2]="sipan"
print(universidad)

print("## 19.3 ##")
cursos={1:"mate",2:"progra",3:"circuitos"}
cursos[3]="analisisIII"
print(cursos)

print("## 19.4 ##")
cap={1:"lima",2:"buenos aires",3:"londres"}
cap[3]="brasilia"
print(cap)

print("## 19.5 ##")
devic={1:"arduino",2:"laptop",3:"tablet"}
devic[1]="python"
print(devic)

print("## 19.6 ##")
pais={1:"brasil",2:"uruguay",3:"chile"}
pais[3]="argentina"
print(pais)

print("## 19.7 ##")
carnivoros={1:"leon",2:"cocodrilo",3:"tigre"}
carnivoros1[2]="oso"
print(carnivoros)

print("## 19.8 ##")
transport={1:"moto",2:"carro",3:"avion"}
transport[3]="bicicleta"
print(transport)

print("## 19.9 ##")
cooloores={1:"rojo",2:"amarillo",3:"verde"}
cooloores[2]="morado"
print(cooloores)

print("## 19.10 ##")
depart={1:"LAMBAYEQUE",2:"LORETO",3:"UCAYALI"}
depart[2]="AREQUIPA"
print(depart)

print("##### 24.VER CLAVES #####")

print("## 24.1 ##")
avon={1:"lentes",2:"colonias",3:"polos"}
print(avon.keys())

print("## 24.2 ##")
tiendas={"ripley":1,"saga falabella":2,"oeschle":3}
print(tiendas.keys())

print("## 24.3 ##")
paices={"ALEMANIA":4,"PORTUGAL":5,"INGLATERRA":6}
print(paices.keys())

print("## 24.4 ##")
peces={"caballa":"salada","bonito":"fresco","furel":1}
print(peces.keys())

print("## 24.5 ##")
nmr_par={60:"primero",80:"segundo",100:"tercero"}
print(nmr_par.keys())

print("## 24.6 ##")
marc_pc={"LENOVO":2,"HP":3}
print(marc_pc.keys())

print("## 24.7 ##")
cant={"MALUMA":"hp","ARCANGEL":"aparentamente","OZUNA":"farzante"}
print(cant.keys())

print("## 24.8 ##")
music={"FESTEJO":5,"SAYA":6,"CUMBIA":7}
print(music.keys())

print("## 24.9 ##")
nmr_imp={25:"uno",45:"dos",75:"tres"}
print(nmr_imp.keys())

print("## 24.10 ##")
prendas={"polo":4,"short":6,"sandalias":8}
print(prendas.keys())

print("##### 25.VER VALORES #####")

print("## 25.1 ##")
nombre={"juan":1,"rosa":2,"andres":3}
print(nombre.values())

print("## 25.2 ##")
notas={"ana":20,"rodrigo":15,"cubas":16}
print(notas.values())

print("## 25.3 ##")
cantantes={"MALUMA":"hp","ARCANGEL":"aparentamente","OZUNA":"farzante"}
print(cantantes.values())

print("## 25.4 ##")
dias_sem1={"domingo":1,"lunes":2}
print(dias_sem1.values())

print("## 25.5 ##")
dias_sem2={"martes":1,"miercoles":2}
print(dias_sem2.values())

print("## 25.6 ##")
programas={1:"linux",2:"python"}
print(programas.values())

print("## 25.7 ##")
restaurant={"jayanca":"pirkas","chiclayo":"origenes"}
print(restaurant.values())

print("## 25.8 ##")
ferret={1:"clavos",2:"cemento",3:"fierro"}
print(ferret.values())

print("## 25.9 ##")
fam={"primero":"padres","segundo":"hijos","tercero":"tios"}
print(fam.values())

print("## 25.10 ##")
cocina={1:"sarten",2:"cuchillo"}
print(cocina.values())



print("##### 26.CONVERCION #####")
print("## 26.1 ##")
frut={1:"manzana",2:"fresa",3:"uva"}
fr=list(fr)
print(l)

print("## 26.2 ##")
nombres={"juan":1,"dorita":2}
nam=list(nombres)
print(nam)

print("## 26.3 ##")
redes={"facebook":1,"whatsapp":2,"instagram":3}
red=set(redes)
print(red)

print("## 26.4 ##")
obras={"carmelo":1,"ollantay":2}
ob=set(obras)
print(ob)

print("## 26.5 ##")
promedio={15:"geral",20:"astrid"}
pro=list(promedio)
print(pro)

print("## 26.6 ##")
platos={"arroz con pato":1,"cabrito":2}
plat=tuple(platos)
print(plat)

print("## 26.7 ##")
tipo_car={"auto":1,"camion":2,"volquete":3}
tip=tuple(tipo_car)
print(tip)

print("## 26.8 ##")
aplicaciones={"free fire":1,"counter":2}
apps=list(aplicaciones)
print(apps)

print("## 26.9 ##")
ingles={"hello":1,"car":2}
pal_ing=list(ingles)
print(pal_ing)

print("## 26.10 ##")
estacion_año={"otono":1,"primavera":2,"invierno":3}
estacion=set(estacion_año)
print(estacion)



print("##################### TAREA TERMINADA ING.#####################")






