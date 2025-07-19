"""ANALISIS DE VENTAS: Supongamos que eres el propietario de una tienda en línea y tienes 
una lista de ventas de los últimos 30 días. Quieres analizar las ventas por día de la semana 
para identificar los días de mayor venta.
Pista 1: Puedes crear dos listas, una con las ventas por cada día del mes como por ejemplo… 
ventas = [120, 80, 140, 200, 75, 100, 180, 220, 160, 110, 90, 120, 170, 190, 250, 300, 95, 110, 
140, 180, 200, 160, 120, 80, 170, 150, 210, 190, 230, 250] Y otra lista con los días de la 
semana: dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", „Domingo“]
 Después puedes crear una nueva lista con una entrada por cada día de la semana y usar un bucle 
 para añadir a esta lista la suma de las ventas correspondientes a cada uno de los días de la 
 semana.
Pista 2: Puede que necesites una variable que lleve la cuenta del día de la semana actual y se 
reinicie a cero cuando llegue al séptimo día."""
#datos de las ventas de todos los dias del mes
ventas = [120, 80, 140, 200, 75, 100, 180, 220, 160, 110, 90, 120, 170, 190, 250, 300, 95, 110, 140, 180, 200, 160, 120, 80,
          170, 150, 210, 190, 230, 250]

#creo listas para agrupas las ventas por los dias de la semana
lunes=[]
martes=[]
miercoles=[]
jueves=[]
viernes=[]
sabado=[]
domingo=[]

#para hacer las sumas de las ventas por dias
venta_lunes=0
venta_martes=0
venta_miercoles=0
venta_jueves=0
venta_viernes=0
venta_sabado=0
venta_domingo=0
venta_mes=0

#recorro las ventas de 7 en 7 y las agrupo el lunes. y asu vez hago la suma de dichas ventas
for i in range(0,len(ventas),7):
 venta=ventas[i]
 lunes.append(venta)
 venta_lunes=sum(lunes)

#q antes pero empiezo en 1 para q lo vaya incluyendo en la lista de los martes y asi todos los dias
for i in range(1,len(ventas),7):
 venta=ventas[i]
 martes.append(venta)
 venta_martes=sum(martes)

for i in range(2,len(ventas),7):
 venta=ventas[i]
 miercoles.append(venta)
 venta_miercoles=sum(miercoles)

for i in range(3,len(ventas),7):
 venta=ventas[i]
 jueves.append(venta)
 venta_jueves=sum(jueves)

for i in range(4,len(ventas),7):
  venta=ventas[i]
  viernes.append(venta)
  venta_viernes=sum(viernes)

for i in range(5,len(ventas),7):
  venta=ventas[i]
  sabado.append(venta)
  venta_sabado=sum(sabado)

for i in range(6,len(ventas),7):
  venta=ventas[i]
  domingo.append(venta)
  venta_domingo=sum(domingo)

venta_mes= venta_lunes + venta_martes + venta_miercoles + venta_jueves + venta_viernes + venta_sabado + venta_domingo

print(f"""Las ventas realizadas por dias son:
      -Lunes {lunes} . Total: {venta_lunes} €
      -Martes {martes} . Total: {venta_martes} €
      -Miercoles {miercoles} . Total: {venta_miercoles} €
      -Jueves {jueves} . Total: {venta_jueves} €
      -Viernes{viernes} . Total: {venta_viernes} €
      -Sabado {sabado} . Total : {venta_sabado} €
      -Domingo{domingo} . Total: {venta_domingo} €

      El total de las ventas del mes es : {venta_mes} €""")