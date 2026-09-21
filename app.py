import os
import base64
import datetime
import html

import streamlit as st
import streamlit.components.v1 as components


# ============================================================
# CONFIGURACIÓN
# ============================================================

st.set_page_config(
    page_title="Nuestro Wrapped 💫",
    page_icon="💖",
    layout="centered",
    initial_sidebar_state="collapsed",
)


# ============================================================
# RUTAS
# ============================================================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

FOTOS_DIR = os.path.join(BASE_DIR, "fotos")
GALERIA_DIR = os.path.join(FOTOS_DIR, "galeria")

# La música está directamente en Main
MUSICA_FONDO = os.path.join(BASE_DIR, "musica.mp3")


# ============================================================
# UTILIDADES
# ============================================================

def render_html(contenido):
    """
    Renderiza HTML evitando espacios/sangría que puedan
    provocar problemas visuales.
    """
    contenido = "\n".join(
        linea.strip()
        for linea in contenido.splitlines()
        if linea.strip()
    )

    st.markdown(contenido, unsafe_allow_html=True)


def esc(texto):
    return html.escape(str(texto))


# ============================================================
# MÚSICA DE FONDO
# ============================================================

@st.cache_data(show_spinner=False)
def obtener_audio_base64(ruta):
    with open(ruta, "rb") as archivo:
        return base64.b64encode(archivo.read()).decode("utf-8")


def musica_fondo():

    if not os.path.exists(MUSICA_FONDO):
        return

    try:
        audio_b64 = obtener_audio_base64(MUSICA_FONDO)
    except Exception:
        return

    html_audio = f"""
    <!DOCTYPE html>
    <html>
    <body style="margin:0;padding:0;background:transparent;overflow:hidden;">

    <script>

    (function() {{

        const AUDIO_ID = "wrapped_background_music";
        const AUDIO_DATA = "{audio_b64}";

        const parentWindow = window.parent;

        let parentDocument;

        try {{
            parentDocument = parentWindow.document;
        }} catch(e) {{
            return;
        }}

        /*
         * Ocultar completamente el iframe de Streamlit
         */
        try {{

            const iframe = window.frameElement;

            if (iframe) {{

                const container =
                    iframe.closest(
                        '[data-testid="stElementContainer"]'
                    );

                if (container) {{
                    container.style.display = "none";
                }}

                iframe.style.display = "none";
            }}

        }} catch(e) {{}}


        /*
         * Buscar si ya existe la música.
         * Esto evita que se reinicie cada vez
         * que Streamlit hace un rerun.
         */

        let audio =
            parentDocument.getElementById(AUDIO_ID);


        /*
         * Crear audio solamente una vez
         */

        if (!audio) {{

            try {{

                const binary =
                    atob(AUDIO_DATA);

                const bytes =
                    new Uint8Array(binary.length);

                for (
                    let i = 0;
                    i < binary.length;
                    i++
                ) {{
                    bytes[i] =
                        binary.charCodeAt(i);
                }}

                const blob =
                    new parentWindow.Blob(
                        [bytes],
                        {{ type: "audio/mpeg" }}
                    );

                const url =
                    parentWindow.URL.createObjectURL(blob);

                audio =
                    parentDocument.createElement("audio");

                audio.id = AUDIO_ID;
                audio.src = url;
                audio.loop = true;
                audio.preload = "auto";

                /*
                 * Volumen tipo música ambiental
                 */

                audio.volume = 0.25;

                audio.style.display = "none";

                parentDocument.body.appendChild(audio);

            }} catch(e) {{
                return;
            }}

        }}


        /*
         * Intentar reproducir.
         * Los navegadores normalmente necesitan
         * interacción del usuario.
         */

        function reproducir() {{

            if (!audio) return;

            const promise = audio.play();

            if (promise && promise.catch) {{
                promise.catch(() => {{}});
            }}

        }}


        /*
         * Eventos que desbloquean autoplay
         */

        const eventos = [
            "click",
            "touchstart",
            "touchend",
            "pointerdown",
            "keydown"
        ];


        function desbloquear() {{

            reproducir();

            if (!audio.paused) {{

                eventos.forEach(evento => {{

                    try {{
                        parentDocument.removeEventListener(
                            evento,
                            desbloquear,
                            true
                        );
                    }} catch(e) {{}}

                }});

            }}

        }}


        /*
         * Evitar listeners duplicados
         */

        if (parentWindow.__wrappedMusicUnlock) {{

            eventos.forEach(evento => {{

                try {{
                    parentDocument.removeEventListener(
                        evento,
                        parentWindow.__wrappedMusicUnlock,
                        true
                    );
                }} catch(e) {{}}

            }});

        }}


        parentWindow.__wrappedMusicUnlock = desbloquear;


        eventos.forEach(evento => {{

            parentDocument.addEventListener(
                evento,
                desbloquear,
                true
            );

        }});


        /*
         * Intento inicial
         */

        reproducir();

    }})();

    </script>

    </body>
    </html>
    """

    components.html(
        html_audio,
        height=0,
        scrolling=False,
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
# TEXTOS
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
            "que tenemos que hacer, siempre quiero encontrar tiempo para ti."
    },

    {
        "titulo":
            "My One and Only Love / They Say It's Wonderful",

        "artista":
            "John Coltrane",

        "significado":
            "Mi descubrimiento personal del amor y una canción que terminó "
            "teniendo un significado muy especial para nosotros."
    },

    {
        "titulo":
            "I Only Have Eyes for You",

        "artista":
            "Louis Armstrong",

        "significado":
            "Porque entre todas las personas, lugares y cosas que existen, "
            "mis ojos siempre terminan buscándote a ti."
    },

    {
        "titulo":
            "Eso y Más",

        "artista":
            "Joan Sebastián",

        "significado":
            "Una canción que representa todo eso que siento y muchas veces "
            "no sé cómo decirte."
    },

    {
        "titulo":
            "Diséñame",

        "artista":
            "Joan Sebastián",

        "significado":
            "Porque de alguna manera nuestro amor fue construyéndose "
            "poco a poco, con nuestras propias historias."
    },

    {
        "titulo":
            "The Nearness of You",

        "artista":
            "Ella Fitzgerald & Louis Armstrong",

        "significado":
            "La cercanía de la persona que amas puede hacer que cualquier "
            "momento cotidiano se sienta especial."
    },

    {
        "titulo":
            "Only You",

        "artista":
            "The Platters",

        "significado":
            "Porque hay personas que simplemente se vuelven únicas "
            "en nuestra vida."
    },

    {
        "titulo":
            "Eres",

        "artista":
            "José María Napoleón",

        "significado":
            "Una forma de decirte todo lo que significas para mí."
    },

    {
        "titulo":
            "Mi Mundo Tú",

        "artista":
            "Camilo Sesto",

        "significado":
            "Porque después de estos años, eres una parte enorme "
            "de mi mundo."
    },

    {
        "titulo":
            "Cama y Mesa",

        "artista":
            "Roberto Carlos",

        "significado":
            "Una canción que habla de compartir la vida, los momentos "
            "íntimos y también los cotidianos."
    },

    {
        "titulo":
            "Invítame un cigarro",

        "artista":
            "Tradicional / Popular",

        "significado":
            "Una de esas canciones que terminan formando parte "
            "de nuestra historia."
    },

]


