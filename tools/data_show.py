import numpy as np
import matplotlib.pyplot as plt
from config import actividades, usuarios, graph_folder

def return_key_from_val(val,dicc):
	for key, value in dicc.items():
		if val == value:
			return key

def run_show(filepath):
	if "/" in filepath: folder,filename = filepath.split("/")
	else: filename=filepath
	
	name,ext = filename.split(".")
	outputpath = graph_folder+"/"+name+".png"
	
	datos = np.loadtxt(filepath, delimiter=',')
	usu=datos[0,:]
	act=datos[1,:]
	t = datos[2,:]
	accel_x = datos[3,:]
	accel_y = datos[4,:]
	accel_z = datos[5,:]
	gyros_x = datos[6,:]
	gyros_y = datos[7,:]
	gyros_z = datos[8,:]

	fig = plt.figure(name)
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
	
	#manager = plt.get_current_fig_manager()
	#manager.full_screen_toggle()
	#manager.window.showMaximized()
	# plt.savefig(outputpath)
	# generate your plot
	#fig.savefig(outputpath,bbox_inches='tight')#dpi=600, 
	
	plt.show()

