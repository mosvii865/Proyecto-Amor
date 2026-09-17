# -*- coding: utf-8 -*-
"""
Nuestro Wrapped 💫 — 3 Años Juntos
-----------------------------------
App en Streamlit estilo "Spotify Wrapped" para celebrar el aniversario.
Un solo archivo: streamlit + Pillow.

Cómo correrla:
    pip install -r requirements.txt
    streamlit run app.py

Organiza tus fotos en la carpeta fotos/ (ver el mensaje de instrucciones
que acompaña este código para la estructura exacta).
"""

import os
import glob
from datetime import date

import streamlit as st
from PIL import Image, ImageOps

# =============================================================================
# CONFIGURACIÓN GENERAL
# =============================================================================

st.set_page_config(
    page_title="Nuestro Wrapped · 3 Años",
    page_icon="💫",
    layout="centered",
    initial_sidebar_state="collapsed",
)

FOTOS_DIR = "fotos"
GALERIA_DIR = os.path.join(FOTOS_DIR, "galeria")

# Mapa de fotos "ancla" por capítulo. Si el archivo no existe, se muestra
# un placeholder elegante en su lugar — la app nunca truena por fotos faltantes.
IMAGENES = {
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

CAPTIONS_DICIEMBRE = ["En el pueblo de mi papá, contigo 🏡", "Rompiendo la piñata juntos 🎉", "Rumbo a Mazatlán 🌊"]
CAPTIONS_2024 = [
    "Emprendiendo con las togas SHESPAT 🎓",
    "Enseñándome a manejar la moto 🏍️",
    "Mi cambio de look, gracias a ti 💇",
    "Nuestra primera Navidad juntos 🎄",
]
CAPTIONS_2025_2026 = ["El reloj para mi papá 🎁", "Carajo y Nena, nuestros conejitos 🐰", "La feria y la rueda de la fortuna 🎡"]

# Paleta: cada capítulo tiene su propio par de acentos, como en un Wrapped real.
ACENTOS = {
    "portada": ("#FF3E7F", "#8C52FF"),
    "inicio": ("#FF8A4C", "#FF3E7F"),
    "caifanes": ("#FFC857", "#FF3E7F"),
    "diciembre_2023": ("#2FD5C4", "#8C52FF"),
    "y2024": ("#FFC857", "#FF8A4C"),
    "y2025_2026": ("#2FD5C4", "#FF3E7F"),
    "gastronomia": ("#FF8A4C", "#FFC857"),
    "playlist": ("#8C52FF", "#FF3E7F"),
    "galeria": ("#2FD5C4", "#FFC857"),
    "cierre": ("#FF3E7F", "#8C52FF"),
}

# Canciones clave con reproductor incrustado (IDs tomados de tus enlaces de YouTube Music).
CANCIONES = [
    {
        "titulo": "Time to Love (Tiempo para Amarte)",
        "artista": "Laureano Brizuela",
        "significado": (
            "A pesar de las cuentas y el estrés diario, siempre quiero guardar tiempo "
            "para amarte otra vez, para que nos amemos y sigamos juntos para siempre."
        ),
        "video_id": "fue4mYwJjeU",
    },
    {
        "titulo": "My One and Only Love / They Say It's Wonderful",
        "artista": "John Coltrane",
        "significado": (
            "Mi descubrimiento personal del amor: el paso de escuchar hablar de él a "
            "sentirlo por primera vez, contigo. Me hiciste experimentar un amor muy bonito."
        ),
        "video_id": "qA_vm6NpSZY",
    },
    {
        "titulo": "I Only Have Eyes for You",
        "artista": "Louis Armstrong",
        "significado": "Dedicada a ti, el amor de mi vida.",
        "video_id": None,
    },
    {
        "titulo": "Eso y Más",
        "artista": "Joan Sebastián",
        "significado": "No importa qué, haría lo que sea e incluso más por ti.",
        "video_id": "kz_HWReUrFA",
    },
    {
        "titulo": "Diséñame",
        "artista": "Joan Sebastián",
        "significado": "Como 'Eso y Más', me recuerda que no hay límite para lo que haría por ti.",
        "video_id": None,
    },
    {
        "titulo": "The Nearness of You",
        "artista": "Ella Fitzgerald & Louis Armstrong",
        "significado": "Tu cercanía es la sensación más hermosa que podría experimentar.",
        "video_id": None,
    },
    {
        "titulo": "Only You",
        "artista": "The Platters",
        "significado": "Solamente tú has hecho que sienta un amor y una atracción tan grandes.",
        "video_id": None,
    },
    {
        "titulo": "Eres",
        "artista": "José María Napoleón",
        "significado": "Eres la respuesta de todo en mi vida: mi camino, mi hogar, mi guía, mi todo.",
        "video_id": None,
    },
    {
        "titulo": "Mi Mundo Tú",
        "artista": "Camilo Sesto",
        "significado": "Para recordarte que tú eres todo mi mundo.",
        "video_id": None,
    },
    {
        "titulo": "Cama y Mesa",
        "artista": "Roberto Carlos",
        "significado": (
            "El deseo de ser tu todo, de que solo me veas y me sientas a mí desde la "
            "mañana hasta el anochecer."
        ),
        "video_id": None,
    },
    {
        "titulo": "Invítame un cigarro",
        "artista": "(agrega aquí el artista o versión que prefieras)",
        "significado": (
            "✏️ Todavía no tengo guardado qué significa esta para ti — cuéntamelo y "
            "la personalizo."
        ),
        "video_id": None,
    },
]

RESTAURANTES = [
    {"nombre": "Ninja Ramen", "emoji": "🍥", "nota": "Nuestro lugar más frecuente. El Sushi Hot Panko aquí es sagrado para nosotros."},
    {"nombre": "Ryu Ramen House", "emoji": "🍜", "nota": "Otra parada obligada en nuestras citas."},
    {"nombre": "Trueke Comida & Amigos", "emoji": "🥢", "nota": "Buena comida, mejor compañía: la tuya."},
]


# =============================================================================
# ESTILOS (CSS)
# =============================================================================

def inyectar_css():
    st.markdown(
        """
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Unbounded:wght@500;600;700;800;900&family=Manrope:wght@400;500;600;700&display=swap');

        html, body, [class*="css"] { font-family: 'Manrope', sans-serif; }

        .stApp {
            background: linear-gradient(160deg, #0B0714 0%, #1C0F2E 55%, #2B0F1F 100%);
            background-attachment: fixed;
            color: #F5F1EC;
        }

        #MainMenu, header[data-testid="stHeader"], footer { visibility: hidden; height: 0; }

        [data-testid="stAppViewContainer"] .main .block-container {
            max-width: 640px;
            padding-top: 2rem;
            padding-bottom: 1rem;
        }

        [data-testid="stSidebar"] { background: #0B0714; }

        @keyframes fadeInUp {
            from { opacity: 0; transform: translateY(16px); }
            to { opacity: 1; transform: translateY(0); }
        }

        @media (prefers-reduced-motion: reduce) {
            * { animation: none !important; opacity: 1 !important; transform: none !important; }
        }

        /* Toda foto (st.image) entra con el mismo desvanecimiento suave */
        [data-testid="stImage"] img {
            animation: fadeInUp 0.6s ease both;
            border-radius: 14px;
        }

        /* ---------- Encabezado de capítulo ---------- */
        .emoji-badge { font-size: 2.4rem; line-height: 1; margin-bottom: 0.35rem; }
        .chapter-title { font-family: 'Unbounded', sans-serif; font-weight: 800; font-size: 2.1rem; line-height: 1.12; margin: 0 0 0.3rem 0; }
        .chapter-sub { color: #B8AEC4; font-size: 0.98rem; margin-bottom: 1.4rem; }

        /* ---------- Bloques de anécdota (sin caja, solo borde vivo) ---------- */
        .anecdote { border-left: 3px solid rgba(255,255,255,0.25); padding: 0.15rem 0 0.15rem 1.1rem; margin: 0 0 1.5rem 0; font-size: 1.02rem; line-height: 1.62; color: #EDE7F6; }

        /* ---------- Fotos ---------- */
        .img-caption { text-align: center; font-size: 0.88rem; color: #B8AEC4; font-style: italic; margin-top: 0.4rem; margin-bottom: 1.3rem; }
        .img-placeholder { display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 0.4rem; border: 1.5px dashed rgba(255,255,255,0.22); border-radius: 16px; padding: 2.2rem 1rem; margin-bottom: 1.3rem; color: #8B8299; font-size: 0.92rem; text-align: center; }

        /* ---------- Franja de estadísticas (estilo boleto) ---------- */
        .stats-row { display: flex; flex-wrap: wrap; gap: 0; margin: 1.6rem 0 1.8rem 0; border-top: 1px dashed rgba(255,255,255,0.2); border-bottom: 1px dashed rgba(255,255,255,0.2); padding: 1.1rem 0; }
        .stat-item { flex: 1 1 25%; min-width: 110px; text-align: center; padding: 0.3rem 0.4rem; border-right: 1px solid rgba(255,255,255,0.12); }
        .stat-item:last-child { border-right: none; }
        .stat-num { font-family: 'Unbounded', sans-serif; font-weight: 800; font-size: 1.7rem; background: linear-gradient(90deg, #FF3E7F, #8C52FF); -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text; }
        .stat-label { font-size: 0.78rem; color: #B8AEC4; margin-top: 0.15rem; }

        /* ---------- Puntos de progreso (tipo stories) ---------- */
        .dots-container { display: flex; gap: 6px; justify-content: center; margin-bottom: 1.6rem; }
        .dot { height: 5px; width: 20px; border-radius: 4px; background: rgba(255,255,255,0.15); transition: all 0.25s ease; }
        .dot.active { width: 34px; background: linear-gradient(90deg, #FF3E7F, #FFC857); }

        /* ---------- Filas de canciones (playlist) ---------- */
        .track-row { display: flex; gap: 0.9rem; align-items: flex-start; padding: 0.9rem 0; border-bottom: 1px solid rgba(255,255,255,0.08); }
        .track-num { font-family: 'Unbounded', sans-serif; font-weight: 700; font-size: 0.95rem; color: #8B8299; min-width: 1.6rem; padding-top: 0.15rem; }
        .track-title { font-weight: 700; font-size: 1rem; color: #F5F1EC; }
        .track-artist { font-size: 0.85rem; color: #B8AEC4; margin-bottom: 0.3rem; }
        .track-meaning { font-size: 0.92rem; color: #D8D0E6; line-height: 1.5; }

        /* ---------- Reproductor de YouTube ---------- */
        .player-label { font-size: 0.82rem; color: #B8AEC4; margin-bottom: 0.4rem; }
        .player-frame { border-radius: 14px; overflow: hidden; border: 1px solid rgba(255,255,255,0.1); }

        /* ---------- Tarjetas de restaurante (ticket) ---------- */
        .food-card { background: rgba(255,255,255,0.045); border: 1px solid rgba(255,255,255,0.08); border-radius: 14px; padding: 1rem 1.1rem; margin-bottom: 0.9rem; display: flex; gap: 0.8rem; align-items: flex-start; }
        .food-emoji { font-size: 1.6rem; }
        .food-name { font-weight: 700; font-size: 1.02rem; margin-bottom: 0.15rem; }
        .food-note { font-size: 0.9rem; color: #B8AEC4; line-height: 1.5; }

        /* ---------- Indicador de carrusel / paginación ---------- */
        .carousel-indicator { text-align: center; padding-top: 0.5rem; color: #B8AEC4; font-size: 0.85rem; }

        /* ---------- Botones de Streamlit ---------- */
        div[data-testid="stButton"] > button {
            border-radius: 999px; border: none; padding: 0.6rem 1rem; font-weight: 700;
            font-family: 'Manrope', sans-serif; transition: transform 0.15s ease, box-shadow 0.15s ease;
            animation: fadeInUp 0.5s ease both; animation-delay: 0.15s;
        }
        div[data-testid="stButton"] > button[kind="primary"] { background: linear-gradient(90deg, #FF3E7F, #8C52FF); color: white; box-shadow: 0 4px 18px rgba(255, 62, 127, 0.35); }
        div[data-testid="stButton"] > button[kind="primary"]:hover { transform: translateY(-2px) scale(1.01); box-shadow: 0 6px 22px rgba(255, 62, 127, 0.5); }
        div[data-testid="stButton"] > button[kind="secondary"] { background: rgba(255,255,255,0.06); color: #F5F1EC; border: 1px solid rgba(255,255,255,0.15); }
        div[data-testid="stButton"] > button[kind="secondary"]:hover { background: rgba(255,255,255,0.1); }

        @media (max-width: 640px) {
            .chapter-title { font-size: 1.65rem; }
            .stat-num { font-size: 1.4rem; }
            .stat-item { flex: 1 1 45%; }
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


# =============================================================================
# HELPERS
# =============================================================================

def _fade_style(delay_idx):
    """Devuelve un inline-style con animación de entrada y un retraso escalonado,
    para el efecto de 'cascada' al cargar cada diapositiva."""
    delay = min(delay_idx * 0.09, 0.6)
    return f"animation: fadeInUp 0.7s ease both; animation-delay: {delay:.2f}s; opacity:0;"


def encabezado(emoji, titulo, subtitulo="", delay=0):
    sub_html = f'<div class="chapter-sub">{subtitulo}</div>' if subtitulo else ""
    st.markdown(
        f"""
        <div style="{_fade_style(delay)}">
            <div class="emoji-badge">{emoji}</div>
            <div class="chapter-title">{titulo}</div>
            {sub_html}
        </div>
        """,
        unsafe_allow_html=True,
    )


def anecdota(texto, color="rgba(255,255,255,0.25)", delay=0):
    st.markdown(
        f'<div class="anecdote" style="border-left-color:{color}; {_fade_style(delay)}">{texto}</div>',
        unsafe_allow_html=True,
    )


def reproductor_youtube(video_id, titulo="", artista="", delay=0, alto=80):
    if not video_id:
        return
    etiqueta = ""
    if titulo:
        extra = f" · {artista}" if artista else ""
        etiqueta = f'<div class="player-label">🎵 {titulo}{extra}</div>'
    st.markdown(
        f"""
        <div style="{_fade_style(delay)} margin-bottom:1.3rem;">
            {etiqueta}
            <div class="player-frame">
                <iframe width="100%" height="{alto}"
                    src="https://www.youtube.com/embed/{video_id}?rel=0&autoplay=1"
                    frameborder="0" allow="autoplay; encrypted-media" allowfullscreen>
                </iframe>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def mostrar_foto(ruta, caption=""):
    """Muestra la foto si existe; si no, un placeholder elegante para que la
    app jamás se rompa por fotos faltantes."""
    if ruta and os.path.exists(ruta):
        try:
            img = Image.open(ruta)
            img = ImageOps.exif_transpose(img)
            st.image(img, use_container_width=True)
            if caption:
                st.markdown(f'<div class="img-caption">{caption}</div>', unsafe_allow_html=True)
            return
        except Exception:
            pass
    nombre_sugerido = os.path.basename(ruta) if ruta else "foto.png"
    st.markdown(
        f"""
        <div class="img-placeholder">
            <span style="font-size:2rem;">📷</span>
            <span>{caption or "Agrega tu foto aquí"}</span>
            <span style="font-size:0.78rem; opacity:0.7;">Colócala como <code>{FOTOS_DIR}/{nombre_sugerido}</code></span>
        </div>
        """,
        unsafe_allow_html=True,
    )


def crear_miniatura(ruta, tam=440):
    try:
        img = Image.open(ruta).convert("RGB")
        img = ImageOps.exif_transpose(img)
        img = ImageOps.fit(img, (tam, tam), method=Image.LANCZOS)
        return img
    except Exception:
        return None


def carrusel_fotos(key, rutas, captions=None):
    """Carrusel horizontal: una foto a la vez, con flechas y un indicador 'i / N'.
    Así navegas entre las fotos de la sección sin tener que hacer scroll."""
    if not rutas:
        return
    n = len(rutas)
    estado_key = f"carousel_{key}"
    if estado_key not in st.session_state:
        st.session_state[estado_key] = 0
    idx = st.session_state[estado_key] % n
    cap = captions[idx] if captions and idx < len(captions) else ""

    mostrar_foto(rutas[idx], caption=cap)

    if n > 1:
        col1, col2, col3 = st.columns([1, 2, 1])
        with col1:
            if st.button("◀", key=f"{estado_key}_prev", use_container_width=True):
                st.session_state[estado_key] = (idx - 1) % n
                st.rerun()
        with col2:
            st.markdown(f'<div class="carousel-indicator">{idx + 1} / {n}</div>', unsafe_allow_html=True)
        with col3:
            if st.button("▶", key=f"{estado_key}_next", use_container_width=True):
                st.session_state[estado_key] = (idx + 1) % n
                st.rerun()


def galeria_paginada(archivos, por_pagina=6, columnas=3):
    n = len(archivos)
    total_paginas = max(1, (n + por_pagina - 1) // por_pagina)
    estado_key = "galeria_pagina"
    if estado_key not in st.session_state:
        st.session_state[estado_key] = 0
    pagina = st.session_state[estado_key] % total_paginas
    lote = archivos[pagina * por_pagina: pagina * por_pagina + por_pagina]

    cols = st.columns(columnas)
    for i, ruta in enumerate(lote):
        miniatura = crear_miniatura(ruta)
        with cols[i % columnas]:
            st.image(miniatura if miniatura is not None else ruta, use_container_width=True)

    if total_paginas > 1:
        col1, col2, col3 = st.columns([1, 2, 1])
        with col1:
            if st.button("◀", key="galeria_prev", use_container_width=True):
                st.session_state[estado_key] = (pagina - 1) % total_paginas
                st.rerun()
        with col2:
            st.markdown(f'<div class="carousel-indicator">Página {pagina + 1} / {total_paginas}</div>', unsafe_allow_html=True)
        with col3:
            if st.button("▶", key="galeria_next", use_container_width=True):
                st.session_state[estado_key] = (pagina + 1) % total_paginas
                st.rerun()


def dias_para_aniversario():
    hoy = date.today()
    aniversario = date(hoy.year, 9, 23)
    if hoy > aniversario:
        aniversario = date(hoy.year + 1, 9, 23)
    return (aniversario - hoy).days


# =============================================================================
# PANTALLAS
# =============================================================================

def slide_portada():
    c1, c2 = ACENTOS["portada"]
    dias = dias_para_aniversario()
    if dias == 0:
        linea_fecha = "¡Hoy es nuestro aniversario! 🎉"
    elif dias == 1:
        linea_fecha = "Falta 1 día para nuestro aniversario 🎈"
    else:
        linea_fecha = f"Faltan {dias} días para nuestro aniversario 🎈"

    st.markdown(
        f"""
        <div style="{_fade_style(0)}">
            <div class="emoji-badge">💫</div>
            <div class="chapter-title" style="font-size:2.5rem;
                 background: linear-gradient(90deg, {c1}, {c2});
                 -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text;">
                Nuestro Wrapped
            </div>
            <div class="chapter-sub" style="font-size:1.05rem;">
                Feliz aniversario, amor mío. 3 años juntos, y contando cada día desde que
                empezamos a escribirnos el 24 de julio de 2023.<br>{linea_fecha}
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        f"""
        <div class="stats-row" style="{_fade_style(1)}">
            <div class="stat-item"><div class="stat-num">3</div><div class="stat-label">años juntos</div></div>
            <div class="stat-item"><div class="stat-num">11</div><div class="stat-label">canciones nuestras</div></div>
            <div class="stat-item"><div class="stat-num">3</div><div class="stat-label">lugares favoritos</div></div>
            <div class="stat-item"><div class="stat-num">2</div><div class="stat-label">conejitos (Carajo y Nena)</div></div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    reproductor_youtube("fue4mYwJjeU", "Time to Love (Tiempo para Amarte)", "Laureano Brizuela", delay=2)
    mostrar_foto(os.path.join(FOTOS_DIR, "portada.png"), caption="")

    if st.button("Comenzar el recorrido ▶", type="primary", use_container_width=True):
        st.session_state.slide = 1
        st.rerun()


def slide_inicio():
    c1, _ = ACENTOS["inicio"]
    encabezado("💬", "El inicio de todo", "24 de julio de 2023", delay=0)
    anecdota(
        "Todo empezó con una historia tuya: si yo reaccionaba, tú me escribías. Te "
        "contesté... y minutos después la borraste porque, según tú, &ldquo;solo iba "
        "para mí&rdquo; (jsjsjs). Así, sin planearlo, empezamos a hablar todos los días "
        "durante los siguientes tres meses hasta conocernos en persona.",
        color=c1, delay=1,
    )
    reproductor_youtube("qA_vm6NpSZY", "My One and Only Love", "John Coltrane", delay=2)
    mostrar_foto(IMAGENES["inicio"], caption="La captura que lo comenzó todo, contigo 📱")


def slide_caifanes():
    c1, _ = ACENTOS["caifanes"]
    encabezado("🎸", "La primera gran aventura", "Concierto de Caifanes", delay=0)
    anecdota(
        "Caifanes es tu banda favorita, y cuando supe que ibas a ir sola al concierto "
        "no lo pensé dos veces: moví cielo, mar y tierra para conseguir el dinero y no "
        "dejarte ir sin mí. Esa noche cantamos cada canción como si el mundo se hubiera "
        "detenido solo para nosotros.",
        color=c1, delay=1,
    )
    reproductor_youtube("kz_HWReUrFA", "Eso y Más", "Joan Sebastián", delay=2)
    mostrar_foto(IMAGENES["caifanes"], caption="En el concierto de Caifanes, contigo 🎶")


def slide_diciembre_2023():
    c1, _ = ACENTOS["diciembre_2023"]
    encabezado("🚐", "Diciembre 2023", "El viaje que lo cambió todo", delay=0)
    anecdota(
        "Renunciamos a nuestros trabajos —yo en Superette, tú en Del Río— para "
        "lanzarnos a un viaje con mi familia al pueblo de mi papá. Ahí conociste a "
        "todos y te acoplaste como si siempre hubieras sido parte de la familia: "
        "cocinando, rompiendo piñata, riendo sin parar.",
        color=c1, delay=1,
    )
    anecdota(
        "Después de la feria pasó algo bastante vergonzoso (jsjsjs), y ahí quedó "
        "clarísimo: por ti no me tiembla la mano para lavar, para ayudarte, para "
        "hacer lo que sea que necesites.",
        color=c1, delay=2,
    )
    anecdota(
        "De regreso paramos en Mazatlán, compartimos habitación y vivimos experiencias "
        "increíbles. Una noche íbamos muy rápido en la carretera, abriste la ventana y "
        "mi papá te regañó... con el tiempo entendimos que no fue con mala intención, jaja.",
        color=c1, delay=3,
    )
    carrusel_fotos("diciembre", IMAGENES["diciembre_2023"], CAPTIONS_DICIEMBRE)


def slide_2024():
    c1, _ = ACENTOS["y2024"]
    encabezado("🌙", "2024", "Togas, motos y los hijos de la luna", delay=0)
    anecdota("Junto con mi mamá emprendimos en la venta y renta de togas, estolas y birretes, además de camisetas personalizadas para SHESPAT.", color=c1, delay=1)
    anecdota("Conseguí mi moto y tú me enseñaste a manejarla como se debe. Verte con el casco puesto me daba tanta risa como ternura.", color=c1, delay=2)
    anecdota("Me ayudaste a vestirme mejor y a cuidar mi cabello: antes lo llevaba liso, y gracias a ti descubrí que ondulado me quedaba precioso.", color=c1, delay=3)
    anecdota("Fuimos juntos a la boda de la amiga de tu mamá, donde te veías preciosa, y en Halloween nos pintamos la cara para ir al Parque Central.", color=c1, delay=4)
    anecdota("Entramos a trabajar juntos al tercer turno en Commscope, convertidos oficialmente en los &ldquo;hijos de la luna&rdquo; 🌙.", color=c1, delay=5)
    anecdota("Pasamos nuestra primera Navidad juntos en tu casa: intercambio de regalos y estrenamos nuestras botas.", color=c1, delay=6)
    carrusel_fotos("y2024", IMAGENES["y2024"], CAPTIONS_2024)


def slide_2025_2026():
    c1, _ = ACENTOS["y2025_2026"]
    encabezado("🐰", "2025 y 2026", "Madurez, conejitos y nuevos looks", delay=0)
    anecdota(
        "Iniciamos el 2025 en el cumpleaños de mi papá, a quien le regalamos un reloj "
        "que le encantó. Tuvimos salidas llenas de momentos especiales —orejitas de "
        "conejo, el cuarto de luces— y en cada foto te veías más hermosa.",
        color=c1, delay=1,
    )
    anecdota(
        "En 2026 empezamos el año arreglándonos juntos para lo que venía. Te "
        "regalaron a Carajo y Nena, nuestros conejitos —sí, nuestros hijos 🐰.",
        color=c1, delay=2,
    )
    anecdota(
        "Te hiciste un cambio radical de look con cabello azul turquesa que te queda "
        "perfecto. Y vivimos una salida inolvidable a la feria, con esa foto icónica "
        "frente a la rueda de la fortuna.",
        color=c1, delay=3,
    )
    carrusel_fotos("y2025", IMAGENES["y2025_2026"], CAPTIONS_2025_2026)


def slide_gastronomia():
    encabezado("🍜", "Nuestro mapa gastronómico", "A donde siempre volvemos, juntos", delay=0)
    for i, r in enumerate(RESTAURANTES, start=1):
        st.markdown(
            f"""
            <div class="food-card" style="{_fade_style(i)}">
                <div class="food-emoji">{r['emoji']}</div>
                <div><div class="food-name">{r['nombre']}</div><div class="food-note">{r['nota']}</div></div>
            </div>
            """,
            unsafe_allow_html=True,
        )


def slide_playlist():
    encabezado("🎧", "Nuestra banda sonora", "Cada canción, una razón para amarte", delay=0)
    for i, cancion in enumerate(CANCIONES, start=1):
        st.markdown(
            f"""
            <div class="track-row" style="{_fade_style(i)}">
                <div class="track-num">{i:02d}</div>
                <div>
                    <div class="track-title">{cancion['titulo']}</div>
                    <div class="track-artist">{cancion['artista']}</div>
                    <div class="track-meaning">{cancion['significado']}</div>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )
        if cancion["video_id"]:
            reproductor_youtube(cancion["video_id"], alto=70)


def slide_galeria():
    encabezado("📸", "Galería de recuerdos", "Cada foto, un momento contigo", delay=0)
    extensiones = ("*.jpg", "*.jpeg", "*.png", "*.webp", "*.JPG", "*.JPEG", "*.PNG", "*.WEBP")
    archivos = []
    if os.path.isdir(GALERIA_DIR):
        for ext in extensiones:
            archivos.extend(glob.glob(os.path.join(GALERIA_DIR, ext)))
    archivos = sorted(set(archivos))

    if not archivos:
        st.markdown(
            f"""
            <div class="img-placeholder" style="padding:3rem 1rem;">
                <span style="font-size:2.2rem;">🖼️</span>
                <span>Aún no hay fotos en la galería</span>
                <span style="font-size:0.8rem; opacity:0.7;">Agrega tus imágenes en <code>{GALERIA_DIR}/</code> (cualquier nombre)</span>
            </div>
            """,
            unsafe_allow_html=True,
        )
        return

    galeria_paginada(archivos)


def slide_cierre():
    c1, c2 = ACENTOS["cierre"]
    st.markdown(
        f"""
        <div style="{_fade_style(0)}">
            <div class="emoji-badge">💫</div>
            <div class="chapter-title" style="background: linear-gradient(90deg, {c1}, {c2});
                 -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text;">
                Gracias por estos 3 años
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
    anecdota(
        "De una historia que se borró a los tres meses de mensajes, a un concierto, a "
        "un viaje que nos cambió, a ser &ldquo;hijos de la luna&rdquo;, a dos conejitos "
        "que ahora son nuestros hijos. Eres mi camino, mi hogar, mi guía, mi todo. "
        "Gracias por elegirme cada día, por quedarte, por seguir construyendo esto "
        "conmigo. Que vengan muchos años más juntos, amor mío. Feliz aniversario. 💫",
        color=c1, delay=1,
    )
    st.markdown(
        f"""
        <div class="stats-row" style="{_fade_style(2)}">
            <div class="stat-item"><div class="stat-num">3</div><div class="stat-label">años</div></div>
            <div class="stat-item"><div class="stat-num">∞</div><div class="stat-label">por venir</div></div>
        </div>
        """,
        unsafe_allow_html=True,
    )
    if st.button("🔄 Volver a vivirlo desde el inicio", type="secondary", use_container_width=True):
        st.session_state.slide = 0
        st.rerun()


# =============================================================================
# NAVEGACIÓN Y MAIN
# =============================================================================

SLIDES = [
    ("Portada", slide_portada),
    ("El inicio de todo", slide_inicio),
    ("Concierto de Caifanes", slide_caifanes),
    ("Diciembre 2023", slide_diciembre_2023),
    ("2024", slide_2024),
    ("2025 y 2026", slide_2025_2026),
    ("Gastronomía", slide_gastronomia),
    ("Nuestra banda sonora", slide_playlist),
    ("Galería de recuerdos", slide_galeria),
    ("Cierre", slide_cierre),
]


def render_puntos(idx, total):
    puntos = "".join(f'<div class="dot {"active" if i == idx else ""}"></div>' for i in range(total))
    st.markdown(f'<div class="dots-container">{puntos}</div>', unsafe_allow_html=True)


def render_navegacion(idx, total):
    st.write("")
    col1, col2 = st.columns(2)
    with col1:
        if idx > 0:
            if st.button("⬅ Anterior", use_container_width=True, key="nav_prev"):
                st.session_state.slide = idx - 1
                st.rerun()
    with col2:
        if idx < total - 1:
            if st.button("Siguiente ➡", type="primary", use_container_width=True, key="nav_next"):
                st.session_state.slide = idx + 1
                st.rerun()


def main():
    inyectar_css()

    if "slide" not in st.session_state:
        st.session_state.slide = 0

    total = len(SLIDES)
    idx = max(0, min(st.session_state.slide, total - 1))

    with st.sidebar:
        st.markdown("#### 🧭 Ir a una sección")
        titulos = [t for t, _ in SLIDES]
        seleccion = st.selectbox(" ", titulos, index=idx, label_visibility="collapsed")
        nueva_idx = titulos.index(seleccion)
        if nueva_idx != idx:
            st.session_state.slide = nueva_idx
            st.rerun()

    render_puntos(idx, total)
    SLIDES[idx][1]()
    render_navegacion(idx, total)

    if idx == total - 1:
        st.balloons()


if __name__ == "__main__":
    main()
