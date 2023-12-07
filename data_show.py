import numpy as np
import matplotlib.pyplot as plt
from config import actividades, usuarios

def return_key_from_val(val,dicc):
	for key, value in dicc.items():
		if val == value:
			return key

datos = np.loadtxt('data/0_prueba_1.csv', delimiter=',')
usu=datos[0,:]
act=datos[1,:]
t = datos[2,:]
accel_x = datos[3,:]
accel_y = datos[4,:]
accel_z = datos[5,:]
gyros_x = datos[6,:]
gyros_y = datos[7,:]
gyros_z = datos[8,:]

plt.figure()
plt.subplot(211)
plt.plot(t,accel_x,'b')
plt.plot(t,accel_y,'r')
plt.plot(t,accel_z,'y')
plt.legend(['x','y','z'])
plt.grid()
plt.xlabel('t (s)')
plt.ylabel('A (Gs)')
plt.title('Datos usuario:'+return_key_from_val(usu[0],usuarios)+' actividad:'+return_key_from_val(act[0],actividades))

plt.subplot(212)
plt.plot(t,gyros_x,'b')
plt.plot(t,gyros_y,'r')
plt.plot(t,gyros_z,'y')
plt.legend(['x','y','z'])
plt.grid()
plt.xlabel('t (s)')
plt.ylabel('V (rad/s)')
plt.show()
