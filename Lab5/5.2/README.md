# Información de la materia:
ST0263 - Tópicos Especiales en Telemática

# Estudiante:
Samuel Ceballos Posada. sceballosp@eafit.edu.co

# Profesor:
Edwin Nelson Montoya Munera, [emontoya@eafit.edu.co](mailto:emontoya@eafit.edu.co)

# 1. Breve descripción de la actividad
Aprender a usar el sistema de archivos HDFS conectandose a un cluster EMR por medio de SSH y la interfaz HUE. 

## 1.1. Que aspectos cumplió o desarrolló de la actividad propuesta por el profesor
- Copiar (gestión) de archivos hacia el HDFS vía HUE.
- Copiar (gestión) de archivos hacia el HDFS vía SSH.
- Copiar (gestión) de archivos hacia AWS S3 vía HUE.
- Copiar (gestión) de archivos hacia el AWS S3 vía SSH.

## 1.2. Que aspectos NO cumplió o desarrolló de la actividad propuesta por el profesor
Todo lo propuesto ha sido implementado.

# 2. información general de diseño
Se utilizo AWS para la creacion del cluster en EMR y posteriomente se activa HUE con usuario hadoop.

# 3. Descripción del ambiente de desarrollo y técnico:

## Detalles técnicos
- AWS: servicio para desplegar las instancias.
- HUE: es una interfaz grafica para la gestion de datos.
- S3: es un servicio ofrecido por Amazon Web Services que proporciona almacenamiento de objetos a través de una interfaz de servicio web.
- EMR: es una plataforma de clúster que ayuda a correr frameworks de datos como Hadoop.
- Hadoop: entorno de trabajo para software, bajo licencia libre, para programar aplicaciones distribuidas que manejen grandes volúmenes de datos.

## Descripción y cómo se configura los parámetros del proyecto 
### Crear un cluster en EMR en AWS:
- Acceder a la consola de AWS.
- Dar click en **EMR**.
- Dar click en **Crear Cluster**.
- Dar click en **CREAR**.

### Gestión de archivos hacia el HDFS vía HUE.
Una vez entramos con un usuario ***hadoop*** en HUE
- Dar click en la pestaña de archivos:

![files](https://user-images.githubusercontent.com/60147093/200116037-0e36863a-8fa7-4569-966f-bba005b4c6fb.PNG)

- Crea un directorio donde se almacenaran los datos:

![crear directorio](https://user-images.githubusercontent.com/60147093/200116034-de620092-c7e8-45cf-a35c-1f2f007900db.PNG)
![directorio datasets](https://user-images.githubusercontent.com/60147093/200116035-fea36378-6ccd-4876-a2c7-c306c6c3f3af.PNG)
![directorio onu](https://user-images.githubusercontent.com/60147093/200116036-a2ed996e-52f8-437e-bf41-eef71476303e.PNG)

- Subir los archivos deseados:

![subir archivos hdfs](https://user-images.githubusercontent.com/60147093/200116039-a062353f-d917-441e-9191-fbe248447d21.PNG)

- Ver el contenido:

![ver contenido](https://user-images.githubusercontent.com/60147093/200116040-c2abe61d-58df-4b46-a72f-29efc5a2a619.PNG)



### Gestión de archivos hacia el HDFS vía SSH.
Acceder al cluster por ssh

- Clonar un repositorio con los datasets deseados en local:

![Clonar git con datos](https://user-images.githubusercontent.com/60147093/200116224-0d03b76d-6e1c-4350-a25c-981da6c4bc44.PNG)

- Copiar los archivos hacia el HDFS con usuario hadoop:

![copiar archivos locales](https://user-images.githubusercontent.com/60147093/200116222-8f408d8a-b465-4ac3-971c-c82fc614b5dc.PNG)

- Listar archivos:

![listar archivos](https://user-images.githubusercontent.com/60147093/200116223-bc941883-0c87-43ac-858d-b4b11c917bea.PNG)

Bonus: copiar archivos de hdfs a local:

![hdfs a local](https://user-images.githubusercontent.com/60147093/200116318-eccf5cd1-cfea-4525-b590-ee28b08f14d1.PNG)


### Gestión de archivos hacia AWS S3 vía HUE.
- Damos click en la pestaña de S3 y creamos un bucket nuevo:

![crear bucket](https://user-images.githubusercontent.com/60147093/200116362-8e238a52-9418-4971-bfc4-62447eb17a83.PNG)

- Se crea un directorio donde se van a almacenar los datos:

![directorio onu](https://user-images.githubusercontent.com/60147093/200116036-a2ed996e-52f8-437e-bf41-eef71476303e.PNG)

- Se suben los datos:

![subir archivos hdfs](https://user-images.githubusercontent.com/60147093/200116039-a062353f-d917-441e-9191-fbe248447d21.PNG)

- Finalmente se pueden visualizar los datos tanto en HUE como en AWS S3:

![visualizar contenido](https://user-images.githubusercontent.com/60147093/200116363-b4385e9f-20ba-46ad-a03f-5faf3a284286.PNG)
![s3](https://user-images.githubusercontent.com/60147093/200116501-780b1254-d83d-4e48-912b-1958e3cb7e22.PNG)

### Gestión de archivos hacia el AWS S3 vía SSH.

- Crear un bucket en AWS S3:

![crear bucket](https://user-images.githubusercontent.com/60147093/200116563-2d3c423d-dbe4-4904-b246-365bfccca348.PNG)

- Acceder al cluster por SSH y copiar los archivos almacenados en local deseados:

![archivos de local a s3](https://user-images.githubusercontent.com/60147093/200116559-58305fda-5b80-4efa-ba0c-000a45c96bb2.PNG)

- Visualizar resultados en AWS S3:

![s3 ssh](https://user-images.githubusercontent.com/60147093/200116560-491e62da-43db-4823-8130-654b23890592.PNG)


# 4. Información relevante

## Referencias:
- https://github.com/st0263eafit/st0263-2022-2/blob/main/bigdata/lab5-1-aws-emr.txt
- https://www.youtube.com/watch?v=MyXSwxN5Zdk
- https://www.youtube.com/watch?v=3sao-qJG34Y
