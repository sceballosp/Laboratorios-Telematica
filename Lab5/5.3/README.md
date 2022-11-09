# Información de la materia:

ST0263 - Tópicos Especiales en Telemática

# Estudiante:

Samuel Ceballos Posada. sceballosp@eafit.edu.co

# Profesor:

Edwin Nelson Montoya Munera, [emontoya@eafit.edu.co](mailto:emontoya@eafit.edu.co)

# 1. Breve descripción de la actividad

Hacer los ejercicios popuestos de MapReduce con MRJOB en Python.

## 1.1. Que aspectos cumplió o desarrolló de la actividad propuesta por el profesor

- Los ejercicios popuestos

## 1.2. Que aspectos NO cumplió o desarrolló de la actividad propuesta por el profesor

Todo lo propuesto ha sido implementado.

# 2. información general de diseño

Se usó la libreria de MRJOB en Python.

# 3. Descripción del ambiente de desarrollo y técnico:

## Detalles técnicos

- MRJOB: se usó esta librería para el uso de MapReduce en Pyhton.
- Python: se usó python como lenguaje de programación para la solución.

## Descripción y cómo se configura los parámetros del proyecto

### Configuracion inicial:

- Clonar repositorio:
```
https://github.com/sceballosp/Laboratorios-Telematica.git
```

- Acceder al directorio Lab5/5.3:
```
cd Laboratorios-Telematica/Lab5/5.3
```

- Instalar MRJOB:
```
pip install mrjob
```

### Parte 1:

1. El salario promedio por Sector Económico (SE)
```
python P1/punto1.py datasets/dataempleados.txt
```

![1 1](https://user-images.githubusercontent.com/60147093/200918766-3facadea-7ad3-43bc-a529-adf3819295d5.PNG)

2. El salario promedio por Empleado
```
python P1/punto2.py datasets/dataempleados.txt
```

![1 2](https://user-images.githubusercontent.com/60147093/200918769-db5a75eb-d20d-486b-b7c9-602a2b6b196c.PNG)

3. Número de SE por Empleado que ha tenido a lo largo de la estadística
```
python P1/punto3.py datasets/dataempleados.txt
```

![1 3](https://user-images.githubusercontent.com/60147093/200918772-5208266e-f6a5-4cf1-85e3-cf6ab88df7ce.PNG)

### Parte 2:

1. Por acción, dia-menor-valor, día-mayor-valor.
```
python P2/punto1.py datasets/dataempresas.txt
```

![2 1](https://user-images.githubusercontent.com/60147093/200918773-84bf89f2-270b-4ff7-a45d-aa401e8d5ebc.PNG)

2. Listado de acciones que siempre han subido o se mantienen estables.
```
python P2/punto2.py datasets/dataempresas.txt
```

![2 2](https://user-images.githubusercontent.com/60147093/200918775-1357b7bb-7cc7-4e2d-9c80-15bf52a0c9ac.PNG)

3. DIA NEGRO: Saque el día en el que la mayor cantidad de acciones tienen el menor valor de acción (DESPLOME), suponga una inflación independiente del tiempo.
```
python P2/punto3.py datasets/dataempresas.txt
```

![2 3](https://user-images.githubusercontent.com/60147093/200918776-97398ca5-0156-4799-8466-dc3fed018c20.PNG)

### Parte 3:

1. Número de películas vista por un usuario, valor promedio de calificación.
```
python P3/punto1.py datasets/datapeliculas.txt
```

![3 1](https://user-images.githubusercontent.com/60147093/200918780-3f3a515f-d1b7-4bdb-91d2-2ae442793c64.PNG)

2. Día en que más películas se han visto.
```
python P3/punto2.py datasets/datapeliculas.txt
```

![3 2](https://user-images.githubusercontent.com/60147093/200918781-1ba0e335-25dc-485e-855d-9f11dd04eb23.PNG)

3. Día en que menos películas se han visto.
```
python P3/punto3.py datasets/datapeliculas.txt
```

![3 3](https://user-images.githubusercontent.com/60147093/200918785-e685f122-be6b-477f-b3df-d409833b5f51.PNG)

4. Número de usuarios que ven una misma película y el rating promedio.
```
python P3/punto4.py datasets/datapeliculas.txt
```

![3 4](https://user-images.githubusercontent.com/60147093/200918788-10589df7-6870-4779-a61f-b93a5ff5c5d3.PNG)

5. Día en que peor evaluación en promedio han dado los usuarios.
```
python P3/punto5.py datasets/datapeliculas.txt
```

![3 5](https://user-images.githubusercontent.com/60147093/200918790-8c818be9-ed84-4d2b-8e4a-e766273a525c.PNG)

6. Día en que mejor evaluación han dado los usuarios.
```
python P3/punto6.py datasets/datapeliculas.txt
```

![3 6](https://user-images.githubusercontent.com/60147093/200918792-28e193dc-31ac-4dfe-96cc-013afbc976b9.PNG)

7. La mejor y peor película evaluada por genero.
```
python P3/punto7.py datasets/datapeliculas.txt
```

![3 7](https://user-images.githubusercontent.com/60147093/200918793-178a1209-59cf-42df-9291-79f49f4e5bba.PNG)

# 4. Información relevante

## Referencias:

- https://github.com/st0263eafit/st0263-2022-2/blob/main/bigdata/lab5-3-mrjob.txt
