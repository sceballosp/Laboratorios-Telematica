# Información de la materia:

ST0263 - Tópicos Especiales en Telemática

# Estudiante:

Samuel Ceballos Posada. sceballosp@eafit.edu.co

# Profesor:

Edwin Nelson Montoya Munera, [emontoya@eafit.edu.co](mailto:emontoya@eafit.edu.co)

# 1. Breve descripción de la actividad

Analisis del dataset de Covid-19 en Google Colab, por medio del dataframe PySpark y PySpark SQL. El analisis se hizo en dos jupyter notebooks distintos, uno con datos de origen en google drive y el otro en AWS S3.

## 1.1. Que aspectos cumplió o desarrolló de la actividad propuesta por el profesor

- Importar datos de Google Drive y AWS S3.
- Hacer operaciones con el dataframe PySpark.
- Hacer operaciones con Pyspark SQL.

## 1.2. Que aspectos NO cumplió o desarrolló de la actividad propuesta por el profesor

Todo lo propuesto ha sido implementado.

# 2. información general de diseño

- Drive: Servicio de almacenamiento de datos de Google.
- S3: Amazon Amazon S3 es un servicio de almacenamiento de objetos que ofrece escalabilidad, disponibilidad de datos, seguridad y rendimiento.
- PySpark: Framework de procesamiento de datos a alta escala.  

# 3. Descripción del ambiente de desarrollo y técnico:

## 0. Almacenar datos en AWS S3 y en Gogle Drive

### Descargar repositorio con los datos:

![descargardatos](https://user-images.githubusercontent.com/60147093/203430696-22082557-ed97-4dcc-b7c8-884ab8c9d329.jpeg)

### Google Drive
- Subir los datos a drive:

![subuirdatosdrive](https://user-images.githubusercontent.com/60147093/203430707-eedec78b-804f-4c52-ac43-37c9d4357029.PNG)

### AWS S3
- Subir los datos a un bucket en S3:

![subirdataset](https://user-images.githubusercontent.com/60147093/203430794-32ca0a08-67ba-4219-b3f6-d2dc00d29460.PNG)

### Abrir el notebook donde se hará en analisis en google colab:

![abrircoolab](https://user-images.githubusercontent.com/60147093/203430717-04878e4e-f4f0-438c-8109-2d520a9db9bc.jpeg)


## 1. Cargar datos desde Google Drive y AWS S3

### Google Drive
- Copiar la ruta donde estan almacenados los datos en drive:

![copiarruta](https://user-images.githubusercontent.com/60147093/203432219-b7bc727b-8088-4e4b-9e50-1b81cc4fe1ed.jpeg)

- Verificar que si carguen los datos:

![prueba1](https://user-images.githubusercontent.com/60147093/203432220-dfe8f045-59d1-4c3f-95c9-7f85e34465ce.PNG)
![prueba2](https://user-images.githubusercontent.com/60147093/203432222-48ce4300-e377-435d-97ec-910a18063b2e.PNG)

### AWS S3
- Copiar las credenciales de AWS para hacer la conexion:

![credencialesAWS](https://user-images.githubusercontent.com/60147093/203432248-a9028c02-e661-4716-b942-3af16402441c.PNG)

- Pegar las credenciales y verificar el funcionamiento:

![prueba1](https://user-images.githubusercontent.com/60147093/203432250-be3a843c-f7d9-4def-a0d6-48fefac21e71.PNG)
![prueba2](https://user-images.githubusercontent.com/60147093/203432252-e197236f-ae74-4440-a173-bb0280fcde73.PNG)
![prueba3](https://user-images.githubusercontent.com/60147093/203432253-6aa14a8f-f4e2-4d5e-b523-3ba3ff4e16d3.PNG)
![prueba4](https://user-images.githubusercontent.com/60147093/203432254-c6d999c2-3b7a-4d42-961c-6115fdd61b99.PNG)

## 2. Análisis exploratorio del dataframe donde cargamos los datos

El analisis se hizo en dos notebooks distintos, cargando los datos desde Google Drive y AWS S3.

- Google Drive: [Proyecto_3_data_processing_using_PySpark_google_colab.ipynb](https://github.com/sceballosp/Laboratorios-Telematica/blob/main/Proyecto3/Proyecto_3_data_processing_using_PySpark_google_colab.ipynb)

- AWS S3: [Proyecto_3_data_processing_using_PySpark_AWS](https://github.com/sceballosp/Laboratorios-Telematica/blob/main/Proyecto3/Proyecto_3_data_processing_using_PySpark_AWS.ipynb)


2.1) Columnas:

![columnas](https://user-images.githubusercontent.com/60147093/203434106-4d414a79-0e77-43c6-b96c-a099ec218e95.PNG)

2.2) Tipos de datos:

![tipodatos](https://user-images.githubusercontent.com/60147093/203434110-b91cac66-3bff-45c6-a811-938b538d7ca3.PNG)

2.3) Seleccionar algunas columnas:

![seleccionarcolumnas](https://user-images.githubusercontent.com/60147093/203434109-e3356fe8-9fe9-4069-88b5-7efdf378c96d.PNG)

2.4) Renombrar columnas:

![renombarcolumnas](https://user-images.githubusercontent.com/60147093/203434108-a4dd8a59-f8e5-4c6c-9bc2-a3a0dd986e54.PNG)

2.5) Agregar columnas:

![agregarcolumna](https://user-images.githubusercontent.com/60147093/203434102-6c093545-dfb6-4122-be95-e7e34e5f36cd.PNG)

2.6) Borrar columnas: 

![borrarcolumna](https://user-images.githubusercontent.com/60147093/203434104-69a22abe-68c9-416e-95ed-a7d48ac5799e.PNG)

2.7) Filtrar datos:

![filtrardatos](https://user-images.githubusercontent.com/60147093/203434107-c28ac7dc-8664-4c8b-b660-d9e94ce7f129.PNG)

2.8) Ejecutar alguna función UDF o lambda sobre alguna columna creando una nueva:

![udf](https://user-images.githubusercontent.com/60147093/203434114-71d24719-fda2-43d9-927d-3ae1ee1c52ea.PNG)


## 3. Contestar las siguientes preguntas sobre los datos de covid
3.1) Los 10 departamentos con más casos de covid en Colombia ordenados de mayor a menor:

- Dataframe:

![1](https://user-images.githubusercontent.com/60147093/203434621-5704134f-efeb-41b9-aeeb-1d9f8ebc223d.PNG)

- SparkSQL:

![1](https://user-images.githubusercontent.com/60147093/203434746-a4b30d4e-9649-4a7e-88f5-8aa0c37ef83d.PNG)

3.2) Las 10 ciudades con más casos de covid en Colombia ordenados de mayor a menor:

- Dataframe:

![2](https://user-images.githubusercontent.com/60147093/203434624-1593a1e9-02aa-4f74-8ca7-9bcf8907f87f.PNG)

- SparkSQL:

![2](https://user-images.githubusercontent.com/60147093/203434748-fb4fbf7b-60f6-4395-a7da-ef8576f9cc65.PNG)

3.3) Los 10 días con más casos de covid en Colombia ordenados de mayor a menor:

- Dataframe:

![3](https://user-images.githubusercontent.com/60147093/203434626-481deb98-e0c2-4251-87ab-cf2b93b819ce.PNG)

- SparkSQL:

![3](https://user-images.githubusercontent.com/60147093/203434749-eb2e438e-1768-4e1d-8303-63cd2ce175c3.PNG)

3.4) Distribución de casos por edades de covid en Colombia:

- Dataframe:

![4](https://user-images.githubusercontent.com/60147093/203434629-3526707a-df7b-4391-b315-19c8b1b10844.PNG)

- SparkSQL:

![4](https://user-images.githubusercontent.com/60147093/203434752-3610cac2-0b0f-4902-a57a-292ec8fbeb88.PNG)

3.5) Distribución de casos por genero:

- Dataframe:

![5](https://user-images.githubusercontent.com/60147093/203434632-1dfe45bd-7d78-4595-9282-7fb294f3c267.PNG)

- SparkSQL:

![5](https://user-images.githubusercontent.com/60147093/203434753-6e6efadb-ddca-4160-ab36-a053a0001b0d.PNG)


## 4. Guardar los datos anteriores en AWS S3

- En el archivo con la conexion a AWS agregar las lineas:

![guardars3](https://user-images.githubusercontent.com/60147093/203435490-f1a36e4e-90f3-44ae-9aa2-030bc1c2fa95.PNG)

- Verificar que si se hayan guardado los datos en S3:

**URI:** s3://datasetssceballosp/s3_csv/

![s3](https://user-images.githubusercontent.com/60147093/203435497-34f1e997-fbd5-4ae5-ab63-5306a0fd3347.jpeg)

### BONUS: Guardar los datos anteriores en drive

![guardargoogle](https://user-images.githubusercontent.com/60147093/203435712-73625cd8-7178-4a24-a099-5aa7cf4ae7ff.PNG)

**Link:** https://drive.google.com/drive/folders/17fCEP7TX3V11MBYcwrE7mV0h7jRokGBz?usp=sharing

![drive](https://user-images.githubusercontent.com/60147093/203435715-19b1afb4-4a4f-4fa3-8cf2-45ea7f5de973.PNG)



# 4. Información relevante

## Referencias:

- https://github.com/st0263eafit/st0263-2022-2/tree/main/bigdata/03-spark
