# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 19:14:35 2024

@author: ProtofurOwO
Z"""
import tkinter as tk
from tkinter import messagebox
import mysql.connector

def insertarRegistro (nombres, apellidos, edad, estatura, telefono, genero): 
    try:
# Conectar con la base de datos
        conexion = mysql.connector.connect(
            host="localhost",
            port="3306",
            user="root",
            # Camabiar con tu usuario de MySQL si se personaliza
            password="Timeshirt#21", # Reemplaza con tu contraseña de MySQL si se personaliza
            database="programacionavanzada" # Reemplaza con el nombre de tu base de datos
        )
        cursor = conexion.cursor()
        # crear el query SQL para insertar el registro
        query = "INSERT INTO registros (nombre, apellidos, telefono, edad, estatura, genero)" +"VALUES (%s, %s, %s, %s, %s, %s)"
        valores = (nombres, apellidos, telefono, edad, estatura, genero)
        # Ejecutar el query
        cursor.execute(query, valores)
        # Guardar los cambios en la base de datos
        conexion.commit()
        # Cerrar la conexión
        cursor.close()
        conexion.close()
        messagebox.showinfo("Información", "Datos guardados en la base de datos con éxito.")
    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Error al insertar los datos: {err}")

def guardar_valores():
    nombres= tbnombre.get()
    apellidos= tbapellidos.get()
    edad= tbedad.get()
    estatura=tbestatura.get()
    telefono=tbtelefono.get()
    genero=""
    if var_genero.get()==1:
        genero="Hombre"
    elif var_genero.get()==2:
        genero="Mujer"
    datos= "Nombres: " + nombres + "\nApellidos: "+ apellidos + "\nEdad: "+ edad +" años\n" + "Estatura: "+estatura + "\nTelefono: " + telefono + "\nGénero: "+ genero + "\n"
    with open("01092024Datos.txt","a") as archivo:
        archivo.write(datos+"\n\n")
    insertarRegistro(nombres, apellidos, edad, estatura, telefono, genero)
    messagebox.showinfo("Informacion", "Datos guardados con éxito: \n\n"+ datos)
    
    
    
def limpiar_campos():
    tbnombre.delete(0,tk.END)
    tbapellidos.delete(0,tk.END)
    tbedad.delete(0,tk.END)
    tbestatura.delete(0,tk.END)
    tbtelefono.delete(0,tk.END)
    var_genero.set(0)

def borrar_fun():
    limpiar_campos()

    
ventana = tk.Tk()
ventana.geometry("520x500")
ventana.title("Formulario Vr.01")
var_genero = tk.IntVar()

lbnombre= tk.Label(ventana, text="Nombres: ")
lbnombre.pack()
tbnombre= tk.Entry()
tbnombre.pack()
lbapellidos= tk.Label(ventana, text="Apellidos: ")
lbapellidos.pack()
tbapellidos = tk.Entry()
tbapellidos.pack()
lbtelefono = tk.Label(ventana, text="Telefono: ")
lbtelefono.pack()
tbtelefono = tk.Entry()
tbtelefono.pack()
lbedad= tk.Label(ventana, text="Edad: ")
lbedad.pack()
tbedad= tk.Entry()
tbedad.pack()
lbestatura= tk.Label(ventana, text="Estatura: ")
lbestatura.pack()
tbestatura= tk.Entry()
tbestatura.pack()
lbgenero= tk.Label(ventana, text="Género: ")
lbgenero.pack()
rbhombre = tk.Radiobutton(ventana, text="Hombre", variable=var_genero, value=1)
rbhombre.pack()
rbmujer=tk.Radiobutton(ventana, text="Mujer", variable=var_genero, value=2)
rbmujer.pack()

btnborrar = tk.Button(ventana, text="Borrar valores", command=limpiar_campos)
btnborrar.pack()
btnguardar= tk.Button(ventana, text="Guardar", command=guardar_valores)
btnguardar.pack()
ventana.mainloop()