# ============================================================
# RESTAURANTES
# ============================================================

RESTAURANTES = [

    {
        "nombre": "Ninja Ramen",
        "descripcion":
            "Uno de esos lugares que se volvieron parte "
            "de nuestros momentos juntos."
    },

    {
        "nombre": "Ryu Ramen House",
        "descripcion":
            "Comida, plática y tiempo juntos. Porque hasta salir "
            "a comer puede convertirse en un recuerdo."
    },

    {
        "nombre": "Trueke Comida & Amigos",
        "descripcion":
            "Otro lugar que quedó guardado dentro "
            "de nuestras pequeñas aventuras."
    },

]


# ============================================================
# TEMA VISUAL
# ============================================================

def inyectar_css():

    render_html("""

<style>

@import url(
    'https://fonts.googleapis.com/css2?family=Manrope:wght@400;500;600;700;800&family=Unbounded:wght@400;500;600;700;800&display=swap'
);


/* ==========================================================
   BASE
   ========================================================== */

html,
body,
[data-testid="stAppViewContainer"],
.stApp {

    background: #08030d !important;

    color: white !important;

    font-family:
        'Manrope',
        sans-serif !important;

}


body {

    overflow-x: hidden;

}


#MainMenu,
footer,
[data-testid="stToolbar"],
[data-testid="stDecoration"] {

    display: none !important;

}


header {

    background: transparent !important;

}


[data-testid="stHeader"] {

    background: transparent !important;

}


/* ==========================================================
   CONTENEDOR PRINCIPAL
   ========================================================== */

.block-container {

    max-width: 760px !important;

    padding-top: 1rem !important;

    padding-bottom: 2rem !important;

    padding-left: 1rem !important;

    padding-right: 1rem !important;

}


/* ==========================================================
   OCULTAR SIDEBAR
   ========================================================== */

[data-testid="stSidebar"] {

    display: none !important;

}


/* ==========================================================
   ANIMACIÓN GENERAL
   ========================================================== */

@keyframes entrada {

    from {

        opacity: 0;

        transform:
            translateY(28px)
            scale(0.97);

    }

    to {

        opacity: 1;

        transform:
            translateY(0)
            scale(1);

    }

}


.wrapped-content {

    animation:
        entrada
        0.65s
        cubic-bezier(.2,.8,.2,1);

}


/* ==========================================================
   PROGRESO
   ========================================================== */

.progress-wrapper {

    display: flex;

    gap: 5px;

    width: 100%;

    margin:
        0.2rem
        0
        1.2rem
        0;

}


.progress-segment {

    height: 4px;

    flex: 1;

    border-radius: 20px;

    background:
        rgba(255,255,255,0.16);

    overflow: hidden;

}


.progress-segment.active {

    background:
        linear-gradient(
            90deg,
            #ff2d75,
            #ff8a00,
            #8c52ff
        );

    box-shadow:
        0 0 12px
        rgba(255,45,117,0.45);

}


/* ==========================================================
   PORTADA
   ========================================================== */

.cover {

    min-height: 78vh;

    display: flex;

    flex-direction: column;

    justify-content: center;

    text-align: center;

    position: relative;

    overflow: hidden;

}


.cover::before {

    content: "";

    position: absolute;

    width: 420px;

    height: 420px;

    border-radius: 50%;

    background:
        radial-gradient(
            circle,
            rgba(255,45,117,.34),
            transparent 70%
        );

    top: 5%;

    left: -25%;

    filter: blur(15px);

    animation:
        flotar
        7s
        ease-in-out
        infinite;

}


.cover::after {

    content: "";

    position: absolute;

    width: 400px;

    height: 400px;

    border-radius: 50%;

    background:
        radial-gradient(
            circle,
            rgba(125,65,255,.28),
            transparent 70%
        );

    bottom: 0;

    right: -25%;

    filter: blur(15px);

    animation:
        flotar
        9s
        ease-in-out
        infinite reverse;

}


@keyframes flotar {

    0%,100% {

        transform:
            translateY(0)
            scale(1);

    }

    50% {

        transform:
            translateY(-25px)
            scale(1.08);

    }

}


.cover-content {

    position: relative;

    z-index: 2;

}


.eyebrow {

    font-size: .68rem;

    letter-spacing: .25em;

    font-weight: 800;

    color:
        rgba(255,255,255,.58);

    margin-bottom: 1.5rem;

}


.cover-title {

    font-family:
        'Unbounded',
        sans-serif;

    font-size:
        clamp(
            2.6rem,
            11vw,
            5.8rem
        );

    line-height: .98;

    font-weight: 800;

    letter-spacing: -.07em;

    background:
        linear-gradient(
            110deg,
            #ff2d75,
            #ff8a00,
            #ffd447,
            #8c52ff
        );

    -webkit-background-clip: text;

    -webkit-text-fill-color: transparent;

    margin: 0;

}


.cover-subtitle {

    max-width: 520px;

    margin:
        1.8rem
        auto
        0;

    color:
        rgba(255,255,255,.7);

    line-height: 1.8;

    font-size:
        clamp(
            .9rem,
            3vw,
            1.05rem
        );

}


/* ==========================================================
   TÍTULOS
   ========================================================== */

.kicker {

    text-transform: uppercase;

    letter-spacing: .18em;

    color:
        #ffcb3d;

    font-size: .68rem;

    font-weight: 800;

    margin-bottom: .7rem;

}


.section-title {

    font-family:
        'Unbounded',
        sans-serif;

    font-size:
        clamp(
            1.8rem,
            7vw,
            3.6rem
        );

    line-height: 1.08;

    letter-spacing: -.05em;

    margin: 0;

}


.section-description {

    color:
        rgba(255,255,255,.63);

    line-height: 1.75;

    margin:
        1rem
        0
        1.5rem;

}


/* ==========================================================
   BIG NUMBER
   ========================================================== */

.big-number {

    font-family:
        'Unbounded',
        sans-serif;

    font-size:
        clamp(
            6rem,
            28vw,
            13rem
        );

    line-height: .8;

    font-weight: 800;

    letter-spacing: -.1em;

    background:
        linear-gradient(
            130deg,
            #ff2d75,
            #ff9a00,
            #8c52ff
        );

    -webkit-background-clip: text;

    -webkit-text-fill-color: transparent;

    text-align: center;

    margin:
        2rem
        0;

}


/* ==========================================================
   TARJETAS DE ESTADÍSTICAS
   ========================================================== */

.stats-grid {

    display: grid;

    grid-template-columns:
        repeat(2, 1fr);

    gap: .7rem;

    margin:
        1.5rem
        0;

}


.stat-card {

    min-height: 150px;

    padding:
        1.2rem;

    border-radius: 25px;

    display: flex;

    flex-direction: column;

    justify-content: space-between;

    background:
        linear-gradient(
            145deg,
            rgba(255,255,255,.10),
            rgba(255,255,255,.035)
        );

    border:
        1px solid
        rgba(255,255,255,.09);

    box-shadow:
        0 20px 50px
        rgba(0,0,0,.2);

}


.stat-number {

    font-family:
        'Unbounded',
        sans-serif;

    font-size:
        clamp(
            1.8rem,
            7vw,
            2.8rem
        );

    font-weight: 800;

}


.stat-label {

    color:
        rgba(255,255,255,.55);

    font-size: .68rem;

    letter-spacing: .12em;

    font-weight: 700;

}


/* ==========================================================
   FOTO HERO
   ========================================================== */

.hero-photo {

    border-radius: 32px;

    overflow: hidden;

    position: relative;

    margin:
        1.5rem
        0;

    border:
        1px solid
        rgba(255,255,255,.1);

    box-shadow:
        0 30px 80px
        rgba(0,0,0,.4);

}


.hero-photo img {

    width: 100%;

    display: block;

}


.photo-overlay {

    position: absolute;

    bottom: 0;

    left: 0;

    right: 0;

    padding:
        4rem
        1.2rem
        1.2rem;

    background:
        linear-gradient(
            transparent,
            rgba(0,0,0,.8)
        );

}


/* ==========================================================
   HISTORIA
   ========================================================== */

.story-card {

    position: relative;

    padding:
        1.4rem;

    border-radius: 28px;

    background:
        rgba(255,255,255,.055);

    border:
        1px solid
        rgba(255,255,255,.08);

    margin:
        1rem
        0;

    line-height: 1.85;

    color:
        rgba(255,255,255,.78);

}


.story-card::before {

    content: "“";

    position: absolute;

    top: -.7rem;

    right: 1rem;

    font-family:
        Georgia,
        serif;

    font-size: 6rem;

    color:
        rgba(255,255,255,.06);

}


/* ==========================================================
   ANÉCDOTAS
   ========================================================== */

.memory {

    padding:
        1.25rem;

    border-radius: 24px;

    margin:
        .8rem
        0;

    background:
        linear-gradient(
            120deg,
            rgba(255,255,255,.08),
            rgba(255,255,255,.025)
        );

    border:
        1px solid
        rgba(255,255,255,.07);

}


.memory-title {

    font-weight: 800;

    font-size: 1rem;

}


.memory-text {

    margin-top: .45rem;

    color:
        rgba(255,255,255,.6);

    font-size: .88rem;

    line-height: 1.7;

}


/* ==========================================================
   CARRUSEL
   ========================================================== */

.carousel {

    position: relative;

    overflow: hidden;

    border-radius: 30px;

    margin-top: 1.5rem;

    box-shadow:
        0 30px 80px
        rgba(0,0,0,.35);

}


.carousel-caption {

    padding:
        1rem
        1.1rem;

    background:
        rgba(255,255,255,.055);

    color:
        rgba(255,255,255,.7);

    font-size: .85rem;

}


/* ==========================================================
   PLAYLIST
   ========================================================== */

.playlist-intro {

    padding:
        1.5rem;

    border-radius: 30px;

    background:
        linear-gradient(
            135deg,
            #22103c,
            #100716
        );

    margin:
        1.5rem
        0;

    border:
        1px solid
        rgba(255,255,255,.08);

}


.track {

    display: grid;

    grid-template-columns:
        42px 1fr;

    gap: .8rem;

    padding:
        1rem
        .5rem;

    border-bottom:
        1px solid
        rgba(255,255,255,.07);

}


.track:last-child {

    border-bottom: none;

}


.track-number {

    font-family:
        'Unbounded',
        sans-serif;

    font-size: .65rem;

    color:
        rgba(255,255,255,.32);

    padding-top: .25rem;

}


.track-title {

    font-weight: 800;

    font-size: .95rem;

}


.track-artist {

    color:
        #ffca3d;

    font-size: .75rem;

    margin-top: .2rem;

}


.track-meaning {

    color:
        rgba(255,255,255,.53);

    font-size: .78rem;

    line-height: 1.55;

    margin-top: .5rem;

}


/* ==========================================================
   RESTAURANTES
   ========================================================== */

.place {

    position: relative;

    padding:
        1.4rem;

    border-radius: 26px;

    margin:
        .8rem
        0;

    overflow: hidden;

    background:
        linear-gradient(
            135deg,
            rgba(255,255,255,.09),
            rgba(255,255,255,.025)
        );

    border:
        1px solid
        rgba(255,255,255,.08);

}


.place-number {

    font-family:
        'Unbounded',
        sans-serif;

    color:
        rgba(255,255,255,.2);

    font-size: 2.2rem;

    font-weight: 800;

}


.place-name {

    font-family:
        'Unbounded',
        sans-serif;

    font-size: .95rem;

    margin:
        .5rem
        0;

}


.place-description {

    color:
        rgba(255,255,255,.58);

    font-size: .85rem;

    line-height: 1.65;

}


/* ==========================================================
   FRASES
   ========================================================== */

.quote {

    text-align: center;

    font-family:
        'Unbounded',
        sans-serif;

    font-size:
        clamp(
            1.15rem,
            5vw,
            2rem
        );

    line-height: 1.5;

    padding:
        2rem
        .5rem;

    background:
        linear-gradient(
            90deg,
            #ff2d75,
            #ffbd3d,
            #9a52ff
        );

    -webkit-background-clip: text;

    -webkit-text-fill-color: transparent;

}


/* ==========================================================
   CIERRE
   ========================================================== */

.final {

    min-height: 72vh;

    display: flex;

    flex-direction: column;

    justify-content: center;

    text-align: center;

}


.final-title {

    font-family:
        'Unbounded',
        sans-serif;

    font-size:
        clamp(
            2rem,
            9vw,
            4.5rem
        );

    line-height: 1.1;

    letter-spacing: -.06em;

    background:
        linear-gradient(
            120deg,
            #ff2d75,
            #ffd447,
            #8c52ff
        );

    -webkit-background-clip: text;

    -webkit-text-fill-color: transparent;

}


.days {

    margin-top: 2rem;

    color:
        rgba(255,255,255,.55);

}


.days-number {

    display: block;

    font-family:
        'Unbounded',
        sans-serif;

    font-size: 3rem;

    margin-top: .5rem;

    background:
        linear-gradient(
            90deg,
            #ff2d75,
            #ffbd3d
        );

    -webkit-background-clip: text;

    -webkit-text-fill-color: transparent;

}


/* ==========================================================
   BOTONES
   ========================================================== */

div.stButton > button {

    border-radius: 999px !important;

    min-height: 48px !important;

    border:
        1px solid
        rgba(255,255,255,.12) !important;

    background:
        rgba(255,255,255,.06) !important;

    color:
        white !important;

    font-weight: 800 !important;

    transition:
        all .25s ease !important;

}


div.stButton > button:hover {

    transform:
        translateY(-2px)
        scale(1.01);

    background:
        rgba(255,255,255,.12) !important;

    border-color:
        rgba(255,255,255,.25) !important;

}


.primary-button button {

    background:
        linear-gradient(
            90deg,
            #ff2d75,
            #8c52ff
        ) !important;

    border: none !important;

    box-shadow:
        0 12px 35px
        rgba(255,45,117,.25);

}


/* ==========================================================
   RESPONSIVE
   ========================================================== */

@media (max-width: 600px) {

    .block-container {

        padding-left: .8rem !important;

        padding-right: .8rem !important;

    }

    .stats-grid {

        gap: .55rem;

    }

    .stat-card {

        min-height: 125px;

        padding: 1rem;

    }

    .section-description {

        font-size: .88rem;

    }

}

</style>

""")


