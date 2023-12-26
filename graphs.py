import os

import config
from tools.data_show import run_show
from tools.menu import menu_show

graphs_folder = config.data_folder+"/all"

data_files = os.listdir(graphs_folder)
file = menu_show("Selecciona un archivo",data_files)
filepath = graphs_folder+"/"+file
print("Mostrando "+filepath)
run_show(filepath)