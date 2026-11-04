# Cambios del lanzamiento de WoW Forever (4-11-2026)

Lo que hay que llevar al proyecto local para que la próxima generación de la guía no pierda el parche que se subió a la web el 4-11-2026.

## Qué se cambió en la web publicada

El `index.html` se parcheó a mano (solo datos, más una frase de la interfaz) con `notas/parche_lanzamiento_2026-11-04.py`. **Al regenerar la guía se pierde todo**, así que hay que pasarlo a las fuentes:

| Bloque del `index.html` | Qué se cambió | Dónde va en el proyecto local |
| --- | --- | --- |
| `window.ACTUALIZACION.pendientes` | 35 avisos «Necesita revisión»: 3 generales y 32 de builds de clase (21 builds inválidas y 11 con valores cambiados) | El fichero del contrato C8 (el que escribe la actualización automática) |
| `window.RAZAS` | Raciales finales (Iracundia 15 s, Toque de la tumba 15 s, Planicies 2 %/60 %, Aguante +5 % de vida, Bendición del viento 2 %, Skysight 15 %) y textos de `porClase` que citaban el +1 % de golpe del tauren o el +1 % de celeridad | `app/datos/razas.js` (contrato C17) |
| `window.NOVEDADES` | 15 entradas nuevas «confirmado», 2 entradas de razas corregidas y el mensaje n.º 9 de las notas de la beta | Se genera con `tools/novedades.py`: hay que añadir las notas del 3-11 a su fuente y regenerar |
| Lógica de la app (`Act.pendientesClase`) | El aviso de clase decía «La actualización automática ha visto cambios en el cliente»; ahora dice «Hay cambios en el cliente o en las notas de Blizzard» | Código de la app |

## Cómo seguir en el PC

1. Pasar los cambios de razas a `app/datos/razas.js` y revisar el orden de razas por clase (el tauren pierde el golpe, el orco recupera Mando para cazador y brujo, el no-muerto mejora con Toque de la tumba a 15 s).
2. Con el cliente de lanzamiento, regenerar talentos (`tools/talentos.py`) y rehacer las 21 builds inválidas de abajo; repasar las 11 que solo cambian valores.
3. Rehacer los tramos de nivelado de guerrero, paladín, pícaro, mago y druida.
4. Añadir las notas del 3-11 a la fuente de `tools/novedades.py` y regenerar.
5. Regenerar la guía y quitar los pendientes que ya estén resueltos.

Blizzard dice que no habrá grandes ajustes de equilibrio hasta que abran las bandas (el mes que viene), salvo errores y casos extremos, así que las builds que se rehagan ahora deberían aguantar hasta entonces.

## Cambios generales

- **Novedades**: Notas finales del 3-11: más daño en todas las clases y más vida en los enemigos de nivel alto para compensar. Blizzard no hará grandes ajustes hasta que abran las bandas (el mes que viene), salvo errores y casos extremos.
- **Razas**: Raciales finales: Iracundia dura 15 s, Toque de la tumba tiene 15 s de reutilización interna, Aguante del tauren se queda en +5 % de vida y el orco pierde Savage y recupera Mando (+5 % de daño de mascota). Las fichas ya traen estos valores; el orden de razas por clase está sin revisar.
- **Nivelado**: Entrenar las facultades de clase del 1 al 60 cuesta 206-207 de oro en todas las clases (al brujo se le descuenta lo que esperan que gaste en grimorios). Los hechizos nuevos ya no se ponen solos en las barras, las bolsas nuevas no se equipan solas y los enemigos reaparecen más rápido en las zonas iniciales.
Otros cambios generales de las notas del 3-11:

- Los talentos ya no pierden probabilidad de activarse al usar rangos bajos, salvo Concentración arcana, Mordedura de Escarcha y Dedos de Escarcha del mago con rangos aprendidos más de 12 niveles por debajo.
- Las raíces de talentos (Mordedura de Escarcha, Atrapar, Corte de ala mejorado, Contraataque, Seccionar mejorado) tienen rendimientos decrecientes.
- Estadísticas base corregidas en todas las razas (p. ej., el guerrero tauren tiene +5 de fuerza sobre el humano, antes +2).
- Lanzamiento: 4-11-2026 a las 23:00 UTC (00:00 en España).

