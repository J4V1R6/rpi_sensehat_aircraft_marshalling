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
 * Decission Tree
```bash
python3 train_cnn1d.py
```

 * Decission Tree
```bash
python3 train_decission_tree.py
```