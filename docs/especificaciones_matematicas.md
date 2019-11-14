# Especificaciones matemáticas

## Cálculo de la Expectancia

Se define la expectancia como la probabilidad esperada del jugador A a ganar al jugador B, más la mitad de la probabilidad de quedar en tablas.

Así, si la expectancia es 0.80, puede significar que A tiene un 80% de probabilidad de ganar a B y un 20% de perder, o un 60% de ganar, un 40% de quedar en tablas y un 0% de perder.

Su fórmula matemática es:

![Expectancia](https://wikimedia.org/api/rest_v1/media/math/render/svg/51346e1c65f857c0025647173ae48ddac904adcb)

Donde R_{A} es la puntuación elo del jugador A y R_{B} la del jugador B.


## Cálculo de nueva puntuación elo

Tras jugar una o más partidas un jugador A contra una lista de jugadores B, C, D... Z, se puede definir R'_{A}: 

![Nuevo Elo](https://wikimedia.org/api/rest_v1/media/math/render/svg/09a11111b433582eccbb22c740486264549d1129)

donde S_{A} es la sumatoria de Expectancia del jugador A de cada partido (ver primer apartado) y E_{A} la sumatoria de Resultados (1 resultado por partido), definiéndose cada resultado numéricamente como 0 (perder), 1 (ganar) o 0.5 (tablas).

El factor K está entre 16 (jugadores veteranos) y 40 (jugadores nuevos) y es usado para favorecer cambios de ELO más o menos extremos dependiendo de la situación.





