import os
import base64
import streamlit as st


# ============================================================
# CONFIGURACIÓN
# ============================================================

st.set_page_config(
    page_title="Nuestro Wrapped · 3 Años",
    page_icon="💫",
    layout="centered",
    initial_sidebar_state="collapsed"
)

FOTOS_DIR = "fotos"
GALERIA_DIR = os.path.join(FOTOS_DIR, "galeria")
MUSICA_FONDO = "musica.mp3"


# ============================================================
# FOTOS
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
# PLAYLIST
# ============================================================

CANCIONES = [
    {
        "titulo": "Tiempo para Amarte",
        "artista": "Laureano Brizuela",
        "significado": (
            "A pesar de las cuentas, el estrés diario y todas las cosas "
            "que tenemos que hacer, siempre quiero encontrar tiempo para ti."
        ),
        "video_id": None,
    },
    {
        "titulo": "My One and Only Love / They Say It's Wonderful",
        "artista": "John Coltrane",
        "significado": (
            "Mi descubrimiento personal del amor y una canción que terminó "
            "teniendo un significado muy especial para nosotros."
        ),
        "video_id": None,
    },
    {
        "titulo": "I Only Have Eyes for You",
        "artista": "Louis Armstrong",
        "significado": (
            "Porque entre todas las personas, lugares y cosas que existen, "
            "mis ojos siempre terminan buscándote a ti."
        ),
        "video_id": None,
    },
    {
        "titulo": "Eso y Más",
        "artista": "Joan Sebastián",
        "significado": (
            "Una canción que representa todo eso que siento y muchas veces "
            "no sé cómo decirte."
        ),
        "video_id": None,
    },
    {
        "titulo": "Diséñame",
        "artista": "Joan Sebastián",
        "significado": (
            "Porque de alguna manera nuestro amor fue construyéndose "
            "poco a poco, con nuestras propias historias."
        ),
        "video_id": None,
    },
    {
        "titulo": "The Nearness of You",
        "artista": "Ella Fitzgerald & Louis Armstrong",
        "significado": (
            "La cercanía de la persona que amas puede hacer que cualquier "
            "momento cotidiano se sienta especial."
        ),
        "video_id": None,
    },
    {
        "titulo": "Only You",
        "artista": "The Platters",
        "significado": (
            "Porque hay personas que simplemente se vuelven únicas "
            "en nuestra vida."
        ),
        "video_id": None,
    },
    {
        "titulo": "Eres",
        "artista": "José María Napoleón",
        "significado": (
            "Una forma de decirte todo lo que significas para mí."
        ),
        "video_id": None,
    },
    {
        "titulo": "Mi Mundo Tú",
        "artista": "Camilo Sesto",
        "significado": (
            "Porque después de estos años, eres una parte enorme "
            "de mi mundo."
        ),
        "video_id": None,
    },
    {
        "titulo": "Cama y Mesa",
        "artista": "Roberto Carlos",
        "significado": (
            "Una canción que habla de compartir la vida, los momentos "
            "íntimos y también los cotidianos."
        ),
        "video_id": None,
    },
    {
        "titulo": "Invítame un cigarro",
        "artista": "Tradicional / Popular",
        "significado": (
            "Una de esas canciones que terminan formando parte "
            "de nuestra historia."
        ),
        "video_id": None,
    },
]


# ============================================================
# RESTAURANTES
# ============================================================

RESTAURANTES = [
    {
        "nombre": "Ninja Ramen",
        "descripcion": (
            "Uno de esos lugares que se volvieron parte de nuestros "
            "momentos juntos."
        ),
    },
    {
        "nombre": "Ryu Ramen House",
        "descripcion": (
            "Comida, plática y tiempo juntos. Porque hasta salir a comer "
            "puede convertirse en un recuerdo."
        ),
    },
    {
        "nombre": "Trueke Comida & Amigos",
        "descripcion": (
            "Otro lugar que quedó guardado dentro de nuestras pequeñas "
            "aventuras."
        ),
    },
]


