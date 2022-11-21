# Información de la materia:

ST0263 - Tópicos Especiales en Telemática

# Estudiante:

Samuel Ceballos Posada. sceballosp@eafit.edu.co

# Profesor:

Edwin Nelson Montoya Munera, [emontoya@eafit.edu.co](mailto:emontoya@eafit.edu.co)

# 1. Breve descripción de la actividad

Usar un cluster EMR para cumplir con las actividades propuestas.

## 1.1. Que aspectos cumplió o desarrolló de la actividad propuesta por el profesor

- Ejecutar el wordcount por linea de comando 'pyspark' INTERACTIVO en EMR con datos en HDFS vía ssh en el nodo master.
- Ejecutar el wordcount por linea de comando 'pyspark' INTERACTIVO en EMR con datos en S3 (tanto de entrada como de salida) vía ssh en el nodo master.
- Ejecutar el wordcount en JupyterHub Notebooks EMR con datos en S3 (tanto datos de entrada como de salida) usando un clúster EMR.
- Replicar, ejecutar y entender el notebook Data_processing_using_PySpark.ipynb con los datos respectivos y ejecutelo en AWS EMR.
- Gestionar datos via SQL con HIVE y SparkSQL.

## 1.2. Que aspectos NO cumplió o desarrolló de la actividad propuesta por el profesor

Todo lo propuesto ha sido implementado.

# 2. información general de diseño

- EMR: Amazon EMR es una plataforma de clúster administrada que simplifica la ejecución de los marcos de trabajo de Big Data.
- S3: Amazon Amazon S3 es un servicio de almacenamiento de objetos que ofrece escalabilidad, disponibilidad de datos, seguridad y rendimiento.

# 3. Descripción del ambiente de desarrollo y técnico:

## Parte 1:
### Ejecutar el wordcount por linea de comando 'pyspark' INTERACTIVO en EMR con datos en HDFS vía ssh en el nodo master.

Importar datasets al usuario hadoop en hdfs:

