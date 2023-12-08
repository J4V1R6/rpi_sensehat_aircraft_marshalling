import os
import pandas as pd

ventana = 40

current_dir = os.getcwd()
print(current_dir)

# Por cada movimiento se carga cada csv y se guarda en un dataframe
datos=pd.read_csv(current_dir+"/data/all/1_emergency_stop_1400.csv", header=None).transpose()#.rename(columns={0: 'ID', 1: 'First Name', 2: 'Last Name'})
datos.columns = ["usuario","accion","tiempo","Ax","Ay","Az","Vx","Vy","Vz"]

print(datos)

usuario = datos["usuario"][0]
actividad = datos["accion"][1]

# Se crean las columnas
name_ax = ["Ax"+str(i) for i in range(ventana)] # columnas que queremos
name_ay = ["Ay"+str(i) for i in range(ventana)]
name_az = ["Az"+str(i) for i in range(ventana)]
name_vx = ["Vx"+str(i) for i in range(ventana)]
name_vy = ["Vy"+str(i) for i in range(ventana)]
name_vz = ["Vz"+str(i) for i in range(ventana)]


# Se crea un dataframe vacio con las columnas que queremos
df = pd.DataFrame(columns = name_ax+name_ay+name_az+name_vx+name_vy+name_vz+["U","A"]).astype(float)

print(datos.shape)
muestras = datos.shape[0]

for i in range(int(muestras/ventana)):
    for j in range(ventana):
        # Toma la muestra numero j de la tercera fila
        df[name_ax[j]] = datos["Ax"][i*ventana:(i+1)*ventana]
        df[name_ay[j]] = datos["Ay"][i*ventana:(i+1)*ventana]
        df[name_az[j]] = datos["Az"][i*ventana:(i+1)*ventana]
        df[name_vx[j]] = datos["Vx"][i*ventana:(i+1)*ventana]
        df[name_vy[j]] = datos["Vy"][i*ventana:(i+1)*ventana]
        df[name_vz[j]] = datos["Vz"][i*ventana:(i+1)*ventana]
        df["U"] = usuario
        df["A"] = actividad

#print(datos["Ax"][0:ventana])
print(datos["Ax"].shape)

df.to_csv(current_dir+"/data/test_1_emergency_stop_1400.csv", index=False)