import os
import base64
import json
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
# ESTILOS CSS PARA ELIMINAR MÁRGENES Y BARRAS DE STREAMLIT
# ============================================================

st.markdown("""
    <style>
        /* Ocultar elementos de navegación y cabeceras de Streamlit */
        #MainMenu {visibility: hidden;}
        header {visibility: hidden;}
        footer {visibility: hidden;}
        [data-testid="stHeader"] {display: none !important;}
        [data-testid="stToolbar"] {visibility: hidden !important;}
        
        /* Ajustar contenedor principal para ocupar toda la pantalla */
        .block-container {
            padding: 0 !important;
            margin: 0 !important;
            max-width: 100% !important;
            overflow: hidden !important;
        }
        
        iframe {
            position: fixed !important;
            top: 0 !important;
            left: 0 !important;
            width: 100vw !important;
            height: 100vh !important;
            border: none !important;
            z-index: 999999 !important;
        }
    </style>
""", unsafe_allow_html=True)


# ============================================================
# RUTAS
# ============================================================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FOTOS_DIR = os.path.join(BASE_DIR, "fotos")
GALERIA_DIR = os.path.join(FOTOS_DIR, "galeria")
MUSICA_FONDO = os.path.join(BASE_DIR, "musica.mp3")


# ============================================================
# FUNCIONES
# ============================================================

def archivo_base64(ruta):
    if not os.path.exists(ruta):
        return None
    try:
        with open(ruta, "rb") as archivo:
            return base64.b64encode(archivo.read()).decode("utf-8")
    except Exception:
        return None

def mime_imagen(ruta):
    extension = os.path.splitext(ruta)[1].lower()
    tipos = {
        ".png": "image/png",
        ".jpg": "image/jpeg",
        ".jpeg": "image/jpeg",
        ".webp": "image/webp",
    }
    return tipos.get(extension, "image/png")

def imagen_data(ruta):
    data = archivo_base64(ruta)
    if not data:
        return None
    return f"data:{mime_imagen(ruta)};base64,{data}"


# ============================================================
# FOTOGRAFÍAS Y DATOS
# ============================================================

FOTOS = {
    "inicio": os.path.join(FOTOS_DIR, "image_0.png"),
    "caifanes": os.path.join(FOTOS_DIR, "image_1.png"),
    "diciembre_2023": [
        os.path.join(FOTOS_DIR, "image_2.png"),
        os.path.join(FOTOS_DIR, "image_3.png"),
        os.path.join(FOTOS_DIR, "image_4.png"),
    ],
    "y2024": [
        os.path.join(FOTOS_DIR, "image_5.png"),
        os.path.join(FOTOS_DIR, "image_6.png"),
        os.path.join(FOTOS_DIR, "image_7.png"),
        os.path.join(FOTOS_DIR, "image_8.png"),
    ],
    "y2025_2026": [
        os.path.join(FOTOS_DIR, "image_9.png"),
        os.path.join(FOTOS_DIR, "image_10.png"),
        os.path.join(FOTOS_DIR, "image_11.png"),
    ],
}

CAPTIONS = {
    "diciembre_2023": [
        "En el pueblo de mi papá, contigo 🏡",
        "Rompiendo la piñata juntos 🎉",
        "Nuestro viaje a Mazatlan 🌊",
    ],
    "y2024": [
        "Enseñándome a manejar la moto 🏍️",
        "Emprendiendo con las togas SHESPAT 🎓",
        "Nuestra aventura por Commscope",
        "El halloween sin presupuesto",
    ],
    "y2025_2026": [
        "Esta foto me encanta porque representa toda tu escencia",
        "El regalo de mi papá",
        "Nuestros hijos Cabo y Copito",
    ],
}

CANCIONES = [
    {
        "titulo": "Tiempo para Amarte",
        "artista": "Laureano Brizuela",
        "significado": "A pesar de las cuentas, el estrés diario y todas las cosas que tenemos que hacer, siempre quiero encontrar tiempo para ti.",
    },
    {
        "titulo": "My One and Only Love / They Say It's Wonderful",
        "artista": "John Coltrane",
        "significado": "Mi descubrimiento personal del amor y una canción que terminó teniendo un significado muy especial para nosotros.",
    },
    {
        "titulo": "I Only Have Eyes for You",
        "artista": "Louis Armstrong",
        "significado": "Entre todas las personas, lugares y cosas que existen, mis ojos siempre terminan buscándote a ti.",
    },
    {
        "titulo": "Eso y Más",
        "artista": "Joan Sebastián",
        "significado": "Una canción que representa todo eso que siento y muchas veces no sé cómo decirte.",
    },
    {
        "titulo": "Diséñame",
        "artista": "Joan Sebastián",
        "significado": "Nuestro amor fue construyéndose poco a poco, con nuestras propias historias.",
    },
    {
        "titulo": "The Nearness of You",
        "artista": "Ella Fitzgerald & Louis Armstrong",
        "significado": "La cercanía de la persona que amas puede hacer que cualquier momento cotidiano se sienta especial.",
    },
    {
        "titulo": "Only You",
        "artista": "The Platters",
        "significado": "Porque hay personas que simplemente se vuelven únicas en nuestra vida.",
    },
    {
        "titulo": "Eres",
        "artista": "José María Napoleón",
        "significado": "Una forma de decirte todo lo que significas para mí.",
    },
    {
        "titulo": "Mi Mundo Tú",
        "artista": "Camilo Sesto",
        "significado": "Después de estos años, eres una parte enorme de mi mundo.",
    },
    {
        "titulo": "Cama y Mesa",
        "artista": "Roberto Carlos",
        "significado": "Una canción sobre compartir la vida, los momentos íntimos y también los cotidianos.",
    },
    {
        "titulo": "Invítame un cigarro",
        "artista": "Tradicional / Popular",
        "significado": "Una de esas canciones que terminaron formando parte de nuestra historia.",
    },
]

RESTAURANTES = [
    {
        "nombre": "Ninja Ramen",
        "descripcion": "Uno de esos lugares que se volvieron parte de nuestros momentos juntos.",
    },
    {
        "nombre": "Ryu Ramen House",
        "descripcion": "Comida, plática y tiempo juntos.",
    },
    {
        "nombre": "Trueke Comida & Amigos",
        "descripcion": "Otro lugar que quedó guardado dentro de nuestras pequeñas aventuras.",
    },
]

def obtener_galeria():
    if not os.path.exists(GALERIA_DIR):
        return []
    extensiones = (".png", ".jpg", ".jpeg", ".webp")
    archivos = []
    for archivo in sorted(os.listdir(GALERIA_DIR)):
        if archivo.lower().endswith(extensiones):
            archivos.append(os.path.join(GALERIA_DIR, archivo))
    return archivos