# ============================================================
# FUNCIONES VISUALES
# ============================================================

def encabezado(titulo, subtitulo="", seccion=""):

    render_html(f"""

    <div class="wrapped-content">

        <div class="kicker">
            {esc(seccion)}
        </div>

        <div class="section-title">
            {esc(titulo)}
        </div>

        <div class="section-description">
            {esc(subtitulo)}
        </div>

    </div>

    """)


def memoria(titulo, texto):

    render_html(f"""

    <div class="memory">

        <div class="memory-title">
            {titulo}
        </div>

        <div class="memory-text">
            {esc(texto)}
        </div>

    </div>

    """)


def mostrar_foto(ruta, caption=None):

    if not ruta or not os.path.exists(ruta):

        return

    try:

        with open(ruta, "rb") as archivo:

            imagen_b64 = base64.b64encode(
                archivo.read()
            ).decode()

        extension = os.path.splitext(ruta)[1].lower()

        mime = {
            ".png": "image/png",
            ".jpg": "image/jpeg",
            ".jpeg": "image/jpeg",
            ".webp": "image/webp",
        }.get(
            extension,
            "image/png"
        )

        caption_html = ""

        if caption:

            caption_html = f"""
            <div class="photo-overlay">
                {esc(caption)}
            </div>
            """

        render_html(f"""

        <div class="hero-photo">

            <img
                src="data:{mime};base64,{imagen_b64}"
            >

            {caption_html}

        </div>

        """)

    except Exception:

        st.warning(
            f"No se pudo cargar la imagen: {ruta}"
        )


