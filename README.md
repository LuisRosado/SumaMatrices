# SumaMatrices
Programa para crear matrices y sumarlas

![image](https://github.com/LuisRosado/SumaMatrices/assets/140114139/3044842b-e99d-429b-a264-037da0f52531)

crear_matriz(Tamaño): Esta función solicita al usuario ingresar los elementos de una matriz cuadrada de tamaño Tamaño. Crea una lista de listas (matriz) y, mediante dos bucles for, llena la matriz con los valores ingresados por el usuario. Luego, muestra la matriz creada y espera a que el usuario presione "Enter" para continuar. La función devuelve la matriz creada.

![image](https://github.com/LuisRosado/SumaMatrices/assets/140114139/23949523-9892-4177-9c94-07eb4cfde22f)

sumar_matriz(m1, m2): Esta función toma dos matrices m1 y m2 como argumentos y devuelve la matriz resultante de la suma de ambas. Para ello, utiliza dos bucles for para recorrer los elementos de ambas matrices y realizar la suma correspondiente para cada elemento, almacenándolos en una nueva matriz m3.

Función Principal: La función principal del programa inicia solicitando al usuario el tamaño de las matrices (Tamaño). Luego, crea dos matrices llamando a la función crear_matriz(Tamaño) para cada una, y las almacena en las variables a y b.

Después de crear las dos matrices, el programa suma ambas matrices utilizando la función sumar_matriz(a, b) y almacena el resultado en la matriz c.

Finalmente, muestra el resultado de la suma (c) en forma de matriz en la pantalla.

Es importante mencionar que este código asume que el usuario ingresará los valores numéricos de los elementos de las matrices y no realiza validaciones para verificar si el usuario ingresa datos válidos. En un escenario real, sería necesario agregar validaciones para garantizar que los valores ingresados sean números enteros o flotantes válidos.
