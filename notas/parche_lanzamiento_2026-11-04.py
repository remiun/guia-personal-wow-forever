"""Parche de lanzamiento (04-11-2026) sobre el index.html generado.

Toca solo datos: window.ACTUALIZACION.pendientes, window.RAZAS y window.NOVEDADES.
La lógica de la app no se modifica.
"""
import json
import sys

RUTA = sys.argv[1]
s = open(RUTA, encoding='utf-8').read()

NOTAS = {
    "titulo": "WoW Forever Beta Development Notes, actualizadas el 3-11-2026 (Blizzard, notas finales antes del lanzamiento)",
    "url": "https://eu.forums.blizzard.com/en/wow/t/wow-forever-beta-development-notes-%E2%80%93-updated-3-november/631316/9",
    "fecha": "2026-11-03",
}
RACIALES = {
    "titulo": "WoW Forever Beta Development Notes: raciales y rasgos finales (Blizzard, 26 y 27-10-2026)",
    "url": "https://eu.forums.blizzard.com/en/wow/t/wow-forever-beta-development-notes-%E2%80%93-updated-3-november/631316/7",
    "fecha": "2026-10-26",
}
D = "2026-11-03"
H = "notas-2026-11-03"  # huella: la build vale, pero cambian valores

# ---------------------------------------------------------------- pendientes
def pc(clase, build, motivo, huella=False, desde=D):
    p = {"profesion": None, "clase": clase, "build": build, "motivo": motivo, "desde": desde}
    if huella:
        p["huella"] = H
    return p