# ============================================================
# CARRUSEL
# ============================================================

def carrusel_fotos(
    fotos,
    captions=None,
    key_prefix="carousel"
):

    if not fotos:
        return

    if captions is None:

        captions = [
            ""
            for _ in fotos
        ]

    key = f"{key_prefix}_index"

    if key not in st.session_state:

        st.session_state[key] = 0

    indice = st.session_state[key]

    indice = max(
        0,
        min(
            indice,
            len(fotos) - 1
        )
    )

    foto = fotos[indice]

    caption = ""

    if indice < len(captions):

        caption = captions[indice]

    mostrar_foto(
        foto,
        caption
    )

    col1, col2, col3 = st.columns(
        [1, 2, 1]
    )

    with col1:

        if st.button(
            "‹",
            key=f"{key_prefix}_prev",
            use_container_width=True
        ):

            st.session_state[key] = (
                indice - 1
            ) % len(fotos)

            st.rerun()

    with col2:

        render_html(f"""

        <div style="
            text-align:center;
            color:rgba(255,255,255,.45);
            padding-top:12px;
            font-size:.72rem;
            letter-spacing:.15em;
        ">

            {indice + 1:02d}
            /
            {len(fotos):02d}

        </div>

        """)

    with col3:

        if st.button(
            "›",
            key=f"{key_prefix}_next",
            use_container_width=True
        ):

            st.session_state[key] = (
                indice + 1
            ) % len(fotos)

            st.rerun()


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
        ".webp"
    )

    return [

        os.path.join(
            GALERIA_DIR,
            archivo
        )

        for archivo in sorted(
            os.listdir(GALERIA_DIR)
        )

        if archivo.lower().endswith(
            extensiones
        )

    ]