## Builds por clase

### Guerrero

- **Armas** (**build inválida**): Maestría táctica mejorada baja de 5 a 3 puntos (retiene 5/10/15 de ira) y Fragor de la sangre de 5 a 2 (10/20 %): sobran 5 puntos. Especialización en armas de dos manos sube a 2/4/6 %, Embate mejorado quita 2,5/5 s y Embate pasa a 15 s de reutilización.
- **Furia** (**build inválida**): Aluvión baja de 5 a 3 puntos (10/20/30 % de velocidad) y ya no pide Deseo de la Muerte; ahora es Sed de sangre la que lo pide. Maestría táctica mejorada baja a 3. Enfurecer sube a la fila 3 y hay dos talentos nuevos: Reckless Swings (fila 4) e Improved Whirlwind (fila 6, 2 puntos).
- **Protección** (la build vale, cambian valores): Actitud defensiva da un 80 % más de amenaza (antes 30 %) y Desafío 7/13/20 % (antes 5/10/15 %). La build vale, pero la amenaza deja de ser el problema: puede compensar mover puntos de amenaza a aguante o daño.
- **Nivelado** (**build inválida**): Los tramos suben Maestría táctica mejorada y Fragor de la sangre a 5 puntos; ahora llegan a 3 y a 2.

### Paladín

- **Sagrado** (**build inválida**): Desaparece Voz de la verdad; Enfoque espiritual pasa a la fila 1 con 5 puntos, Reverencia se queda en 2 e Intelecto divino se va a Protección. Poder Sagrado sube ahora la sanación de los críticos (10-50 %) en vez de su probabilidad, y Vigilia de la Luz solo sirve sobre aliados. Nuevos: Oath of Light (fila 4) y Boundless Light (fila 5).
- **Protección** (**build inválida**): Desaparecen Especialización en armas de una mano y Sello de furia mejorado; Sellos mejorados pasa a 5 puntos, Credo férreo a 3 y Especialización en escudos a 2. Cambian de fila Baluarte de templario (3), Escudo Sagrado (5), Dureza (3) y Anticipación (4); nuevos: Stoicism (fila 5) y Shieldsworn (fila 7). Furia justa se aprende a nivel 10 (+33 % de amenaza y +90 % con daño sagrado) y desaparece Salvación.
- **Reprensión** (**build inválida**): Desaparecen Giro de la Luz e Instrumento de la ley; Convicción pasa a 3 puntos (2/4/6 % de crítico con todo), Conducto Sagrado se va a Sagrado y Fe implacable llega a Reprensión. Venganza acumula hasta 5 y ahora pide Sello de orden; Reivindicación ya no da poder de ataque. Nuevo talento de 31 puntos: Unsealed Wrath (pide Repentance).
- **Nivelado** (**build inválida**): Los tramos llevan Giro de la Luz e Instrumento de la ley (desaparecen), Convicción a 5 (ahora máximo 3), Sellos mejorados a 3 (ahora 5 puntos) y Conducto Sagrado e Intelecto divino, que cambian de árbol.

### Cazador

- **Dominio de bestias** (la build vale, cambian valores): Ningún talento roto (Encontrar camino baja a la fila 3), pero cambian las prioridades: Disparo Arcano +30 % (coeficiente 0,15), Picadura de serpiente +20 % (5 % de poder de ataque por tic), Disparo apuntado +110 % y Aspecto del halcón 20/35/50/70/90/110. Todas las trampas comparten 30 s.
- **Puntería** (la build vale, cambian valores): Aluvión 5/10/15 % (antes 3/7/10 %), Disparo de francotirador +100 % y Aura de disparo certero 20/35/50/75/100 de poder de ataque a distancia; Disparo apuntado +110 %. La build vale.
- **Supervivencia** (la build vale, cambian valores): Reflejos de relámpago pasa a 3/6/9/12/15 % de agilidad y Golpes lacerantes siempre sobrescribe el tuyo. Todas las trampas comparten 30 s de reutilización. La build vale.

### Pícaro

