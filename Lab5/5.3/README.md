# Información de la materia:

ST0263 - Tópicos Especiales en Telemática

# Estudiante:

Samuel Ceballos Posada. sceballosp@eafit.edu.co

# Profesor:

Edwin Nelson Montoya Munera, [emontoya@eafit.edu.co](mailto:emontoya@eafit.edu.co)

# 1. Breve descripción de la actividad

Hacer los ejercicios popuestos de MapReduce con MRJOB en Python.

## 1.1. Que aspectos cumplió o desarrolló de la actividad propuesta por el profesor

- Desplegar cluster en EMR.
- Activacion de HUE.
- Crear un usuario hadoop.

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

2. El salario promedio por Empleado

```
python P1/punto2.py datasets/dataempleados.txt
```

3. Número de SE por Empleado que ha tenido a lo largo de la estadística

```
python P1/punto3.py datasets/dataempleados.txt
```

### Parte 2:

1. Por acción, dia-menor-valor, día-mayor-valor.

```
python P2/punto1.py datasets/dataempresas.txt
```

2. Listado de acciones que siempre han subido o se mantienen estables.

```
python P2/punto2.py datasets/dataempresas.txt
```

3. DIA NEGRO: Saque el día en el que la mayor cantidad de acciones tienen el menor valor de acción (DESPLOME), suponga una inflación independiente del tiempo.

```
python P2/punto3.py datasets/dataempresas.txt
```

### Parte 3:

1. Número de películas vista por un usuario, valor promedio de calificación.

```
python P3/punto1.py datasets/datapeliculas.txt
```

2. Día en que más películas se han visto.

```
python P3/punto2.py datasets/datapeliculas.txt
```

3. Día en que menos películas se han visto.

```
python P3/punto3.py datasets/datapeliculas.txt
```

4. Número de usuarios que ven una misma película y el rating promedio.

```
python P3/punto4.py datasets/datapeliculas.txt
```

5. Día en que peor evaluación en promedio han dado los usuarios.

```
python P3/punto5.py datasets/datapeliculas.txt
```

6. Día en que mejor evaluación han dado los usuarios.

```
python P3/punto6.py datasets/datapeliculas.txt
```

7. La mejor y peor película evaluada por genero.

```
python P3/punto7.py datasets/datapeliculas.txt
```

# 4. Información relevante

## Referencias:

- https://github.com/st0263eafit/st0263-2022-2/blob/main/bigdata/lab5-3-mrjob.txt