def galeria():

    fotos = obtener_galeria()

    if not fotos:
        return

    carrusel_fotos(
        fotos,
        key_prefix="galeria"
    )


# ============================================================
# ANIVERSARIO
# ============================================================

def dias_para_aniversario():

    hoy = datetime.date.today()

    aniversario = datetime.date(
        hoy.year,
        9,
        23
    )

    if aniversario < hoy:

        aniversario = datetime.date(
            hoy.year + 1,
            9,
            23
        )

    return (
        aniversario - hoy
    ).days


# ============================================================
# SLIDES
# ============================================================

def slide_portada():

    render_html("""

    <div class="cover wrapped-content">

        <div class="cover-content">

            <div class="eyebrow">
                NUESTRO WRAPPED · 2023 — 2026
            </div>

            <h1 class="cover-title">
                3 Años<br>
                Juntos
            </h1>

            <div class="cover-subtitle">

                Tres años.
                Cientos de momentos.
                Algunas canciones.
                Muchos recuerdos.

                <br><br>

                Esta es una pequeña parte
                de nuestra historia.

            </div>

        </div>

    </div>

    """)

    portada = os.path.join(
        FOTOS_DIR,
        "portada.png"
    )

    if os.path.exists(portada):

        mostrar_foto(
            portada,
            "Nuestra historia ❤️"
        )

    render_html("""

    <div class="quote">

        Todo comenzó con una fecha.
        Lo demás lo fuimos construyendo juntos.

    </div>

    """)


