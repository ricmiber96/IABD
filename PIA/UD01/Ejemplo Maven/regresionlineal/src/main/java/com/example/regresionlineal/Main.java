package com.example.regresionlineal;

import org.apache.commons.math3.stat.regression.SimpleRegression;

public class Main {
    public static void main(String[] args) {
        SimpleRegression regr = new SimpleRegression();

        regr.addData(1, 3);
        regr.addData(2, 5);
        regr.addData(3, 7);
        regr.addData(4, 9);
        regr.addData(5, 11);

        System.out.println("Pendiente: " + regr.getSlope());
        System.out.println("Ordenada en el origen: " + regr.getIntercept());
        System.out.println("Coeficiente de correlación: " + regr.getR());

        double prediction = regr.predict(6);
        System.out.println("Predicción para X = 6: " + prediction);
    }
}