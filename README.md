# Script de generación de códigos QR

> [!NOTE]
> Este repositorio aún está en desarrollo

Este script genera una serie de códigos QR (tickets) por cada miembro de una lista en formato `.csv`. Este repositorio forma parte de una solución ad-hoc a un problema de control de accesos a un evento. Es complementario a una app para escanear y verificar los códigos QR. Esta app actualmente no está desarrollada.

Tras la ejecución del script, se generará una carpeta con los datos de salida que contendrá un archivo `dataBase.csv` con un listado de los códigos QR generados y una carpeta con el nombre de cada asistente al evento que contendrá cada uno de sus códigos QR correspondientes. El archivo `dataBase.csv` se utilizará para alimentar la base de datos de la app. 

> [!NOTE]
> El script está diseñado para que el archivo csv tenga un formato concreto pero se puede adaptar fácilmente al formato necesitado.

## Funcionamiento del script

El script recoge como primer argumento el archivo csv con el listado de asistentes y como segundo un número entero que implica la cantidad de QRs generados por cada asistente en la lista quedando el siguiente formato:

`python createQR.py ruta/al/archivo.csv numbero_de_QR_por_asistente`

Tras la ejecución, se creará en la misma ruta en la que se encuentre descargado el script la carpeta llamada outputs. Esta carpeta contendrá el archivo de salida `dataBase.csv` y una subcarpeta por cada asistente con su nombre que contendrá todos sus códigos QR correspondientes.

>[!NOTE]
>
>Actualmente también es necesario tener la imagen `etsii.jpeg` en la misma ruta del script para incluirla en el centro del QR.
>
>Esta característica se modificará próximamente.

## Archivos de entrada y salida

El primer archivo a tener en cuenta es el utilizado como primer argumento al llamar al programa, siendo un archivo `.csv` con la primera fila de cabecera. Debe tener, al menos, 3 columnas, siendo la primera columna el nombre del asistente, la segunda su(s) apellido(s) y la tercera un campo de ID. Los campos de nombre y apellidos pueden contener espacios. 

El archivo de salida `dataBase.csv` cuenta con la primera fila de cabecera con los campos `Code` que representa el código que devuelve el QR y `Passed` rellenado siempre con una 'F' que representa que el código no ha sido escaneado por la app. Cuando la app escanee el código, este campo se cambiará por una 'T'.

El resto de archivos de salida dentro de la carpeta outputs son las subcarpetas que contienen los códigos QR. 

## Ejemplo 
Se va a utilizar el archivo de ejemplo `alumnos.csv`. Este archivo contiene cuatro campos: nombre, apellidos, ID y email. El contenido del archivo es el siguiente: 

~~~

nombre,Apellidos,ID,email
Roberto,Navarro García,12345,roberto@uma.es
Eduard,Tucson,23456,edu@uma.es
Miguel Angel,Castaño,32145,miguel@uma.es

~~~

Al ejecutar el script con este archivo y pidiendo 3 QRs por cada asistente, el archivo `dataBase.csv` tendría el siguiente contenido:

~~~
Code,Passed
12345_1,F
12345_2,F
12345_3,F
23456_1,F
23456_2,F
23456_3,F
32145_1,F
32145_2,F
32145_3,F
~~~