def slide_estadisticas():

    encabezado(
        "Tu año en números",
        "Si nuestra historia pudiera convertirse en estadísticas, probablemente se vería algo así.",
        "NUESTRO WRAPPED"
    )

    render_html("""

    <div class="stats-grid">

        <div class="stat-card">

            <div class="stat-number">
                3
            </div>

            <div class="stat-label">
                AÑOS JUNTOS
            </div>

        </div>


        <div class="stat-card">

            <div class="stat-number">
                11
            </div>

            <div class="stat-label">
                CANCIONES
            </div>

        </div>


        <div class="stat-card">

            <div class="stat-number">
                3
            </div>

            <div class="stat-label">
                LUGARES FAVORITOS
            </div>

        </div>


        <div class="stat-card">

            <div class="stat-number">
                2
            </div>

            <div class="stat-label">
                CONEJITOS 🐰
            </div>

        </div>

    </div>

    """)

    render_html("""

    <div class="story-card">

        Nuestra estadística favorita no se puede medir:

        <br><br>

        <strong>
        todas las veces que elegimos estar juntos.
        </strong>

    </div>

    """)


def slide_inicio():

    encabezado(
        "Todo comenzó aquí",
        "Hay fechas que terminan convirtiéndose en algo mucho más grande de lo que imaginábamos.",
        "24 · 07 · 2023"
    )

    render_html("""

    <div class="big-number">
        24
    </div>

    """)

    render_html("""

    <div class="story-card">

        El 24 de julio de 2023 comenzó nuestra historia.

        <br><br>

        Desde ese momento empezamos a crear recuerdos,
        aprender uno del otro y descubrir todo lo que
        podíamos vivir juntos.

    </div>

    """)

    mostrar_foto(
        FOTOS["inicio"],
        "El comienzo de nosotros ❤️"
    )