PENDIENTES = [
    # Generales (portada)
    {"profesion": None, "clase": None, "build": "novedades", "desde": D,
     "motivo": "Notas finales del 3-11: más daño en todas las clases y más vida en los enemigos de nivel alto para compensar. Blizzard no hará grandes ajustes hasta que abran las bandas (el mes que viene), salvo errores y casos extremos."},
    {"profesion": None, "clase": None, "build": "razas", "desde": "2026-10-27",
     "motivo": "Raciales finales: Iracundia dura 15 s, Toque de la tumba tiene 15 s de reutilización interna, Aguante del tauren se queda en +5 % de vida y el orco pierde Savage y recupera Mando (+5 % de daño de mascota). Las fichas ya traen estos valores; el orden de razas por clase está sin revisar."},
    {"profesion": None, "clase": None, "build": "nivelado", "desde": D,
     "motivo": "Entrenar las facultades de clase del 1 al 60 cuesta 206-207 de oro en todas las clases (al brujo se le descuenta lo que esperan que gaste en grimorios). Los hechizos nuevos ya no se ponen solos en las barras, las bolsas nuevas no se equipan solas y los enemigos reaparecen más rápido en las zonas iniciales."},

    # Guerrero
    pc("guerrero", "arbol 161", "Maestría táctica mejorada baja de 5 a 3 puntos (retiene 5/10/15 de ira) y Fragor de la sangre de 5 a 2 (10/20 %): sobran 5 puntos. Especialización en armas de dos manos sube a 2/4/6 %, Embate mejorado quita 2,5/5 s y Embate pasa a 15 s de reutilización."),
    pc("guerrero", "arbol 164", "Aluvión baja de 5 a 3 puntos (10/20/30 % de velocidad) y ya no pide Deseo de la Muerte; ahora es Sed de sangre la que lo pide. Maestría táctica mejorada baja a 3. Enfurecer sube a la fila 3 y hay dos talentos nuevos: Reckless Swings (fila 4) e Improved Whirlwind (fila 6, 2 puntos)."),
    pc("guerrero", "arbol 163", "Actitud defensiva da un 80 % más de amenaza (antes 30 %) y Desafío 7/13/20 % (antes 5/10/15 %). La build vale, pero la amenaza deja de ser el problema: puede compensar mover puntos de amenaza a aguante o daño.", huella=True),
    pc("guerrero", "nivelado", "Los tramos suben Maestría táctica mejorada y Fragor de la sangre a 5 puntos; ahora llegan a 3 y a 2."),

    # Paladín
    pc("paladin", "arbol 382", "Desaparece Voz de la verdad; Enfoque espiritual pasa a la fila 1 con 5 puntos, Reverencia se queda en 2 e Intelecto divino se va a Protección. Poder Sagrado sube ahora la sanación de los críticos (10-50 %) en vez de su probabilidad, y Vigilia de la Luz solo sirve sobre aliados. Nuevos: Oath of Light (fila 4) y Boundless Light (fila 5)."),
    pc("paladin", "arbol 383", "Desaparecen Especialización en armas de una mano y Sello de furia mejorado; Sellos mejorados pasa a 5 puntos, Credo férreo a 3 y Especialización en escudos a 2. Cambian de fila Baluarte de templario (3), Escudo Sagrado (5), Dureza (3) y Anticipación (4); nuevos: Stoicism (fila 5) y Shieldsworn (fila 7). Furia justa se aprende a nivel 10 (+33 % de amenaza y +90 % con daño sagrado) y desaparece Salvación."),
    pc("paladin", "arbol 381", "Desaparecen Giro de la Luz e Instrumento de la ley; Convicción pasa a 3 puntos (2/4/6 % de crítico con todo), Conducto Sagrado se va a Sagrado y Fe implacable llega a Reprensión. Venganza acumula hasta 5 y ahora pide Sello de orden; Reivindicación ya no da poder de ataque. Nuevo talento de 31 puntos: Unsealed Wrath (pide Repentance)."),
    pc("paladin", "nivelado", "Los tramos llevan Giro de la Luz e Instrumento de la ley (desaparecen), Convicción a 5 (ahora máximo 3), Sellos mejorados a 3 (ahora 5 puntos) y Conducto Sagrado e Intelecto divino, que cambian de árbol."),

    # Cazador
    pc("cazador", "arbol 361", "Ningún talento roto (Encontrar camino baja a la fila 3), pero cambian las prioridades: Disparo Arcano +30 % (coeficiente 0,15), Picadura de serpiente +20 % (5 % de poder de ataque por tic), Disparo apuntado +110 % y Aspecto del halcón 20/35/50/70/90/110. Todas las trampas comparten 30 s.", huella=True),
    pc("cazador", "arbol 363", "Aluvión 5/10/15 % (antes 3/7/10 %), Disparo de francotirador +100 % y Aura de disparo certero 20/35/50/75/100 de poder de ataque a distancia; Disparo apuntado +110 %. La build vale.", huella=True),
    pc("cazador", "arbol 362", "Reflejos de relámpago pasa a 3/6/9/12/15 % de agilidad y Golpes lacerantes siempre sobrescribe el tuyo. Todas las trampas comparten 30 s de reutilización. La build vale.", huella=True),

    # Pícaro
    pc("picaro", "arbol 182", "Desaparece Asesinar; Letalidad pasa a 2 puntos (10/20 % de daño crítico), Sello del destino a 3, Golpes despiadados a 5 puntos en la fila 5 y Oportunidad (Sutileza) a 5. Veneno baja a la fila 5 y pasa a depender de Shank; Vigor sube a la fila 3 y Mutilar a la 7 (90 % de daño de arma). Nuevo: Blood Splatter (fila 3). Eviscerar mejorado se llama ahora Coup de Grace."),
    pc("picaro", "arbol 181", "Desaparece Asesinar; Letalidad pasa a 2 puntos, Golpes despiadados a 5 y Especialización en doble empuñadura a 2 (25/50 %). Agresión pasa a 5/10/15 % a Golpe siniestro y Eviscerar, Experiencia con armas sube a la fila 4, Ejecución impecable quita 15 de energía y Golpe siniestro mejorado (ahora Efficient Strikes) abarata también Hemorragia. Nuevos: Composure (fila 3) y Flash of Steel (fila 6)."),
    pc("picaro", "arbol 183", "Desaparecen Asesinar, Quietus, Mil cortes y Distraer mejorado; Letalidad pasa a 2 puntos, Camuflaje a 3 y Oportunidad a 5, y varios talentos cambian de fila. Nuevos: Quick Getaway (fila 4), Boot Knife (fila 6) y Death Mark como talento de 31 puntos."),
    pc("picaro", "nivelado", "Los tramos usan Asesinar (desaparece), Letalidad y Especialización en doble empuñadura (bajan a 2 puntos) y Golpes despiadados (pasa a 5). Para subir hay facultades nuevas: Poised (nivel 18) y Shank (nivel 24)."),

    # Sacerdote
    pc("sacerdote", "arbol 202", "Desaparece Sanación conjunta; en su hueco entra Holy Binding: cuando curas a otro con Sanación relámpago recibes tú el 50 % de esa curación, sin generar amenaza."),
    pc("sacerdote", "arbol 203", "Unirse a vampírica ya no hace críticos y Palabra de las Sombras: Muerte, si no mata, te quita el 30 % de la vida máxima (antes 10 %). La build vale.", huella=True),

    # Chamán
    pc("chaman", "arbol 261", "Desaparece Ráfaga de lava (la sustituye Llamada del trueno: +5 % de crítico a Descarga de relámpagos y Cadena de relámpagos); Sobrecarga de relámpagos pasa a 10/20/30 % y Elemental Mastery se llama Lightning Mastery. Descarga de relámpagos +80 % en el rango máximo, Cadena de relámpagos 2,5 s de lanzamiento y los choques vuelven a los valores de Classic, más altos."),
    pc("chaman", "arbol 263", "Golpe de tormenta hace 150 % de daño de arma con 6 s de reutilización (antes 100 % y 8 s), Arma vorágine salta el doble, Maña mental da 50/100/150 % del intelecto y Aluvión 6-30 %. La build vale y sale bastante mejor.", huella=True),
    pc("chaman", "arbol 262", "Mareas vivas ya no cura al instante: solo cura en el tiempo, cuesta un 40 % menos de maná y tiene 12 s de reutilización (antes 6 s).", huella=True),

    # Mago
    pc("mago", "arbol 81", "Desaparece Enfoque Arcano (se funde en Precisión, de Escarcha). Tromba de misiles baja a la fila 2 y se consume al empezar a canalizar; Recuperación Arcana sube a la fila 1 con hasta 3 puntos. Explosión Arcana: +100 % de coste por carga (antes 175 %), +12 % de daño por carga (antes 15 %) y 18 s. En Fuego, Bola de Fuego mejorada se llama Accelerant e Incineración llega a 5 puntos."),
    pc("mago", "arbol 41", "Enfoque elemental (ahora Precisión) vuelve a 3 puntos (2/4/6 % de golpe) y desaparece Enfoque Arcano: sobran puntos. Incineración llega a 5 puntos (10 % de crítico), Masa crítica se queda en 3 (6 %), Explosión de Fuego mejorada baja a la fila 3 y Bola de Fuego mejorada se llama Accelerant. Ignición ya se aplica a todo el daño de Fogonazo."),
    pc("mago", "arbol 61", "Desaparecen Hielo penetrante, Explosión de Escarcha y Enfoque Arcano, y Enfoque elemental (ahora Precisión) vuelve a 3 puntos. Lanza de hielo: 8 s de reutilización compartida con Explosión de Fuego y vuelve al 300 % contra congelados. Barrera de hielo da +15 % de daño de Escarcha 1 min (+5 % mientras aguanta), Escalofrío del invierno sube un 20 % por carga el daño de Cono de frío y Custodia de Escarcha ya no refleja: anula el hechizo."),
    pc("mago", "nivelado", "Los tramos llevan Hielo penetrante y Enfoque Arcano (desaparecen) y Enfoque elemental a 5 (ahora máximo 3)."),

    # Brujo
    pc("brujo", "arbol 302", "Arruinar duplica su coeficiente y a nivel 60 pasa de 36 a 86 de daño por segundo base; Drenajes mejorados ya no lo potencia y Amplificar maldición afecta ahora a Maldición de agotamiento y Bane of Agony. Las mascotas ganan 2 de vida por punto de aguante tuyo (antes 7,5).", huella=True),
    pc("brujo", "arbol 303", "Las mascotas ganan solo 2 de vida por punto de aguante del brujo (antes 7,5): aguantan mucho menos. Las piedras de hechizo ya solo suben el daño de Sombras.", huella=True),
    pc("brujo", "arbol 301", "Sombras y llamas pasa a 4/8/12/16/20 % (antes 2-10 %) y las piedras de hechizo ya solo suben el daño de Sombras. La build vale y sale mejor.", huella=True),

    # Druida
    pc("druida", "arbol 283", "Génesis 2/4/6/8/10 % (antes 1-5 %), Fuego estelar +40 % de daño base y Naturalista (Restauración) da 2-10 % a todo el daño. El aura de crítico de Forma de lechúcico lunar vuelve a valer para todo, pero no se suma con Líder de la manada.", huella=True),
    pc("druida", "arbol 281", "Desaparece Rabia (Berserk); Corazón de lo Salvaje se va a Restauración y Furor viene a Feral. Laceración pasa a ser un talento de 1 punto en la fila 4 y hay nuevos: Predatory Discipline, Primal Bite (31 puntos, oso) y Shifting Power (31 puntos, gato). Desgarrar y rasgar 3-15 %. La forma de oso da un 115 % más de amenaza (antes 50 %) porque desaparece Bendición de salvación."),
    pc("druida", "arbol 281 gato", "Igual que el oso: sin Rabia, Corazón de lo Salvaje en Restauración y Furor en Feral. A cambio, Triturar hace 200 % de daño de arma (antes 155 %), Garra 140 %, Devastar 435 % y Destripar, Arañazo, Mordedura feroz y Abalanzarse un 25 % más. Nuevo pasivo Poised (nivel 32)."),
    pc("druida", "arbol 282", "Desaparece Don de la Madre Tierra; Furor se va a Feral y llega Corazón de lo Salvaje. Naturalista da 2-10 % a todo el daño y acorta Crecimiento salvaje (3 s de base), y hay un talento nuevo, Bloom. Arreglo rápido solo consume tu propio Rejuvenecimiento o Recrecimiento."),
    pc("druida", "nivelado", "Los tramos llevan Rabia (desaparece) y Corazón de lo Salvaje y Furor, que cambian de árbol."),
]

