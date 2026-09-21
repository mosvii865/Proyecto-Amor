
import os
import base64
import json
import html
import datetime

import streamlit as st
import streamlit.components.v1 as components


# ============================================================
# CONFIGURACIÓN
# ============================================================

st.set_page_config(
    page_title="Nuestro Wrapped 💫",
    page_icon="💖",
    layout="wide",
    initial_sidebar_state="collapsed",
)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

FOTOS_DIR = os.path.join(BASE_DIR, "fotos")
GALERIA_DIR = os.path.join(FOTOS_DIR, "galeria")

# Música directamente dentro de Main
MUSICA_FONDO = os.path.join(BASE_DIR, "musica.mp3")


# ============================================================
# UTILIDADES
# ============================================================

def archivo_base64(ruta):
    """
    Convierte una imagen/audio en base64 para que todo el
    Wrapped funcione dentro de un único componente HTML.
    """

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
    extension = os.path.splitext(ruta)[1].lower()

    return {
        ".png": "image/png",
        ".jpg": "image/jpeg",
        ".jpeg": "image/jpeg",
        ".webp": "image/webp",
    }.get(extension, "image/png")


def imagen_data(ruta):
    data = archivo_base64(ruta)

    if not data:
        return None

    return f"data:{mime_imagen(ruta)};base64,{data}"


def esc(texto):
    return html.escape(str(texto))


# ============================================================
# FOTOGRAFÍAS
# ============================================================

FOTOS = {
    "inicio": os.path.join(
        FOTOS_DIR,
        "image_0.png"
    ),

    "caifanes": os.path.join(
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
# TEXTOS DE FOTOS
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
        "Mi cambio de look, gracias a ti 💇",
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
        "titulo": "Tiempo para Amarte",
        "artista": "Laureano Brizuela",
        "significado":
            "A pesar de las cuentas, el estrés diario y todas las cosas "
            "que tenemos que hacer, siempre quiero encontrar tiempo para ti.",
    },

    {
        "titulo":
            "My One and Only Love / They Say It's Wonderful",
        "artista":
            "John Coltrane",
        "significado":
            "Mi descubrimiento personal del amor y una canción que terminó "
            "teniendo un significado muy especial para nosotros.",
    },

    {
        "titulo":
            "I Only Have Eyes for You",
        "artista":
            "Louis Armstrong",
        "significado":
            "Porque entre todas las personas, lugares y cosas que existen, "
            "mis ojos siempre terminan buscándote a ti.",
    },

    {
        "titulo":
            "Eso y Más",
        "artista":
            "Joan Sebastián",
        "significado":
            "Una canción que representa todo eso que siento y muchas veces "
            "no sé cómo decirte.",
    },

    {
        "titulo":
            "Diséñame",
        "artista":
            "Joan Sebastián",
        "significado":
            "Porque de alguna manera nuestro amor fue construyéndose "
            "poco a poco, con nuestras propias historias.",
    },

    {
        "titulo":
            "The Nearness of You",
        "artista":
            "Ella Fitzgerald & Louis Armstrong",
        "significado":
            "La cercanía de la persona que amas puede hacer que cualquier "
            "momento cotidiano se sienta especial.",
    },

    {
        "titulo":
            "Only You",
        "artista":
            "The Platters",
        "significado":
            "Porque hay personas que simplemente se vuelven únicas "
            "en nuestra vida.",
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
            "Porque después de estos años, eres una parte enorme "
            "de mi mundo.",
    },

    {
        "titulo":
            "Cama y Mesa",
        "artista":
            "Roberto Carlos",
        "significado":
            "Una canción que habla de compartir la vida, los momentos "
            "íntimos y también los cotidianos.",
    },

    {
        "titulo":
            "Invítame un cigarro",
        "artista":
            "Tradicional / Popular",
        "significado":
            "Una de esas canciones que terminan formando parte "
            "de nuestra historia.",
    },
]


# ============================================================
# RESTAURANTES
# ============================================================

RESTAURANTES = [

    {
        "nombre": "Ninja Ramen",
        "descripcion":
            "Uno de esos lugares que se volvieron parte de nuestros "
            "momentos juntos.",
    },

    {
        "nombre": "Ryu Ramen House",
        "descripcion":
            "Comida, plática y tiempo juntos. Porque hasta salir a comer "
            "puede convertirse en un recuerdo.",
    },

    {
        "nombre": "Trueke Comida & Amigos",
        "descripcion":
            "Otro lugar que quedó guardado dentro de nuestras pequeñas "
            "aventuras.",
    },
]


# ============================================================
# GALERÍA
# ============================================================

