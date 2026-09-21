import os
import base64
import json
import html

import streamlit as st
import streamlit.components.v1 as components


# ============================================================
# CONFIGURACIÓN STREAMLIT
# ============================================================

st.set_page_config(
    page_title="Nuestro Wrapped ❤️",
    page_icon="❤️",
    layout="wide",
    initial_sidebar_state="collapsed",
)


# ============================================================
# RUTAS
# ============================================================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

FOTOS_DIR = os.path.join(
    BASE_DIR,
    "fotos"
)

GALERIA_DIR = os.path.join(
    FOTOS_DIR,
    "galeria"
)

# IMPORTANTE:
# La música está directamente dentro de Main
MUSICA_FONDO = os.path.join(
    BASE_DIR,
    "musica.mp3"
)


# ============================================================
# FUNCIONES
# ============================================================

def archivo_base64(ruta):

    if not os.path.exists(ruta):
        return None

    try:

        with open(ruta, "rb") as archivo:

            return base64.b64encode(
                archivo.read()
            ).decode("utf-8")

    except Exception:

        return None


def mime_imagen(ruta):

    extension = (
        os.path.splitext(ruta)[1]
        .lower()
    )

    tipos = {

        ".png":
            "image/png",

        ".jpg":
            "image/jpeg",

        ".jpeg":
            "image/jpeg",

        ".webp":
            "image/webp",

    }

    return tipos.get(
        extension,
        "image/png"
    )


def imagen_data(ruta):

    data = archivo_base64(ruta)

    if not data:
        return None

    return (
        f"data:{mime_imagen(ruta)};"
        f"base64,{data}"
    )


# ============================================================
# FOTOGRAFÍAS
# ============================================================

FOTOS = {

    "inicio":
        os.path.join(
            FOTOS_DIR,
            "image_0.png"
        ),

    "caifanes":
        os.path.join(
            FOTOS_DIR,
            "image_1.png"
        ),

    "diciembre_2023": [

        os.path.join(
            FOTOS_DIR,
            "image_2.png"
        ),

        os.path.join(
            FOTOS_DIR,
            "image_3.png"
        ),

        os.path.join(
            FOTOS_DIR,
            "image_4.png"
        ),

    ],

    "y2024": [

        os.path.join(
            FOTOS_DIR,
            "image_5.png"
        ),

        os.path.join(
            FOTOS_DIR,
            "image_6.png"
        ),

        os.path.join(
            FOTOS_DIR,
            "image_7.png"
        ),

        os.path.join(
            FOTOS_DIR,
            "image_8.png"
        ),

    ],

    "y2025_2026": [

        os.path.join(
            FOTOS_DIR,
            "image_9.png"
        ),

        os.path.join(
            FOTOS_DIR,
            "image_10.png"
        ),

        os.path.join(
            FOTOS_DIR,
            "image_11.png"
        ),

    ],

}


# ============================================================
# TEXTOS DE LAS FOTOS
# ============================================================

CAPTIONS = {

    "diciembre_2023": [

        "En el pueblo de mi papá, contigo 🏡",

        "Rompiendo la piñata juntos 🎉",

        "Rumbo a Mazatlán 🌊",

    ],

    "y2024": [

        "Emprendiendo con las togas SHESPAT 🎓",

        "Enseñándome a manejar la moto 🏍️",

        "Mi cambio de look 💇",

        "Nuestra primera Navidad juntos 🎄",

    ],

    "y2025_2026": [

        "El reloj para mi papá 🎁",

        "Carajo y Nena, nuestros conejitos 🐰",

        "La feria y la rueda de la fortuna 🎡",

    ],

}


# ============================================================
# CANCIONES
# ============================================================

CANCIONES = [

    {
        "titulo":
            "Tiempo para Amarte",

        "artista":
            "Laureano Brizuela",

        "significado":
            "A pesar de las cuentas, el estrés diario y todas "
            "las cosas que tenemos que hacer, siempre quiero "
            "encontrar tiempo para ti.",
    },

    {
        "titulo":
            "My One and Only Love / They Say It's Wonderful",

        "artista":
            "John Coltrane",

        "significado":
            "Mi descubrimiento personal del amor y una canción "
            "que terminó teniendo un significado muy especial "
            "para nosotros.",
    },

    {
        "titulo":
            "I Only Have Eyes for You",

        "artista":
            "Louis Armstrong",

        "significado":
            "Entre todas las personas, lugares y cosas que "
            "existen, mis ojos siempre terminan buscándote a ti.",
    },

    {
        "titulo":
            "Eso y Más",

        "artista":
            "Joan Sebastián",

        "significado":
            "Una canción que representa todo eso que siento "
            "y muchas veces no sé cómo decirte.",
    },

    {
        "titulo":
            "Diséñame",

        "artista":
            "Joan Sebastián",

        "significado":
            "Nuestro amor fue construyéndose poco a poco, "
            "con nuestras propias historias.",
    },

    {
        "titulo":
            "The Nearness of You",

        "artista":
            "Ella Fitzgerald & Louis Armstrong",

        "significado":
            "La cercanía de la persona que amas puede hacer "
            "que cualquier momento cotidiano se sienta especial.",
    },

    {
        "titulo":
            "Only You",

        "artista":
            "The Platters",

        "significado":
            "Porque hay personas que simplemente se vuelven "
            "únicas en nuestra vida.",
    },

    {
        "titulo":
            "Eres",

        "artista":
            "José María Napoleón",

        "significado":
            "Una forma de decirte todo lo que significas para mí.",
    },

    {
        "titulo":
            "Mi Mundo Tú",

        "artista":
            "Camilo Sesto",

        "significado":
            "Después de estos años, eres una parte enorme "
            "de mi mundo.",
    },

    {
        "titulo":
            "Cama y Mesa",

        "artista":
            "Roberto Carlos",

        "significado":
            "Una canción sobre compartir la vida, los momentos "
            "íntimos y también los cotidianos.",
    },

    {
        "titulo":
            "Invítame un cigarro",

        "artista":
            "Tradicional / Popular",

        "significado":
            "Una de esas canciones que terminaron formando "
            "parte de nuestra historia.",
    },

]


# ============================================================
# RESTAURANTES
# ============================================================

RESTAURANTES = [

    {
        "nombre":
            "Ninja Ramen",

        "descripcion":
            "Uno de esos lugares que se volvieron parte "
            "de nuestros momentos juntos.",
    },

    {
        "nombre":
            "Ryu Ramen House",

        "descripcion":
            "Comida, plática y tiempo juntos.",
    },

    {
        "nombre":
            "Trueke Comida & Amigos",

        "descripcion":
            "Otro lugar que quedó guardado dentro "
            "de nuestras pequeñas aventuras.",
    },

]


# ============================================================
# GALERÍA
# ============================================================

def obtener_galeria():

    if not os.path.exists(
        GALERIA_DIR
    ):
        return []

    extensiones = (
        ".png",
        ".jpg",
        ".jpeg",
        ".webp"
    )

    archivos = []

    for archivo in sorted(
        os.listdir(GALERIA_DIR)
    ):

        if archivo.lower().endswith(
            extensiones
        ):

            archivos.append(
                os.path.join(
                    GALERIA_DIR,
                    archivo
                )
            )

    return archivos


# ============================================================
# PREPARAR IMÁGENES
# ============================================================

def preparar_imagenes():

    imagenes = {}

    portada = os.path.join(
        FOTOS_DIR,
        "portada.png"
    )

    if os.path.exists(portada):

        imagenes["portada"] = (
            imagen_data(portada)
        )

    for nombre, valor in FOTOS.items():

        if isinstance(
            valor,
            list
        ):

            imagenes[nombre] = []

            for ruta in valor:

                data = imagen_data(
                    ruta
                )

                if data:

                    imagenes[
                        nombre
                    ].append(data)

        else:

            data = imagen_data(
                valor
            )

            if data:

                imagenes[
                    nombre
                ] = data

    imagenes["galeria"] = []

    for ruta in obtener_galeria():

        data = imagen_data(
            ruta
        )

        if data:

            imagenes[
                "galeria"
            ].append(data)

    return imagenes


IMAGENES = preparar_imagenes()


# ============================================================
# MÚSICA
# ============================================================