ACT_VIEJO = '"cambios": [],\n  "pendientes": []\n};'
assert s.count(ACT_VIEJO) == 1, 'ACTUALIZACION no encontrado'
s = s.replace(ACT_VIEJO, '"cambios": [],\n  "pendientes": ' + json.dumps(PENDIENTES, ensure_ascii=False, indent=2).replace('\n', '\n  ') + '\n};')

# ---------------------------------------------------------------- razas
RAZAS = [
    ('"revisado": "2026-10-07",\n  "build": "1.60.1.70235",\n  "aviso": "Las raciales son datos oficiales y del cliente de la beta (pueden cambiar antes del 4 de noviembre).',
     '"revisado": "2026-11-04",\n  "build": "1.60.1.70235",\n  "aviso": "Raciales con los cambios finales de Blizzard (26 y 27-10-2026, repetidos en las notas del 3-11); lo que esas notas no tocan sigue siendo de la beta. El orden por clase se escribió antes de esos cambios y está pendiente de revisar.'),
    ('"Iracundia del trol pasa a ser un 10 % fijo de velocidad durante 10 s; desaparece la especialización en arcos.",',
     '"Iracundia del trol pasa a ser un 10 % fijo de velocidad durante 15 s (10 s en la beta); desaparece la especialización en arcos.",'),
    ('"Canibalizar devuelve también maná; Aguante del tauren añade +1 % de golpe.",',
     '"Canibalizar devuelve también maná y se puede usar siendo inmune al daño físico. Aguante del tauren se queda en +5 % de vida: pierde el golpe y el daño crítico que tuvo en la beta.",\n    "Cambios finales (26 y 27-10): el orco pierde Savage (+1 % de crítico) y recupera Mando (+5 % de daño de las mascotas de brujo y cazador); Furia sangrienta pasa a 2 min de reutilización; Toque de la tumba salta más a menudo, con 15 s de reutilización interna.",\n    "Skyborne: Bendición del viento baja a +2 % de celeridad; Read Leyline da +50 % de regeneración de vida y maná 15 s (100 % si estás Attuned, 1 h tras usarla en una línea ley); Skysight da +15 % de velocidad 15 s (30 % si estás Charged). Attuned y Charged duran 1 h, aguantan la muerte y se quitan al entrar en banda.",'),
    ('"Probabilidad de drenar vida al objetivo, hasta el 5 % de tu vida máxima, con 1 s de reutilización."',
     '"Probabilidad de drenar vida al objetivo, hasta el 5 % de tu vida máxima, con 15 s de reutilización interna (cambio final del 27-10)."'),
    ('"+1 % de velocidad por cada 5 s en movimiento, hasta +30 %; recibir daño o pararse lo reduce."',
     '"+2 % de velocidad por cada 5 s en movimiento, hasta +60 %; ya no afecta a la montura. Recibir daño o pararse lo reduce."'),
    ('"efecto": "+5 % de vida total y +1 % de golpe."', '"efecto": "+5 % de vida total (ya no da golpe)."'),
    ('"efecto": "+10 % de velocidad de ataque y de lanzamiento durante 10 s (3 min)."',
     '"efecto": "+10 % de velocidad de ataque y de lanzamiento durante 15 s (3 min)."'),
    ('"efecto": "+10 % de velocidad a pie y en montura durante 30 s, o 15 min junto a una convergencia elemental (2 min)."',
     '"efecto": "+15 % de velocidad durante 15 s; junto a una convergencia elemental te deja Charged 1 h y sube al 30 % (2 min)."'),
    ('"efecto": "+1 % de celeridad cuerpo a cuerpo, a distancia y con hechizos."',
     '"efecto": "+2 % de celeridad cuerpo a cuerpo, a distancia y con hechizos."'),
    # porClase
    ('"pve": "Para tanque: +5 % de vida y +1 % de golpe de Aguante, y Pisotón de guerra',
     '"pve": "Para tanque: +5 % de vida de Aguante (ya sin el +1 % de golpe), y Pisotón de guerra'),
    ('"pve": "+1 % de celeridad es útil pero menor que lo que dan las demás."',
     '"pve": "+2 % de celeridad es útil pero menor que lo que dan las demás."'),
    ('Furia sangrienta da un 10 % de poder de ataque y se nota en el daño a distancia; ya no mejora a la mascota.',
     'Furia sangrienta da un 10 % de poder de ataque y se nota en el daño a distancia; con los cambios finales, Mando vuelve a dar +5 % de daño a la mascota.'),
    ('"pve": "+1 % de golpe y +5 % de vida de Aguante: sólido en raid."',
     '"pve": "+5 % de vida de Aguante; sin el +1 % de golpe de la beta pierde peso en raid."'),
    ('"pve": "+1 % de celeridad, menor que las anteriores."', '"pve": "+2 % de celeridad, menor que las anteriores."'),
    ('"pve": "Bendición del viento da +1 % de celeridad;', '"pve": "Bendición del viento da +2 % de celeridad;'),
    ('"pve": "+1 % de golpe y +5 % de vida; Pisotón de guerra para Mejora y Recuperación."',
     '"pve": "+5 % de vida (ya sin el +1 % de golpe); Pisotón de guerra para Mejora y Recuperación."'),
    ('"pve": "+1 % de celeridad, útil para sanar y lanzar."', '"pve": "+2 % de celeridad, útil para sanar y lanzar."'),
    ('"pve": "Furia sangrienta da un 10 % de poder con hechizos durante el pico de daño."',
     '"pve": "Furia sangrienta da un 10 % de poder con hechizos durante el pico de daño, y Mando vuelve a dar +5 % de daño a la mascota."'),
    ('"pve": "+5 % de vida y +1 % de golpe valen para oso, gato y sanador;',
     '"pve": "+5 % de vida vale para oso, gato y sanador (el +1 % de golpe desapareció);'),
    ('"pve": "+1 % de celeridad y +5 % contra elementales."', '"pve": "+2 % de celeridad y +5 % contra elementales."'),
]
ri = s.index('window.RAZAS = {')
rj = s.index('</script>', ri)
r = s[ri:rj]
for viejo, nuevo in RAZAS:
    n = r.count(viejo)
    assert n == 1, f'RAZAS: {n} coincidencias para {viejo[:70]!r}'
    r = r.replace(viejo, nuevo)
