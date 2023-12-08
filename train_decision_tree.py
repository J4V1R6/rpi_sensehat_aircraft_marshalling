# -*- coding: utf-8 -*-
"""
Created on 

@author: 

ARBOL DE DECISION CON SERIE TEMPORAL

"""
import datetime
import config
import pandas as pd
import matplotlib.pyplot as plt

clases=len(config.actividades.keys())

datos = pd.read_csv('data/Dataset.csv')

print(datos.shape)
print(datos.info())
print(datos.columns)


#%% después de elinar los algunas columnas

print(datos.columns)
print(datos.shape)
 

#%% dividimos los datos

from sklearn.model_selection import train_test_split

X = datos.drop(columns = ["A"])
y = datos["A"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, stratify=y, random_state=42)

print("=====================================================")
print("X_train, X_test, y_train, y_test")
print("=====================================================")
print(X_train.shape)
print(X_test.shape)
print(y_train.shape)
print(y_test.shape)

#%% Entrenamiento simple

from sklearn.tree import DecisionTreeClassifier
max_depth          = 10
min_samples_leaf   = 5
min_samples_split  = 2
criterion          = "gini"
tree_clf = DecisionTreeClassifier(max_depth=max_depth, min_samples_leaf=min_samples_leaf, min_samples_split=min_samples_split,
                                  criterion=criterion)
tree_clf.fit(X_train, y_train)

#%% resultados de test

ypred = tree_clf.predict(X_test)

from sklearn.metrics import accuracy_score

print("Modelo:")
print("\tmax_depth:",max_depth)
print("\tmin_samples_leaf:",min_samples_leaf)
print("\tmin_samples_split:",min_samples_split)
print("\tcriterion:",criterion)
print("accuracy:",accuracy_score(y_test, ypred)) 


#%% resultados hiper parametrización Grid
# TARDA 10-15 MINUTOS

from sklearn import model_selection
from sklearn.tree import DecisionTreeClassifier


param_grid = {"max_depth": [1, 10, 20, 30],
          "min_samples_split":[2, 4, 8, 10, 20],
          "min_samples_leaf": [1, 2, 3, 4, 5],
          "criterion":["entropy","gini"]}

print("GridSearch starts")
model = model_selection.GridSearchCV(estimator= DecisionTreeClassifier(),
                                     param_grid=param_grid,
                                     scoring="accuracy",
                                     cv=5)


model.fit(X_train, y_train)

#%% resultados 

print("val. score: %s" % model.best_score_)
print("test score: %s" % model.score(X_test, y_test))

print("Mejores parámetros:", model.best_params_)

parametros = model.best_params_
print(type(parametros))

#%% comprobamos los mejores resultados

from sklearn.metrics import accuracy_score

scores = list()
for i in range(10):
    
    modelo_final = DecisionTreeClassifier()
    modelo_final.set_params(**model.best_params_)
    
    modelo_final.fit(X_train, y_train)
    
    ypred_final = modelo_final.predict(X_test)
    
    score = accuracy_score(y_test, ypred_final) *100.0
    print("Iteration",i,":",score)
    scores.append(score)
    
    # model.save_weights('./models/%s_decission_tree_model_%d.h5'%(datetime.datetime.now().strftime("%Y%m%d_%H%M%S"),i))

print(scores)

from numpy import mean
print("Accuracy medio de:",mean(scores))

from matplotlib import pyplot
pyplot.figure()
pyplot.boxplot(scores)
pyplot.title('Accuracy para max_deph=%s, min_samples_split=%s, min_samples_leaf=%s, criterion=%s' % (parametros['max_depth'], parametros['min_samples_split'], parametros['min_samples_leaf'], parametros['criterion']))
pyplot.ylabel("Accuracy (%)")
pyplot.grid(linestyle='-', linewidth=0.3)


#%% matriz de confusion

from sklearn.metrics import confusion_matrix

ypred = modelo_final.predict(X_test)

cm = confusion_matrix(y_test, ypred)
print(cm)

#%% matriz de confusión 

#Se muestra la matriz de confusion de la ultima iteracion del bucle for. 
#Si se quiere mostrar la de todas las iteraciones, meter la llamada a la funcion dentro del bucle for

import numpy as np

import itertools

acts = y.unique()

def plot_confusion_matrix(cm, classes,
                          normalize=False,
                          title='Confusion matrix',
                          cmap=plt.cm.Blues):
    """
    This function prints and plots the confusion matrix.
    Normalization can be applied by setting `normalize=True`.
    """
    plt.imshow(cm, interpolation='nearest', cmap=cmap)
    plt.colorbar()
    tick_marks = np.arange(len(classes))
    plt.xticks(tick_marks, classes, rotation=45)
    plt.yticks(tick_marks, classes)

    if normalize:
        cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]

    thresh = cm.max() / 2.
    for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
        plt.text(j, i, cm[i, j],
                 horizontalalignment="center",
                 color="white" if cm[i, j] > thresh else "black")

    plt.tight_layout()
    plt.ylabel('Actual')
    plt.xlabel('Prediction')
    plt.xticks(range(clases), acts)
    plt.yticks(range(clases), acts)
    

plt.figure()
plot_confusion_matrix(cm, classes = range(clases))  

plt.show()