def slide_caifanes():

    encabezado(
        "Una noche con Caifanes",
        "Porque algunos recuerdos se quedan asociados para siempre a una canción.",
        "CAIFANES 🎸"
    )

    mostrar_foto(
        FOTOS["caifanes"],
        "Una noche para recordar 🎸❤️"
    )

    render_html("""

    <div class="story-card">

        Entre música, gente y emoción vivimos una de
        esas noches que se quedan guardadas.

        <br><br>

        Porque no solamente importa a dónde vamos,
        sino con quién compartimos el momento.

    </div>

    """)


def slide_diciembre_2023():

    encabezado(
        "Nuestro primer diciembre",
        "Un mes lleno de pequeños momentos que terminaron siendo grandes recuerdos.",
        "DICIEMBRE · 2023"
    )

    memoria(
        "🏡 El pueblo de mi papá",
        "Un lugar diferente, pero mucho más especial porque estabas conmigo."
    )

    memoria(
        "🎉 La piñata",
        "Compartiendo momentos sencillos que terminaron convirtiéndose en recuerdos."
    )

    memoria(
        "🌊 Rumbo a Mazatlán",
        "Una aventura más de tantas que hemos ido sumando a nuestra historia."
    )

    carrusel_fotos(
        FOTOS["diciembre_2023"],
        CAPTIONS["diciembre_2023"],
        "diciembre"
    )


def slide_2024():

    encabezado(
        "2024",
        "Un año de cambios, proyectos, aventuras y nuestra primera Navidad juntos.",
        "CAPÍTULO · 2024"
    )

    memoria(
        "🎓 SHESPAT",
        "Emprendiendo juntos con las togas y estolas."
    )

    memoria(
        "🏍️ La moto",
        "Ese momento en el que empezaste a enseñarme a manejar."
    )

    memoria(
        "💇 Mi cambio de look",
        "Gracias a ti también llegaron nuevos cambios y nuevas versiones de mí."
    )

    memoria(
        "🎄 Nuestra primera Navidad",
        "Nuestra primera Navidad juntos, creando una tradición propia."
    )

    carrusel_fotos(
        FOTOS["y2024"],
        CAPTIONS["y2024"],
        "y2024"
    )


def slide_2025_2026():

    encabezado(
        "Seguimos escribiendo la historia",
        "Porque después de tres años todavía seguimos acumulando momentos.",
        "2025 · 2026"
    )

    memoria(
        "🎁 El reloj para mi papá",
        "Un detalle que terminó convirtiéndose en otro recuerdo de nuestra historia."
    )

    memoria(
        "🐰 Carajo y Nena",
        "Nuestros conejitos y dos pequeños integrantes de nuestra historia."
    )

    memoria(
        "🎡 La feria",
        "La feria, la rueda de la fortuna y otra aventura juntos."
    )

    carrusel_fotos(
        FOTOS["y2025_2026"],
        CAPTIONS["y2025_2026"],
        "y2025"
    )


def slide_gastronomia():

    encabezado(
        "Nuestros lugares",
        "Porque una relación también se construye alrededor de una mesa.",
        "FOOD · FOOD · FOOD 🍜"
    )

    for indice, restaurante in enumerate(
        RESTAURANTES,
        start=1
    ):

        render_html(f"""

        <div class="place">

            <div class="place-number">
                {indice:02d}
            </div>

            <div class="place-name">
                {esc(restaurante["nombre"])}
            </div>

            <div class="place-description">
                {esc(restaurante["descripcion"])}
            </div>

        </div>

        """)

    render_html("""

    <div class="quote">

        Comida + plática + nosotros
        = otro recuerdo.

    </div>

    """)


def slide_playlist():

    encabezado(
        "Nuestra banda sonora",
        "11 canciones que, de una u otra manera, terminaron formando parte de nuestra historia.",
        "SOUNDTRACK 🎵"
    )

    render_html("""

    <div class="playlist-intro">

        <div style="
            font-size:.68rem;
            letter-spacing:.15em;
            color:rgba(255,255,255,.45);
            font-weight:800;
        ">

            TU PLAYLIST PERSONAL

        </div>

        <div style="
            font-family:'Unbounded';
            font-size:1.5rem;
            margin-top:.5rem;
        ">

            Nuestra historia
            <br>
            en canciones.

        </div>

    </div>

    """)

    for indice, cancion in enumerate(
        CANCIONES,
        start=1
    ):

        render_html(f"""

        <div class="track">

            <div class="track-number">

                {indice:02d}

            </div>

            <div>

                <div class="track-title">

                    {esc(cancion["titulo"])}

                </div>

                <div class="track-artist">

                    {esc(cancion["artista"])}

                </div>

                <div class="track-meaning">

                    {esc(cancion["significado"])}

                </div>

            </div>

        </div>

        """)


