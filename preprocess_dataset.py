import os,sys
import numpy as np
import pandas as pd

ventana = 40
num_muestras = 1400

current_dir = os.getcwd()
data_folder = current_dir+"/data/all"
print(current_dir)

# Obtain all the files in the data folder
files = os.listdir(data_folder)

# Se crean las columnas
name_ax = ["Ax"+str(i) for i in range(ventana)] # columnas que queremos
name_ay = ["Ay"+str(i) for i in range(ventana)]
name_az = ["Az"+str(i) for i in range(ventana)]
name_vx = ["Vx"+str(i) for i in range(ventana)]
name_vy = ["Vy"+str(i) for i in range(ventana)]
name_vz = ["Vz"+str(i) for i in range(ventana)]

num_all_chunks = num_muestras/ventana*len(files)

# Se crea un dataframe vacio con las columnas que queremos
df = pd.DataFrame(0, index=np.arange(num_all_chunks), columns = name_ax+name_ay+name_az+name_vx+name_vy+name_vz+["U","A"]).astype(float)

contador=0
for file in files:
    # Por cada movimiento se carga cada csv y se guarda en un dataframe
    datos=pd.read_csv(data_folder+"/"+file, header=None).transpose()
    datos.columns = ["usuario","accion","tiempo","Ax","Ay","Az","Vx","Vy","Vz"]
    #print(datos)

    usuario = datos["usuario"][0]
    actividad = datos["accion"][0]

    print("Usuario: %s | Actividad: %s"%(usuario,actividad))

    muestras = datos.shape[0]
    num_chunks = int(muestras/ventana)
    #print(df)

    for i in range(num_chunks):
        temp_ax = datos["Ax"][i*ventana:(i+1)*ventana].to_list()
        temp_ay = datos["Ay"][i*ventana:(i+1)*ventana].to_list()
        temp_az = datos["Az"][i*ventana:(i+1)*ventana].to_list()
        temp_vx = datos["Vx"][i*ventana:(i+1)*ventana].to_list()
        temp_vy = datos["Vy"][i*ventana:(i+1)*ventana].to_list()
        temp_vz = datos["Vz"][i*ventana:(i+1)*ventana].to_list()

        for j in range(ventana):
            # Toma la muestra numero j de la tercera fila
            df[name_ax[j]][i+contador*num_chunks] = temp_ax[j]
            df[name_ay[j]][i+contador*num_chunks] = temp_ay[j]
            df[name_az[j]][i+contador*num_chunks] = temp_az[j]
            df[name_vx[j]][i+contador*num_chunks] = temp_vx[j]
            df[name_vy[j]][i+contador*num_chunks] = temp_vy[j]
            df[name_vz[j]][i+contador*num_chunks] = temp_vz[j]
            df["U"][i+contador*num_chunks] = usuario
            df["A"][i+contador*num_chunks] = actividad

    contador+=1

df.to_csv(current_dir+"/data/Dataset.csv", index=False)