- **Asesinato** (**build inválida**): Desaparece Asesinar; Letalidad pasa a 2 puntos (10/20 % de daño crítico), Sello del destino a 3, Golpes despiadados a 5 puntos en la fila 5 y Oportunidad (Sutileza) a 5. Veneno baja a la fila 5 y pasa a depender de Shank; Vigor sube a la fila 3 y Mutilar a la 7 (90 % de daño de arma). Nuevo: Blood Splatter (fila 3). Eviscerar mejorado se llama ahora Coup de Grace.
- **Combate** (**build inválida**): Desaparece Asesinar; Letalidad pasa a 2 puntos, Golpes despiadados a 5 y Especialización en doble empuñadura a 2 (25/50 %). Agresión pasa a 5/10/15 % a Golpe siniestro y Eviscerar, Experiencia con armas sube a la fila 4, Ejecución impecable quita 15 de energía y Golpe siniestro mejorado (ahora Efficient Strikes) abarata también Hemorragia. Nuevos: Composure (fila 3) y Flash of Steel (fila 6).
- **Sutileza** (**build inválida**): Desaparecen Asesinar, Quietus, Mil cortes y Distraer mejorado; Letalidad pasa a 2 puntos, Camuflaje a 3 y Oportunidad a 5, y varios talentos cambian de fila. Nuevos: Quick Getaway (fila 4), Boot Knife (fila 6) y Death Mark como talento de 31 puntos.
- **Nivelado** (**build inválida**): Los tramos usan Asesinar (desaparece), Letalidad y Especialización en doble empuñadura (bajan a 2 puntos) y Golpes despiadados (pasa a 5). Para subir hay facultades nuevas: Poised (nivel 18) y Shank (nivel 24).

### Sacerdote

- **Sagrado** (**build inválida**): Desaparece Sanación conjunta; en su hueco entra Holy Binding: cuando curas a otro con Sanación relámpago recibes tú el 50 % de esa curación, sin generar amenaza.
- **Sombra** (la build vale, cambian valores): Unirse a vampírica ya no hace críticos y Palabra de las Sombras: Muerte, si no mata, te quita el 30 % de la vida máxima (antes 10 %). La build vale.

### Chamán

- **Elemental** (**build inválida**): Desaparece Ráfaga de lava (la sustituye Llamada del trueno: +5 % de crítico a Descarga de relámpagos y Cadena de relámpagos); Sobrecarga de relámpagos pasa a 10/20/30 % y Elemental Mastery se llama Lightning Mastery. Descarga de relámpagos +80 % en el rango máximo, Cadena de relámpagos 2,5 s de lanzamiento y los choques vuelven a los valores de Classic, más altos.
- **Mejora** (la build vale, cambian valores): Golpe de tormenta hace 150 % de daño de arma con 6 s de reutilización (antes 100 % y 8 s), Arma vorágine salta el doble, Maña mental da 50/100/150 % del intelecto y Aluvión 6-30 %. La build vale y sale bastante mejor.
- **Recuperación** (la build vale, cambian valores): Mareas vivas ya no cura al instante: solo cura en el tiempo, cuesta un 40 % menos de maná y tiene 12 s de reutilización (antes 6 s).

### Mago

- **Arcano** (**build inválida**): Desaparece Enfoque Arcano (se funde en Precisión, de Escarcha). Tromba de misiles baja a la fila 2 y se consume al empezar a canalizar; Recuperación Arcana sube a la fila 1 con hasta 3 puntos. Explosión Arcana: +100 % de coste por carga (antes 175 %), +12 % de daño por carga (antes 15 %) y 18 s. En Fuego, Bola de Fuego mejorada se llama Accelerant e Incineración llega a 5 puntos.
- **Fuego** (**build inválida**): Enfoque elemental (ahora Precisión) vuelve a 3 puntos (2/4/6 % de golpe) y desaparece Enfoque Arcano: sobran puntos. Incineración llega a 5 puntos (10 % de crítico), Masa crítica se queda en 3 (6 %), Explosión de Fuego mejorada baja a la fila 3 y Bola de Fuego mejorada se llama Accelerant. Ignición ya se aplica a todo el daño de Fogonazo.
- **Escarcha** (**build inválida**): Desaparecen Hielo penetrante, Explosión de Escarcha y Enfoque Arcano, y Enfoque elemental (ahora Precisión) vuelve a 3 puntos. Lanza de hielo: 8 s de reutilización compartida con Explosión de Fuego y vuelve al 300 % contra congelados. Barrera de hielo da +15 % de daño de Escarcha 1 min (+5 % mientras aguanta), Escalofrío del invierno sube un 20 % por carga el daño de Cono de frío y Custodia de Escarcha ya no refleja: anula el hechizo.
- **Nivelado** (**build inválida**): Los tramos llevan Hielo penetrante y Enfoque Arcano (desaparecen) y Enfoque elemental a 5 (ahora máximo 3).