# ============================================================
# CSS
# ============================================================

def inyectar_css():
    st.markdown(
        """
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Manrope:wght@400;500;600;700;800&family=Unbounded:wght@400;500;600;700&display=swap');

        html, body, [class*="css"] {
            font-family: 'Manrope', sans-serif;
        }

        .stApp {
            background:
                radial-gradient(circle at 20% 10%, rgba(255, 62, 127, 0.20), transparent 30%),
                radial-gradient(circle at 90% 20%, rgba(140, 82, 255, 0.18), transparent 30%),
                linear-gradient(145deg, #100718 0%, #19091f 45%, #0d0615 100%);
            color: #ffffff;
        }

        header, footer, #MainMenu {
            visibility: hidden;
        }

        .block-container {
            max-width: 640px !important;
            padding-top: 2rem !important;
            padding-bottom: 3rem !important;
        }

        .hero {
            text-align: center;
            padding: 2rem 0 1rem 0;
        }

        .eyebrow {
            text-transform: uppercase;
            letter-spacing: 0.22em;
            font-size: 0.70rem;
            color: rgba(255,255,255,0.55);
            font-weight: 700;
            margin-bottom: 0.9rem;
        }

        .title {
            font-family: 'Unbounded', sans-serif;
            font-size: clamp(2rem, 8vw, 4rem);
            line-height: 1.05;
            font-weight: 700;
            margin: 0;
            background: linear-gradient(90deg, #FF3E7F, #FFC857, #8C52FF);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }

        .subtitle {
            color: rgba(255,255,255,0.72);
            font-size: 1rem;
            margin-top: 1rem;
            line-height: 1.7;
        }

        .section-title {
            font-family: 'Unbounded', sans-serif;
            font-size: clamp(1.45rem, 5vw, 2.3rem);
            line-height: 1.2;
            margin-bottom: 0.6rem;
        }

        .section-subtitle {
            color: rgba(255,255,255,0.65);
            line-height: 1.7;
            margin-bottom: 1.5rem;
        }

        .date {
            color: #FFC857;
            font-size: 0.9rem;
            font-weight: 700;
            letter-spacing: 0.08em;
            margin-bottom: 0.8rem;
        }

        .story {
            background: rgba(255,255,255,0.055);
            border: 1px solid rgba(255,255,255,0.08);
            border-radius: 24px;
            padding: 1.3rem;
            line-height: 1.8;
            color: rgba(255,255,255,0.82);
            margin: 1rem 0;
            box-shadow: 0 15px 45px rgba(0,0,0,0.15);
        }

        .quote {
            border-left: 3px solid #FF3E7F;
            padding-left: 1rem;
            color: rgba(255,255,255,0.78);
            font-style: italic;
            line-height: 1.7;
            margin: 1.5rem 0;
        }

        .stats {
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            gap: 0.7rem;
            margin: 1.5rem 0;
        }

        .stat {
            background: rgba(255,255,255,0.055);
            border: 1px solid rgba(255,255,255,0.08);
            border-radius: 20px;
            padding: 1.1rem 0.7rem;
            text-align: center;
        }

        .stat-number {
            font-family: 'Unbounded', sans-serif;
            font-size: 1.5rem;
            font-weight: 700;
        }

        .stat-label {
            color: rgba(255,255,255,0.55);
            font-size: 0.75rem;
            margin-top: 0.4rem;
        }

        .photo-card {
            overflow: hidden;
            border-radius: 25px;
            margin: 1rem 0;
            background: rgba(255,255,255,0.05);
            border: 1px solid rgba(255,255,255,0.08);
        }

        .photo-caption {
            padding: 0.9rem 1rem 1rem;
            color: rgba(255,255,255,0.75);
            font-size: 0.9rem;
        }

        .anecdote {
            padding: 1.1rem 1.2rem;
            border-radius: 20px;
            background: linear-gradient(135deg, rgba(255,255,255,0.07), rgba(255,255,255,0.025));
            border: 1px solid rgba(255,255,255,0.07);
            margin: 0.8rem 0;
        }

        .anecdote-title {
            font-weight: 800;
            margin-bottom: 0.35rem;
        }

        .anecdote-text {
            color: rgba(255,255,255,0.68);
            line-height: 1.65;
            font-size: 0.92rem;
        }

        .track {
            background: rgba(255,255,255,0.045);
            border: 1px solid rgba(255,255,255,0.07);
            border-radius: 20px;
            padding: 1rem;
            margin: 0.7rem 0;
        }

        .track-number {
            color: rgba(255,255,255,0.38);
            font-size: 0.75rem;
            margin-bottom: 0.3rem;
        }

        .track-title {
            font-weight: 800;
            font-size: 1rem;
        }

        .track-artist {
            color: #FFC857;
            font-size: 0.82rem;
            margin-top: 0.2rem;
        }

        .track-meaning {
            color: rgba(255,255,255,0.62);
            font-size: 0.84rem;
            line-height: 1.55;
            margin-top: 0.65rem;
        }

        .restaurant {
            padding: 1.2rem;
            border-radius: 22px;
            background: rgba(255,255,255,0.05);
            border: 1px solid rgba(255,255,255,0.07);
            margin: 0.8rem 0;
        }

        .restaurant-name {
            font-family: 'Unbounded', sans-serif;
            font-size: 1rem;
            margin-bottom: 0.55rem;
        }

        .restaurant-description {
            color: rgba(255,255,255,0.65);
            line-height: 1.6;
            font-size: 0.88rem;
        }

        .progress-text {
            text-align: center;
            color: rgba(255,255,255,0.48);
            font-size: 0.7rem;
            letter-spacing: 0.1em;
            text-transform: uppercase;
            margin-bottom: 0.7rem;
        }

        .dots {
            display: flex;
            justify-content: center;
            gap: 6px;
            margin: 0.8rem 0 1.5rem;
        }

        .dot {
            width: 7px;
            height: 7px;
            border-radius: 50%;
            background: rgba(255,255,255,0.2);
        }

        .dot.active {
            width: 24px;
            border-radius: 20px;
            background: linear-gradient(90deg, #FF3E7F, #8C52FF);
        }

        .love-message {
            text-align: center;
            font-family: 'Unbounded', sans-serif;
            font-size: clamp(1.4rem, 5vw, 2.2rem);
            line-height: 1.45;
            margin: 2rem 0;
            background: linear-gradient(90deg, #FF3E7F, #FFC857, #8C52FF);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }

        div.stButton > button {
            width: 100%;
            border-radius: 18px;
            min-height: 48px;
            border: 1px solid rgba(255,255,255,0.10);
            background: rgba(255,255,255,0.06);
            color: white;
            font-weight: 700;
            transition: all 0.2s ease;
        }

        div.stButton > button:hover {
            border-color: rgba(255,255,255,0.3);
            transform: translateY(-2px);
            background: rgba(255,255,255,0.10);
        }

        [data-testid="stSidebar"] {
            background: #100718;
        }
        </style>
        """,
        unsafe_allow_html=True
    )


