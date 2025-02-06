import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import classification_report, confusion_matrix, roc_curve, auc, precision_recall_curve, average_precision_score, classification_report
import matplotlib.pyplot as plt

# Cargar el dataset
df = pd.read_csv('alumnos.csv', encoding='utf-8')

# Mostrar los primeros 5 filas del dataset
print(df.head())
print(df.info())
print(df.describe())

def matriz_correlaciones(y,X,se_dibuja=False):
    '''
    Calcula y dibuja la matriz de correlaciones
    Devuelve:
    yX - datos concatenado
    yC_corr - matriz de correlacioness, correlacion de Person entre [-1, +1]
    yX_abs_corre - matriz de correlaciones en valor absoluto
    '''
    yX = pd.concat([y,X],axis=1)
    yX = yX.rename(columns={0: 'TARGET'})
    #Calcula la matriz y convierte a Dataframe para visualizar mejor
    yX_corr = yX.corr(method='pearson')
    yX_abs_corr = np.abs(yX_corr) #Convierte el valor a absoluto
    if se_dibuja:
        plt.figure(figsize=(10,10))
        plt.imshow(yX_abs_corr,cmap='RdYlGn',interpolation='none', aspect='auto')
        plt.colorbar()
        plt.xticks(range(len(yX_abs_corr)),yX_abs_corr.columns,rotation='vertical')
        plt.yticks(range(len(yX_abs_corr)),yX_abs_corr.columns)
        plt.suptitle('Mapa de Calor de Correlacion (valor absoluto)', fontsize=13, fontweight='bold')
        plt.show()
    return yX, yX_corr, yX_abs_corr

# Seleccion de variables predictoras
X = df.drop(columns=['NOMBRE','LLEVA_GAFAS']) # Eliminamos Variables no predictoras y target (nos quedamos con las variables predictoras)
# Variable objetivo (target)
y = df['LLEVA_GAFAS']


# Correlacion entre variables predictoras y la variable objetivo
df = df.drop(columns=['NOMBRE'])
correlations = df.corr()
print(correlations["LLEVA_GAFAS"].sort_values(ascending=False))

# Dividimos el dataset en train y test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Creamos y entrenamos los modelos clasificadores
# Creamos un modelo de regresión logística
logistic_regression = LogisticRegression(max_iter=1000)
logistic_regression.fit(X_train, y_train)

# Creamos un modelo de GBM
gbm = GradientBoostingClassifier(n_estimators=100, learning_rate=0.1, max_depth=3, random_state=42)
gbm.fit(X_train, y_train)

# Calculamos las predicciones
logistic_pred = logistic_regression.predict(X_test)
gbm_pred = gbm.predict(X_test)


# Evaluamos los modelos
print("Regresión Logística:")
print(confusion_matrix(y_test, logistic_pred))
print(classification_report(y_test, logistic_pred))

print("Gradient Boosting Machine")
print(confusion_matrix(y_test, gbm_pred))
print(classification_report(y_test, gbm_pred))

yX, yX_corr, yX_abs_corr = matriz_correlaciones(y_train, X_train,se_dibuja=True)

# Calculamos las curvas ROC y precisión-recall
models = {'Regresión Logística': logistic_regression, 'Gradient Boosting Machine': gbm}
result = {}
plt.figure(figsize=(15, 6))


for i, (name,model) in enumerate(models.items(),start=1):
    #Prediccion de probabilidad
    y_pred_proba = model.predict_proba(X_test)[:, 1]

    # Curva ROC y AUC
    fpr, tpr, _ = roc_curve(y_test, y_pred_proba)
    roc_auc = auc(fpr, tpr)
    result[name] = {'ROC AUC': roc_auc}

    # Curva Precision-Recall
    precision, recall, _ = precision_recall_curve(y_test, y_pred_proba)
    average_precision = average_precision_score(y_test, y_pred_proba)
    result[name]['Precision-Recall AUC'] = average_precision

    # Graficas
    plt.subplot(1, 2, 1)
    plt.plot(fpr, tpr, label=f'{name} (AUC = {roc_auc:.2f})')
    plt.title('Curva ROC')
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.legend(loc='lower right')

    plt.subplot(1, 2, 2)
    plt.plot(recall, precision, label=f'{name} (Precision-Recall AUC = {average_precision:.2f})')
    plt.title('Curva Precision-Recall')
    plt.xlabel('Recall')
    plt.ylabel('Precision')
    plt.legend(loc='lower left')

plt.tight_layout()
plt.show()

# Informe de clasificación
for name, model in models.items():
    print(f"\n=== {name} ===")
    y_pred = model.predict(X_test)
    print("Informe de Clasificación:")
    print(classification_report(y_test, y_pred))
    print(f"ROC AUC: {result[name]['ROC AUC']:.2f}")
    print(f"Precision-Recall AUC: {result[name]['Precision-Recall AUC']:.2f}")
