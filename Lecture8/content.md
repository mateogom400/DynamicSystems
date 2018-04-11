# Sistemas Dinámicos - Modelos de Sistemas Hidráulicos

> Gerardo de J. Becerra B.  
> Facultad de Ingeniería, Pontificia Universidad Javeriana.  
> Bogotá, Colombia.

## Introducción
Un sistema hidráulico se caracteriza por el flujo de liquidos, los cuales en general pueden considerarse incompresibles. Dichos sistemas aparecen comúnmente en procesos quimicos, equipos de manufactura y equipos de construcción/agricultura. Usualmente se interconectan usando bombas, válvulas, y pistones.

Comparado con otras tecnologías existentes (mecánica, eléctrica, neumática) para generar fuerzas y movimiento, algunas de las **ventajas** de los sistemas hidráulicos son:
- Transmisión de grandes fuerzas usando componentes pequeños.
- Precisión en el posicionamiento.
- Arranque bajo alta carga.
- Movimiento contínuo independiente de la carga (debido a la incompresibilidad del líquido).
- Buen control y regulación.
- Disipación de calor favorable.

Algunas de las **desventajas** de los sistemas hidráulicos frente a otras tecnologías:
- Contaminación ambiental por residuos de aceite.
- Susceptible al polvo.
- Peligros resultantes de presiones excesivas.
- Dependiencia de la temperatura (cambio de la viscosidad).

Un análisis exacto de sistemas hidráulicos require considerar su naturaleza distrubuída y las propiedades no lineales del flujo. En nuestro caso únicamente consideraremos elementos concentrados y utilizaremos linealización para simplificar el análisis.

## Variables
Las variables usadas para describir el comportamiento dinámico de los sistemas hidráulicos son:

| Símbolo   | Variable          | Unidades |
|:---------:|:-----------------:|:--------:|
| *w*       | Flujo volumétrico | m^3/s    |
| *v*       | Volumen           | m^3      |
| *h*       | Altura líquido    | m        |
| *p*       | Presión           | N/m^2    |

La presión puede expresarse de diferentes formas:
![Presion](http://www.calscan.net/images/AN-004%20Graphic.png)
La relación entre las diferentes presiones se puede escribir como
$$p^*(t) = p(t) - p_a$$
donde 