def preparar_imagenes():
    imagenes = {}
    portada = os.path.join(FOTOS_DIR, "portada.png")
    if os.path.exists(portada):
        imagenes["portada"] = imagen_data(portada)

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
MUSICA_B64 = archivo_base64(MUSICA_FONDO)

DATOS = {
    "imagenes": IMAGENES,
    "canciones": CANCIONES,
    "restaurantes": RESTAURANTES,
    "captions": CAPTIONS,
}

DATOS_JSON = json.dumps(DATOS, ensure_ascii=False)

AUDIO_HTML = f"""
    <audio id="backgroundMusic" preload="auto" loop>
        <source src="data:audio/mpeg;base64,{MUSICA_B64}" type="audio/mpeg">
    </audio>
""" if MUSICA_B64 else ""


# ============================================================
# HTML DE LA APLICACIÓN (CADENA NORMAL)
# ============================================================

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1, user-scalable=no"/>
<style>
* {
    box-sizing: border-box;
    -webkit-tap-highlight-color: transparent;
}
html, body {
    margin: 0;
    padding: 0;
    width: 100vw;
    height: 100vh;
    overflow: hidden;
    background: #07030b;
    color: white;
    font-family: Arial, sans-serif;
    touch-action: none;
}
#app {
    position: fixed;
    inset: 0;
    width: 100vw;
    height: 100dvh;
    overflow: hidden;
    background: #07030b;
    touch-action: none;
    user-select: none;
    -webkit-user-select: none;
}
#background {
    position: absolute;
    inset: -10%;
    z-index: 0;
    transition: background 0.7s ease;
}
/* Capas decorativas independientes: ningún efecto intercepta los gestos. */
#ambient, #celebration, #transitionGlow, #effects {
    position: absolute;
    inset: 0;
    overflow: hidden;
    pointer-events: none;
}
#ambient, #celebration { z-index: 5; }
#transitionGlow { z-index: 55; opacity: 0; }
#effects { z-index: 60; }
.ambient-light {
    position: absolute;
    width: 5px;
    height: 5px;
    border-radius: 50%;
    background: #fff4d6;
    box-shadow: 0 0 12px 4px rgba(255,210,175,.35);
    opacity: 0;
    animation: ambientTwinkle var(--twinkle-time) ease-in-out infinite;
    animation-delay: var(--twinkle-delay);
}
@keyframes ambientTwinkle {
    0%, 100% { opacity: 0; transform: translate3d(0,8px,0) scale(.5); }
    48% { opacity: .55; transform: translate3d(8px,-12px,0) scale(1); }
}
.transition-flash { animation: transitionFlash .7s ease-out both; }
@keyframes transitionFlash {
    0% { opacity: 0; background: radial-gradient(circle at 50% 50%, rgba(255,202,230,.27), transparent 68%); }
    27% { opacity: 1; }
    100% { opacity: 0; }
}
.sparkle {
    position: absolute;
    width: var(--size);
    height: var(--size);
    border-radius: 50%;
    background: #fff;
    box-shadow: 0 0 10px 3px rgba(255,221,194,.6);
    animation: sparkleBurst var(--lifetime) ease-out forwards;
}
.sparkle::before, .sparkle::after {
    content: "";
    position: absolute;
    top: 50%; left: 50%;
    background: rgba(255,244,229,.85);
    transform: translate(-50%, -50%);
}
.sparkle::before { width: 1px; height: 12px; }
.sparkle::after { width: 12px; height: 1px; }
@keyframes sparkleBurst {
    0% { opacity: 0; transform: translate3d(0,8px,0) scale(.3); }
    25% { opacity: .9; }
    100% { opacity: 0; transform: translate3d(var(--travel-x),var(--travel-y),0) scale(.35); }
}
.confetti {
    position: absolute;
    width: 6px;
    height: 10px;
    border-radius: 2px;
    background: var(--particle-color);
    opacity: 0;
    animation: confettiFall var(--lifetime) ease-out forwards;
    animation-delay: var(--delay);
}
@keyframes confettiFall {
    0% { opacity: 0; transform: translate3d(0,-12vh,0) rotate(0deg); }
    12% { opacity: .8; }
    82% { opacity: .7; }
    100% { opacity: 0; transform: translate3d(var(--travel-x),105vh,0) rotate(var(--rotation)); }
}
.balloon {
    position: absolute;
    bottom: -165px;
    width: clamp(35px, 8vw, 62px);
    height: clamp(48px, 11vw, 83px);
    border-radius: 50% 50% 47% 47%;
    opacity: .38;
    background: radial-gradient(circle at 35% 27%, rgba(255,255,255,.8), transparent 24%), var(--balloon-color);
    box-shadow: inset -10px -13px 16px rgba(0,0,0,.19), 0 0 20px rgba(255,141,215,.12);
    animation: balloonRise var(--rise-time) linear var(--delay) infinite;
}
.balloon::before {
    content: "";
    position: absolute;
    left: 44%; bottom: -8px;
    border-left: 4px solid transparent;
    border-right: 4px solid transparent;
    border-top: 8px solid var(--balloon-color);
}
.balloon::after {
    content: "";
    position: absolute;
    left: 50%; bottom: -64px;
    width: 1px; height: 58px;
    background: rgba(255,255,255,.4);
}
@keyframes balloonRise {
    0% { transform: translate3d(0,0,0) rotate(-7deg); }
    50% { transform: translate3d(16px,-62vh,0) rotate(6deg); }
    100% { transform: translate3d(-8px,-126vh,0) rotate(-5deg); }
}
#grain {
    position: absolute;
    inset: 0;
    z-index: 40;
    pointer-events: none;
    opacity: .055;
    background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='180' height='180'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='.9' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)' opacity='.8'/%3E%3C/svg%3E");
}
#progress {
    position: absolute;
    top: max(10px, env(safe-area-inset-top));
    left: 12px;
    right: 12px;
    z-index: 100;
    display: flex;
    gap: 4px;
}
.progress-bar {
    flex: 1;
    height: 3px;
    border-radius: 10px;
    overflow: hidden;
    background: rgba(255,255,255,.22);
}
.progress-fill {
    width: 0%;
    height: 100%;
    border-radius: inherit;
    background: white;
    transition: width linear;
    will-change: width;
}
#counter {
    position: absolute;
    z-index: 100;
    right: 15px;
    top: calc(max(10px, env(safe-area-inset-top)) + 14px);
    font-size: 9px;
    font-weight: 800;
    letter-spacing: .15em;
    color: rgba(255,255,255,.6);
}
#slides {
    position: relative;
    width: 100%;
    height: 100%;
    z-index: 10;
}
.slide {
    position: absolute;
    inset: 0;
    width: 100%;
    height: 100%;
    padding: 60px 20px calc(55px + env(safe-area-inset-bottom));
    display: flex;
    justify-content: center;
    align-items: center;
    opacity: 0;
    pointer-events: none;
    transform: translateX(60px) scale(.97);
    transition: opacity .5s ease, transform .6s ease;
    overflow: hidden;
}
.slide.active {
    opacity: 1;
    pointer-events: auto;
    transform: translateX(0) scale(1);
}

