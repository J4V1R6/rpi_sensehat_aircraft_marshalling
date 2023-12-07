import sys
from data_collect import run_collector
from data_show import run_show

usu_key=sys.argv[1] # "rober"
act_key=sys.argv[2] # "identify_gate"
if len(sys.argv)>=4: samples=int(sys.argv[3]) # "identify_gate"
else: samples=None

print("Recoleccion datos trabajo AIOT")

archivo = run_collector(usu_key, act_key, samples)
run_show(archivo)

print("Fin.")