s = s[:ri] + r + s[rj:]

# ---------------------------------------------------------------- novedades
CAB = 'window.NOVEDADES='
i = s.index(CAB) + len(CAB)
j = s.index('</script>', i)
cuerpo = s[i:j].rstrip()
assert cuerpo.endswith(';')
N = json.loads(cuerpo[:-1])

def ent(sec, texto, fuente=NOTAS, fecha=D):
    if sec not in N['secciones']:
        sec = 'clases' if sec.startswith('clase-') else sec
    assert sec in N['secciones'], sec
    return {"s": sec, "texto": texto, "estado": "confirmado", "fecha": fecha, "fechaDe": "nota", "fuente": fuente}

NUEVAS = [
    ent('clases', 'Ajuste final antes del lanzamiento: sube el daño de casi todas las clases y los enemigos de nivel alto tienen más vida para compensar. Blizzard no hará grandes cambios de equilibrio hasta que abran las bandas, salvo errores y casos extremos.'),
    ent('clases', 'Los talentos ya no pierden probabilidad de activarse al lanzar un rango bajo de un hechizo, salvo Concentración arcana, Mordedura de Escarcha y Dedos de Escarcha del mago con rangos aprendidos más de 12 niveles por debajo del tuyo.'),
    ent('clases', 'Las raíces que salen de talentos (Mordedura de Escarcha, Atrapar, Corte de ala mejorado, Contraataque y Seccionar mejorado) tienen ahora rendimientos decrecientes.'),
    ent('clase-guerrero', 'Guerrero: Actitud defensiva da un 80 % más de amenaza (antes 30 %) y Embate baja a 15 s de reutilización. En Armas, Maestría táctica mejorada pasa a 3 puntos y Fragor de la sangre a 2; en Furia, Aluvión pasa a 3 puntos y llegan Reckless Swings e Improved Whirlwind.'),
    ent('clase-paladin', 'Paladín: desaparecen Salvación, Salvación masiva, Revocar y Bendición de luz; Furia justa se aprende a nivel 10. Los tres árboles cambian mucho: Sagrado gana Oath of Light y Boundless Light, Protección gana Stoicism y Shieldsworn y Reprensión tiene como talento de 31 puntos Unsealed Wrath.'),
    ent('clase-cazador', 'Cazador: Disparo apuntado +110 %, Disparo Arcano +30 %, Picadura de serpiente +20 %, Aspecto del halcón y Aura de disparo certero dan más poder de ataque a distancia y Aluvión pasa a 5/10/15 %. Todas las trampas comparten 30 s de reutilización.'),
    ent('clase-picaro', 'Pícaro: facultades nuevas Poised (nivel 18) y Shank (nivel 24, golpe con la mano izquierda que da energía); los venenos escalan el doble con el poder de ataque. Desaparecen Asesinar, Quietus, Mil cortes y Distraer mejorado; Mutilar y Death Mark son los talentos de 31 puntos de Asesinato y Sutileza.'),
    ent('clase-sacerdote', 'Sacerdote: Sanación conjunta desaparece y la sustituye Holy Binding; Palabra de las Sombras: Muerte, si no mata, quita un 30 % de la vida máxima (antes 10 %).'),
    ent('clase-chaman', 'Chamán: desaparece Ráfaga de lava y entra Llamada del trueno; Descarga de relámpagos +80 % en el rango máximo y los choques vuelven a sus valores de Classic. Golpe de tormenta 150 % y 6 s; Mareas vivas solo cura en el tiempo. Proyección totémica pasa a llamarse Llamada totémica (30 s).'),
    ent('clase-mago', 'Mago: desaparecen Explosión de Escarcha, Hielo penetrante y Enfoque Arcano; Precisión vuelve a 3 puntos (2/4/6 %), Masa crítica a 3 e Incineración llega a 5. Lanza de hielo tiene 8 s de reutilización compartida con Explosión de Fuego y Barrera de hielo da daño de Escarcha.'),
    ent('clase-brujo', 'Brujo: las mascotas ganan 2 de vida por punto de aguante del brujo (antes 7,5), Arruinar casi triplica su daño a nivel 60, Sombras y llamas pasa a 4-20 % y el coste de entrenamiento se rebaja lo que se espera gastar en grimorios.'),
    ent('clase-druida', 'Druida: desaparece Rabia (Berserk); Feral gana Primal Bite (oso) y Shifting Power (gato), la forma de oso da un 115 % más de amenaza y Triturar sube a 200 % de daño de arma. Fuego estelar +40 %, nuevo pasivo Poised (nivel 32) y Restauración gana Bloom y pierde Don de la Madre Tierra.'),
    ent('razas', 'Raciales finales de la Horda: el orco pierde Savage y recupera Mando (+5 % de daño de mascota), con Furia sangrienta a 2 min; Iracundia dura 15 s; Toque de la tumba tiene 15 s de reutilización interna; Aguante del tauren se queda en +5 % de vida y Planicies da hasta +60 % de velocidad (no en montura); Skyborne baja a +2 % de celeridad.', fuente=RACIALES, fecha='2026-10-27'),
    ent('nivelado', 'Entrenar las facultades de clase del 1 al 60 cuesta 206-207 de oro en todas las clases. Los hechizos nuevos ya no se ponen solos en las barras de acción: tras pasar por el entrenador, arrástralos desde el libro de hechizos.'),
    ent('nivelado', 'Las bolsas nuevas ya no se equipan solas en los huecos libres, y los enemigos reaparecen más deprisa en las zonas iniciales (Blizzard lo bajará cuando pase la avalancha del lanzamiento).'),
]
# Las entradas de razas de la beta que los cambios finales dejan mal
ARREGLOS = [
    ('Iracundia del trol pasa a ser un 10 % fijo de velocidad durante 10 s;',
     'Iracundia del trol pasa a ser un 10 % fijo de velocidad durante 15 s (10 s en la beta);'),
    ('Aguante del tauren añade +1 % de golpe.',
     'Aguante del tauren se queda en +5 % de vida (el +1 % de golpe de la beta desapareció en los cambios finales).'),
]
for viejo, nuevo in ARREGLOS:
    xs = [e for e in N['entradas'] if viejo in e.get('texto', '')]
    assert len(xs) == 1, (viejo, len(xs))
    xs[0]['texto'] = xs[0]['texto'].replace(viejo, nuevo)

