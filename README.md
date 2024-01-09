# rpi_sensehat_aircraft_marshalling
Trabajo para la asignatura Aplicaciones IOT, del Máster de Ingeniería de Telecomunicaciones de la Universidad de Sevilla.
Desarrollado por:
 - Roberto Lama Rodríguez
 - Javier Ros Raposo

## Uso

**Recolección de datos**
```bash
python3 collect.py usuario accion
```

**Preprocesamiento de los datos**
```bash
python3 preprocess_dataset.py
```

**Entrenamiento de la red**

 * Red puramente densa
```bash
python3 train_densev1.py
```

 * Árbol de decisión
```bash
python3 train_decission_tree.py
```

		* Red Convolucional 1 dimensión: 1 convolucional + 1 densa 
```bash
python3 train_cnn1d_1c1d.py
```

		* Red Convolucional 1 dimensión: 1 convolucional + 2 densas 
```bash
python3 train_cnn1d_1c2d.py
```

		* Red Convolucional 1 dimensión: 2 convolucionales + 1 densa 
```bash
python3 train_cnn1d_2c1d.py
```

		* Red Convolucional 1 dimensión: 2 convolucionales + 2 densas
```bash
python3 train_cnn1d_2c2d.py
```