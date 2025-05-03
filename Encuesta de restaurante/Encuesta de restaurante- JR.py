from tkinter import*
from tkinter import simpledialog
import random
ventana=Tk()

"""
nombre y proposito:
consultarAspecto: se encarga en dar el promedio de un aspecto individual
contrato: consultarAspecto([,]float,int)->float
encabezado: consultarAspecto(matriz,aspecto)
ejemplo:matriz
[4.12, 3.55, 2.87, 1.99, 4.65, 2.36, 3.23]
[2.33, 1.57, 3.74, 4.26, 1.86, 2.17, 5.0]
[3.91, 2.34, 1.62, 4.57, 1.12, 3.29, 4.78]
[1.24, 3.47, 2.41, 4.92, 2.13, 1.68, 3.06]
[4.44, 1.81, 3.15, 2.78, 4.01, 3.99, 1.93]
aspecto:1
el promedio del aspecto 1 es:3.6

"""
def consultarAspecto(matriz,aspecto):
    suma_calificaciones = 0
    num_calificaciones = 0
    for fila in matriz:
        if aspecto < len(matriz[0]):
            calificacion = fila[aspecto]
            suma_calificaciones += calificacion
            num_calificaciones += 1
    if num_calificaciones > 0:
        promedio_calificacion = round((suma_calificaciones / num_calificaciones),1)
    else:
        promedio_calificacion = 0
    return promedio_calificacion
    
"""
nombre y proposito:
reporteR: mostrar los datos en un reporte
contrato: reporteR([,]float)->str
encabezado:reporteR([,]matriz)->reporte
ejemplo:
matriz=[[4.2, 5.1, 3.5, 2.7, 4.3, 2.8, 3.9],
        [3.3, 2.7, 4.5, 5.0, 2.1, 3.6, 5.0],
        [2.8, 3.4, 5.0, 4.3, 3.9, 4.6, 2.7],
        [5.0, 4.1, 2.9, 3.7, 4.5, 2.4, 4.2],
        [4.5, 2.5, 3.8, 4.9, 4.1, 4.9, 3.3]]
aspecto a evaluar                   cliente 1     cliente 2     cliente 3     cliente 4     cliente 5
atencion de parte de los empleados  4.2           3.3           2.8            5.0           4.5
calidad de la comida                5.1           2.7           3.4            4.1           2.5
musica adecuada                     3.5           4.5           5.0            2.9           3.8
iluminacion suficiente              2.7           5.0           4.3            3.7           4.9
ambiente(sillas)                    4.3           2.1           3.9            4.5           4.1
justicia del precio                 2.8           3.6           4.6            2.4           4.9
decoracion del sitio                3.9           5.0           2.7            4.2           3.3

"""

def reporteR(matriz):
    reporte = "aspecto a evaluar\n"
    aspectos = ["atencion de parte de los empleados", "calidad de la comida", "musica adecuada",
                "iluminacion suficiente", "ambiente(sillas)", "justicia del precio", "decoracion del sitio"]

    for c in range(7):
        aspecto = aspectos[c].ljust(40)
        reporte += aspecto
        for f in range(5):
            reporte += str(matriz[f][c]) + "\t\t"
        reporte += "\n"
    
    return reporte


"""
nombre y proposito:
mayor: determinar la mayor calificacion de las diferentes reseñas
contrato: mayor([,]float)->str
encabezado:reporteR([,]matriz)->reporte
ejemplo:
matriz= [[4.2, 5.1, 3.5, 2.7, 4.3, 2.8, 3.9],
        [3.3, 2.7, 4.5, 5.0, 2.1, 3.6, 5.0],
        [2.8, 3.4, 5.0, 4.3, 3.9, 4.6, 2.7],
        [5.0, 4.1, 2.9, 3.7, 4.5, 2.4, 4.2],
        [4.5, 2.5, 3.8, 4.9, 4.1, 4.9, 3.3]]
aspecto a evaluar                   Mayor Cal.
atencion de parte de los empleados  5.0
calidad de la comida                5.1
musica adecuada                     5.0
iluminacion suficente               5.0
ambiente(sillas)                    4.5
justicia del precio                  4.9
decoracion del sitio                5.0

"""
def mayor(matriz):
    maximo=[]
    reporte="aspecto a evaluar\t\t\t            Mayor Cal.\n"
    aspectos=["atencion de parte de los empleados","calidad de la comida","musica adecuada","iluminacion suficente","ambiente(sillas)","justicia del precio","decoracion del sitio"]
    for j in range(7):
        maximo_columnas=matriz[0][j]
        for i in range(1,5):
            if matriz[i][j]>maximo_columnas:
                maximo_columnas=matriz[i][j]
        maximo.append(maximo_columnas)
    for i in range(len(maximo)):
        aspecto = aspectos[i].ljust(40)
        reporte += aspecto + str(maximo[i]) + "\n"

    return reporte


"""
nombre y proposito:
promedioCalificaciones: calcular el promedio de las calificacion de los clientes
contrato: promedioCalificaciones([,]float)->str
encabezado:reporteR([,]matriz)->reporte
ejemplo:
matriz= [[4.2, 5.1, 3.5, 2.7, 4.3, 2.8, 3.9],
        [3.3, 2.7, 4.5, 5.0, 2.1, 3.6, 5.0],
        [2.8, 3.4, 5.0, 4.3, 3.9, 4.6, 2.7],
        [5.0, 4.1, 2.9, 3.7, 4.5, 2.4, 4.2],
        [4.5, 2.5, 3.8, 4.9, 4.1, 4.9, 3.3]]
aspecto a evaluar                   promedio
atencion de parte de los empleados  3.6
calidad de la comida                3.5
musica adecuada                     4.4
iluminacion suficente               3.5
ambiente(sillas)                    3.9
justicia del precio                 3.7
decoracion del sitio                3.4

"""
def promedioCalificaciones(matriz):
    promedio=[]
    aspectos=["atencion de parte de los empleados","calidad de la comida","musica adecuada","iluminacion suficente","ambiente(sillas)","justicia del precio","decoracion del sitio"]
    reporte="aspecto a evaluar\t\t\t            Promedio.\n"
    for j in range(len(matriz[0])):
        suma=0
        for i in range(len(matriz)):
            suma+=matriz[i][j]
        prom=round((suma/5),1)
        promedio.append(prom)
    for i in range(len(promedio)):
        aspecto = aspectos[i].ljust(40)
        reporte += aspecto + str(promedio[i]) + "\n"

    return reporte
    
