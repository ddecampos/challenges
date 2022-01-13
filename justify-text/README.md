# Justify Text

Hacer un programa que "justifique" un texto.

## Live Mode 

Puedes hacer uso de este script dandole 'run' en este enlace: https://replit.com/@eldanigeek/justify-text#main.py

## Instructions

### Input

- Un string de una sola linea
- El ancho de la línea esperada

Ninguna palabra del string será más larga que el ancho de línea esperado.

### Output

Mostrar por standard output el texto justificado, de acuerdo a las siguientes reglas:

- Use espacios para separar las palabras
- Cada línea deberá contener la mayor cantidad de palabras posibles
- Usar \n para separar líneas
- El máximo y el mínimo gap de una misma fila no puede diferir en más de 1 espacio
    - Incorrecto: Lorem-----ipsum--dolor
    - Correcto: Lorem----ipsum---dolor
- Las líneas deberán terminar en una palabra, no un espacio
- '\n' no está incluido en el largo de una línea
- Espacios más largos van primero, luego los espacios más pequeños.
    - Correcto: 'Lorem---ipsum---dolor--sit--amet' (3, 3, 2, 2 espacios).
    - Incorrecto: 'Lorem--ipsum--dolor---sit---amet' (2, 2, 3, 3 espacios).
- La última línea no estará justificada, sólo un espacio entre palabras
- Líneas con una sola palabra larga no necesitan espacios ('unapalabralarga\n').

## Ejemplo:

### Input:

```
La historia de la ópera tiene una duración relativamente corta dentro del contexto de la historia de la música en general apareció en 1597, fecha en que se creó la primera ópera.
```

Largo de la línea: 30

### Output:

```
La  historia de la ópera tiene
una   duración   relativamente
corta  dentro  del contexto de
la  historia  de  la música en
general   apareció   en  1597,
fecha   en   que  se  creó  la
primera ópera.
```

<aside>
☝ Notar que todas las líneas, salvo la última, terminan exactamente en la misma columna. Esa es la idea de justificar.

</aside>