# ============================================================
# MÚSICA DE FONDO
# ============================================================

def musica_fondo():
    if not os.path.exists(MUSICA_FONDO):
        return

    try:
        with open(MUSICA_FONDO, "rb") as archivo:
            audio_data = base64.b64encode(archivo.read()).decode("utf-8")
    except Exception:
        return

    st.markdown(
        f"""
        <audio
            id="wrapped-background-music"
            loop
            preload="auto"
            style="position: fixed; width: 1px; height: 1px; opacity: 0; pointer-events: none; left: -100px; top: -100px;"
        >
            <source src="data:audio/mpeg;base64,{audio_data}" type="audio/mpeg">
        </audio>
        <script>
        (() => {{
            const STORAGE_TIME = "wrapped_music_current_time";
            const STORAGE_PLAYING = "wrapped_music_playing";
            const audio = document.getElementById("wrapped-background-music");
            if (!audio) return;
            audio.volume = 0.28;

            const savedTime = parseFloat(localStorage.getItem(STORAGE_TIME) || "0");
            audio.addEventListener("loadedmetadata", () => {{
                if (Number.isFinite(savedTime) && savedTime > 0 && savedTime < audio.duration) {{
                    audio.currentTime = savedTime;
                }}
                if (localStorage.getItem(STORAGE_PLAYING) === "1") {{
                    audio.play().catch(() => {{}});
                }}
            }}, {{ once: true }});

            setInterval(() => {{
                if (!audio.paused) {{
                    localStorage.setItem(STORAGE_TIME, String(audio.currentTime));
                }}
            }}, 500);

            audio.addEventListener("play", () => {{ localStorage.setItem(STORAGE_PLAYING, "1"); }});
            audio.addEventListener("pause", () => {{ localStorage.setItem(STORAGE_PLAYING, "0"); }});
            window.addEventListener("beforeunload", () => {{
                localStorage.setItem(STORAGE_TIME, String(audio.currentTime));
            }});

            const iniciarMusica = () => {{ audio.play().catch(() => {{}}); }};
            document.addEventListener("click", iniciarMusica, {{ once: true }});
            document.addEventListener("touchstart", iniciarMusica, {{ once: true }});
        }})();
        </script>
        """,
        unsafe_allow_html=True
    )