"""
nombre y proposito:
NumerosRam: generar numeros aleatoriamente de las calificaciones
contrato: NumerosRam([,]float)->[]float
encabezado:reporteR([,]matriz)->[,]matriz
ejemplo:
matriz=[5,7]matriz 5x7 vacia
[2.4, 1.5, 4.9, 3.8, 0.5, 2.3, 4.2]
[3.9, 1.2, 2.7, 0.3, 4.5, 0.6, 1.7]
[2.1, 3.4, 4.2, 3.7, 1.9, 4.8, 3.2]
[0.6, 1.3, 4.7, 1.0, 0.1, 1.4, 2.5]
[3.1, 3.3, 0.9, 1.2, 3.5, 3.6, 4.8]

"""       
def NumerosRam(matriz):
    for i in range(5):
        for j in range(7):
            matriz[i][j]=round(random.uniform(0.0,5),1)
    return matriz


"""
nombre y proposito:
Principal: recibir todos los datos de entrada y retornar una salida
contrato: principal()
encabezado:principal()
ejemplo:


"""
def principal():
    matriz=[[0.0]*7 for _ in range(5)]
    numeros=NumerosRam(matriz)
    maximo=[]
    promedio=[]
    n=1
    salir=0
    while n!=0:
        n=simpledialog.askinteger("","ingrese la opcion que desea realizar.\n0-salir\n1-consultar todas las calificaciones\n2-consultar las calificaciones mayores\n3-consultar el promedio de las calificaciones\n4-consultar promedio de un aspecto\n")
        if n==1:
            report=reporteR(matriz)
            reporteT.config(state="normal")
            reporteT.delete('1.0', END)
            reporteT.insert(INSERT, report)
            reporteT.config(state="disable")
        elif n==2:
            mayor_Que=mayor(matriz)
            reporteT.config(state="normal")
            reporteT.delete('1.0', END)
            reporteT.insert(INSERT, mayor_Que)
            reporteT.config(state="disable")
        elif n==3:
            prom=promedioCalificaciones(matriz)
            reporteT.config(state="normal")
            reporteT.delete('1.0', END)
            reporteT.insert(INSERT, prom)
            reporteT.config(state="disable")
        elif n==4:
            aspecto=simpledialog.askinteger("","digite el numero del aspecto que desea consultar el promedio\n0-atencion de parte de los empleados\n1-calidad de la comida\n2-musica adecuada\n3-iluminacion suficente\n4-ambiente(sillas)\n5-justicia del precio\n6-decoracion del sitio\n")
            while aspecto<0 or aspecto >6:
                aspecto=simpledialog.askinteger("","error, ingrese una opcion 0 a 6\n0-atencion de parte de los empleados\n1-calidad de la comida\n2-musica adecuada\n3-iluminacion suficente\n4-ambiente(sillas)\n5-justicia del precio\n6-decoracion del sitio\n")
            aspectoPromedio=consultarAspecto(matriz,aspecto)
            respuesta="El promedio de la calificación en el aspecto "+str(aspecto)+" es: "+str(aspectoPromedio)
            reporteT.config(state="normal")
            reporteT.delete('1.0', END)
            reporteT.insert(INSERT, respuesta)
            reporteT.config(state="disable")

    return salir
def borrarText():
    reporteT.config(state="normal")
    reporteT.delete("1.0",END)
    reporteT.config(state="disable")

def salir():
    ventana.destroy()
    
#------------------------------------------
ventana.geometry("800x500")
ventana.title("caso 1- Encuesta")
ventana.resizable(0,0)
#frame bienvenida
titulo=Label(ventana,text="Encuestas de restaurante",bg="red",font=("Roboto Cn",20),fg="white")
titulo.pack(pady=10,fill=X)
#marco
marco=LabelFrame(ventana, text="informes encuestas")
marco.config(width=700,height=400, bd=3, relief="raised")
marco.pack(pady=10,padx=10)
#texto
reporteT=Text(marco)
reporteT.config(state="normal",width=95,height=20)
reporteT.grid(row=0, column=0)
reporteT.config(state="disable")
#marco botones
marcoB=LabelFrame(ventana,bg="red")
marcoB.config(width=600,height=100, bd=3, relief="raised")
marcoB.pack(pady=10,fill=X)
#boton MENU
Menu=Button(marcoB,text="Menú",pady=10,padx=10,command=principal)
Menu.grid(row=0,column=3)
#boton borrar Texto
borrar=Button(marcoB,text="Limpiar",pady=10,padx=10,command=borrarText)
borrar.grid(row=0, column=1)
#boton salir
salir=Button(marcoB, text="Salir",pady=10,padx=10,command=salir)
salir.grid(row=0,column=2)
#label
info=Label(marcoB, text="Selecione el boton menú para consultar",bg="red",font=("Roboto Cn",20),fg="white",padx=20)
info.grid(row=0,column=4)

ventana.mainloop()
            
            