MUSICA_B64 = archivo_base64(
    MUSICA_FONDO
)


# ============================================================
# DATOS JAVASCRIPT
# ============================================================

DATOS = {

    "imagenes":
        IMAGENES,

    "canciones":
        CANCIONES,

    "restaurantes":
        RESTAURANTES,

    "captions":
        CAPTIONS,

}


DATOS_JSON = json.dumps(
    DATOS,
    ensure_ascii=False
)


# ============================================================
# AUDIO
# ============================================================

if MUSICA_B64:

    AUDIO_HTML = f"""

    <audio
        id="backgroundMusic"
        preload="auto"
        loop
    >

        <source
            src="data:audio/mpeg;base64,{MUSICA_B64}"
            type="audio/mpeg"
        >

    </audio>

    """

else:

    AUDIO_HTML = ""


# ============================================================
# HTML
# ============================================================

HTML = f"""

<!DOCTYPE html>

<html lang="es">

<head>

<meta charset="UTF-8">

<meta
    name="viewport"
    content="width=device-width,
             initial-scale=1,
             maximum-scale=1,
             user-scalable=no"
/>


<style>

/* ============================================================
   RESET
   ============================================================ */

* {{

    box-sizing:
        border-box;

    -webkit-tap-highlight-color:
        transparent;

}}


html,
body {{

    margin:
        0;

    padding:
        0;

    width:
        100%;

    height:
        100%;

    overflow:
        hidden;

    background:
        #07030b;

    color:
        white;

    font-family:
        Arial,
        sans-serif;

    touch-action:
        none;

}}


/* ============================================================
   APP
   ============================================================ */

#app {{

    position:
        fixed;

    inset:
        0;

    width:
        100vw;

    height:
        100dvh;

    overflow:
        hidden;

    background:
        #07030b;

    touch-action:
        none;

    user-select:
        none;

    -webkit-user-select:
        none;

}}


/* ============================================================
   FONDO
   ============================================================ */

#background {{

    position:
        absolute;

    inset:
        -10%;

    z-index:
        0;

    transition:
        background 0.7s ease;

}}


#background::before {{

    content:
        "";

    position:
        absolute;

    width:
        70vw;

    height:
        70vw;

    left:
        -25%;

    top:
        -15%;

    border-radius:
        50%;

    background:
        radial-gradient(
            circle,
            rgba(255,255,255,.12),
            transparent 68%
        );

    filter:
        blur(15px);

    animation:
        floatingOne
        10s
        ease-in-out
        infinite;

}}


#background::after {{

    content:
        "";

    position:
        absolute;

    width:
        65vw;

    height:
        65vw;

    right:
        -25%;

    bottom:
        -15%;

    border-radius:
        50%;

    background:
        radial-gradient(
            circle,
            rgba(255,255,255,.1),
            transparent 68%
        );

    filter:
        blur(20px);

    animation:
        floatingTwo
        12s
        ease-in-out
        infinite;

}}


@keyframes floatingOne {{

    0%,
    100% {{
        transform:
            translate(0,0)
            scale(1);
    }}

    50% {{
        transform:
            translate(30px,40px)
            scale(1.1);
    }}

}}


@keyframes floatingTwo {{

    0%,
    100% {{
        transform:
            translate(0,0)
            scale(1);
    }}

    50% {{
        transform:
            translate(-30px,-25px)
            scale(1.08);
    }}

}}


/* ============================================================
   GRANO
   ============================================================ */

#grain {{

    position:
        absolute;

    inset:
        0;

    z-index:
        40;

    pointer-events:
        none;

    opacity:
        .055;

    background-image:
        url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='180' height='180'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='.9' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)' opacity='.8'/%3E%3C/svg%3E");

}}


/* ============================================================
   PROGRESO
   ============================================================ */

#progress {{

    position:
        absolute;

    top:
        max(
            10px,
            env(safe-area-inset-top)
        );

    left:
        12px;

    right:
        12px;

    z-index:
        100;

    display:
        flex;

    gap:
        4px;

}}


.progress-bar {{

    flex:
        1;

    height:
        3px;

    border-radius:
        10px;

    overflow:
        hidden;

    background:
        rgba(255,255,255,.22);

}}


.progress-fill {{

    width:
        0%;

    height:
        100%;

    border-radius:
        inherit;

    background:
        white;

}}


/* ============================================================
   CONTADOR
   ============================================================ */

#counter {{

    position:
        absolute;

    z-index:
        100;

    right:
        15px;

    top:
        calc(
            max(
                10px,
                env(safe-area-inset-top)
            ) + 14px
        );

    font-size:
        9px;

    font-weight:
        800;

    letter-spacing:
        .15em;

    color:
        rgba(255,255,255,.6);

}}


/* ============================================================
   SLIDES
   ============================================================ */

#slides {{

    position:
        relative;

    width:
        100%;

    height:
        100%;

    z-index:
        10;

}}


.slide {{

    position:
        absolute;

    inset:
        0;

    width:
        100%;

    height:
        100%;

    padding:
        60px 20px
        calc(
            55px +
            env(safe-area-inset-bottom)
        );

    display:
        flex;

    justify-content:
        center;

    align-items:
        center;

    opacity:
        0;

    pointer-events:
        none;

    transform:
        translateX(60px)
        scale(.97);

    transition:
        opacity .5s ease,
        transform .6s ease;

    overflow:
        hidden;

}}


.slide.active {{

    opacity:
        1;

    pointer-events:
        auto;

    transform:
        translateX(0)
        scale(1);

}}


.slide.previous {{

    transform:
        translateX(-60px)
        scale(.97);

}}


/* ============================================================
   CONTENIDO
   ============================================================ */

.content {{

    width:
        100%;

    max-width:
        850px;

    height:
        100%;

    display:
        flex;

    flex-direction:
        column;

    justify-content:
        center;

    align-items:
        center;

    text-align:
        center;

    overflow-y:
        auto;

    scrollbar-width:
        none;

}}


.content::-webkit-scrollbar {{
    display:
        none;
}}


/* ============================================================
   TIPOGRAFÍA
   ============================================================ */

.eyebrow {{

    font-size:
        clamp(
            9px,
            2.3vw,
            12px
        );

    letter-spacing:
        .23em;

    text-transform:
        uppercase;

    font-weight:
        800;

    color:
        rgba(255,255,255,.65);

    margin-bottom:
        15px;

}}


.title,
.section-title,
.final-title {{

    font-family:
        Arial,
        sans-serif;

    font-weight:
        900;

    line-height:
        .98;

    letter-spacing:
        -.065em;

    margin:
        0;

}}


.title {{

    font-size:
        clamp(
            2.8rem,
            12vw,
            7rem
        );

    background:
        linear-gradient(
            115deg,
            #ff2d75,
            #ff8a00,
            #ffd447,
            #9b52ff
        );

    -webkit-background-clip:
        text;

    -webkit-text-fill-color:
        transparent;

}}


.section-title {{

    font-size:
        clamp(
            2rem,
            8vw,
            5rem
        );

}}


.subtitle {{

    max-width:
        580px;

    margin-top:
        20px;

    color:
        rgba(255,255,255,.72);

    font-size:
        clamp(
            .9rem,
            3vw,
            1.1rem
        );

    line-height:
        1.7;

}}


/* ============================================================
   PORTADA
   ============================================================ */

.cover-number {{

    font-size:
        clamp(
            7rem,
            30vw,
            15rem
        );

    line-height:
        .7;

    font-weight:
        900;

    letter-spacing:
        -.13em;

    background:
        linear-gradient(
            120deg,
            #ff2d75,
            #ff8a00,
            #ffd447,
            #8c52ff
        );

    -webkit-background-clip:
        text;

    -webkit-text-fill-color:
        transparent;

}}


/* ============================================================
   FOTOS
   ============================================================ */

.photo-frame {{

    position:
        relative;

    width:
        min(
            88vw,
            600px
        );

    max-height:
        50vh;

    margin:
        20px auto;

    overflow:
        hidden;

    border-radius:
        28px;

    border:
        1px solid
        rgba(255,255,255,.12);

    box-shadow:
        0 30px 80px
        rgba(0,0,0,.45);

}}


.photo-frame img {{

    display:
        block;

    width:
        100%;

    max-height:
        50vh;

    object-fit:
        cover;

}}


.photo-caption {{

    position:
        absolute;

    left:
        0;

    right:
        0;

    bottom:
        0;

    padding:
        50px 18px 18px;

    text-align:
        left;

    background:
        linear-gradient(
            transparent,
            rgba(0,0,0,.85)
        );

    font-weight:
        700;

    font-size:
        .8rem;

}}


/* ============================================================
   ESTADÍSTICAS
   ============================================================ */

.stats {{

    width:
        min(
            100%,
            650px
        );

    display:
        grid;

    grid-template-columns:
        repeat(2, 1fr);

    gap:
        10px;

    margin-top:
        24px;

}}


.stat {{

    min-height:
        135px;

    padding:
        20px;

    border-radius:
        24px;

    display:
        flex;

    flex-direction:
        column;

    justify-content:
        space-between;

    text-align:
        left;

    background:
        rgba(255,255,255,.07);

    border:
        1px solid
        rgba(255,255,255,.09);

    backdrop-filter:
        blur(15px);

}}


.stat-number {{

    font-size:
        clamp(
            2rem,
            9vw,
            3.5rem
        );

    font-weight:
        900;

}}


.stat-label {{

    font-size:
        9px;

    font-weight:
        800;

    letter-spacing:
        .12em;

    color:
        rgba(255,255,255,.5);

}}


/* ============================================================
   FECHA
   ============================================================ */

.big-date {{

    font-size:
        clamp(
            6rem,
            28vw,
            12rem
        );

    line-height:
        .8;

    font-weight:
        900;

    letter-spacing:
        -.1em;

    margin:
        25px 0;

    background:
        linear-gradient(
            120deg,
            #ff2d75,
            #ffd447
        );

    -webkit-background-clip:
        text;

    -webkit-text-fill-color:
        transparent;

}}


/* ============================================================
   TEXTOS
   ============================================================ */

.section-text {{

    max-width:
        620px;

    margin-top:
        15px;

    color:
        rgba(255,255,255,.63);

    line-height:
        1.75;

}}


/* ============================================================
   MEMORIAS
   ============================================================ */

.memories {{

    width:
        min(
            100%,
            650px
        );

    text-align:
        left;

    margin-top:
        10px;

}}


.memory {{

    display:
        flex;

    gap:
        13px;

    padding:
        14px 0;

    border-bottom:
        1px solid
        rgba(255,255,255,.08);

}}


.memory-icon {{

    font-size:
        1.4rem;

}}


.memory-title {{

    font-weight:
        800;

}}


.memory-text {{

    color:
        rgba(255,255,255,.55);

    font-size:
        .8rem;

    line-height:
        1.5;

    margin-top:
        3px;

}}


/* ============================================================
   RESTAURANTES
   ============================================================ */

.places {{

    width:
        min(
            100%,
            650px
        );

    margin-top:
        15px;

}}


.place {{

    padding:
        17px;

    margin:
        8px 0;

    border-radius:
        22px;

    background:
        rgba(255,255,255,.06);

    border:
        1px solid
        rgba(255,255,255,.08);

    text-align:
        left;

}}


.place-number {{

    font-size:
        1.4rem;

    font-weight:
        900;

    color:
        rgba(255,255,255,.2);

}}


.place-name {{

    margin-top:
        6px;

    font-weight:
        900;

}}


.place-description {{

    margin-top:
        5px;

    color:
        rgba(255,255,255,.5);

    font-size:
        .78rem;

    line-height:
        1.5;

}}


/* ============================================================
   MÚSICA
   ============================================================ */

.album {{

    width:
        min(
            65vw,
            280px
        );

    aspect-ratio:
        1;

    margin:
        22px 0;

    border-radius:
        25px;

    display:
        flex;

    justify-content:
        center;

    align-items:
        center;

    background:
        linear-gradient(
            135deg,
            #ff2d75,
            #ff8a00,
            #7a38ff
        );

    box-shadow:
        0 25px 70px
        rgba(0,0,0,.45);

}}


.album::before {{

    content:
        "♪";

    font-size:
        9rem;

    font-family:
        Georgia,
        serif;

    color:
        rgba(255,255,255,.9);

}}


.featured-song {{

    width:
        min(
            100%,
            600px
        );

    text-align:
        left;

}}


.song-number {{

    font-size:
        9px;

    letter-spacing:
        .2em;

    color:
        rgba(255,255,255,.4);

}}


.song-title {{

    font-size:
        clamp(
            1.3rem,
            6vw,
            2.4rem
        );

    font-weight:
        900;

    margin-top:
        7px;

}}


.song-artist {{

    color:
        #ffd447;

    font-size:
        .85rem;

    font-weight:
        700;

    margin-top:
        6px;

}}


.song-meaning {{

    color:
        rgba(255,255,255,.58);

    line-height:
        1.7;

    font-size:
        .82rem;

    margin-top:
        13px;

}}


/* ============================================================
   GALERÍA
   ============================================================ */

.gallery-photo {{

    width:
        min(
            90vw,
            700px
        );

    height:
        min(
            60vh,
            650px
        );

    margin:
        20px auto;

    overflow:
        hidden;

    border-radius:
        30px;

    box-shadow:
        0 30px 80px
        rgba(0,0,0,.5);

}}


.gallery-photo img {{

    width:
        100%;

    height:
        100%;

    object-fit:
        contain;

}}


/* ============================================================
   FINAL
   ============================================================ */

.final-title {{

    font-size:
        clamp(
            2.2rem,
            10vw,
            5rem
        );

    background:
        linear-gradient(
            120deg,
            #ff2d75,
            #ffd447,
            #9b52ff
        );

    -webkit-background-clip:
        text;

    -webkit-text-fill-color:
        transparent;

}}


.days-label {{

    margin-top:
        28px;

    color:
        rgba(255,255,255,.48);

}}


.days-number {{

    margin-top:
        5px;

    font-size:
        clamp(
            3rem,
            15vw,
            6rem
        );

    font-weight:
        900;

}}


.quote {{

    max-width:
        600px;

    margin-top:
        28px;

    font-size:
        clamp(
            1rem,
            4vw,
            1.45rem
        );

    font-weight:
        800;

    line-height:
        1.5;

    background:
        linear-gradient(
            90deg,
            #ff2d75,
            #ffd447,
            #9b52ff
        );

    -webkit-background-clip:
        text;

    -webkit-text-fill-color:
        transparent;

}}


/* ============================================================
   MÚSICA - BOTÓN
   ============================================================ */

#musicControl {{

    position:
        absolute;

    z-index:
        500;

    right:
        16px;

    bottom:
        calc(
            17px +
            env(safe-area-inset-bottom)
        );

    width:
        42px;

    height:
        42px;

    border-radius:
        50%;

    border:
        1px solid
        rgba(255,255,255,.18);

    background:
        rgba(0,0,0,.25);

    backdrop-filter:
        blur(15px);

    color:
        white;

    display:
        flex;

    justify-content:
        center;

    align-items:
        center;

    padding:
        0;

}}


.sound-bars {{

    height:
        16px;

    display:
        flex;

    align-items:
        flex-end;

    gap:
        2px;

}}


.sound-bar {{

    width:
        2px;

    height:
        6px;

    background:
        white;

    border-radius:
        4px;

}}


.music-playing .sound-bar:nth-child(1) {{

    animation:
        sound .55s infinite alternate;

}}


.music-playing .sound-bar:nth-child(2) {{

    animation:
        sound .4s infinite alternate;

}}


.music-playing .sound-bar:nth-child(3) {{

    animation:
        sound .7s infinite alternate;

}}


@keyframes sound {{

    from {{
        height:
            4px;
    }}

    to {{
        height:
            15px;
    }}

}}


/* ============================================================
   MOBILE
   ============================================================ */

@media (
    max-width: 600px
) {{

    .slide {{

        padding:
            60px 18px
            calc(
                55px +
                env(safe-area-inset-bottom)
            );

    }}

}}


/* ============================================================
   PANTALLAS PEQUEÑAS
   ============================================================ */

@media (
    max-width: 600px
) and (
    max-height: 700px
) {{

    .photo-frame {{

        max-height:
            38vh;

    }}

    .photo-frame img {{

        max-height:
            38vh;

    }}

    .stat {{

        min-height:
            105px;

    }}

}}

</style>

</head>


<body>


<div id="app">


    <div id="background"></div>


    <div id="grain"></div>


    <div id="progress"></div>


    <div id="counter">
        01 / 11
    </div>


    <div id="slides">


        <!-- =================================================
             01
             ================================================= -->

        <section
            class="slide active"
            data-theme="cover"
        >

            <div class="content">

                <div class="eyebrow">
                    NUESTRO WRAPPED · 2023 — 2026
                </div>

                <div class="cover-number">
                    3
                </div>

                <h1 class="title">

                    Años<br>
                    Juntos

                </h1>

                <p class="subtitle">

                    Tres años.
                    Cientos de momentos.
                    Algunas canciones.
                    Muchos recuerdos.

                    <br><br>

                    Esta es una pequeña parte
                    de nuestra historia.

                </p>

            </div>

        </section>


        <!-- =================================================
             02
             ================================================= -->

        <section
            class="slide"
            data-theme="stats"
        >

            <div class="content">

                <div class="eyebrow">
                    NUESTRO WRAPPED
                </div>

                <h2 class="section-title">

                    Nuestra historia<br>
                    en números

                </h2>


                <div class="stats">


                    <div class="stat">

                        <div class="stat-number">
                            3
                        </div>

                        <div class="stat-label">
                            AÑOS JUNTOS
                        </div>

                    </div>


                    <div class="stat">

                        <div class="stat-number">
                            11
                        </div>

                        <div class="stat-label">
                            CANCIONES
                        </div>

                    </div>


                    <div class="stat">

                        <div class="stat-number">
                            3
                        </div>

                        <div class="stat-label">
                            LUGARES
                        </div>

                    </div>


                    <div class="stat">

                        <div class="stat-number">
                            2
                        </div>

                        <div class="stat-label">
                            CONEJITOS 🐰
                        </div>

                    </div>


                </div>


                <p class="section-text">

                    Pero hay una estadística
                    que nunca podremos calcular:

                    <br><br>

                    <strong>
                        todas las veces que
                        elegimos estar juntos.
                    </strong>

                </p>

            </div>

        </section>


        <!-- =================================================
             03
             ================================================= -->

        <section
            class="slide"
            data-theme="start"
        >

            <div class="content">

                <div class="eyebrow">
                    24 · 07 · 2023
                </div>

                <h2 class="section-title">

                    Todo comenzó<br>
                    aquí

                </h2>

                <div class="big-date">
                    24
                </div>

                <p class="section-text">

                    Hay fechas que terminan
                    convirtiéndose en algo mucho
                    más grande de lo que imaginábamos.

                    <br><br>

                    El 24 de julio de 2023
                    comenzó nuestra historia.

                </p>

                <div
                    class="photo-frame"
                    id="inicioPhoto"
                ></div>

            </div>

        </section>


        <!-- =================================================
             04
             ================================================= -->

        <section
            class="slide"
            data-theme="concert"
        >

            <div class="content">

                <div class="eyebrow">
                    CAIFANES 🎸
                </div>

                <h2 class="section-title">

                    Una noche<br>
                    para recordar

                </h2>

                <div
                    class="photo-frame"
                    id="caifanesPhoto"
                ></div>

                <p class="section-text">

                    No solamente importa
                    a dónde vamos,

                    <br>

                    sino con quién
                    compartimos el momento.

                </p>

            </div>

        </section>


        <!-- =================================================
             05
             ================================================= -->

        <section
            class="slide"
            data-theme="december"
        >

            <div class="content">

                <div class="eyebrow">
                    DICIEMBRE · 2023
                </div>

                <h2 class="section-title">

                    Nuestro primer<br>
                    diciembre

                </h2>


                <div class="memories">


                    <div class="memory">

                        <div class="memory-icon">
                            🏡
                        </div>

                        <div>

                            <div class="memory-title">
                                El pueblo de mi papá
                            </div>

                            <div class="memory-text">
                                Un lugar diferente,
                                pero especial porque
                                estabas conmigo.
                            </div>

                        </div>

                    </div>


                    <div class="memory">

                        <div class="memory-icon">
                            🎉
                        </div>

                        <div>

                            <div class="memory-title">
                                La piñata
                            </div>

                            <div class="memory-text">
                                Momentos sencillos
                                que terminaron convirtiéndose
                                en recuerdos.
                            </div>

                        </div>

                    </div>


                    <div class="memory">

                        <div class="memory-icon">
                            🌊
                        </div>

                        <div>

                            <div class="memory-title">
                                Rumbo a Mazatlán
                            </div>

                            <div class="memory-text">
                                Una aventura más
                                de nuestra historia.
                            </div>

                        </div>

                    </div>


                </div>


                <div
                    class="photo-frame"
                    id="decemberPhoto"
                ></div>

            </div>

        </section>


        <!-- =================================================
             06
             ================================================= -->

        <section
            class="slide"
            data-theme="year2024"
        >

            <div class="content">

                <div class="eyebrow">
                    CAPÍTULO · 2024
                </div>

                <h2 class="section-title">

                    Un año de<br>
                    cambios

                </h2>


                <div class="memories">


                    <div class="memory">

                        <div class="memory-icon">
                            🎓
                        </div>

                        <div>

                            <div class="memory-title">
                                SHESPAT
                            </div>

                            <div class="memory-text">
                                Emprendiendo juntos.
                            </div>

                        </div>

                    </div>


                    <div class="memory">

                        <div class="memory-icon">
                            🏍️
                        </div>

                        <div>

                            <div class="memory-title">
                                La moto
                            </div>

                            <div class="memory-text">
                                Aprendiendo a manejar.
                            </div>

                        </div>

                    </div>


                    <div class="memory">

                        <div class="memory-icon">
                            💇
                        </div>

                        <div>

                            <div class="memory-title">
                                Mi cambio de look
                            </div>

                            <div class="memory-text">
                                Una nueva versión de mí.
                            </div>

                        </div>

                    </div>


                    <div class="memory">

                        <div class="memory-icon">
                            🎄
                        </div>

                        <div>

                            <div class="memory-title">
                                Nuestra primera Navidad
                            </div>

                            <div class="memory-text">
                                Creando una tradición propia.
                            </div>

                        </div>

                    </div>


                </div>


                <div
                    class="photo-frame"
                    id="year2024Photo"
                ></div>

            </div>

        </section>


        <!-- =================================================
             07
             ================================================= -->

        <section
            class="slide"
            data-theme="year2025"
        >

            <div class="content">

                <div class="eyebrow">
                    2025 · 2026
                </div>

                <h2 class="section-title">

                    Seguimos<br>
                    escribiendo

                </h2>


                <div class="memories">


                    <div class="memory">

                        <div class="memory-icon">
                            🎁
                        </div>

                        <div>

                            <div class="memory-title">
                                El reloj para mi papá
                            </div>

                            <div class="memory-text">
                                Otro recuerdo de nuestra historia.
                            </div>

                        </div>

                    </div>


                    <div class="memory">

                        <div class="memory-icon">
                            🐰
                        </div>

                        <div>

                            <div class="memory-title">
                                Carajo y Nena
                            </div>

                            <div class="memory-text">
                                Dos pequeños integrantes
                                de nuestra historia.
                            </div>

                        </div>

                    </div>


                    <div class="memory">

                        <div class="memory-icon">
                            🎡
                        </div>

                        <div>

                            <div class="memory-title">
                                La feria
                            </div>

                            <div class="memory-text">
                                Otra aventura juntos.
                            </div>

                        </div>

                    </div>


                </div>


                <div
                    class="photo-frame"
                    id="year2025Photo"
                ></div>

            </div>

        </section>


        <!-- =================================================
             08
             ================================================= -->

        <section
            class="slide"
            data-theme="food"
        >

            <div class="content">

                <div class="eyebrow">
                    FOOD · FOOD · FOOD 🍜
                </div>

                <h2 class="section-title">

                    Nuestros<br>
                    lugares

                </h2>

                <p class="section-text">

                    Porque una relación también
                    se construye alrededor de una mesa.

                </p>


                <div class="places">


                    <div class="place">

                        <div class="place-number">
                            01
                        </div>

                        <div class="place-name">
                            Ninja Ramen
                        </div>

                        <div class="place-description">
                            Uno de esos lugares que se volvieron
                            parte de nuestros momentos juntos.
                        </div>

                    </div>


                    <div class="place">

                        <div class="place-number">
                            02
                        </div>

                        <div class="place-name">
                            Ryu Ramen House
                        </div>

                        <div class="place-description">
                            Comida, plática y tiempo juntos.
                        </div>

                    </div>


                    <div class="place">

                        <div class="place-number">
                            03
                        </div>

                        <div class="place-name">
                            Trueke Comida & Amigos
                        </div>

                        <div class="place-description">
                            Otra pequeña aventura guardada
                            dentro de nuestra historia.
                        </div>

                    </div>


                </div>

            </div>

        </section>


        <!-- =================================================
             09
             ================================================= -->

        <section
            class="slide"
            data-theme="music"
        >

            <div class="content">

                <div class="eyebrow">
                    SOUNDTRACK 🎵
                </div>

                <h2 class="section-title">

                    Nuestra<br>
                    banda sonora

                </h2>

                <p class="section-text">

                    11 canciones que terminaron
                    formando parte de nuestra historia.

                </p>


                <div class="album"></div>


                <div class="featured-song">

                    <div class="song-number">
                        CANCIÓN #01
                    </div>

                    <div class="song-title">
                        Tiempo para Amarte
                    </div>

                    <div class="song-artist">
                        Laureano Brizuela
                    </div>

                    <div class="song-meaning">

                        A pesar de las cuentas,
                        el estrés diario y todas
                        las cosas que tenemos que hacer,
                        siempre quiero encontrar
                        tiempo para ti.

                    </div>

                </div>

            </div>

        </section>


        <!-- =================================================
             10
             ================================================= -->

        <section
            class="slide"
            data-theme="gallery"
        >

            <div class="content">

                <div class="eyebrow">
                    MEMORIES 📸
                </div>

                <h2 class="section-title">

                    Nuestros<br>
                    recuerdos

                </h2>


                <div
                    class="gallery-photo"
                    id="galleryPhoto"
                ></div>


                <div
                    id="galleryCaption"
                    class="section-text"
                ></div>

            </div>

        </section>


        <!-- =================================================
             11
             ================================================= -->

        <section
            class="slide"
            data-theme="final"
        >

            <div class="content">

                <div class="eyebrow">
                    Y ESTO APENAS ES UNA PARTE
                </div>


                <div class="final-title">

                    Gracias por<br>
                    estos 3 años ❤️

                </div>


                <div class="days-label">

                    Faltan aproximadamente

                </div>


                <div
                    class="days-number"
                    id="daysNumber"
                >
                    --
                </div>


                <div class="days-label">

                    días para nuestro próximo aniversario 💫

                </div>


                <div class="quote">

                    Y si pudiera volver al
                    24 de julio de 2023,
                    volvería a elegir comenzar
                    esta historia contigo.

                </div>

            </div>

        </section>


    </div>


    <!-- ======================================================
         CONTROL DE MÚSICA
         ====================================================== -->

    <button
        id="musicControl"
        type="button"
        aria-label="Música"
    >

        <div
            class="sound-bars"
            id="soundBars"
        >

            <div class="sound-bar"></div>
            <div class="sound-bar"></div>
            <div class="sound-bar"></div>

        </div>

    </button>


</div>


{AUDIO_HTML}


<script>

/* ============================================================
   DATOS
   ============================================================ */

const DATA =
    {DATOS_JSON};


/* ============================================================
   REFERENCIAS
   ============================================================ */

const app =
    document.getElementById(
        "app"
    );

const slides =
    Array.from(
        document.querySelectorAll(
            ".slide"
        )
    );

const progress =
    document.getElementById(
        "progress"
    );

const counter =
    document.getElementById(
        "counter"
    );

const background =
    document.getElementById(
        "background"
    );

const music =
    document.getElementById(
        "backgroundMusic"
    );

const musicControl =
    document.getElementById(
        "musicControl"
    );

const soundBars =
    document.getElementById(
        "soundBars"
    );


/* ============================================================
   ESTADO
   ============================================================ */

let current = 0;

let galleryIndex = 0;

let photoIndexes = {

    december:
        0,

    year2024:
        0,

    year2025:
        0

};


/* ============================================================
   TEMAS
   ============================================================ */

const themes = {

    cover:
        "radial-gradient(circle at 20% 15%, #ff2d75 0%, transparent 32%), radial-gradient(circle at 85% 80%, #7738ff 0%, transparent 38%), linear-gradient(145deg,#17040d,#08030c)",

    stats:
        "radial-gradient(circle at 20% 20%, #ff8a00 0%, transparent 30%), radial-gradient(circle at 90% 70%, #ff2d75 0%, transparent 35%), linear-gradient(145deg,#16080b,#09030b)",

    start:
        "radial-gradient(circle at 75% 15%, #ffbd3d 0%, transparent 30%), radial-gradient(circle at 20% 80%, #ff2d75 0%, transparent 35%), linear-gradient(145deg,#1a0c04,#0b0408)",

    concert:
        "radial-gradient(circle at 20% 25%, #7a38ff 0%, transparent 35%), radial-gradient(circle at 80% 80%, #ff2d75 0%, transparent 35%), linear-gradient(145deg,#0d061b,#08030c)",

    december:
        "radial-gradient(circle at 20% 15%, #00a6a6 0%, transparent 30%), radial-gradient(circle at 90% 80%, #ff2d75 0%, transparent 35%), linear-gradient(145deg,#041313,#09040c)",

    year2024:
        "radial-gradient(circle at 20% 15%, #ff2d75 0%, transparent 30%), radial-gradient(circle at 85% 25%, #ffbd3d 0%, transparent 32%), linear-gradient(145deg,#17040e,#09030b)",

    year2025:
        "radial-gradient(circle at 80% 20%, #9b52ff 0%, transparent 35%), radial-gradient(circle at 15% 85%, #ff2d75 0%, transparent 35%), linear-gradient(145deg,#0e0619,#08030c)",

    food:
        "radial-gradient(circle at 20% 20%, #ff8a00 0%, transparent 30%), radial-gradient(circle at 85% 85%, #ffd447 0%, transparent 30%), linear-gradient(145deg,#170903,#09040a)",

    music:
        "radial-gradient(circle at 20% 20%, #ff2d75 0%, transparent 35%), radial-gradient(circle at 85% 75%, #8c52ff 0%, transparent 38%), linear-gradient(145deg,#17051b,#08030d)",

    gallery:
        "radial-gradient(circle at 80% 20%, #00a6a6 0%, transparent 35%), radial-gradient(circle at 15% 80%, #ff2d75 0%, transparent 35%), linear-gradient(145deg,#031313,#08030c)",

    final:
        "radial-gradient(circle at 20% 20%, #ff2d75 0%, transparent 35%), radial-gradient(circle at 80% 80%, #8c52ff 0%, transparent 40%), linear-gradient(145deg,#17030e,#08030d)"

};


/* ============================================================
   PROGRESO
   ============================================================ */

function createProgress() {

    progress.innerHTML = "";

    slides.forEach(
        function () {

            const bar =
                document.createElement(
                    "div"
                );

            bar.className =
                "progress-bar";


            const fill =
                document.createElement(
                    "div"
                );

            fill.className =
                "progress-fill";


            bar.appendChild(
                fill
            );

            progress.appendChild(
                bar
            );

        }
    );

}


createProgress();


/* ============================================================
   FOTO
   ============================================================ */

function renderPhoto(
    elementId,
    image,
    caption
) {

    const element =
        document.getElementById(
            elementId
        );

    if (
        !element ||
        !image
    ) {
        return;
    }


    element.innerHTML = `

        <img
            src="${image}"
            draggable="false"
        >

        ${
            caption
            ?
            `
            <div class="photo-caption">
                ${caption}
            </div>
            `
            :
            ""
        }

    `;

}


/* ============================================================
   FOTOS PRINCIPALES
   ============================================================ */

if (
    DATA.imagenes.inicio
) {

    renderPhoto(
        "inicioPhoto",
        DATA.imagenes.inicio,
        "El comienzo de nosotros ❤️"
    );

}


if (
    DATA.imagenes.caifanes
) {

    renderPhoto(
        "caifanesPhoto",
        DATA.imagenes.caifanes,
        "Una noche para recordar 🎸❤️"
    );

}


/* ============================================================
   DICIEMBRE
   ============================================================ */

function renderDecember() {

    const images =
        DATA.imagenes.diciembre_2023 ||
        [];

    if (!images.length) {
        return;
    }


    const index =
        photoIndexes.december %
        images.length;


    renderPhoto(
        "decemberPhoto",
        images[index],
        DATA.captions
            .diciembre_2023[index]
    );

}


/* ============================================================
   2024
   ============================================================ */

function render2024() {

    const images =
        DATA.imagenes.y2024 ||
        [];

    if (!images.length) {
        return;
    }


    const index =
        photoIndexes.year2024 %
        images.length;


    renderPhoto(
        "year2024Photo",
        images[index],
        DATA.captions
            .y2024[index]
    );

}


/* ============================================================
   2025 / 2026
   ============================================================ */

function render2025() {

    const images =
        DATA.imagenes.y2025_2026 ||
        [];

    if (!images.length) {
        return;
    }


    const index =
        photoIndexes.year2025 %
        images.length;


    renderPhoto(
        "year2025Photo",
        images[index],
        DATA.captions
            .y2025_2026[index]
    );

}


/* ============================================================
   GALERÍA
   ============================================================ */

function renderGallery() {

    const images =
        DATA.imagenes.galeria ||
        [];

    const photo =
        document.getElementById(
            "galleryPhoto"
        );

    const caption =
        document.getElementById(
            "galleryCaption"
        );


    if (
        !photo ||
        !caption
    ) {
        return;
    }


    if (!images.length) {

        photo.innerHTML = "";

        caption.textContent =
            "Agrega fotografías a fotos/galeria";

        return;

    }


    const index =
        galleryIndex %
        images.length;


    photo.innerHTML = `

        <img
            src="${images[index]}"
            draggable="false"
        >

    `;


    caption.textContent =
        "Recuerdo " +
        (index + 1) +
        " de " +
        images.length;

}


/* ============================================================
   DÍAS
   ============================================================ */

function updateDays() {

    const now =
        new Date();


    let year =
        now.getFullYear();


    let anniversary =
        new Date(
            year,
            8,
            23
        );


    if (
        anniversary <= now
    ) {

        anniversary =
            new Date(
                year + 1,
                8,
                23
            );

    }


    const difference =
        anniversary - now;


    const days =
        Math.ceil(
            difference /
            (
                1000 *
                60 *
                60 *
                24
            )
        );


    const element =
        document.getElementById(
            "daysNumber"
        );


    if (element) {

        element.textContent =
            days;

    }

}


updateDays();


/* ============================================================
   MOSTRAR SLIDE
   ============================================================ */

function showSlide(
    index,
    direction
) {

    if (
        index < 0 ||
        index >= slides.length
    ) {
        return;
    }


    if (
        index === current
    ) {
        return;
    }


    const oldSlide =
        slides[current];

    const newSlide =
        slides[index];


    oldSlide.classList.remove(
        "active"
    );


    oldSlide.classList.remove(
        "previous"
    );


    if (
        direction < 0
    ) {

        oldSlide.classList.add(
            "previous"
        );

    }


    newSlide.classList.remove(
        "previous"
    );


    newSlide.classList.add(
        "active"
    );


    current =
        index;


    const theme =
        newSlide.dataset.theme;


    if (
        background &&
        themes[theme]
    ) {

        background.style.background =
            themes[theme];

    }


    counter.textContent =
        String(
            current + 1
        ).padStart(
            2,
            "0"
        )
        +
        " / "
        +
        String(
            slides.length
        ).padStart(
            2,
            "0"
        );


    const bars =
        document.querySelectorAll(
            ".progress-fill"
        );


    bars.forEach(
        function (bar, i) {

            if (
                i <= current
            ) {

                bar.style.width =
                    "100%";

            }
            else {

                bar.style.width =
                    "0%";

            }

        }
    );


    if (
        current === 4
    ) {

        renderDecember();

    }


    if (
        current === 5
    ) {

        render2024();

    }


    if (
        current === 6
    ) {

        render2025();

    }


    if (
        current === 9
    ) {

        renderGallery();

    }

}


/* ============================================================
   INICIO
   ============================================================ */

background.style.background =
    themes.cover;


const firstBar =
    document.querySelector(
        ".progress-fill"
    );


if (firstBar) {

    firstBar.style.width =
        "100%";

}


renderDecember();
render2024();
render2025();
renderGallery();


/* ============================================================
   NAVEGACIÓN
   ============================================================ */

function nextSlide() {

    if (
        current <
        slides.length - 1
    ) {

        showSlide(
            current + 1,
            1
        );

    }

}


function previousSlide() {

    if (
        current > 0
    ) {

        showSlide(
            current - 1,
            -1
        );

    }

}


/* ============================================================
   SWIPE
   ============================================================ */

let touchStartX = 0;

let touchStartY = 0;

let touching = false;


app.addEventListener(
    "touchstart",
    function (event) {

        if (
            !event.touches.length
        ) {
            return;
        }


        touchStartX =
            event.touches[0].clientX;

        touchStartY =
            event.touches[0].clientY;

        touching =
            true;


        event.preventDefault();

    },
    {
        passive: false
    }
);


app.addEventListener(
    "touchmove",
    function (event) {

        if (!touching) {
            return;
        }


        /*
         * MUY IMPORTANTE:
         *
         * evita que Android/Chrome
         * interprete el gesto como
         * navegación de la página.
         */

        event.preventDefault();

    },
    {
        passive: false
    }
);


app.addEventListener(
    "touchend",
    function (event) {

        if (!touching) {
            return;
        }


        touching =
            false;


        const touch =
            event.changedTouches[0];


        const endX =
            touch.clientX;

        const endY =
            touch.clientY;


        const deltaX =
            endX -
            touchStartX;


        const deltaY =
            endY -
            touchStartY;


        event.preventDefault();


        /*
         * Ignorar movimientos verticales.
         */

        if (
            Math.abs(deltaX) <
            45
        ) {
            return;
        }


        if (
            Math.abs(deltaX) <=
            Math.abs(deltaY)
        ) {
            return;
        }


        /*
         * IZQUIERDA
         * = SIGUIENTE
         */

        if (
            deltaX < 0
        ) {

            nextSlide();

        }


        /*
         * DERECHA
         * = ANTERIOR
         */

        else {

            previousSlide();

        }

    },
    {
        passive: false
    }
);


/* ============================================================
   TAP
   ============================================================ */

app.addEventListener(
    "click",
    function (event) {

        if (
            event.target.closest(
                "#musicControl"
            )
        ) {

            return;

        }


        if (
            window.innerWidth >=
            800
        ) {

            if (
                event.clientX <
                window.innerWidth / 2
            ) {

                previousSlide();

            }
            else {

                nextSlide();

            }

        }

    }
);


/* ============================================================
   TECLADO
   ============================================================ */

document.addEventListener(
    "keydown",
    function (event) {

        if (
            event.key ===
            "ArrowRight"
        ) {

            nextSlide();

        }


        if (
            event.key ===
            "ArrowLeft"
        ) {

            previousSlide();

        }


        if (
            event.key ===
            " "
        ) {

            event.preventDefault();

            nextSlide();

        }

    }
);


/* ============================================================
   CAMBIO AUTOMÁTICO DE FOTOS
   ============================================================ */

setInterval(
    function () {


        if (
            current === 4
        ) {

            const images =
                DATA.imagenes
                    .diciembre_2023 ||
                [];

            if (
                images.length > 1
            ) {

                photoIndexes.december =
                    (
                        photoIndexes.december +
                        1
                    ) %
                    images.length;


                renderDecember();

            }

        }


        if (
            current === 5
        ) {

            const images =
                DATA.imagenes.y2024 ||
                [];

            if (
                images.length > 1
            ) {

                photoIndexes.year2024 =
                    (
                        photoIndexes.year2024 +
                        1
                    ) %
                    images.length;


                render2024();

            }

        }


        if (
            current === 6
        ) {

            const images =
                DATA.imagenes
                    .y2025_2026 ||
                [];

            if (
                images.length > 1
            ) {

                photoIndexes.year2025 =
                    (
                        photoIndexes.year2025 +
                        1
                    ) %
                    images.length;


                render2025();

            }

        }


        if (
            current === 9
        ) {

            const images =
                DATA.imagenes.galeria ||
                [];

            if (
                images.length > 1
            ) {

                galleryIndex =
                    (
                        galleryIndex +
                        1
                    ) %
                    images.length;


                renderGallery();

            }

        }


    },
    5000
);


/* ============================================================
   MÚSICA
   ============================================================ */

let musicStarted =
    false;


function startMusic() {

    if (
        !music ||
        musicStarted
    ) {

        return;

    }


    music.play()
        .then(
            function () {

                musicStarted =
                    true;


                if (soundBars) {

                    soundBars.classList.add(
                        "music-playing"
                    );

                }

            }
        )
        .catch(
            function () {

                /*
                 * Chrome/Android puede bloquear
                 * autoplay hasta una interacción.
                 */

            }
        );

}


app.addEventListener(
    "touchstart",
    startMusic,
    {
        once: true,
        passive: true
    }
);


app.addEventListener(
    "click",
    startMusic,
    {
        once: true
    }
);


/* ============================================================
   CONTROL DE MÚSICA
   ============================================================ */

if (musicControl) {

    musicControl.addEventListener(
        "click",
        function (event) {

            event.stopPropagation();


            if (!music) {
                return;
            }


            if (
                music.paused
            ) {

                music.play()
                    .then(
                        function () {

                            if (
                                soundBars
                            ) {

                                soundBars.classList.add(
                                    "music-playing"
                                );

                            }

                        }
                    )
                    .catch(
                        function () {}
                    );

            }

            else {

                music.pause();


                if (
                    soundBars
                ) {

                    soundBars.classList.remove(
                        "music-playing"
                    );

                }

            }

        }
    );

}

</script>


<!-- ========================================================
     FULLSCREEN REAL PARA STREAMLIT
     ======================================================== -->

<script>

(function () {


    /*
     * Esta parte es la importante para que el Wrapped
     * deje de parecer una página dentro de otra página.
     */

    setTimeout(
        function () {

            try {


                /* =============================================
                   DOCUMENTO PADRE
                   ============================================= */

                const parentDoc =
                    window.parent.document;


                const parentBody =
                    parentDoc.body;


                const originalApp =
                    document.getElementById(
                        "app"
                    );


                if (!originalApp) {
                    return;
                }


                /* =============================================
                   EVITAR DUPLICADOS
                   ============================================= */

                const previous =
                    parentDoc.getElementById(
                        "wrappedFullscreen"
                    );


                if (previous) {

                    previous.remove();

                }


                const previousStyle =
                    parentDoc.getElementById(
                        "wrappedFullscreenStyle"
                    );


                if (previousStyle) {

                    previousStyle.remove();

                }


                /* =============================================
                   COPIAR ESTILOS
                   ============================================= */

                const styles =
                    document.querySelectorAll(
                        "style"
                    );


                let css =
                    "";


                styles.forEach(
                    function (style) {

                        css +=
                            style.textContent +
                            "\n";

                    }
                );


                const style =
                    parentDoc.createElement(
                        "style"
                    );


                style.id =
                    "wrappedFullscreenStyle";


                style.textContent = `

                    ${css}

                    html,
                    body {

                        margin:
                            0 !important;

                        padding:
                            0 !important;

                        width:
                            100% !important;

                        height:
                            100% !important;

                        overflow:
                            hidden !important;

                        background:
                            #07030b !important;

                    }


                    header,
                    [data-testid="stHeader"],
                    [data-testid="stToolbar"],
                    [data-testid="stDecoration"],
                    #MainMenu,
                    footer {

                        display:
                            none !important;

                    }


                    [data-testid="stAppViewContainer"],
                    [data-testid="stAppViewContainer"] > div,
                    [data-testid="stAppViewContainer"] .main,
                    [data-testid="stAppViewContainer"] .block-container {

                        margin:
                            0 !important;

                        padding:
                            0 !important;

                        max-width:
                            none !important;

                        width:
                            100% !important;

                    }


                    #wrappedFullscreen {

                        position:
                            fixed !important;

                        inset:
                            0 !important;

                        width:
                            100vw !important;

                        height:
                            100dvh !important;

                        z-index:
                            2147483647 !important;

                        overflow:
                            hidden !important;

                        background:
                            #07030b !important;

                    }


                    #wrappedFullscreen #app {

                        position:
                            fixed !important;

                        inset:
                            0 !important;

                        width:
                            100vw !important;

                        height:
                            100dvh !important;

                    }

                `;


                parentDoc.head.appendChild(
                    style
                );


                /* =============================================
                   CREAR CONTENEDOR FULLSCREEN
                   ============================================= */

                const fullscreen =
                    parentDoc.createElement(
                        "div"
                    );


                fullscreen.id =
                    "wrappedFullscreen";


                /* =============================================
                   CLONAR WRAPPED
                   ============================================= */

                const clonedApp =
                    originalApp.cloneNode(
                        true
                    );


                fullscreen.appendChild(
                    clonedApp
                );


                /* =============================================
                   CLONAR AUDIO
                   ============================================= */

                const originalAudio =
                    document.getElementById(
                        "backgroundMusic"
                    );


                if (originalAudio) {

                    const clonedAudio =
                        originalAudio.cloneNode(
                            true
                        );


                    clonedAudio.id =
                        "backgroundMusic";


                    fullscreen.appendChild(
                        clonedAudio
                    );

                }


                parentBody.appendChild(
                    fullscreen
                );


                /* =============================================
                   OCULTAR EL IFRAME
                   ============================================= */

                const frame =
                    window.frameElement;


                if (frame) {

                    const frameParent =
                        frame.parentElement;


                    if (
                        frameParent
                    ) {

                        frameParent.style.display =
                            "none";

                        frameParent.style.width =
                            "0";

                        frameParent.style.height =
                            "0";

                        frameParent.style.overflow =
                            "hidden";

                    }

                }


                /* =============================================
                   BLOQUEAR SCROLL DEL PADRE
                   ============================================= */

                parentDoc.documentElement.style.overflow =
                    "hidden";


                parentBody.style.overflow =
                    "hidden";


                /* =============================================
                   RECONECTAR CONTROLES
                   ============================================= */

                const app =
                    fullscreen.querySelector(
                        "#app"
                    );


                const slides =
                    Array.from(
                        app.querySelectorAll(
                            ".slide"
                        )
                    );


                const progress =
                    app.querySelector(
                        "#progress"
                    );


                const counter =
                    app.querySelector(
                        "#counter"
                    );


                const background =
                    app.querySelector(
                        "#background"
                    );


                const music =
                    fullscreen.querySelector(
                        "#backgroundMusic"
                    );


                const musicControl =
                    app.querySelector(
                        "#musicControl"
                    );


                const soundBars =
                    app.querySelector(
                        "#soundBars"
                    );


                /* =============================================
                   ESTADO
                   ============================================= */

                let current = 0;

                let startX = 0;

                let startY = 0;

                let touching = false;


                /* =============================================
                   TEMAS
                   ============================================= */

                const themes = {

                    cover:
                        "radial-gradient(circle at 20% 15%, #ff2d75 0%, transparent 32%), radial-gradient(circle at 85% 80%, #7738ff 0%, transparent 38%), linear-gradient(145deg,#17040d,#08030c)",

                    stats:
                        "radial-gradient(circle at 20% 20%, #ff8a00 0%, transparent 30%), radial-gradient(circle at 90% 70%, #ff2d75 0%, transparent 35%), linear-gradient(145deg,#16080b,#09030b)",

                    start:
                        "radial-gradient(circle at 75% 15%, #ffbd3d 0%, transparent 30%), radial-gradient(circle at 20% 80%, #ff2d75 0%, transparent 35%), linear-gradient(145deg,#1a0c04,#0b0408)",

                    concert:
                        "radial-gradient(circle at 20% 25%, #7a38ff 0%, transparent 35%), radial-gradient(circle at 80% 80%, #ff2d75 0%, transparent 35%), linear-gradient(145deg,#0d061b,#08030c)",

                    december:
                        "radial-gradient(circle at 20% 15%, #00a6a6 0%, transparent 30%), radial-gradient(circle at 90% 80%, #ff2d75 0%, transparent 35%), linear-gradient(145deg,#041313,#09040c)",

                    year2024:
                        "radial-gradient(circle at 20% 15%, #ff2d75 0%, transparent 30%), radial-gradient(circle at 85% 25%, #ffbd3d 0%, transparent 32%), linear-gradient(145deg,#17040e,#09030b)",

                    year2025:
                        "radial-gradient(circle at 80% 20%, #9b52ff 0%, transparent 35%), radial-gradient(circle at 15% 85%, #ff2d75 0%, transparent 35%), linear-gradient(145deg,#0e0619,#08030c)",

                    food:
                        "radial-gradient(circle at 20% 20%, #ff8a00 0%, transparent 30%), radial-gradient(circle at 85% 85%, #ffd447 0%, transparent 30%), linear-gradient(145deg,#170903,#09040a)",

                    music:
                        "radial-gradient(circle at 20% 20%, #ff2d75 0%, transparent 35%), radial-gradient(circle at 85% 75%, #8c52ff 0%, transparent 38%), linear-gradient(145deg,#17051b,#08030d)",

                    gallery:
                        "radial-gradient(circle at 80% 20%, #00a6a6 0%, transparent 35%), radial-gradient(circle at 15% 80%, #ff2d75 0%, transparent 35%), linear-gradient(145deg,#031313,#08030c)",

                    final:
                        "radial-gradient(circle at 20% 20%, #ff2d75 0%, transparent 35%), radial-gradient(circle at 80% 80%, #8c52ff 0%, transparent 40%), linear-gradient(145deg,#17030e,#08030d)"

                };


                /* =============================================
                   SLIDE
                   ============================================= */

                function showSlide(
                    index,
                    direction
                ) {

                    if (
                        index < 0 ||
                        index >= slides.length
                    ) {

                        return;

                    }


                    if (
                        index === current
                    ) {

                        return;

                    }


                    const oldSlide =
                        slides[current];


                    const newSlide =
                        slides[index];


                    oldSlide.classList.remove(
                        "active"
                    );


                    oldSlide.classList.remove(
                        "previous"
                    );


                    if (
                        direction < 0
                    ) {

                        oldSlide.classList.add(
                            "previous"
                        );

                    }


                    newSlide.classList.add(
                        "active"
                    );


                    current =
                        index;


                    const theme =
                        newSlide.dataset.theme;


                    if (
                        background &&
                        themes[theme]
                    ) {

                        background.style.background =
                            themes[theme];

                    }


                    if (counter) {

                        counter.textContent =
                            String(
                                current + 1
                            ).padStart(
                                2,
                                "0"
                            )
                            +
                            " / "
                            +
                            String(
                                slides.length
                            ).padStart(
                                2,
                                "0"
                            );

                    }


                    const bars =
                        progress.querySelectorAll(
                            ".progress-fill"
                        );


                    bars.forEach(
                        function (
                            bar,
                            i
                        ) {

                            bar.style.width =
                                i <= current
                                ? "100%"
                                : "0%";

                        }
                    );

                }


                /* =============================================
                   SIGUIENTE / ANTERIOR
                   ============================================= */

                function next() {

                    if (
                        current <
                        slides.length - 1
                    ) {

                        showSlide(
                            current + 1,
                            1
                        );

                    }

                }


                function previous() {

                    if (
                        current > 0
                    ) {

                        showSlide(
                            current - 1,
                            -1
                        );

                    }

                }


                /* =============================================
                   INICIALIZAR
                   ============================================= */

                if (background) {

                    background.style.background =
                        themes.cover;

                }


                const first =
                    progress.querySelector(
                        ".progress-fill"
                    );


                if (first) {

                    first.style.width =
                        "100%";

                }


                /* =============================================
                   SWIPE
                   ============================================= */

                app.addEventListener(
                    "touchstart",
                    function (event) {

                        if (
                            !event.touches.length
                        ) {

                            return;

                        }


                        startX =
                            event.touches[0].clientX;


                        startY =
                            event.touches[0].clientY;


                        touching =
                            true;


                        event.preventDefault();

                    },
                    {
                        passive:
                            false
                    }
                );


                app.addEventListener(
                    "touchmove",
                    function (event) {

                        if (
                            !touching
                        ) {

                            return;

                        }


                        /*
                         * Esta línea es la clave:
                         * Chrome no desplaza la página.
                         */

                        event.preventDefault();

                    },
                    {
                        passive:
                            false
                    }
                );


                app.addEventListener(
                    "touchend",
                    function (event) {

                        if (
                            !touching
                        ) {

                            return;

                        }


                        touching =
                            false;


                        const touch =
                            event.changedTouches[0];


                        const deltaX =
                            touch.clientX -
                            startX;


                        const deltaY =
                            touch.clientY -
                            startY;


                        event.preventDefault();


                        if (
                            Math.abs(deltaX) <
                            45
                        ) {

                            return;

                        }


                        if (
                            Math.abs(deltaX) <=
                            Math.abs(deltaY)
                        ) {

                            return;

                        }


                        if (
                            deltaX < 0
                        ) {

                            next();

                        }
                        else {

                            previous();

                        }

                    },
                    {
                        passive:
                            false
                    }
                );


                /* =============================================
                   TAP
                   ============================================= */

                app.addEventListener(
                    "click",
                    function (event) {

                        if (
                            event.target.closest(
                                "#musicControl"
                            )
                        ) {

                            return;

                        }


                        if (
                            window.innerWidth <
                            800
                        ) {

                            if (
                                event.clientX <
                                window.innerWidth *
                                0.35
                            ) {

                                previous();

                            }
                            else {

                                next();

                            }

                        }
                        else {

                            if (
                                event.clientX <
                                window.innerWidth /
                                2
                            ) {

                                previous();

                            }
                            else {

                                next();

                            }

                        }

                    }
                );


                /* =============================================
                   TECLADO
                   ============================================= */

                parentDoc.addEventListener(
                    "keydown",
                    function (event) {

                        if (
                            event.key ===
                            "ArrowRight"
                        ) {

                            next();

                        }


                        if (
                            event.key ===
                            "ArrowLeft"
                        ) {

                            previous();

                        }


                        if (
                            event.key ===
                            " "
                        ) {

                            event.preventDefault();

                            next();

                        }

                    }
                );


                /* =============================================
                   MÚSICA
                   ============================================= */

                if (
                    music &&
                    musicControl
                ) {

                    musicControl.addEventListener(
                        "click",
                        function (event) {

                            event.stopPropagation();


                            if (
                                music.paused
                            ) {

                                music.play()
                                    .then(
                                        function () {

                                            if (
                                                soundBars
                                            ) {

                                                soundBars.classList.add(
                                                    "music-playing"
                                                );

                                            }

                                        }
                                    )
                                    .catch(
                                        function () {}
                                    );

                            }
                            else {

                                music.pause();


                                if (
                                    soundBars
                                ) {

                                    soundBars.classList.remove(
                                        "music-playing"
                                    );

                                }

                            }

                        }
                    );

                }


                /*
                 * Primera interacción:
                 * intentar comenzar música.
                 */

                let started =
                    false;


                function startMusic() {

                    if (
                        !music ||
                        started
                    ) {

                        return;

                    }


                    music.play()
                        .then(
                            function () {

                                started =
                                    true;


                                if (
                                    soundBars
                                ) {

                                    soundBars.classList.add(
                                        "music-playing"
                                    );

                                }

                            }
                        )
                        .catch(
                            function () {}
                        );

                }


                app.addEventListener(
                    "touchstart",
                    startMusic,
                    {
                        once:
                            true,
                        passive:
                            true
                    }
                );


                app.addEventListener(
                    "click",
                    startMusic,
                    {
                        once:
                            true
                    }
                );


            }
            catch (error) {

                console.error(
                    "Wrapped fullscreen:",
                    error
                );

            }

        },
        250
    );

})();

</script>


</body>

</html>

"""


# ============================================================
# RENDER STREAMLIT
# ============================================================
#
# El iframe original solamente sirve como "puente".
# El Wrapped se copia a la ventana principal y ocupa
# todo el viewport.
#

components.html(
    HTML,
    height=1,
    scrolling=False
)
