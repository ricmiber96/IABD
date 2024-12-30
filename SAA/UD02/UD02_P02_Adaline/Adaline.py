import numppy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

class AdalineGDB(object):
    """
    Clasificador Adaline de Ricardo
    Parametros:
    ----------------------
    eta: float, tasa de aprendizaje
    n_iter: int, numero de iteraciones max al dataset de entrenamiento
    seed: int, semilla aleatoria para la generacion de numeros aleatorios
    ----------------------
    Atributos:
    w_: array-1d, pesos actualizados tras el ajuste despues del entrenamiento
    cost_: list, lista de valores de la funcion de coste SSE por epoca
    """

    