# ============================================================
# ENCABEZADO Y COMPONENTES
# ============================================================

def encabezado(titulo, subtitulo=None, seccion=None):
    if seccion:
        st.markdown(f'<div class="date">{seccion}</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="section-title">{titulo}</div>', unsafe_allow_html=True)
    if subtitulo:
        st.markdown(f'<div class="section-subtitle">{subtitulo}</div>', unsafe_allow_html=True)


def anecdota(titulo, texto):
    st.markdown(
        f"""
        <div class="anecdote">
            <div class="anecdote-title">{titulo}</div>
            <div class="anecdote-text">{texto}</div>
        </div>
        """,
        unsafe_allow_html=True
    )


def mostrar_foto(ruta, caption=None):
    if not ruta or not os.path.exists(ruta):
        st.warning(f"No se encontró la imagen: {ruta}")
        return

    st.markdown('<div class="photo-card">', unsafe_allow_html=True)
    st.image(ruta, width="stretch")
    if caption:
        st.markdown(f'<div class="photo-caption">{caption}</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)


def carrusel_fotos(fotos, captions=None, key_prefix="carousel"):
    if not fotos:
        return

    if captions is None:
        captions = [""] * len(fotos)

    key = f"{key_prefix}_index"
    if key not in st.session_state:
        st.session_state[key] = 0

    indice = st.session_state[key]
    indice = max(0, min(indice, len(fotos) - 1))

    mostrar_foto(fotos[indice], captions[indice])

    col1, col2, col3 = st.columns([1, 2, 1])
    with col1:
        if st.button("‹", key=f"{key_prefix}_prev", use_container_width=True):
            st.session_state[key] = (indice - 1) % len(fotos)
            st.rerun()
    with col2:
        st.markdown(f'<div style="text-align:center;color:rgba(255,255,255,0.45);padding-top:10px;font-size:0.75rem;">{indice + 1} / {len(fotos)}</div>', unsafe_allow_html=True)
    with col3:
        if st.button("›", key=f"{key_prefix}_next", use_container_width=True):
            st.session_state[key] = (indice + 1) % len(fotos)
            st.rerun()


def galeria_paginada():
    if not os.path.exists(GALERIA_DIR):
        return

    extensiones = (".png", ".jpg", ".jpeg", ".webp")
    fotos = [
        os.path.join(GALERIA_DIR, archivo)
        for archivo in sorted(os.listdir(GALERIA_DIR))
        if archivo.lower().endswith(extensiones)
    ]

    if not fotos:
        return

    key = "galeria_index"
    if key not in st.session_state:
        st.session_state[key] = 0

    indice = st.session_state[key]
    indice = max(0, min(indice, len(fotos) - 1))

    mostrar_foto(fotos[indice])

    col1, col2, col3 = st.columns([1, 2, 1])
    with col1:
        if st.button("‹", key="galeria_prev", use_container_width=True):
            st.session_state[key] = (indice - 1) % len(fotos)
            st.rerun()
    with col2:
        st.markdown(f'<div style="text-align:center;color:rgba(255,255,255,0.45);padding-top:10px;font-size:0.75rem;">{indice + 1} / {len(fotos)}</div>', unsafe_allow_html=True)
    with col3:
        if st.button("›", key="galeria_next", use_container_width=True):
            st.session_state[key] = (indice + 1) % len(fotos)
            st.rerun()


def dias_para_aniversario():
    import datetime
    hoy = datetime.date.today()
    aniversario = datetime.date(hoy.year, 9, 23)
    if aniversario < hoy:
        aniversario = datetime.date(hoy.year + 1, 9, 23)
    return (aniversario - hoy).days


# ============================================================
# SLIDES
# ============================================================

def slide_portada():
    st.markdown(
        """
        <div class="hero">
            <div class="eyebrow">NUESTRO WRAPPED 💫</div>
            <div class="title">3 Años Juntos</div>
            <div class="subtitle">Una pequeña recopilación de nuestra historia, nuestras canciones, nuestros lugares y todos esos momentos que hicieron estos años tan especiales.</div>
        </div>
        """,
        unsafe_allow_html=True
    )
    st.markdown(
        """
        <div class="stats">
            <div class="stat"><div class="stat-number">3</div><div class="stat-label">AÑOS JUNTOS</div></div>
            <div class="stat"><div class="stat-number">11</div><div class="stat-label">CANCIONES</div></div>
            <div class="stat"><div class="stat-number">3</div><div class="stat-label">LUGARES FAVORITOS</div></div>
            <div class="stat"><div class="stat-number">2</div><div class="stat-label">CONEJITOS 🐰</div></div>
        </div>
        """,
        unsafe_allow_html=True
    )
    portada = os.path.join(FOTOS_DIR, "portada.png")
    if os.path.exists(portada):
        mostrar_foto(portada)
    st.markdown(
        """
        <div class="quote">Tres años pueden parecer solamente un número, pero cuando los llenas de recuerdos, personas, lugares, canciones y momentos, se convierten en una historia.</div>
        """,
        unsafe_allow_html=True
    )
    if st.button("Comenzar el recorrido ▶", key="comenzar", use_container_width=True):
        st.session_state.slide = 1
        st.rerun()


def slide_inicio():
    encabezado("El inicio de todo", "La historia comenzó el 24 de julio de 2023.", "24 · 07 · 2023")
    st.markdown(
        """
        <div class="story">
        Hay fechas que terminan convirtiéndose en algo mucho más grande de lo que imaginábamos.<br><br>
        El 24 de julio de 2023 comenzó nuestra historia. Desde ese momento empezamos a crear recuerdos, aprender uno del otro y descubrir todo lo que podíamos vivir juntos.
        </div>
        """,
        unsafe_allow_html=True
    )
    mostrar_foto(FOTOS["inicio"], "Aquí comenzó una parte muy importante de nuestra historia ❤️")


def slide_caifanes():
    encabezado("Nuestro concierto de Caifanes", "Una noche que terminó convirtiéndose en uno de nuestros recuerdos.", "CAIFANES 🎸")
    st.markdown(
        """
        <div class="story">
        Entre música, gente y emoción vivimos una de esas noches que se quedan guardadas.<br><br>
        Porque no solamente importa a dónde vamos, sino con quién compartimos el momento.
        </div>
        """,
        unsafe_allow_html=True
    )
    mostrar_foto(FOTOS["caifanes"], "Una noche para recordar 🎸❤️")


def slide_diciembre_2023():
    encabezado("Diciembre 2023", "Nuestro primer diciembre lleno de recuerdos.", "DICIEMBRE · 2023")
    anecdota("🏡 El pueblo de mi papá", "Un lugar diferente, pero mucho más especial porque estabas conmigo.")
    anecdota("🎉 La piñata", "Compartiendo momentos sencillos que terminaron convirtiéndose en recuerdos.")
    anecdota("🌊 Rumbo a Mazatlán", "Una aventura más de tantas que hemos ido sumando a nuestra historia.")
    carrusel_fotos(FOTOS["diciembre_2023"], CAPTIONS["diciembre_2023"], "diciembre")


def slide_2024():
    encabezado("2024", "Un año lleno de cambios, proyectos y momentos juntos.", "2024")
    anecdota("🎓 SHESPAT", "Emprendiendo juntos con las togas y estolas SHESPAT.")
    anecdota("🏍️ La moto", "Ese momento en el que empezaste a enseñarme a manejar.")
    anecdota("💇 Mi cambio de look", "Gracias a ti también llegaron nuevos cambios y nuevas versiones de mí.")
    anecdota("🎄 Nuestra primera Navidad", "Nuestra primera Navidad juntos, creando una tradición propia.")
    carrusel_fotos(FOTOS["y2024"], CAPTIONS["y2024"], "y2024")


def slide_2025_2026():
    encabezado("2025 · 2026", "Seguimos acumulando recuerdos.", "NUEVOS RECUERDOS")
    anecdota("🎁 El reloj para mi papá", "Un detalle que terminó convirtiéndose en otro recuerdo de nuestra historia.")
    anecdota("🐰 Carajo y Nena", "Nuestros conejitos y dos pequeños integrantes de nuestra historia.")
    anecdota("🎡 La feria", "La feria, la rueda de la fortuna y otra aventura juntos.")
    carrusel_fotos(FOTOS["y2025_2026"], CAPTIONS["y2025_2026"], "y2025_2026")


def slide_gastronomia():
    encabezado("También hemos comido juntos", "Porque una relación también se construye alrededor de una mesa.", "NUESTROS LUGARES 🍜")
    for restaurante in RESTAURANTES:
        st.markdown(
            f"""
            <div class="restaurant">
                <div class="restaurant-name">{restaurante["nombre"]}</div>
                <div class="restaurant-description">{restaurante["descripcion"]}</div>
            </div>
            """,
            unsafe_allow_html=True
        )
    st.markdown(
        """
        <div class="quote">Al final, muchos de nuestros recuerdos favoritos también tienen algo en común: comida, plática y nosotros dos.</div>
        """,
        unsafe_allow_html=True
    )


def slide_playlist():
    encabezado("Nuestra banda sonora", "11 canciones que, de una u otra manera, forman parte de nuestra historia.", "NUESTRA PLAYLIST 🎵")
    for indice, cancion in enumerate(CANCIONES, start=1):
        st.markdown(
            f"""
            <div class="track">
                <div class="track-number">#{indice:02d}</div>
                <div class="track-title">{cancion["titulo"]}</div>
                <div class="track-artist">{cancion["artista"]}</div>
                <div class="track-meaning">{cancion["significado"]}</div>
            </div>
            """,
            unsafe_allow_html=True
        )


def slide_galeria():
    encabezado("Galería de recuerdos", "Una colección de pequeños momentos que queremos conservar.", "NUESTROS RECUERDOS 📸")
    galeria_paginada()


def slide_cierre():
    dias = dias_para_aniversario()
    st.markdown(
        """
        <div class="hero">
            <div class="eyebrow">Y ESTO APENAS ES UNA PARTE</div>
            <div class="love-message">Gracias por estos<br>3 años ❤️</div>
        </div>
        """,
        unsafe_allow_html=True
    )
    st.markdown(
        """
        <div class="story">
        Hemos cambiado, aprendido, reído, salido, comido, viajado y vivido muchas cosas juntos.<br><br>
        Y aunque este Wrapped solamente puede guardar algunas fotografías y canciones, nuestra historia tiene muchísimos más momentos.<br><br>
        Gracias por formar parte de mi vida.
        </div>
        """,
        unsafe_allow_html=True
    )
    st.markdown(
        f"""
        <div style="text-align:center;margin:2rem 0;color:rgba(255,255,255,0.55);">
            Faltan aproximadamente
            <div style="font-family:'Unbounded',sans-serif;font-size:2rem;margin:0.5rem 0;background:linear-gradient(90deg, #FF3E7F, #FFC857, #8C52FF);-webkit-background-clip:text;-webkit-text-fill-color:transparent;">
                {dias} días
            </div>
            para nuestro próximo aniversario 💫
        </div>
        """,
        unsafe_allow_html=True
    )
    st.markdown(
        """
        <div class="quote">Y si pudiera volver al 24 de julio de 2023, volvería a elegir comenzar esta historia contigo.</div>
        """,
        unsafe_allow_html=True
    )


SLIDES = [
    ("Portada", slide_portada, "portada"),
    ("El inicio de todo", slide_inicio, "inicio"),
    ("Concierto de Caifanes", slide_caifanes, "caifanes"),
    ("Diciembre 2023", slide_diciembre_2023, "diciembre_2023"),
    ("2024", slide_2024, "y2024"),
    ("2025 y 2026", slide_2025_2026, "y2025_2026"),
    ("Gastronomía", slide_gastronomia, "gastronomia"),
    ("Nuestra banda sonora", slide_playlist, "playlist"),
    ("Galería de recuerdos", slide_galeria, "galeria"),
    ("Cierre", slide_cierre, "cierre"),
]


def render_puntos(indice):
    puntos = ""
    for i in range(len(SLIDES)):
        clase = "dot active" if i == indice else "dot"
        puntos += f'<div class="{clase}"></div>'
    st.markdown(f'<div class="dots">{puntos}</div>', unsafe_allow_html=True)


def render_navegacion(indice):
    total = len(SLIDES)
    st.markdown(f'<div class="progress-text">{indice + 1} / {total}</div>', unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        if indice > 0:
            if st.button("← Anterior", key=f"prev_{indice}", use_container_width=True):
                st.session_state.slide = indice - 1
                st.rerun()
    with col2:
        if indice < total - 1:
            if st.button("Siguiente →", key=f"next_{indice}", use_container_width=True):
                st.session_state.slide = indice + 1
                st.rerun()


# ============================================================
# MAIN
# ============================================================

def main():
    inyectar_css()
    musica_fondo()

    if "slide" not in st.session_state:
        st.session_state.slide = 0

    indice = st.session_state.slide
    indice = max(0, min(indice, len(SLIDES) - 1))
    st.session_state.slide = indice

    # SIDEBAR
    with st.sidebar:
        st.markdown("### Nuestro Wrapped 💫")
        opciones = [slide[0] for slide in SLIDES]
        
        seleccion = st.selectbox(
            "Ir a:",
            opciones,
            index=indice,
            key="selector_slide"
        )
        
        nuevo_indice = opciones.index(seleccion)
        if nuevo_indice != indice:
            st.session_state.slide = nuevo_indice
            st.rerun()

    render_puntos(indice)

    funcion_slide = SLIDES[indice][1]
    funcion_slide()

    render_navegacion(indice)

    if indice == len(SLIDES) - 1:
        st.balloons()


if __name__ == "__main__":
    main()
