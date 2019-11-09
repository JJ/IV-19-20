# Especificaciones matemáticas

## Cálculo de la Expectancia

Se define la expectancia como la probabilidad esperada del jugador A a ganar al jugador B, más la mitad de la probabilidad de quedar en tablas.

Así, si la expectancia es 0.80, puede significar que A tiene un 80% de probabilidad de ganar a B y un 20% de perder, o un 60% de ganar, un 40% de quedar en tablas y un 0% de perder.

Su fórmula matemática es:

$$E_{A} = {1\over {1+10^{(Rb-Ra)/400}}.$$

Donde $$R_{A}.$$ es la puntuación elo del jugador A y $$R_{B}.$$ la del jugador B.


## Cálculo de nueva puntuación elo

Tras jugar una o más partidas un jugador A contra una lista de jugadores B, C, D... Z, se puede definir $$R'_{A}.$$: 

$$R'_{A} = {R_{A} + K(S_{A} - E_{A})}.$$

donde $$S_{A}.$$ es la sumatoria de Expectancia del jugador A de cada partido (ver primer apartado) y $$E_{A}.$$ la sumatoria de Resultados (1 resultado por partido), definiéndose cada resultado numéricamente como 0 (perder), 1 (ganar) o 0.5 (tablas).

El factor K está entre 16 (jugadores veteranos) y 40 (jugadores nuevos) y es usado para favorecer cambios de ELO más o menos extremos dependiendo de la situación.





