import numpy as np
import sklearn as sk
#CALCULO DEL COEFICIENTE DE DETERMINACION
#SOLUCION 1
def coficient_deter(array_real, array_predic):
    media = np.mean(array_real)
    numerador = np.sum((array_real - array_predic)**2)
    denominador = np.sum((array_real - media)**2)
    r = 1 - (numerador / denominador)
    return r


y_real = np.array([3, -0.5, 2, 7, 4.2])
y_predicho = np.array([2.5, 0.0, 2, 8, 4.1])


result = coficient_deter(y_real, y_predicho)
print(f"Coeficiente de determinacion {result:.2f}")

#SOLUCION 2 CON SKLEARN
print(sk.r2_score(y_real, y_predicho))