![hdfsdatasets](https://user-images.githubusercontent.com/60147093/202988770-f938006c-f4b9-4ea5-86f7-ff26fc8d1acf.PNG)

Acceder al nodo master del cluster por ssh y entrar a la consola de spark:

![pyspark1](https://user-images.githubusercontent.com/60147093/202988783-97ad9b7b-c68e-4a0d-a75d-6ca406a74135.PNG)

Correr los siguientes comandos:

![parte1comandoshdfs](https://user-images.githubusercontent.com/60147093/202988773-dcea74bd-3a37-494c-ac8f-a43aa3b53528.PNG)

Verificar que si se hayan guardado los archivos:

![parte1hdfsls](https://user-images.githubusercontent.com/60147093/202988780-98e386da-f78d-482c-9733-1eb15ef088d9.PNG)

### Ejecutar el wordcount por linea de comando 'pyspark' INTERACTIVO en EMR con datos en S3 (tanto de entrada como de salida) vía ssh en el nodo master.

Importar datasets en el bucket S3:

![parte1datasetss3](https://user-images.githubusercontent.com/60147093/202988779-ecc42a17-b818-4ec1-ac29-4fde8f07d8cc.PNG)

Ejecutar los siguientes comandos y verificar que si se hayan guardado los archivos:

![parte1comandoss3](https://user-images.githubusercontent.com/60147093/202988777-1fed1d0d-be20-4635-9a3b-3417ac012e05.PNG)

### Ejecutar el wordcount en JupyterHub Notebooks EMR con datos en S3 (tanto datos de entrada como de salida) usando un clúster EMR.

- Acceder al URL que da el EMR para entrar a jupyter.
- Crear un notebook pyspark.
- Correr las siguientes lineas:

![parte1comandosjupyter](https://user-images.githubusercontent.com/60147093/202988774-2c6e35e5-3cc3-427a-b6ba-41a785c2dfb0.PNG)

Verificar que si se hayan guardado los archivos:

![parte1jupyter](https://user-images.githubusercontent.com/60147093/202988781-21ef1582-109b-4d63-9602-7635be6bb41f.PNG)

## Parte 2:
### Replicar, ejecutar y entender el notebook Data_processing_using_PySpark.ipynb con los datos respectivos y ejecutelo en AWS EMR.
Crear un nuevo jupyter notebook (Ver archivo: [Data_processing_using_PySpark.ipynb](https://github.com/sceballosp/Laboratorios-Telematica/blob/main/Lab6/Data_processing_using_PySpark.ipynb))

Cambiar version de python:

![1](https://user-images.githubusercontent.com/60147093/202991465-75ce08e4-1849-4310-9370-26f21e08e11c.PNG)

Los comandos en las siguientes imagenes representan la siguiente lista:
- [4] Listas columnas
- [5] Número de columnas 
- [6] Número de registros 
- [7] Forma del dataset 
- [8] Imprimir esquema 
- [9] Primeras 5 filas 
- [10] Seleccionar 2 columnas y 5 registros 
- [11] Información del dataframe 

![2](https://user-images.githubusercontent.com/60147093/202991467-0e1588e6-da6f-4480-b872-30eb37cd24f4.PNG)
![3](https://user-images.githubusercontent.com/60147093/202993055-7a3dc710-3bb6-4f4d-bcd9-39660ab19438.PNG)

- [13] Se agrega columna que calcula la edad de las personas dentro de 10 años
- [14] Se pasa la edad a double
- [16] Filtra los registros en los que 'mobile' sea igual a 'Vivo'
- [17] Filtra los registros en los que 'mobile' sea igual a 'Vivo' y muestra las columnas 'age', 'ratings', 'mobile'
- [18] [19] Filtra los registros en los que 'mobile' sea igual a 'Vivo' y 'experiencia' mayor a 10
- [20] Filtra los valores de la columba 'mobile' sin repetir
- [21] Cuenta los valores de la columba 'mobile' sin repetir
- [22] Agrupa registros cuyo valor coincida respecto a la columba 'mobile' y cuenta
- [23] Cuenta las coincidencias de un valor de la columba 'mobile' y los agrupa de mayor a menor
- [24] Agrupa y muestra el promedio en que aparece el valor para cada columna en 'mobile'
- [25] Agrupa y muestra la suma en que aparece el valor para cada columna en 'mobile'
- [26] Agrupa y muestra el maximo en que aparece el valor para cada columna en 'mobile'
- [27] Agrupa y muestra el minimo en que aparece el valor para cada columna en 'mobile'
- [28] Agrupa y muestra la agregación en 'mobile'
- [31] Catalogar las marcas en 'High price', 'Mid Price' y 'Low Price'
- [32] Utilizar funcion lambda para determinar si la persona es joven o adulta.
- [52] Años faltantes para los 100
- [54] Multiplicar el 'rating' por 'experience'
- [38] Cuenta valores duplicados y drop a los valores duplicados
- [41] Drop a los valores de la columba 'mobile'

![3 5](https://user-images.githubusercontent.com/60147093/202993063-3e07dca9-3f9c-4a5e-a472-3dd41778179c.png)
![4](https://user-images.githubusercontent.com/60147093/202991471-e3316b6a-bc79-4a3e-9279-2c7ba9d4685b.PNG)
![5](https://user-images.githubusercontent.com/60147093/202991472-72964ae7-308b-484c-b2d4-27c89c0857d9.PNG)
![6](https://user-images.githubusercontent.com/60147093/202991474-39285e22-7bfc-4c5b-8f9c-739815ad0c43.PNG)
![7](https://user-images.githubusercontent.com/60147093/202991479-90a9fc52-a3ce-4c9a-9e9f-ab4e446ba82e.PNG)
![8](https://user-images.githubusercontent.com/60147093/202991482-6ffb68f1-5b7c-48d6-9e25-433aa48d709d.PNG)
![9](https://user-images.githubusercontent.com/60147093/202999287-a3a07a79-7f20-4d7d-8bfa-f5a416875e6a.jpeg)
![12](https://user-images.githubusercontent.com/60147093/202998605-5871813b-2fb2-49a3-84e9-297a170f9133.PNG)
![13](https://user-images.githubusercontent.com/60147093/202998608-5f7559d0-a196-4a80-a798-05dceb9bc626.PNG)
![10](https://user-images.githubusercontent.com/60147093/202998872-ce80028b-6e35-40af-b167-2bf958195dbb.PNG)

- Guardar archivos

![11](https://user-images.githubusercontent.com/60147093/202991488-f05a33db-eeb0-4c52-a046-b612e824cade.PNG)


## Parte 3:
### Gestionar datos via SQL con HIVE y SparkSQL.

Entrar a Hive por la interfaz de HUE en el EMR:

![WhatsApp Image 2022-11-21 at 1 31 10 AM](https://user-images.githubusercontent.com/60147093/203001619-65fa7e7d-d61f-42c5-a9fb-921e2e5c55dc.jpeg)

Crear una tabla HDI en HDFS:

![tablaHDI](https://user-images.githubusercontent.com/60147093/203001613-827c6177-6766-42af-8ee3-93c338fa9a1d.PNG)

Consultar paises con un gni mayor a 2000:

![gniMenor2000](https://user-images.githubusercontent.com/60147093/203001590-9ac4ba58-e461-45aa-a815-cce0739570e4.PNG)

Crear una tabla EXPO:

![tablaEXPO](https://user-images.githubusercontent.com/60147093/203001605-52b80629-c8d1-4942-bb17-1a23179c43b1.PNG)

Hacer un JOIN con las tablas EXPO y HDI:

![jointablasHDIexpo](https://user-images.githubusercontent.com/60147093/203001595-aedcbbfa-f555-4ff6-b93d-b2152fcbc3ca.PNG)

Crear una tabla para hacer el wordcount en Hive:

![wordcount](https://user-images.githubusercontent.com/60147093/203001622-1cc27ab5-1d68-454c-8dd3-8e835035bbce.PNG)

Wordcount ordenado por palabra:

![wordcountordenado](https://user-images.githubusercontent.com/60147093/203001624-19d60237-24f1-4a5c-8e12-97422a98dbb4.PNG)

Wordcount ordenado de menor a mayor:

![menor a mayor](https://user-images.githubusercontent.com/60147093/203001601-ce835c41-64c2-48d6-8e26-1d2ab28a8912.PNG)

# 4. Información relevante

## Referencias:

- https://github.com/st0263eafit/st0263-2022-2/tree/main/bigdata/03-spark
- https://github.com/st0263eafit/st0263-2022-2/tree/main/bigdata/04-hive-sparksql
