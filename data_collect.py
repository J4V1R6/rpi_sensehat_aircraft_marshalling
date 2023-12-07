import numpy as np
import time
import statistics as stats
import os.path
from time import sleep
from sense_hat import SenseHat
from config import actividades, usuarios, data_folder

def run_collector(usu_key, act_key, samples=1400):
    sense=SenseHat()
    
    print("Recording %s %s"%(usu_key, act_key))

    USUARIO=usuarios[usu_key]
    ACTIVIDAD=actividades[act_key]

    usuario_list=[]
    actividad_list=[]
    t=[]
    t_sample=[]
    accel_x, accel_y, accel_z = [], [], []
    gyros_x, gyros_y, gyros_z = [], [], []
    t_ini=time.time()
    t_ant=t_ini
    # 
    # 40*3*400/28  = 1800
    # 40*2*400/28  = 1200
    # 40*2*1200/67 = 1400 -> En 1min y 7 seg, captura 1200 muestras. 
    # Queremos 40 repeticiones de 2 segundos
    muestras=samples # muestras que tomamos
    accel_average=[]

    archivo=data_folder+"/"+str(USUARIO)+"_"+act_key+"_"+str(muestras) # nombre del archivo
    tipo_archivo=".csv" # extension 

    #bucle for para tomar los datos
    for i in range(muestras):
        usuario_list.append(USUARIO)
        actividad_list.append(ACTIVIDAD)
        t_actual=time.time()
        acceleration = sense.get_accelerometer_raw()
        #datos de aceleración en Gs
        accel_x.append(acceleration['x'])
        accel_y.append(acceleration['y'])
        accel_z.append(acceleration['z'])
        gyroscope = sense.get_gyroscope_raw()
        #datos de velocidad rad/s
        gyros_x.append(gyroscope['x'])
        gyros_y.append(gyroscope['y'])
        gyros_z.append(gyroscope['z'])
        
        t.append(t_actual-t_ini)
        t_sample.append(t_actual-t_ant)
        
        t_ant=t_actual
        
    sense=SenseHat()
    O = [255,0,0]
    X = [255,255,0]

    UNO = [
      O, O, O, O, O, O, O, O,
      O, O, O, O, O, O, O, O,
      O, O, O, O, O, O, O, O,
      O, O, O, X, X, O, O, O,
      O, O, O, X, X, O, O, O,
      O, O, O, O, O, O, O, O,
      O, O, O, O, O, O, O, O,
      O, O, O, O, O, O, O, O,
      ]

    # fin de la toma de muestras
    sense.set_pixels(UNO) 
    sleep(10)
    sense.clear()

    print("Rate: ",int(1/float(format(stats.mean(t_sample),"f")))," Hz")

    datosIMU=np.array([usuario_list, actividad_list, t,accel_x,accel_y,accel_z,gyros_x,gyros_y,gyros_z])

    #El siguiente código comprueba que no hay ningun archivo con su nombre para no sobreescribirlo
    intentos=0
    while(os.path.isfile(archivo+tipo_archivo)):
        #En caso de que exista un fichero con dicho nombre, le pone un numero al final (consecutivo)
        print("El archivo",archivo,"ya existe")
        intentos+=1
        if(intentos>1):
            archivo=archivo[:-2]
        archivo=archivo+"_"+str(intentos)

    print("Se guardará el archivo con nombre: ",archivo)
    # Crea un archivo csv y guarda los datos
    np.savetxt(archivo+tipo_archivo,datosIMU,delimiter=',',fmt='%.6f')

    return archivo+tipo_archivo
