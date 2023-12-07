import sys
import config
from tools.data_collect import run_collector
from tools.data_show import run_show

if len(sys.argv)<3:
    print("Error: se requieren dos argumentos: usuario y accion")
    print("Ejemplo: python main.py rober identify_gate")
    sys.exit(1)

usu_key=sys.argv[1] # "rober"
act_key=sys.argv[2] # "identify_gate"
if len(sys.argv)>=4: samples=int(sys.argv[3]) # "identify_gate"
else: samples=None

if not usu_key in config.usuarios.keys():
    print("Error: usuario no reconocido")
    sys.exit(1)
if not act_key in config.actividades.keys():
    print("Error: accion no reconocida")
    sys.exit(1)

print("Recoleccion datos trabajo AIOT")

archivo = run_collector(usu_key, act_key, samples)
run_show(archivo)

print("Fin.")