def slide_galeria():

    encabezado(
        "Nuestros recuerdos",
        "Una colección de momentos que queremos conservar.",
        "MEMORIES 📸"
    )

    galeria()


def slide_cierre():

    dias = dias_para_aniversario()

    render_html(f"""

    <div class="final wrapped-content">

        <div class="eyebrow">
            Y ESTO APENAS ES UNA PARTE
        </div>

        <div class="final-title">

            Gracias por estos
            <br>
            3 años ❤️

        </div>

        <div class="days">

            Faltan aproximadamente

            <span class="days-number">
                {dias}
            </span>

            días para nuestro próximo aniversario 💫

        </div>

    </div>

    """)

    render_html("""

    <div class="story-card">

        Hemos cambiado, aprendido, reído, salido,
        comido, viajado y vivido muchas cosas juntos.

        <br><br>

        Este Wrapped solamente puede guardar algunas
        fotografías y canciones.

        <br><br>

        Nuestra historia tiene muchísimos más momentos.

    </div>

    """)

    render_html("""

    <div class="quote">

        Y si pudiera volver al
        24 de julio de 2023,
        volvería a elegir comenzar
        esta historia contigo.

    </div>

    """)


# ============================================================
# LISTA DE SLIDES
# ============================================================

SLIDES = [

    (
        "Portada",
        slide_portada
    ),

    (
        "Estadísticas",
        slide_estadisticas
    ),

    (
        "El inicio",
        slide_inicio
    ),

    (
        "Caifanes",
        slide_caifanes
    ),

    (
        "Diciembre 2023",
        slide_diciembre_2023
    ),

    (
        "2024",
        slide_2024
    ),

    (
        "2025 · 2026",
        slide_2025_2026
    ),

    (
        "Nuestros lugares",
        slide_gastronomia
    ),

    (
        "Nuestra banda sonora",
        slide_playlist
    ),

    (
        "Galería",
        slide_galeria
    ),

    (
        "Cierre",
        slide_cierre
    ),

]


# ============================================================
# BARRA DE PROGRESO
# ============================================================

def progreso(indice):

    elementos = ""

    for i in range(len(SLIDES)):

        clase = (
            "progress-segment active"
            if i <= indice
            else "progress-segment"
        )

        elementos += (
            f'<div class="{clase}"></div>'
        )

    render_html(
        f"""
        <div class="progress-wrapper">
            {elementos}
        </div>
        """
    )


# ============================================================
# NAVEGACIÓN
# ============================================================

def navegacion(indice):

    total = len(SLIDES)

    st.write("")

    col1, col2, col3 = st.columns(
        [1, 2, 1]
    )

    with col1:

        if indice > 0:

            if st.button(
                "←",
                key=f"back_{indice}",
                use_container_width=True
            ):

                st.session_state.slide = (
                    indice - 1
                )

                st.rerun()

    with col2:

        render_html(f"""

        <div style="
            text-align:center;
            color:rgba(255,255,255,.4);
            font-size:.68rem;
            letter-spacing:.16em;
            padding-top:12px;
        ">

            {indice + 1:02d}
            /
            {total:02d}

        </div>

        """)

    with col3:

        if indice < total - 1:

            if st.button(
                "→",
                key=f"forward_{indice}",
                use_container_width=True
            ):

                st.session_state.slide = (
                    indice + 1
                )

                st.rerun()


# ============================================================
# MAIN
# ============================================================

def main():

    # CSS
    inyectar_css()

    # Música
    musica_fondo()

    # Estado
    if "slide" not in st.session_state:

        st.session_state.slide = 0

    indice = max(
        0,
        min(
            st.session_state.slide,
            len(SLIDES) - 1
        )
    )

    st.session_state.slide = indice

    # Progreso
    progreso(indice)

    # Slide
    SLIDES[indice][1]()

    # Navegación
    navegacion(indice)

    # Instrucción de navegación
    if indice == 0:

        render_html("""

        <div style="
            text-align:center;
            color:rgba(255,255,255,.3);
            font-size:.65rem;
            margin-top:1rem;
        ">

            DESLIZA O PRESIONA →
            PARA COMENZAR

        </div>

        """)


# ============================================================
# EJECUCIÓN
# ============================================================

if __name__ == "__main__":
    main()