.slide.active .eyebrow,
.slide.active .title,
.slide.active .section-title,
.slide.active .final-title,
.slide.active .subtitle,
.slide.active .section-text,
.slide.active .stats,
.slide.active .memories,
.slide.active .places,
.slide.active .album,
.slide.active .featured-song,
.slide.active .gallery-photo,
.slide.active .photo-frame,
.slide.active .big-date,
.slide.active .days-label,
.slide.active .days-number,
.slide.active .quote {
    animation: wrappedFadeUp .75s cubic-bezier(.2,.8,.2,1) both;
}

.slide.active .photo-frame img,
.slide.active .gallery-photo img {
    animation: wrappedKenBurns 8s ease-out both;
}
.slide.active .content > :nth-child(2) { animation-delay: .08s; }
.slide.active .content > :nth-child(3) { animation-delay: .16s; }

@keyframes wrappedFadeUp {
    from {
        opacity: 0;
        transform: translateY(20px) scale(.985);
        filter: blur(5px);
    }
    to {
        opacity: 1;
        transform: translateY(0) scale(1);
        filter: blur(0);
    }
}

@keyframes wrappedKenBurns {
    from { transform: scale(1.02); }
    to   { transform: scale(1.08); }
}

#background {
    animation: wrappedBackground 12s ease-in-out infinite alternate;
}

