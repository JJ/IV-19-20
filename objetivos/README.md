`meta`
======

Directorio para objetivos. Inicialmente repositorio de objetivos
cumplidos, pero mas adelante podría ser otra cosa.

## Cómo usarlo

Ya deberías tener un *fork* de éste repositorio en tu cuenta
particular. Al principio del curso, crea un fichero de objetivos. Cada
vez que lo actualices,
[haz un *pull request*](http://aprendegit.com/tag/pull-request/)
para poder incorporarlo aquí. En [este fichero](JJ.md) tienes un
ejemplo de cómo tienes que formatear los objetivos, que puedes
copiar/pegar de la página correspondiente.

Recuerda que tienes que mantener tu copia actualizada con el
repositorio original. Para ello, define un repositorio *upstream* de
esta forma

	git remote add upstream https://github.com/JJ/IV-19-20.git

(Si no es el curso 18-19, sustituir arriba por el año que quieras).

y antes de ponerte a trabajar con tu *fork* local del repositorio
recuerda hacer

	git pull upstream master --rebase

## Qué hacer si ya hemos modificado el fichero del hito

git hace relativamente fácil el crear ramas desde cualquier punto de
la historia. Supongamos que el fichero de los objetivos lo hemos
modificado en un commit que está el tercero en la lista (si hacemos
`git log`). Podemos hacer entonces 

    git checkout HEAD~2

Esto creará un estado llamado *detached HEAD*, que básicamente implica
que es de "sólo lectura". Pero puedes crear, a partir de ahí, como te
indica en el mensaje, una rama

    git checkout -b solo-objetivos
    
Esto te creará una nueva rama, en la cual HEAD (el último commit) será
el que has, efectivamente, elegido. Esa rama puedes modificarla si
quieres, pero si lo que quieres es hacer un PR sólo con ese cambio, 

    git push -u origin solo-objetivos
    
Eso creará una nueva rama llamada solo-objetivos en tu repo de
origen. 

Ahora, tendrás que hacer el pull request desde esa rama. Simplemente,
selecciona la rama del menú *pull-down* que indica *Branch* y hazlo
tal como lo harías si se tratara de la rama *master* del repo.

Una vez hecho esto

   git checkout master
   
volverá tu repo al estado original. Simplemente tienes que esperar a
que te acepten el PR, para hacer el nuevo PR con el hito.

Una vez aceptado el PR, puedes borrar la rama local y en GitHub
tranquilamente. 