### Brujo

- **Aflicción** (la build vale, cambian valores): Arruinar duplica su coeficiente y a nivel 60 pasa de 36 a 86 de daño por segundo base; Drenajes mejorados ya no lo potencia y Amplificar maldición afecta ahora a Maldición de agotamiento y Bane of Agony. Las mascotas ganan 2 de vida por punto de aguante tuyo (antes 7,5).
- **Demonología** (la build vale, cambian valores): Las mascotas ganan solo 2 de vida por punto de aguante del brujo (antes 7,5): aguantan mucho menos. Las piedras de hechizo ya solo suben el daño de Sombras.
- **Destrucción** (la build vale, cambian valores): Sombras y llamas pasa a 4/8/12/16/20 % (antes 2-10 %) y las piedras de hechizo ya solo suben el daño de Sombras. La build vale y sale mejor.

### Druida

- **Equilibrio** (la build vale, cambian valores): Génesis 2/4/6/8/10 % (antes 1-5 %), Fuego estelar +40 % de daño base y Naturalista (Restauración) da 2-10 % a todo el daño. El aura de crítico de Forma de lechúcico lunar vuelve a valer para todo, pero no se suma con Líder de la manada.
- **Combate feral (oso)** (**build inválida**): Desaparece Rabia (Berserk); Corazón de lo Salvaje se va a Restauración y Furor viene a Feral. Laceración pasa a ser un talento de 1 punto en la fila 4 y hay nuevos: Predatory Discipline, Primal Bite (31 puntos, oso) y Shifting Power (31 puntos, gato). Desgarrar y rasgar 3-15 %. La forma de oso da un 115 % más de amenaza (antes 50 %) porque desaparece Bendición de salvación.
- **Combate feral (gato)** (**build inválida**): Igual que el oso: sin Rabia, Corazón de lo Salvaje en Restauración y Furor en Feral. A cambio, Triturar hace 200 % de daño de arma (antes 155 %), Garra 140 %, Devastar 435 % y Destripar, Arañazo, Mordedura feroz y Abalanzarse un 25 % más. Nuevo pasivo Poised (nivel 32).
- **Recuperación** (**build inválida**): Desaparece Don de la Madre Tierra; Furor se va a Feral y llega Corazón de lo Salvaje. Naturalista da 2-10 % a todo el daño y acorta Crecimiento salvaje (3 s de base), y hay un talento nuevo, Bloom. Arreglo rápido solo consume tu propio Rejuvenecimiento o Recrecimiento.
- **Nivelado** (**build inválida**): Los tramos llevan Rabia (desaparece) y Corazón de lo Salvaje y Furor, que cambian de árbol.
## Fuentes

- [WoW Forever Beta Development Notes, actualizadas el 3-11-2026 (Blizzard)](https://eu.forums.blizzard.com/en/wow/t/wow-forever-beta-development-notes-%E2%80%93-updated-3-november/631316/9)
- [Raciales finales, 26 y 27-10-2026 (Blizzard)](https://eu.forums.blizzard.com/en/wow/t/wow-forever-beta-development-notes-%E2%80%93-updated-3-november/631316/7)
- [Resumen y registro de hotfixes (timesaver.gg)](https://timesaver.gg/blog/wow-forever-launch-patch-notes): los valores del cazador del 3-11 también salen en los datos del cliente, sin confirmar hasta el lanzamiento.