@keyframes wrappedBackground {
    from { transform: scale(1) translate3d(0,0,0); }
    to   { transform: scale(1.06) translate3d(-1.5%,1%,0); }
}
.slide.previous {
    transform: translateX(-60px) scale(.97);
}
.content {
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
}
.content::-webkit-scrollbar { display: none; }
.eyebrow {
    font-size: clamp(9px, 2.3vw, 12px);
    letter-spacing: .23em;
    text-transform: uppercase;
    font-weight: 800;
    color: rgba(255,255,255,.65);
    margin-bottom: 15px;
}
.title, .section-title, .final-title {
    font-family: Arial, sans-serif;
    font-weight: 900;
    line-height: .98;
    letter-spacing: -.065em;
    margin: 0;
}
.title {
    font-size: clamp(2.8rem, 12vw, 7rem);
    background: linear-gradient(115deg, #ff2d75, #ff8a00, #ffd447, #9b52ff);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}
.section-title {
    font-size: clamp(2rem, 8vw, 5rem);
}
.subtitle {
    max-width: 580px;
    margin-top: 20px;
    color: rgba(255,255,255,.72);
    font-size: clamp(.9rem, 3vw, 1.1rem);
    line-height: 1.7;
}
.cover-number {
    font-size: clamp(7rem, 30vw, 15rem);
    line-height: .7;
    font-weight: 900;
    letter-spacing: -.13em;
    background: linear-gradient(120deg, #ff2d75, #ff8a00, #ffd447, #8c52ff);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}
.photo-frame {
    position: relative;
    width: min(88vw, 600px);
    max-height: 50vh;
    margin: 20px auto;
    overflow: hidden;
    border-radius: 28px;
    border: 1px solid rgba(255,255,255,.12);
    box-shadow: 0 30px 80px rgba(0,0,0,.45);
}
.photo-frame img {
    display: block;
    width: 100%;
    max-height: 50vh;
    object-fit: cover;
}
.photo-caption {
    position: absolute;
    left: 0;
    right: 0;
    bottom: 0;
    padding: 50px 18px 18px;
    text-align: left;
    background: linear-gradient(transparent, rgba(0,0,0,.85));
    font-weight: 700;
    font-size: .8rem;
}
.stats {
    width: min(100%, 650px);
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 10px;
    margin-top: 24px;
}
.stat {
    min-height: 135px;
    padding: 20px;
    border-radius: 24px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    text-align: left;
    background: rgba(255,255,255,.07);
    border: 1px solid rgba(255,255,255,.09);
    backdrop-filter: blur(15px);
}
.stat-number {
    font-size: clamp(2rem, 9vw, 3.5rem);
    font-weight: 900;
}
.stat-label {
    font-size: 9px;
    font-weight: 800;
    letter-spacing: .12em;
    color: rgba(255,255,255,.5);
}
.big-date {
    font-size: clamp(6rem, 28vw, 12rem);
    line-height: .8;
    font-weight: 900;
    letter-spacing: -.1em;
    margin: 25px 0;
    background: linear-gradient(120deg, #ff2d75, #ffd447);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}
.section-text {
    max-width: 620px;
    margin-top: 15px;
    color: rgba(255,255,255,.63);
    line-height: 1.75;
}
.memories {
    width: min(100%, 650px);
    text-align: left;
    margin-top: 10px;
}
.memory {
    display: flex;
    gap: 13px;
    padding: 14px 0;
    border-bottom: 1px solid rgba(255,255,255,.08);
}
.memory-icon { font-size: 1.4rem; }
.memory-title { font-weight: 800; }
.memory-text {
    color: rgba(255,255,255,.55);
    font-size: .8rem;
    line-height: 1.5;
    margin-top: 3px;
}
.places {
    width: min(100%, 650px);
    margin-top: 15px;
}
.place {
    padding: 17px;
    margin: 8px 0;
    border-radius: 22px;
    background: rgba(255,255,255,.06);
    border: 1px solid rgba(255,255,255,.08);
    text-align: left;
}
.place-number {
    font-size: 1.4rem;
    font-weight: 900;
    color: rgba(255,255,255,.2);
}
.place-name {
    margin-top: 6px;
    font-weight: 900;
}
.place-description {
    margin-top: 5px;
    color: rgba(255,255,255,.5);
    font-size: .78rem;
    line-height: 1.5;
}
.album {
    width: min(65vw, 280px);
    aspect-ratio: 1;
    margin: 22px 0;
    border-radius: 25px;
    display: flex;
    justify-content: center;
    align-items: center;
    background: linear-gradient(135deg, #ff2d75, #ff8a00, #7a38ff);
    box-shadow: 0 25px 70px rgba(0,0,0,.45);
}
.album::before {
    content: "♪";
    font-size: 9rem;
    font-family: Georgia, serif;
    color: rgba(255,255,255,.9);
}
.featured-song {
    width: min(100%, 600px);
    text-align: left;
}
.song-number {
    font-size: 9px;
    letter-spacing: .2em;
    color: rgba(255,255,255,.4);
}
.song-title {
    font-size: clamp(1.3rem, 6vw, 2.4rem);
    font-weight: 900;
    margin-top: 7px;
}
.song-artist {
    color: #ffd447;
    font-size: .85rem;
    font-weight: 700;
    margin-top: 6px;
}
.song-meaning {
    color: rgba(255,255,255,.58);
    line-height: 1.7;
    font-size: .82rem;
    margin-top: 13px;
}
.gallery-photo {
    width: min(90vw, 700px);
    height: min(60vh, 650px);
    margin: 20px auto;
    overflow: hidden;
    border-radius: 30px;
    box-shadow: 0 30px 80px rgba(0,0,0,.5);
}
.gallery-photo img {
    width: 100%;
    height: 100%;
    object-fit: contain;
}
.final-title {
    font-size: clamp(2.2rem, 10vw, 5rem);
    background: linear-gradient(120deg, #ff2d75, #ffd447, #9b52ff);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}
.days-label {
    margin-top: 28px;
    color: rgba(255,255,255,.48);
}
.days-number {
    margin-top: 5px;
    font-size: clamp(3rem, 15vw, 6rem);
    font-weight: 900;
}
.quote {
    max-width: 600px;
    margin-top: 28px;
    font-size: clamp(1rem, 4vw, 1.45rem);
    font-weight: 800;
    line-height: 1.5;
    background: linear-gradient(90deg, #ff2d75, #ffd447, #9b52ff);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}
#musicControl {
    position: absolute;
    z-index: 500;
    right: 16px;
    bottom: calc(17px + env(safe-area-inset-bottom));
    width: 42px;
    height: 42px;
    border-radius: 50%;
    border: 1px solid rgba(255,255,255,.18);
    background: rgba(0,0,0,.25);
    backdrop-filter: blur(15px);
    color: white;
    display: flex;
    justify-content: center;
    align-items: center;
    padding: 0;
}
.sound-bars {
    height: 16px;
    display: flex;
    align-items: flex-end;
    gap: 2px;
}
.sound-bar {
    width: 2px;
    height: 6px;
    background: white;
    border-radius: 4px;
}
.music-playing .sound-bar:nth-child(1) { animation: sound .55s infinite alternate; }
.music-playing .sound-bar:nth-child(2) { animation: sound .4s infinite alternate; }
.music-playing .sound-bar:nth-child(3) { animation: sound .7s infinite alternate; }
@keyframes sound {
    from { height: 4px; }
    to { height: 15px; }
}
@media (max-width: 600px) {
    .ambient-light:nth-child(n+6) { display: none; }
    .balloon { opacity: .28; }
}
@media (prefers-reduced-motion: reduce) {
    .slide, #background, .progress-fill { transition-duration: .01ms !important; }
    .slide.active *, .slide.active, #background, .ambient-light,
    .sparkle, .confetti, .balloon, .transition-flash {
        animation: none !important;
    }
    #ambient, #celebration, #effects, #transitionGlow { display: none; }
}
</style>
</head>
<body>

<div id="app">
    <div id="background"></div>
    <div id="ambient" aria-hidden="true"></div>
    <div id="celebration" aria-hidden="true"></div>
    <div id="grain"></div>
    <div id="transitionGlow" aria-hidden="true"></div>
    <div id="effects" aria-hidden="true"></div>
    <div id="progress"></div>
    <div id="counter">01 / 11</div>

    <div id="slides">
        <section class="slide active" data-theme="cover">
            <div class="content">
                <div class="eyebrow">NUESTRO WRAPPED · 2023 — 2026</div>
                <div class="cover-number">3</div>
                <h1 class="title">Años<br>Juntos</h1>
                <p class="subtitle">
                    Tres años. Cientos de momentos. Algunas canciones. Muchos recuerdos.<br><br>
                    Esta es una pequeña parte de nuestra historia.
                </p>
            </div>
        </section>

        <section class="slide" data-theme="stats">
            <div class="content">
                <div class="eyebrow">NUESTRO WRAPPED</div>
                <h2 class="section-title">Nuestra historia<br>en números</h2>
                <div class="stats">
                    <div class="stat"><div class="stat-number">3</div><div class="stat-label">AÑOS JUNTOS</div></div>
                    <div class="stat"><div class="stat-number">11</div><div class="stat-label">CANCIONES</div></div>
                    <div class="stat"><div class="stat-number">3</div><div class="stat-label">LUGARES</div></div>
                    <div class="stat"><div class="stat-number">2</div><div class="stat-label">CONEJITOS 🐰</div></div>
                </div>
                <p class="section-text">
                    Pero hay una estadística que nunca podremos calcular:<br><br>
                    <strong>todas las veces que elegimos estar juntos.</strong>
                </p>
            </div>
        </section>

        <section class="slide" data-theme="start">
            <div class="content">
                <div class="eyebrow">24 · 07 · 2023</div>
                <h2 class="section-title">Todo comenzó<br>aquí</h2>
                <div class="big-date">24</div>
                <p class="section-text">
                    Hay fechas que terminan convirtiéndose en algo mucho más grande de lo que imaginábamos.<br><br>
                    El 24 de julio de 2023 comenzó nuestra historia.
                </p>
                <div class="photo-frame" id="inicioPhoto"></div>
            </div>
        </section>

        <section class="slide" data-theme="concert">
            <div class="content">
                <div class="eyebrow">CAIFANES 🎸</div>
                <h2 class="section-title">Una noche<br>para recordar</h2>
                <div class="photo-frame" id="caifanesPhoto"></div>
                <p class="section-text">
                    No solamente importa a dónde vamos,<br>sino con quién compartimos el momento.
                </p>
            </div>
        </section>

        <section class="slide" data-theme="december">
            <div class="content">
                <div class="eyebrow">DICIEMBRE · 2023</div>
                <h2 class="section-title">Nuestro primer<br>diciembre</h2>
                <div class="memories">
                    <div class="memory"><div class="memory-icon">🏡</div><div><div class="memory-title">El pueblo de mi papá</div><div class="memory-text">Un lugar diferente, pero especial porque estabas conmigo.</div></div></div>
                    <div class="memory"><div class="memory-icon">🎉</div><div><div class="memory-title">La piñata</div><div class="memory-text">Momentos sencillos que terminaron convirtiéndose en recuerdos.</div></div></div>
                    <div class="memory"><div class="memory-icon">🌊</div><div><div class="memory-title">Rumbo al malecón</div><div class="memory-text">Una aventura más de nuestra historia.</div></div></div>
                </div>
                <div class="photo-frame" id="decemberPhoto"></div>
            </div>
        </section>

        <section class="slide" data-theme="year2024">
            <div class="content">
                <div class="eyebrow">CAPÍTULO · 2024</div>
                <h2 class="section-title">Un año de<br>cambios</h2>
                <div class="memories">
                    <div class="memory"><div class="memory-icon">🏍️</div><div><div class="memory-title">La moto</div><div class="memory-text">Enseñándome a manejar la moto.</div></div></div>
                    <div class="memory"><div class="memory-icon">🎓</div><div><div class="memory-title">SHESPAT</div><div class="memory-text">Emprendiendo con las togas.</div></div></div>
                    <div class="memory"><div class="memory-icon">🏢</div><div><div class="memory-title">Commscope</div><div class="memory-text">Nuestra aventura por Commscope.</div></div></div>
                    <div class="memory"><div class="memory-icon">🎃</div><div><div class="memory-title">Halloween</div><div class="memory-text">El Halloween sin presupuesto.</div></div></div>
                </div>
                <div class="photo-frame" id="year2024Photo"></div>
            </div>
        </section>

        <section class="slide" data-theme="year2025">
            <div class="content">
                <div class="eyebrow">2025 · 2026</div>
                <h2 class="section-title">Seguimos<br>escribiendo</h2>
                <div class="memories">
                    <div class="memory"><div class="memory-icon">❤️</div><div><div class="memory-title">Tu esencia</div><div class="memory-text">Esta foto me encanta porque representa toda tu escencia.</div></div></div>
                    <div class="memory"><div class="memory-icon">🎁</div><div><div class="memory-title">El regalo de mi papá</div><div class="memory-text">Un regalo que también forma parte de nuestra historia.</div></div></div>
                    <div class="memory"><div class="memory-icon">🐰</div><div><div class="memory-title">Cabo y Copito</div><div class="memory-text">Nuestros hijos y dos pequeños integrantes de nuestra historia.</div></div></div>
                </div>
                <div class="photo-frame" id="year2025Photo"></div>
            </div>
        </section>

        <section class="slide" data-theme="food">
            <div class="content">
                <div class="eyebrow">FOOD · FOOD · FOOD 🍜</div>
                <h2 class="section-title">Nuestros<br>lugares</h2>
                <p class="section-text">Porque una relación también se construye alrededor de una mesa.</p>
                <div class="places">
                    <div class="place"><div class="place-number">01</div><div class="place-name">Ninja Ramen</div><div class="place-description">Uno de esos lugares que se volvieron parte de nuestros momentos juntos.</div></div>
                    <div class="place"><div class="place-number">02</div><div class="place-name">Ryu Ramen House</div><div class="place-description">Comida, plática y tiempo juntos.</div></div>
                    <div class="place"><div class="place-number">03</div><div class="place-name">Trueke Comida & Amigos</div><div class="place-description">Otra pequeña aventura guardada dentro de nuestra historia.</div></div>
                </div>
            </div>
        </section>

        <section class="slide" data-theme="music">
            <div class="content">
                <div class="eyebrow">SOUNDTRACK 🎵</div>
                <h2 class="section-title">Nuestra<br>banda sonora</h2>
                <p class="section-text">11 canciones que terminaron formando parte de nuestra historia.</p>
                <div class="album"></div>
                <div class="featured-song">
                    <div class="song-number" id="songNumber">--</div>
                    <div class="song-title" id="songTitle">--</div>
                    <div class="song-artist" id="songArtist">--</div>
                    <div class="song-meaning" id="songMeaning">--</div>
                </div>
            </div>
        </section>

        <section class="slide" data-theme="gallery">
            <div class="content">
                <div class="eyebrow">MEMORIES 📸</div>
                <h2 class="section-title">Nuestros<br>recuerdos</h2>
                <div class="gallery-photo" id="galleryPhoto"></div>
                <div id="galleryCaption" class="section-text"></div>
            </div>
        </section>

        <section class="slide" data-theme="final">
            <div class="content">
                <div class="eyebrow">Y ESTO APENAS ES UNA PARTE</div>
                <div class="final-title">Gracias por<br>estos 3 años ❤️</div>
                <div class="days-label">Faltan aproximadamente</div>
                <div class="days-number" id="daysNumber">--</div>
                <div class="days-label">días para nuestro próximo aniversario 💫</div>
                <div class="quote">
                    Y si pudiera volver al 24 de julio de 2023, volvería a elegir comenzar esta historia contigo.
                </div>
            </div>
        </section>
    </div>

    <button id="musicControl" type="button" aria-label="Música">
        <div class="sound-bars" id="soundBars">
            <div class="sound-bar"></div>
            <div class="sound-bar"></div>
            <div class="sound-bar"></div>
        </div>
    </button>
</div>

__AUDIO_HTML__

<script>
const DATA = __DATOS_JSON__;

const app = document.getElementById("app");
const slides = Array.from(document.querySelectorAll(".slide"));
const progress = document.getElementById("progress");
const counter = document.getElementById("counter");
const background = document.getElementById("background");
const music = document.getElementById("backgroundMusic");
const musicControl = document.getElementById("musicControl");
const soundBars = document.getElementById("soundBars");
const ambient = document.getElementById("ambient");
const celebration = document.getElementById("celebration");
const effects = document.getElementById("effects");
const transitionGlow = document.getElementById("transitionGlow");
const reducedMotion = window.matchMedia("(prefers-reduced-motion: reduce)");

// Pocas partículas a la vez y se eliminan al terminar: apto para celulares.
function removeAfterAnimation(element) {
    element.addEventListener("animationend", function () { element.remove(); }, { once: true });
}

function setUpAmbient() {
    if (reducedMotion.matches) return;
    for (let i = 0; i < 9; i++) {
        const light = document.createElement("span");
        light.className = "ambient-light";
        light.style.left = (7 + ((i * 37) % 87)) + "%";
        light.style.top = (8 + ((i * 41) % 78)) + "%";
        light.style.setProperty("--twinkle-time", (4.5 + (i % 4)) + "s");
        light.style.setProperty("--twinkle-delay", (-i * .73) + "s");
        ambient.appendChild(light);
    }
}

function transitionSparkles() {
    if (reducedMotion.matches) return;
    transitionGlow.classList.remove("transition-flash");
    void transitionGlow.offsetWidth;
    transitionGlow.classList.add("transition-flash");

    const amount = window.innerWidth < 600 ? 7 : 12;
    for (let i = 0; i < amount; i++) {
        const star = document.createElement("span");
        star.className = "sparkle";
        star.style.left = (12 + Math.random() * 76) + "%";
        star.style.top = (12 + Math.random() * 72) + "%";
        star.style.setProperty("--size", (2 + Math.random() * 3) + "px");
        star.style.setProperty("--travel-x", ((Math.random() - .5) * 68) + "px");
        star.style.setProperty("--travel-y", (-20 - Math.random() * 60) + "px");
        star.style.setProperty("--lifetime", (650 + Math.random() * 500) + "ms");
        effects.appendChild(star);
        removeAfterAnimation(star);
    }
}

function showerConfetti(amount) {
    if (reducedMotion.matches) return;
    const colors = ["#ffcae4", "#ffd447", "#a684ff", "#9af6e4"];
    for (let i = 0; i < amount; i++) {
        const piece = document.createElement("span");
        piece.className = "confetti";
        piece.style.left = (5 + Math.random() * 90) + "%";
        piece.style.setProperty("--particle-color", colors[i % colors.length]);
        piece.style.setProperty("--travel-x", ((Math.random() - .5) * 90) + "px");
        piece.style.setProperty("--rotation", (180 + Math.random() * 520) + "deg");
        piece.style.setProperty("--delay", (Math.random() * 350) + "ms");
        piece.style.setProperty("--lifetime", (2400 + Math.random() * 1200) + "ms");
        effects.appendChild(piece);
        removeAfterAnimation(piece);
    }
}

function showBalloons() {
    celebration.replaceChildren();
    if (reducedMotion.matches) return;
    const colors = ["#ff77ba", "#b897ff", "#ffd271", "#ff9dcf"];
    const amount = window.innerWidth < 600 ? 3 : 5;
    for (let i = 0; i < amount; i++) {
        const balloon = document.createElement("span");
        balloon.className = "balloon";
        balloon.style.left = (6 + i * (88 / amount)) + "%";
        balloon.style.setProperty("--balloon-color", colors[i % colors.length]);
        balloon.style.setProperty("--rise-time", (14 + i * 2) + "s");
        balloon.style.setProperty("--delay", (-i * 2.7) + "s");
        celebration.appendChild(balloon);
    }
}

setUpAmbient();

let current = 0;
let galleryIndex = 0;
let musicIndex = 0;
let photoIndexes = { december: 0, year2024: 0, year2025: 0 };

const ITEM_DURATION = 3500;
const DEFAULT_SLIDE_DURATION = 7500;

let storyTimer = null;
let contentTimer = null;
let storyStartedAt = 0;
let storyDuration = DEFAULT_SLIDE_DURATION;
let storyRemaining = DEFAULT_SLIDE_DURATION;
let storyPaused = false;

const themes = {
    cover: "radial-gradient(circle at 20% 15%, #ff2d75 0%, transparent 32%), radial-gradient(circle at 85% 80%, #7738ff 0%, transparent 38%), linear-gradient(145deg,#17040d,#08030c)",
    stats: "radial-gradient(circle at 20% 20%, #ff8a00 0%, transparent 30%), radial-gradient(circle at 90% 70%, #ff2d75 0%, transparent 35%), linear-gradient(145deg,#16080b,#09030b)",
    start: "radial-gradient(circle at 75% 15%, #ffbd3d 0%, transparent 30%), radial-gradient(circle at 20% 80%, #ff2d75 0%, transparent 35%), linear-gradient(145deg,#1a0c04,#0b0408)",
    concert: "radial-gradient(circle at 20% 25%, #7a38ff 0%, transparent 35%), radial-gradient(circle at 80% 80%, #ff2d75 0%, transparent 35%), linear-gradient(145deg,#0d061b,#08030c)",
    december: "radial-gradient(circle at 20% 15%, #00a6a6 0%, transparent 30%), radial-gradient(circle at 90% 80%, #ff2d75 0%, transparent 35%), linear-gradient(145deg,#041313,#09040c)",
    year2024: "radial-gradient(circle at 20% 15%, #ff2d75 0%, transparent 30%), radial-gradient(circle at 85% 25%, #ffbd3d 0%, transparent 32%), linear-gradient(145deg,#17040e,#09030b)",
    year2025: "radial-gradient(circle at 80% 20%, #9b52ff 0%, transparent 35%), radial-gradient(circle at 15% 85%, #ff2d75 0%, transparent 35%), linear-gradient(145deg,#0e0619,#08030c)",
    food: "radial-gradient(circle at 20% 20%, #ff8a00 0%, transparent 30%), radial-gradient(circle at 85% 85%, #ffd447 0%, transparent 30%), linear-gradient(145deg,#170903,#09040a)",
    music: "radial-gradient(circle at 20% 20%, #ff2d75 0%, transparent 35%), radial-gradient(circle at 85% 75%, #8c52ff 0%, transparent 38%), linear-gradient(145deg,#17051b,#08030d)",
    gallery: "radial-gradient(circle at 80% 20%, #00a6a6 0%, transparent 35%), radial-gradient(circle at 15% 80%, #ff2d75 0%, transparent 35%), linear-gradient(145deg,#031313,#08030c)",
    final: "radial-gradient(circle at 20% 20%, #ff2d75 0%, transparent 35%), radial-gradient(circle at 80% 80%, #8c52ff 0%, transparent 40%), linear-gradient(145deg,#17030e,#08030d)"
};

function createProgress() {
    progress.innerHTML = "";
    slides.forEach(function () {
        const bar = document.createElement("div");
        bar.className = "progress-bar";
        const fill = document.createElement("div");
        fill.className = "progress-fill";
        bar.appendChild(fill);
        progress.appendChild(bar);
    });
}
createProgress();

function renderPhoto(elementId, image, caption) {
    const element = document.getElementById(elementId);
    if (!element || !image) return;
    element.innerHTML = `<img src="${image}" draggable="false">${caption ? `<div class="photo-caption">${caption}</div>` : ""}`;
}

if (DATA.imagenes.inicio) renderPhoto("inicioPhoto", DATA.imagenes.inicio, "El comienzo de nosotros ❤️");
if (DATA.imagenes.caifanes) renderPhoto("caifanesPhoto", DATA.imagenes.caifanes, "Una noche para recordar 🎸❤️");

function renderDecember() {
    const images = DATA.imagenes.diciembre_2023 || [];
    if (!images.length) return;
    const index = photoIndexes.december % images.length;
    renderPhoto("decemberPhoto", images[index], DATA.captions.diciembre_2023[index]);
}

function render2024() {
    const images = DATA.imagenes.y2024 || [];
    if (!images.length) return;
    const index = photoIndexes.year2024 % images.length;
    renderPhoto("year2024Photo", images[index], DATA.captions.y2024[index]);
}

function render2025() {
    const images = DATA.imagenes.y2025_2026 || [];
    if (!images.length) return;
    const index = photoIndexes.year2025 % images.length;
    renderPhoto("year2025Photo", images[index], DATA.captions.y2025_2026[index]);
}

// NUEVA FUNCIÓN PARA RENDERIZAR LA MÚSICA DINÁMICA
function renderMusic() {
    const songs = DATA.canciones || [];
    if (!songs.length) return;
    const index = musicIndex % songs.length;
    const song = songs[index];

    const num = document.getElementById("songNumber");
    const title = document.getElementById("songTitle");
    const artist = document.getElementById("songArtist");
    const meaning = document.getElementById("songMeaning");

    if (num) num.textContent = "CANCIÓN #" + String(index + 1).padStart(2, "0");
    if (title) title.textContent = song.titulo;
    if (artist) artist.textContent = song.artista;
    if (meaning) meaning.textContent = song.significado;
}

function renderGallery() {
    const images = DATA.imagenes.galeria || [];
    const photo = document.getElementById("galleryPhoto");
    const caption = document.getElementById("galleryCaption");
    if (!photo || !caption) return;
    if (!images.length) {
        photo.innerHTML = "";
        caption.textContent = "Agrega fotografías a fotos/galeria";
        return;
    }
    const index = galleryIndex % images.length;
    photo.innerHTML = `<img src="${images[index]}" draggable="false">`;
    caption.textContent = "Recuerdo " + (index + 1) + " de " + images.length;
}

function updateDays() {
    const now = new Date();
    let year = now.getFullYear();
    let anniversary = new Date(year, 8, 23);
    if (anniversary <= now) anniversary = new Date(year + 1, 8, 23);
    const difference = anniversary - now;
    const days = Math.ceil(difference / (1000 * 60 * 60 * 24));
    const element = document.getElementById("daysNumber");
    if (element) element.textContent = days;
}
updateDays();

function getSlideDuration(index) {
    if (index === slides.length - 1) return 0;

    if (index === 4) {
        const total = (DATA.imagenes.diciembre_2023 || []).length;
        return Math.max(DEFAULT_SLIDE_DURATION, total * ITEM_DURATION);
    }
    if (index === 5) {
        const total = (DATA.imagenes.y2024 || []).length;
        return Math.max(DEFAULT_SLIDE_DURATION, total * ITEM_DURATION);
    }
    if (index === 6) {
        const total = (DATA.imagenes.y2025_2026 || []).length;
        return Math.max(DEFAULT_SLIDE_DURATION, total * ITEM_DURATION);
    }
    if (index === 8) {
        const total = (DATA.canciones || []).length;
        return Math.max(DEFAULT_SLIDE_DURATION, total * ITEM_DURATION);
    }
    if (index === 9) {
        const total = (DATA.imagenes.galeria || []).length;
        return Math.max(DEFAULT_SLIDE_DURATION, total * ITEM_DURATION);
    }

    if (index === 1 || index === 7) return 9000;
    return DEFAULT_SLIDE_DURATION;
}

function stopTimers() {
    if (storyTimer) {
        clearTimeout(storyTimer);
        storyTimer = null;
    }
    if (contentTimer) {
        clearInterval(contentTimer);
        contentTimer = null;
    }
}

function updateProgressBars(duration, remaining = duration) {
    const bars = Array.from(document.querySelectorAll(".progress-fill"));

    bars.forEach(function (bar, i) {
        bar.style.transition = "none";

        if (i < current) {
            bar.style.width = "100%";
        } else {
            bar.style.width = "0%";
        }
    });

    const activeBar = bars[current];
    if (!activeBar) return;

    if (duration === 0) {
        activeBar.style.width = "100%";
        return;
    }

    const elapsedFraction = Math.max(0, Math.min(1, 1 - (remaining / duration)));
    activeBar.style.width = (elapsedFraction * 100) + "%";

    void activeBar.offsetWidth;

    activeBar.style.transition = `width ${remaining}ms linear`;
    activeBar.style.width = "100%";
}

function resetSectionContent(index) {
    if (index === 4) {
        photoIndexes.december = 0;
        renderDecember();
    }
    if (index === 5) {
        photoIndexes.year2024 = 0;
        render2024();
    }
    if (index === 6) {
        photoIndexes.year2025 = 0;
        render2025();
    }
    if (index === 8) {
        musicIndex = 0;
        renderMusic();
    }
    if (index === 9) {
        galleryIndex = 0;
        renderGallery();
    }
}

function startContentRotation() {
    if (contentTimer) clearInterval(contentTimer);

    contentTimer = setInterval(function () {
        if (storyPaused) return;

        if (current === 4) {
            const images = DATA.imagenes.diciembre_2023 || [];
            if (images.length > 1) {
                photoIndexes.december = (photoIndexes.december + 1) % images.length;
                renderDecember();
            }
        }

        if (current === 5) {
            const images = DATA.imagenes.y2024 || [];
            if (images.length > 1) {
                photoIndexes.year2024 = (photoIndexes.year2024 + 1) % images.length;
                render2024();
            }
        }

        if (current === 6) {
            const images = DATA.imagenes.y2025_2026 || [];
            if (images.length > 1) {
                photoIndexes.year2025 = (photoIndexes.year2025 + 1) % images.length;
                render2025();
            }
        }

        if (current === 8) {
            const songs = DATA.canciones || [];
            if (songs.length > 1) {
                musicIndex = (musicIndex + 1) % songs.length;
                renderMusic();
            }
        }

        if (current === 9) {
            const images = DATA.imagenes.galeria || [];
            if (images.length > 1) {
                galleryIndex = (galleryIndex + 1) % images.length;
                renderGallery();
            }
        }
    }, ITEM_DURATION);
}

function startStoryTimer(customRemaining = null) {
    if (storyTimer) clearTimeout(storyTimer);

    storyDuration = getSlideDuration(current);
    storyRemaining = customRemaining === null ? storyDuration : customRemaining;
    storyStartedAt = performance.now();
    storyPaused = false;

    updateProgressBars(storyDuration, storyRemaining);

    if (storyDuration === 0) {
        if (contentTimer) {
            clearInterval(contentTimer);
            contentTimer = null;
        }
        return;
    }

    storyTimer = setTimeout(function () {
        storyTimer = null;
        if (current < slides.length - 1) {
            showSlide(current + 1, 1, true);
        }
    }, storyRemaining);
}

function pauseStory() {
    if (storyPaused || storyDuration === 0) return;

    storyPaused = true;

    if (storyTimer) {
        clearTimeout(storyTimer);
        storyTimer = null;
    }

    const elapsed = performance.now() - storyStartedAt;
    storyRemaining = Math.max(0, storyRemaining - elapsed);

    const activeBar = document.querySelectorAll(".progress-fill")[current];
    if (activeBar) {
        const computedWidth = getComputedStyle(activeBar).width;
        const parentWidth = activeBar.parentElement.getBoundingClientRect().width || 1;
        const pct = (parseFloat(computedWidth) / parentWidth) * 100;
        activeBar.style.transition = "none";
        activeBar.style.width = pct + "%";
    }
}

function resumeStory() {
    if (!storyPaused || storyDuration === 0) return;

    storyPaused = false;
    storyStartedAt = performance.now();

    const activeBar = document.querySelectorAll(".progress-fill")[current];
    if (activeBar) {
        void activeBar.offsetWidth;
        activeBar.style.transition = `width ${storyRemaining}ms linear`;
        activeBar.style.width = "100%";
    }

    storyTimer = setTimeout(function () {
        storyTimer = null;
        if (current < slides.length - 1) {
            showSlide(current + 1, 1, true);
        }
    }, storyRemaining);
}

function showSlide(index, direction, automatic = false) {
    if (index < 0 || index >= slides.length || index === current) return;

    stopTimers();

    const oldSlide = slides[current];
    const newSlide = slides[index];

    oldSlide.classList.remove("active", "previous");
    if (direction < 0) oldSlide.classList.add("previous");

    newSlide.classList.remove("previous");
    newSlide.classList.add("active");

    current = index;
    celebration.replaceChildren();
    transitionSparkles();
    if (current === slides.length - 1) {
        showBalloons();
        showerConfetti(window.innerWidth < 600 ? 16 : 25);
    }
    if (current === 0) showerConfetti(window.innerWidth < 600 ? 7 : 12);

    const theme = newSlide.dataset.theme;
    if (background && themes[theme]) background.style.background = themes[theme];

    counter.textContent =
        String(current + 1).padStart(2, "0") +
        " / " +
        String(slides.length).padStart(2, "0");

    resetSectionContent(current);
    startContentRotation();
    startStoryTimer();
}

background.style.background = themes.cover;
showerConfetti(window.innerWidth < 600 ? 7 : 12);

// Primera renderización inicial.
renderDecember();
render2024();
render2025();
renderMusic();
renderGallery();

function nextSlide() {
    if (current < slides.length - 1) showSlide(current + 1, 1, false);
}

function previousSlide() {
    if (current > 0) showSlide(current - 1, -1, false);
}

// Iniciar automáticamente como una historia tipo Wrapped.
resetSectionContent(0);
startContentRotation();
startStoryTimer();

let touchStartX = 0;
let touchStartY = 0;
let touchStartedAt = 0;
let touching = false;
let holdTimer = null;

app.addEventListener("touchstart", function (event) {
    if (!event.touches.length) return;

    touchStartX = event.touches[0].clientX;
    touchStartY = event.touches[0].clientY;
    touchStartedAt = performance.now();
    touching = true;

    holdTimer = setTimeout(function () {
        if (touching) pauseStory();
    }, 220);
}, { passive: true });

app.addEventListener("touchmove", function (event) {
    if (!touching) return;
    event.preventDefault();
}, { passive: false });

app.addEventListener("touchend", function (event) {
    if (!touching) return;

    touching = false;
    if (holdTimer) {
        clearTimeout(holdTimer);
        holdTimer = null;
    }

    const touch = event.changedTouches[0];
    const deltaX = touch.clientX - touchStartX;
    const deltaY = touch.clientY - touchStartY;
    const heldFor = performance.now() - touchStartedAt;

    if (storyPaused) {
        resumeStory();
        if (heldFor >= 220) return;
    }

    if (Math.abs(deltaX) >= 45 && Math.abs(deltaX) > Math.abs(deltaY)) {
        if (deltaX < 0) nextSlide();
        else previousSlide();
        return;
    }

    // Toque corto: izquierda retrocede, derecha avanza.
    if (heldFor < 220) {
        if (touch.clientX < window.innerWidth * 0.32) previousSlide();
        else if (touch.clientX > window.innerWidth * 0.68) nextSlide();
    }
}, { passive: true });

app.addEventListener("mousedown", function (event) {
    if (event.target.closest("#musicControl")) return;
    holdTimer = setTimeout(pauseStory, 220);
});

app.addEventListener("mouseup", function (event) {
    if (event.target.closest("#musicControl")) return;

    if (holdTimer) {
        clearTimeout(holdTimer);
        holdTimer = null;
    }

    if (storyPaused) {
        resumeStory();
        return;
    }

    if (window.innerWidth >= 800) {
        if (event.clientX < window.innerWidth / 2) previousSlide();
        else nextSlide();
    }
});

document.addEventListener("keydown", function (event) {
    if (event.key === "ArrowRight") nextSlide();
    if (event.key === "ArrowLeft") previousSlide();

    if (event.key === " ") {
        event.preventDefault();
        if (storyPaused) resumeStory();
        else pauseStory();
    }
});

document.addEventListener("visibilitychange", function () {
    if (document.hidden) {
        pauseStory();
    } else if (storyPaused) {
        resumeStory();
    }
});

let musicStarted = false;
function startMusic() {
    if (!music || musicStarted) return;
    music.play().then(function () {
        musicStarted = true;
        if (soundBars) soundBars.classList.add("music-playing");
    }).catch(function () {});
}

app.addEventListener("touchstart", startMusic, { once: true, passive: true });
app.addEventListener("click", startMusic, { once: true });

if (musicControl) {
    musicControl.addEventListener("click", function (event) {
        event.stopPropagation();
        if (!music) return;
        if (music.paused) {
            music.play().then(function () {
                if (soundBars) soundBars.classList.add("music-playing");
            }).catch(function () {});
        } else {
            music.pause();
            if (soundBars) soundBars.classList.remove("music-playing");
        }
    });
}
</script>
</body>
</html>
"""

# Reemplazamos los datos de manera limpia, sin romper el HTML/JS
HTML = HTML_TEMPLATE.replace("__DATOS_JSON__", DATOS_JSON).replace("__AUDIO_HTML__", AUDIO_HTML)

# ============================================================
# RENDER STREAMLIT CON PANTALLA COMPLETA NATIVA
# ============================================================

components.html(
    HTML,
    height=800,
    scrolling=False
)