def obtener_galeria():

    if not os.path.exists(GALERIA_DIR):
        return []

    extensiones = (
        ".png",
        ".jpg",
        ".jpeg",
        ".webp",
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
# PREPARAR IMÁGENES PARA JAVASCRIPT
# ============================================================

def preparar_imagenes():

    imagenes = {}

    portada = os.path.join(
        FOTOS_DIR,
        "portada.png"
    )

    if os.path.exists(portada):

        imagenes["portada"] = imagen_data(
            portada
        )

    for nombre, valor in FOTOS.items():

        if isinstance(valor, list):

            imagenes[nombre] = []

            for ruta in valor:

                data = imagen_data(ruta)

                if data:
                    imagenes[nombre].append(data)

        else:

            data = imagen_data(valor)

            if data:
                imagenes[nombre] = data

    imagenes["galeria"] = []

    for ruta in obtener_galeria():

        data = imagen_data(ruta)

        if data:
            imagenes["galeria"].append(data)

    return imagenes


IMAGENES = preparar_imagenes()


# ============================================================
# MÚSICA
# ============================================================

MUSICA_B64 = archivo_base64(
    MUSICA_FONDO
)


# ============================================================
# DATOS PARA JAVASCRIPT
# ============================================================

datos_js = {
    "imagenes": IMAGENES,
    "canciones": CANCIONES,
    "restaurantes": RESTAURANTES,
    "captions": CAPTIONS,
}

DATOS_JSON = json.dumps(
    datos_js,
    ensure_ascii=False
)


# ============================================================
# HTML COMPLETO
# ============================================================

audio_html = ""

if MUSICA_B64:

    audio_html = f"""
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

<title>
Nuestro Wrapped
</title>


<style>

/* ==========================================================
   FUENTES
   ========================================================== */

@import url(
'https://fonts.googleapis.com/css2?family=Manrope:wght@400;500;600;700;800&family=Unbounded:wght@400;500;600;700;800&display=swap'
);


/* ==========================================================
   RESET
   ========================================================== */

* {{
    box-sizing: border-box;
    -webkit-tap-highlight-color: transparent;
}}


html,
body {{

    width: 100%;
    height: 100%;

    margin: 0;
    padding: 0;

    overflow: hidden;

    background: #07030b;

    font-family:
        'Manrope',
        sans-serif;

    color: white;

    touch-action:
        manipulation;

}}


body {{

    overscroll-behavior:
        none;

}}


/* ==========================================================
   APP
   ========================================================== */

#app {{

    position: fixed;

    inset: 0;

    width: 100vw;
    height: 100dvh;

    overflow: hidden;

    background: #07030b;

}}


/* ==========================================================
   FONDO DINÁMICO
   ========================================================== */

#background {{

    position: absolute;

    inset: -10%;

    z-index: 0;

    transition:
        background
        0.8s ease,
        transform
        1.2s ease;

}}


#background::before {{

    content: "";

    position: absolute;

    width: 70vw;
    height: 70vw;

    max-width: 800px;
    max-height: 800px;

    border-radius: 50%;

    left: -25%;
    top: -15%;

    background:
        radial-gradient(
            circle,
            rgba(255,255,255,.12),
            transparent 68%
        );

    filter: blur(15px);

    animation:
        floatOne
        10s
        ease-in-out
        infinite;

}}


#background::after {{

    content: "";

    position: absolute;

    width: 65vw;
    height: 65vw;

    max-width: 750px;
    max-height: 750px;

    border-radius: 50%;

    right: -25%;
    bottom: -15%;

    background:
        radial-gradient(
            circle,
            rgba(255,255,255,.10),
            transparent 68%
        );

    filter: blur(20px);

    animation:
        floatTwo
        12s
        ease-in-out
        infinite;

}}


@keyframes floatOne {{

    0%,
    100% {{
        transform:
            translate3d(0,0,0)
            scale(1);
    }}

    50% {{
        transform:
            translate3d(30px,40px,0)
            scale(1.1);
    }}

}}


@keyframes floatTwo {{

    0%,
    100% {{
        transform:
            translate3d(0,0,0)
            scale(1);
    }}

    50% {{
        transform:
            translate3d(-35px,-25px,0)
            scale(1.08);
    }}

}}


/* ==========================================================
   GRANO
   ========================================================== */

#grain {{

    position: absolute;

    inset: 0;

    z-index: 30;

    pointer-events: none;

    opacity: .07;

    background-image:
        url("data:image/svg+xml,%3Csvg viewBox='0 0 180 180' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='.9' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)' opacity='.8'/%3E%3C/svg%3E");

}}


/* ==========================================================
   PROGRESO
   ========================================================== */

#progress {{

    position: absolute;

    z-index: 50;

    top:
        max(
            12px,
            env(safe-area-inset-top)
        );

    left: 12px;
    right: 12px;

    display: flex;

    gap: 4px;

}}


.progress-bar {{

    height: 3px;

    flex: 1;

    border-radius: 999px;

    overflow: hidden;

    background:
        rgba(255,255,255,.22);

}}


.progress-fill {{

    width: 0%;

    height: 100%;

    background:
        rgba(255,255,255,.95);

    border-radius: inherit;

    transition:
        width .25s linear;

}}


/* ==========================================================
   CONTADOR
   ========================================================== */

#counter {{

    position: absolute;

    z-index: 50;

    top:
        calc(
            max(
                12px,
                env(safe-area-inset-top)
            ) + 14px
        );

    right: 16px;

    font-size: 9px;

    letter-spacing: .15em;

    font-weight: 800;

    color:
        rgba(255,255,255,.6);

}}


/* ==========================================================
   SLIDES
   ========================================================== */

#slides {{

    position: relative;

    z-index: 10;

    width: 100%;
    height: 100%;

}}


.slide {{

    position: absolute;

    inset: 0;

    display: flex;

    flex-direction: column;

    justify-content: center;

    align-items: center;

    padding:
        65px
        clamp(20px, 5vw, 70px)
        calc(
            55px +
            env(safe-area-inset-bottom)
        );

    opacity: 0;

    pointer-events: none;

    transform:
        translateX(70px)
        scale(.96);

    transition:
        opacity .55s cubic-bezier(.2,.8,.2,1),
        transform .65s cubic-bezier(.2,.8,.2,1);

    overflow: hidden;

}}


.slide.active {{

    opacity: 1;

    pointer-events: auto;

    transform:
        translateX(0)
        scale(1);

}}


.slide.previous {{

    transform:
        translateX(-70px)
        scale(.96);

}}


/* ==========================================================
   CONTENIDO
   ========================================================== */

.content {{

    width: 100%;

    max-width: 850px;

    height: 100%;

    display: flex;

    flex-direction: column;

    justify-content: center;

    align-items: center;

    text-align: center;

    overflow-y: auto;

    scrollbar-width: none;

}}


.content::-webkit-scrollbar {{
    display: none;
}}


/* ==========================================================
   TIPOGRAFÍA
   ========================================================== */

.eyebrow {{

    font-size:
        clamp(9px, 2.3vw, 12px);

    letter-spacing:
        .24em;

    text-transform:
        uppercase;

    font-weight: 800;

    color:
        rgba(255,255,255,.68);

    margin-bottom: 14px;

}}


.title {{

    font-family:
        'Unbounded',
        sans-serif;

    font-size:
        clamp(
            2.5rem,
            12vw,
            7rem
        );

    line-height:
        .98;

    letter-spacing:
        -.075em;

    font-weight: 800;

    margin: 0;

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


.subtitle {{

    max-width:
        580px;

    margin-top:
        22px;

    color:
        rgba(255,255,255,.72);

    font-size:
        clamp(
            .88rem,
            3vw,
            1.1rem
        );

    line-height:
        1.75;

}}


.section-title {{

    font-family:
        'Unbounded',
        sans-serif;

    font-size:
        clamp(
            1.8rem,
            8vw,
            4.8rem
        );

    line-height:
        1.05;

    letter-spacing:
        -.065em;

    font-weight:
        800;

    margin:
        0;

}}


.section-text {{

    color:
        rgba(255,255,255,.65);

    max-width:
        600px;

    line-height:
        1.75;

    margin-top:
        16px;

}}


/* ==========================================================
   BOTÓN INVISIBLE / TAP
   ========================================================== */

.tap-hint {{

    position:
        absolute;

    bottom:
        calc(
            20px +
            env(safe-area-inset-bottom)
        );

    left: 50%;

    transform:
        translateX(-50%);

    font-size:
        9px;

    letter-spacing:
        .18em;

    color:
        rgba(255,255,255,.35);

    text-transform:
        uppercase;

}}


/* ==========================================================
   PORTADA
   ========================================================== */

.cover-number {{

    font-family:
        'Unbounded',
        sans-serif;

    font-size:
        clamp(
            6rem,
            30vw,
            15rem
        );

    line-height:
        .7;

    font-weight:
        800;

    letter-spacing:
        -.12em;

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

    opacity:
        .95;

}}


/* ==========================================================
   IMÁGENES
   ========================================================== */

.photo-frame {{

    width:
        min(
            88vw,
            600px
        );

    max-height:
        58vh;

    margin:
        24px auto;

    border-radius:
        clamp(
            20px,
            5vw,
            36px
        );

    overflow:
        hidden;

    position:
        relative;

    box-shadow:
        0 35px 90px
        rgba(0,0,0,.45);

    border:
        1px solid
        rgba(255,255,255,.12);

    transform:
        rotate(-1deg);

    transition:
        transform .4s ease;

}}


.photo-frame:hover {{
    transform:
        rotate(0deg)
        scale(1.015);
}}


.photo-frame img {{

    display:
        block;

    width:
        100%;

    max-height:
        58vh;

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
        55px
        18px
        18px;

    text-align:
        left;

    background:
        linear-gradient(
            transparent,
            rgba(0,0,0,.8)
        );

    font-weight:
        700;

    font-size:
        .85rem;

}}


/* ==========================================================
   CARD
   ========================================================== */

.story-card {{

    width:
        min(
            100%,
            620px
        );

    padding:
        clamp(
            18px,
            5vw,
            30px
        );

    border-radius:
        28px;

    background:
        rgba(255,255,255,.07);

    border:
        1px solid
        rgba(255,255,255,.09);

    backdrop-filter:
        blur(20px);

    -webkit-backdrop-filter:
        blur(20px);

    color:
        rgba(255,255,255,.8);

    line-height:
        1.8;

    text-align:
        left;

}}


/* ==========================================================
   ESTADÍSTICAS
   ========================================================== */

.stats {{

    display:
        grid;

    grid-template-columns:
        repeat(2, 1fr);

    gap:
        9px;

    width:
        min(
            100%,
            650px
        );

    margin-top:
        25px;

}}


.stat {{

    min-height:
        145px;

    padding:
        20px;

    border-radius:
        25px;

    display:
        flex;

    flex-direction:
        column;

    justify-content:
        space-between;

    text-align:
        left;

    background:
        linear-gradient(
            145deg,
            rgba(255,255,255,.11),
            rgba(255,255,255,.035)
        );

    border:
        1px solid
        rgba(255,255,255,.09);

}}


.stat-number {{

    font-family:
        'Unbounded',
        sans-serif;

    font-size:
        clamp(
            2rem,
            9vw,
            3.5rem
        );

    font-weight:
        800;

}}


.stat-label {{

    color:
        rgba(255,255,255,.5);

    font-size:
        9px;

    letter-spacing:
        .13em;

    font-weight:
        800;

}}


/* ==========================================================
   BIG DATE
   ========================================================== */

.big-date {{

    font-family:
        'Unbounded',
        sans-serif;

    font-size:
        clamp(
            5rem,
            27vw,
            12rem
        );

    font-weight:
        800;

    line-height:
        .8;

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


/* ==========================================================
   MEMORIAS
   ========================================================== */

.memories {{

    width:
        min(
            100%,
            650px
        );

    text-align:
        left;

}}


.memory {{

    display:
        flex;

    gap:
        13px;

    padding:
        15px 0;

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
        rgba(255,255,255,.58);

    font-size:
        .82rem;

    line-height:
        1.55;

    margin-top:
        3px;

}}


/* ==========================================================
   PLAYLIST
   ========================================================== */

.album {{

    width:
        min(
            65vw,
            280px
        );

    aspect-ratio:
        1;

    border-radius:
        24px;

    background:
        linear-gradient(
            135deg,
            #ff2d75,
            #ff8a00,
            #7a38ff
        );

    display:
        flex;

    align-items:
        center;

    justify-content:
        center;

    margin:
        22px 0;

    box-shadow:
        0 25px 70px
        rgba(0,0,0,.4);

    position:
        relative;

    overflow:
        hidden;

}}


.album::before {{

    content:
        "♪";

    font-family:
        Georgia;

    font-size:
        10rem;

    line-height:
        1;

    color:
        rgba(255,255,255,.9);

    transform:
        rotate(-15deg);

}}


.album::after {{

    content:
        "";

    position:
        absolute;

    width:
        70%;

    height:
        70%;

    border:
        1px solid
        rgba(255,255,255,.25);

    border-radius:
        50%;

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

    font-family:
        'Unbounded',
        sans-serif;

    font-size:
        clamp(
            1.3rem,
            6vw,
            2.4rem
        );

    font-weight:
        800;

    line-height:
        1.15;

    margin-top:
        8px;

}}


.song-artist {{

    color:
        #ffd447;

    margin-top:
        7px;

    font-size:
        .85rem;

    font-weight:
        700;

}}


.song-meaning {{

    margin-top:
        15px;

    color:
        rgba(255,255,255,.6);

    line-height:
        1.7;

    font-size:
        .84rem;

}}


/* ==========================================================
   SONG LIST
   ========================================================== */

.song-list {{

    width:
        min(
            100%,
            650px
        );

    margin-top:
        20px;

}}


.song-row {{

    display:
        grid;

    grid-template-columns:
        35px 1fr;

    text-align:
        left;

    gap:
        10px;

    padding:
        12px 0;

    border-bottom:
        1px solid
        rgba(255,255,255,.07);

}}


.song-index {{

    color:
        rgba(255,255,255,.3);

    font-family:
        'Unbounded';

    font-size:
        9px;

}}


.song-name {{

    font-weight:
        800;

    font-size:
        .85rem;

}}


.song-artist-small {{

    color:
        rgba(255,255,255,.45);

    font-size:
        .72rem;

    margin-top:
        3px;

}}


/* ==========================================================
   RESTAURANTES
   ========================================================== */

.places {{

    width:
        min(
            100%,
            650px
        );

}}


.place {{

    padding:
        18px;

    border-radius:
        24px;

    margin:
        9px 0;

    text-align:
        left;

    background:
        rgba(255,255,255,.065);

    border:
        1px solid
        rgba(255,255,255,.08);

}}


.place-number {{

    font-family:
        'Unbounded';

    color:
        rgba(255,255,255,.2);

    font-size:
        1.5rem;

}}


.place-name {{

    font-family:
        'Unbounded';

    font-size:
        .85rem;

    margin-top:
        8px;

}}


.place-description {{

    color:
        rgba(255,255,255,.55);

    font-size:
        .78rem;

    line-height:
        1.6;

    margin-top:
        7px;

}}


/* ==========================================================
   GALERÍA
   ========================================================== */

.gallery-photo {{

    width:
        min(
            90vw,
            700px
        );

    height:
        min(
            68vh,
            650px
        );

    border-radius:
        32px;

    overflow:
        hidden;

    box-shadow:
        0 35px 90px
        rgba(0,0,0,.45);

}}


.gallery-photo img {{

    width:
        100%;

    height:
        100%;

    object-fit:
        contain;

}}


/* ==========================================================
   FINAL
   ========================================================== */

.final-title {{

    font-family:
        'Unbounded',
        sans-serif;

    font-size:
        clamp(
            2rem,
            10vw,
            5rem
        );

    line-height:
        1.08;

    letter-spacing:
        -.07em;

    font-weight:
        800;

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

    color:
        rgba(255,255,255,.5);

    margin-top:
        35px;

}}


.days-number {{

    font-family:
        'Unbounded',
        sans-serif;

    font-size:
        clamp(
            3rem,
            15vw,
            6rem
        );

    font-weight:
        800;

    margin-top:
        5px;

}}


.quote {{

    margin-top:
        30px;

    max-width:
        600px;

    font-family:
        'Unbounded',
        sans-serif;

    font-size:
        clamp(
            1rem,
            4vw,
            1.5rem
        );

    line-height:
        1.55;

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


/* ==========================================================
   MÚSICA
   ========================================================== */

#musicControl {{

    position:
        absolute;

    z-index:
        100;

    right:
        16px;

    bottom:
        calc(
            18px +
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

    align-items:
        center;

    justify-content:
        center;

    font-size:
        16px;

    cursor:
        pointer;

}}


/* ==========================================================
   INDICADOR DE SONIDO
   ========================================================== */

.sound-bars {{

    display:
        flex;

    align-items:
        flex-end;

    justify-content:
        center;

    gap:
        2px;

    height:
        16px;

}}


.sound-bar {{

    width:
        2px;

    height:
        7px;

    background:
        white;

    border-radius:
        5px;

}}


.music-playing .sound-bar:nth-child(1) {{
    animation:
        sound .6s infinite alternate;
}}


.music-playing .sound-bar:nth-child(2) {{
    animation:
        sound .45s infinite alternate;
}}


.music-playing .sound-bar:nth-child(3) {{
    animation:
        sound .7s infinite alternate;
}}


@keyframes sound {{

    from {{
        height: 4px;
    }}

    to {{
        height: 15px;
    }}

}}


/* ==========================================================
   DESKTOP
   ========================================================== */

@media (min-width: 800px) {{

    .slide {{
        padding:
            70px
            40px
            60px;
    }}

    .tap-hint {{
        display: none;
    }}

}}


/* ==========================================================
   TELÉFONO PEQUEÑO
   ========================================================== */

@media (max-height: 700px) and (max-width: 600px) {{

    .slide {{
        padding-top:
            55px;
    }}

    .section-title {{
        font-size:
            1.7rem;
    }}

    .photo-frame {{
        max-height:
            43vh;
    }}

    .photo-frame img {{
        max-height:
            43vh;
    }}

    .stat {{
        min-height:
            110px;
    }}

}}


/* ==========================================================
   SAFE AREA
   ========================================================== */

@supports (
    padding:
    max(
        0px,
        env(safe-area-inset-top)
    )
) {{

    .slide {{
        padding-top:
            max(
                60px,
                calc(
                    45px +
                    env(safe-area-inset-top)
                )
            );

        padding-bottom:
            max(
                55px,
                calc(
                    40px +
                    env(safe-area-inset-bottom)
                )
            );
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


        <!-- ==================================================
             01 PORTADA
             ================================================== -->

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

                <div class="tap-hint">
                    toca para comenzar
                </div>

            </div>

        </section>


        <!-- ==================================================
             02 ESTADÍSTICAS
             ================================================== -->

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
                            LUGARES FAVORITOS
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

                    Pero hay una estadística que nunca
                    podremos calcular:

                    <br>

                    <strong>
                    todas las veces que elegimos
                    estar juntos.
                    </strong>

                </p>

            </div>

        </section>


        <!-- ==================================================
             03 INICIO
             ================================================== -->

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

                    Hay fechas que terminan convirtiéndose
                    en algo mucho más grande de lo que
                    imaginábamos.

                    <br><br>

                    El 24 de julio de 2023 comenzó
                    nuestra historia.

                </p>

                <div
                    class="photo-frame"
                    id="inicioPhoto"
                ></div>

            </div>

        </section>


        <!-- ==================================================
             04 CAIFANES
             ================================================== -->

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

                    Porque no solamente importa
                    a dónde vamos,

                    <br>

                    sino con quién compartimos
                    el momento.

                </p>

            </div>

        </section>


        <!-- ==================================================
             05 DICIEMBRE
             ================================================== -->

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
                                pero mucho más especial
                                porque estabas conmigo.
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
                                Compartiendo momentos sencillos
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
                                Una aventura más de tantas
                                que hemos ido sumando.
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


        <!-- ==================================================
             06 2024
             ================================================== -->

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


        <!-- ==================================================
             07 2025-2026
             ================================================== -->

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


        <!-- ==================================================
             08 GASTRONOMÍA
             ================================================== -->

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


        <!-- ==================================================
             09 PLAYLIST
             ================================================== -->

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
                        TU CANCIÓN #01
                    </div>

                    <div class="song-title">
                        Tiempo para Amarte
                    </div>

                    <div class="song-artist">
                        Laureano Brizuela
                    </div>

                    <div class="song-meaning">
                        A pesar de las cuentas, el estrés diario
                        y todas las cosas que tenemos que hacer,
                        siempre quiero encontrar tiempo para ti.
                    </div>

                </div>

            </div>

        </section>


        <!-- ==================================================
             10 GALERÍA
             ================================================== -->

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
                    class="photo-caption"
                    style="
                        position:static;
                        background:none;
                        text-align:center;
                    "
                ></div>

            </div>

        </section>


        <!-- ==================================================
             11 FINAL
             ================================================== -->

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


{audio_html}


<script>

/* ============================================================
   DATOS
   ============================================================ */

const DATA =
    {DATOS_JSON};


/* ============================================================
   ELEMENTOS
   ============================================================ */

const slides =
    Array.from(
        document.querySelectorAll(".slide")
    );

const progress =
    document.getElementById("progress");

const counter =
    document.getElementById("counter");

const background =
    document.getElementById("background");

const music =
    document.getElementById("backgroundMusic");

const musicControl =
    document.getElementById("musicControl");

const soundBars =
    document.getElementById("soundBars");


/* ============================================================
   ESTADO
   ============================================================ */

let current = 0;

let galleryIndex = 0;

let photoIndexes = {{
    december: 0,
    year2024: 0,
    year2025: 0
}};


/* ============================================================
   TEMAS
   ============================================================ */

const themes = {{

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

}};


/* ============================================================
   PROGRESO
   ============================================================ */

function buildProgress() {{

    progress.innerHTML = "";

    slides.forEach(
        (_, index) => {{

            const bar =
                document.createElement("div");

            bar.className =
                "progress-bar";

            const fill =
                document.createElement("div");

            fill.className =
                "progress-fill";

            bar.appendChild(fill);

            progress.appendChild(bar);

        }}
    );

}}


buildProgress();


/* ============================================================
   FOTOS
   ============================================================ */

function renderPhoto(
    elementId,
    image,
    caption = ""
) {{

    const element =
        document.getElementById(
            elementId
        );

    if (!element || !image)
        return;

    element.innerHTML = `

        <img src="${{image}}">

        ${{caption
            ? `<div class="photo-caption">${{caption}}</div>`
            : ""
        }}

    `;

}}


/* ============================================================
   FOTO INICIAL
   ============================================================ */

if (DATA.imagenes.inicio) {{

    renderPhoto(
        "inicioPhoto",
        DATA.imagenes.inicio,
        "El comienzo de nosotros ❤️"
    );

}}


/* ============================================================
   CAIFANES
   ============================================================ */

if (DATA.imagenes.caifanes) {{

    renderPhoto(
        "caifanesPhoto",
        DATA.imagenes.caifanes,
        "Una noche para recordar 🎸❤️"
    );

}}


/* ============================================================
   CARRUSEL DE DICIEMBRE
   ============================================================ */

function renderDecember() {{

    const images =
        DATA.imagenes.diciembre_2023 || [];

    if (!images.length)
        return;

    const index =
        photoIndexes.december %
        images.length;

    renderPhoto(
        "decemberPhoto",
        images[index],
        DATA.captions.diciembre_2023[index] || ""
    );

}}


/* ============================================================
   CARRUSEL 2024
   ============================================================ */

function render2024() {{

    const images =
        DATA.imagenes.y2024 || [];

    if (!images.length)
        return;

    const index =
        photoIndexes.year2024 %
        images.length;

    renderPhoto(
        "year2024Photo",
        images[index],
        DATA.captions.y2024[index] || ""
    );

}}


/* ============================================================
   CARRUSEL 2025
   ============================================================ */

function render2025() {{

    const images =
        DATA.imagenes.y2025_2026 || [];

    if (!images.length)
        return;

    const index =
        photoIndexes.year2025 %
        images.length;

    renderPhoto(
        "year2025Photo",
        images[index],
        DATA.captions.y2025_2026[index] || ""
    );

}}


/* ============================================================
   GALERÍA
   ============================================================ */

function renderGallery() {{

    const images =
        DATA.imagenes.galeria || [];

    const photo =
        document.getElementById(
            "galleryPhoto"
        );

    const caption =
        document.getElementById(
            "galleryCaption"
        );

    if (!images.length) {{

        photo.innerHTML = `
            <div style="
                height:100%;
                display:flex;
                align-items:center;
                justify-content:center;
                color:rgba(255,255,255,.4);
            ">
                No hay fotos todavía
            </div>
        `;

        return;

    }}

    const index =
        galleryIndex %
        images.length;

    photo.innerHTML =
        `<img src="${{images[index]}}">`;

    caption.textContent =
        `Recuerdo ${{index + 1}} de ${{images.length}}`;

}}


/* ============================================================
   DÍAS PARA ANIVERSARIO
   ============================================================ */

function updateDays() {{

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

    if (anniversary < now) {{

        anniversary =
            new Date(
                year + 1,
                8,
                23
            );

    }}

    const diff =
        anniversary - now;

    const days =
        Math.ceil(
            diff /
            (1000 * 60 * 60 * 24)
        );

    document.getElementById(
        "daysNumber"
    ).textContent = days;

}}

updateDays();


/* ============================================================
   CAMBIO DE SLIDE
   ============================================================ */

function showSlide(
    index,
    direction = 1
) {{

    if (index < 0)
        index = 0;

    if (index >= slides.length)
        index = slides.length - 1;

    if (index === current)
        return;

    const old =
        slides[current];

    const next =
        slides[index];

    old.classList.remove(
        "active"
    );

    old.classList.add(
        direction > 0
            ? "previous"
            : ""
    );

    next.classList.remove(
        "previous"
    );

    next.classList.add(
        "active"
    );

    current = index;


    /* Fondo */

    const theme =
        next.dataset.theme ||
        "cover";

    background.style.background =
        themes[theme];


    /* Contador */

    counter.textContent =
        String(current + 1).padStart(2,"0")
        +
        " / "
        +
        String(slides.length).padStart(2,"0");


    /* Barras */

    const bars =
        document.querySelectorAll(
            ".progress-fill"
        );

    bars.forEach(
        (bar, i) => {{

            if (i < current) {{

                bar.style.width =
                    "100%";

            }}

            else if (i === current) {{

                bar.style.width =
                    "100%";

            }}

            else {{

                bar.style.width =
                    "0%";

            }}

        }}
    );


    /* Carruseles */

    if (current === 4) {{
        renderDecember();
    }}

    if (current === 5) {{
        render2024();
    }}

    if (current === 6) {{
        render2025();
    }}

    if (current === 9) {{
        renderGallery();
    }}

}}


/* ============================================================
   ESTADO INICIAL
   ============================================================ */

background.style.background =
    themes.cover;

const initialBars =
    document.querySelectorAll(
        ".progress-fill"
    );

if (initialBars.length) {{

    initialBars[0].style.width =
        "100%";

}}


/* ============================================================
   SIGUIENTE
   ============================================================ */

function nextSlide() {{

    if (
        current <
        slides.length - 1
    ) {{

        showSlide(
            current + 1,
            1
        );

    }}

}}


/* ============================================================
   ANTERIOR
   ============================================================ */

function previousSlide() {{

    if (current > 0) {{

        showSlide(
            current - 1,
            -1
        );

    }}

}}


/* ============================================================
   TAP
   ============================================================ */

let touchStartX = 0;
let touchStartY = 0;
let touchStartTime = 0;


document.addEventListener(
    "touchstart",
    event => {{

        if (!event.touches.length)
            return;

        touchStartX =
            event.touches[0].clientX;

        touchStartY =
            event.touches[0].clientY;

        touchStartTime =
            Date.now();

    }},
    {{ passive: true }}
);


document.addEventListener(
    "touchend",
    event => {{

        if (!event.changedTouches.length)
            return;

        const endX =
            event.changedTouches[0].clientX;

        const endY =
            event.changedTouches[0].clientY;

        const dx =
            endX - touchStartX;

        const dy =
            endY - touchStartY;

        const duration =
            Date.now() -
            touchStartTime;


        /*
         * Swipe horizontal
         */

        if (
            Math.abs(dx) > 55 &&
            Math.abs(dx) > Math.abs(dy)
        ) {{

            if (dx < 0)
                nextSlide();
            else
                previousSlide();

            return;

        }}


        /*
         * Tap
         */

        if (
            Math.abs(dx) < 25 &&
            Math.abs(dy) < 25 &&
            duration < 450
        ) {{

            const width =
                window.innerWidth;

            if (endX < width / 2)
                previousSlide();
            else
                nextSlide();

        }}

    }},
    {{ passive: true }}
);


/* ============================================================
   CLICK DESKTOP
   ============================================================ */

document.addEventListener(
    "click",
    event => {{

        if (
            event.target.closest(
                "#musicControl"
            )
        )
            return;

        if (
            window.innerWidth <= 799
        )
            return;

        const width =
            window.innerWidth;

        if (event.clientX < width / 2)
            previousSlide();
        else
            nextSlide();

    }}
);


/* ============================================================
   TECLADO
   ============================================================ */

document.addEventListener(
    "keydown",
    event => {{

        if (
            event.key === "ArrowRight" ||
            event.key === " "
        ) {{

            event.preventDefault();

            nextSlide();

        }}

        else if (
            event.key === "ArrowLeft"
        ) {{

            event.preventDefault();

            previousSlide();

        }}

    }}
);


/* ============================================================
   CAMBIO AUTOMÁTICO DE FOTOS
   ============================================================ */

setInterval(
    () => {{

        if (current === 4) {{

            const images =
                DATA.imagenes.diciembre_2023 || [];

            if (images.length > 1) {{

                photoIndexes.december =
                    (
                        photoIndexes.december + 1
                    ) %
                    images.length;

                renderDecember();

            }}

        }}


        if (current === 5) {{

            const images =
                DATA.imagenes.y2024 || [];

            if (images.length > 1) {{

                photoIndexes.year2024 =
                    (
                        photoIndexes.year2024 + 1
                    ) %
                    images.length;

                render2024();

            }}

        }}


        if (current === 6) {{

            const images =
                DATA.imagenes.y2025_2026 || [];

            if (images.length > 1) {{

                photoIndexes.year2025 =
                    (
                        photoIndexes.year2025 + 1
                    ) %
                    images.length;

                render2025();

            }}

        }}


        if (current === 9) {{

            const images =
                DATA.imagenes.galeria || [];

            if (images.length > 1) {{

                galleryIndex =
                    (
                        galleryIndex + 1
                    ) %
                    images.length;

                renderGallery();

            }}

        }}

    }},
    5000
);


/* ============================================================
   MÚSICA
   ============================================================ */

let musicStarted = false;


function startMusic() {{

    if (!music)
        return;

    if (musicStarted)
        return;

    const promise =
        music.play();

    if (
        promise &&
        promise.then
    ) {{

        promise.then(
            () => {{

                musicStarted =
                    true;

                soundBars.classList.add(
                    "music-playing"
                );

            }}
        ).catch(
            () => {{}}
        );

    }}

}}


/*
 * El navegador móvil necesita interacción.
 */

document.addEventListener(
    "touchstart",
    startMusic,
    {{
        once: true,
        passive: true
    }}
);


document.addEventListener(
    "click",
    startMusic,
    {{
        once: true
    }}
);


document.addEventListener(
    "keydown",
    startMusic,
    {{
        once: true
    }}
);


/* ============================================================
   BOTÓN DE MÚSICA
   ============================================================ */

if (musicControl) {{

    musicControl.addEventListener(
        "click",
        event => {{

            event.stopPropagation();

            if (!music)
                return;

            if (music.paused) {{

                music.play()
                    .then(
                        () => {{

                            soundBars.classList.add(
                                "music-playing"
                            );

                        }}
                    )
                    .catch(
                        () => {{}}
                    );

            }}

            else {{

                music.pause();

                soundBars.classList.remove(
                    "music-playing"
                );

            }}

        }}
    );

}}


/* ============================================================
   CARRUSELES POR TOQUE
   ============================================================ */

document.addEventListener(
    "click",
    event => {{

        const active =
            slides[current];

        if (!active)
            return;


        if (current === 4) {{

            const rect =
                active.getBoundingClientRect();

            if (
                event.clientY >
                rect.top + 120
            ) {{

                if (
                    event.clientX >
                    window.innerWidth * .5
                ) {{

                    const images =
                        DATA.imagenes.diciembre_2023 || [];

                    if (images.length) {{

                        photoIndexes.december =
                            (
                                photoIndexes.december + 1
                            ) %
                            images.length;

                        renderDecember();

                    }}

                }}

                else {{

                    const images =
                        DATA.imagenes.diciembre_2023 || [];

                    if (images.length) {{

                        photoIndexes.december =
                            (
                                photoIndexes.december - 1 +
                                images.length
                            ) %
                            images.length;

                        renderDecember();

                    }}

                }}

            }}

        }}

    }}
);


/* ============================================================
   PREPARAR PRIMERAS IMÁGENES
   ============================================================ */

renderDecember();
render2024();
render2025();
renderGallery();


</script>

</body>

</html>
"""


# ============================================================
# RENDER
# ============================================================

components.html(
    HTML,
    height=900,
    scrolling=False,
)
