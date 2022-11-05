# Información de la materia:
ST0263 - Tópicos Especiales en Telemática

# Estudiante:
Samuel Ceballos Posada. sceballosp@eafit.edu.co

# Profesor:
Edwin Nelson Montoya Munera, [emontoya@eafit.edu.co](mailto:emontoya@eafit.edu.co)

# 1. Breve descripción de la actividad
Crear un Cluster AWS EMR en Amazon con activacion de HUE con usuario hadoop.

## 1.1. Que aspectos cumplió o desarrolló de la actividad propuesta por el profesor
- Desplegar cluster en EMR.
- Activacion de HUE.
- Crear un usuario hadoop.

## 1.2. Que aspectos NO cumplió o desarrolló de la actividad propuesta por el profesor
Todo lo propuesto ha sido implementado.

# 2. información general de diseño
Se utilizo AWS para la creacion del cluster en EMR y posteriomente se activa HUE con usuario hadoop.

# 3. Descripción del ambiente de desarrollo y técnico:

## Detalles técnicos
- AWS: servicio para desplegar las instancias.
- HUE: es una interfaz grafica para la gestion de datos.
- EMR: es una plataforma de clúster que ayuda a correr frameworks de datos como Hadoop.
- Hadoop: entorno de trabajo para software, bajo licencia libre, para programar aplicaciones distribuidas que manejen grandes volúmenes de datos.

## Descripción y cómo se configura los parámetros del proyecto 
### Crear un cluster en EMR en AWS:
- Acceder a la consola de AWS.
- Dar click en **EMR**.
- Dar click en **Crear Cluster**.
- Dar click en **CREAR**.

### Configuracion de Cluster:
- Primero se selcciona la version ***emr-6.3.1*** y se seleccionan las herramientas que se ven en la siguiente foto:
(Se puede indicar la persistencia de un bucker S3 con las siguientes lineas)

![5-1-1](https://user-images.githubusercontent.com/60147093/200109314-5d42d333-65c4-4da9-9634-b5a03f3cf934.PNG)

- Se debe cambiar el tipo de maquina a ***m4.xlarge*** tanto para el master como para los slave y seleccionar la opcion de spot:

![5-1-2](https://user-images.githubusercontent.com/60147093/200109316-77f60155-d8a6-4a48-a5f1-41fd7d61c45a.PNG)

- Activar la auto terminacion del cluster despues de una hora de inactividad: 

![5-1-3](https://user-images.githubusercontent.com/60147093/200109318-d0e9aff4-90f0-43cf-ad9f-546bce60dcd8.PNG)

- Asignarle un nombre al cluster:

![5-1-4](https://user-images.githubusercontent.com/60147093/200109320-783570dc-c3f0-472b-b106-6c847563a07d.PNG)

- Asignarle un par de claves previamente creadas:

![5-1-5](https://user-images.githubusercontent.com/60147093/200109321-5fc9523a-9082-4e56-999e-cbbda18376ea.PNG)

Finalmente dele click a ***crear*** para finalizar la configuracion del cluster. 

### Persistencia:
- Acceder al servicio de S3 en AWS y crear un bucket para usar en el EMR:

![5-1-6](https://user-images.githubusercontent.com/60147093/200109322-33ab85c8-f5ce-4bb3-b79d-d23673f322e0.PNG)

### Conexion via SHH:
- Descargar el par de claves creado anteriormente en formato .pkk y acceder al cluster via SSH:

![5-1-9](https://user-images.githubusercontent.com/60147093/200115300-9b298d8b-f0d0-44ee-9cdc-41a6d073980e.PNG)

### Conexion via HUE:
- Crear un usuario **hadoop** con cualquier clave:

![5-1-7](https://user-images.githubusercontent.com/60147093/200115297-cfc4fe58-7568-4297-b752-b33c3e56e967.PNG)

- Ingresar:

![5-1-8](https://user-images.githubusercontent.com/60147093/200115299-18c92318-9db4-4184-9485-04834fcdeae8.PNG)


# 4. Información relevante

## Referencias:
- https://github.com/st0263eafit/st0263-2022-2/blob/main/bigdata/lab5-1-aws-emr.txt
- https://www.youtube.com/watch?v=MyXSwxN5Zdk
- https://www.youtube.com/watch?v=3sao-qJG34Y