N['entradas'] = NUEVAS + N['entradas']

beta = N.get('beta') or {}
beta['titulo'] = 'WoW Forever Beta Development Notes – Updated 3 November'
beta.setdefault('mensajes', []).append({
    "n": 9, "fecha": "2026-11-03", "url": NOTAS['url'],
    "titulo": "Notas finales del 3-11: más daño de clase, más vida en enemigos y raciales definitivas",
    "puntos": [
        "Sube el daño de casi todas las clases y la vida de los enemigos de nivel alto; no habrá grandes ajustes hasta que abran las bandas.",
        "Entrenar del 1 al 60 cuesta 206-207 de oro en todas las clases; los hechizos nuevos no se ponen solos en las barras y las bolsas no se equipan solas.",
        "Druida sin Rabia y con Primal Bite y Shifting Power; paladín sin Salvación ni Bendición de luz; mago sin Explosión de Escarcha; chamán sin Ráfaga de lava; pícaro con Shank y Poised.",
        "Raíces de talentos con rendimientos decrecientes y estadísticas base corregidas en todas las razas.",
        "Lanzamiento el 4 de noviembre a las 23:00 UTC (00:00 en España).",
    ],
})
N['beta'] = beta

s = s[:i] + json.dumps(N, ensure_ascii=False, separators=(',', ':')) + ';\n' + s[j:]
open(RUTA, 'w', encoding='utf-8').write(s)
print('ok', len(PENDIENTES), 'pendientes,', len(NUEVAS), 'novedades')
