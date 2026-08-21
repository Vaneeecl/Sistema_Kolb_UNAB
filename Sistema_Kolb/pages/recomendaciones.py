import streamlit as st

# =====================================================
# ICONOS SVG PROFESIONALES (SIN EMOJIS)
# =====================================================

ICON_LIGHT = """
<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#F58220" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
<path d="M9 18h6"/><path d="M10 22h4"/><path d="M12 2a7 7 0 0 0-4 12c.8.8 1.4 1.8 1.6 3h4.8c.2-1.2.8-2.2 1.6-3A7 7 0 0 0 12 2z"/>
</svg>
"""

ICON_BOOK = """
<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#F58220" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
<path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"/><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5V4.5A2.5 2.5 0 0 1 6.5 2z"/>
</svg>
"""

ICON_TEAM = """
<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#F58220" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
<path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"></path><circle cx="9" cy="7" r="4"></circle><path d="M23 21v-2a4 4 0 0 0-3-3.87"></path><path d="M16 3.13a4 4 0 0 1 0 7.75"></path>
</svg>
"""

ICON_SEARCH = """
<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#F58220" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
<circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line>
</svg>
"""

ICON_MAP = """
<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#F58220" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
<circle cx="18" cy="5" r="3"></circle><circle cx="6" cy="12" r="3"></circle><circle cx="18" cy="19" r="3"></circle><line x1="8.59" y1="13.51" x2="15.42" y2="17.49"></line><line x1="15.41" y1="6.51" x2="8.59" y2="10.49"></line>
</svg>
"""

ICON_NOTE = """
<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#F58220" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
<path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline><line x1="16" y1="13" x2="8" y2="13"></line><line x1="16" y1="17" x2="8" y2="17"></line><polyline points="10 9 9 9 8 9"></polyline>
</svg>
"""

ICON_PLAY = """
<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#F58220" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
<polygon points="5 3 19 12 5 21 5 3"></polygon>
</svg>
"""

ICON_DOC = """
<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#F58220" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
<path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline><line x1="16" y1="13" x2="8" y2="13"></line><line x1="16" y1="17" x2="8" y2="17"></line>
</svg>
"""

ICON_INTERACTIVE = """
<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#F58220" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
<rect x="2" y="3" width="20" height="14" rx="2" ry="2"></rect><line x1="8" y1="21" x2="16" y2="21"></line><line x1="12" y1="17" x2="12" y2="21"></line>
</svg>
"""

# =====================================================
# STEPPER
# =====================================================

def render_stepper():
    pasos = ["Información", "Cuestionario", "Resultados", "Recomendaciones"]
    html = ""
    for i, paso in enumerate(pasos, start=1):
        activo = i <= 4
        color = "#F58220" if activo else "#E5E7EB"
        color_texto = "#1F2D4D" if i == 4 else "#6B7280"

        html += f'<div style="display:flex;flex-direction:column;align-items:center;"><div style="width:32px;height:32px;border-radius:50%;background:{color};color:white;display:flex;align-items:center;justify-content:center;font-weight:700;">{i}</div><div style="margin-top:6px;font-size:12px;color:{color_texto};font-weight:700;">{paso}</div></div>'

        if i < 4:
            html += '<div style="flex:1;height:3px;background:#F58220;margin:0 10px 22px 10px;"></div>'

    st.markdown(f'<div style="display:flex;align-items:flex-start;margin-bottom:35px;">{html}</div>', unsafe_allow_html=True)

# =====================================================
# ESTILOS CSS PARA FIJAR LA ALTURA EXACTA DE LAS 3 TARJETAS
# =====================================================

st.markdown("""
<style>
[data-testid="column"] > div {
    height: 100%;
}
[data-testid="column"] > div > div {
    height: 100% !important;
    min-height: 680px !important;
    display: flex;
    flex-direction: column;
    justify-content: flex-start;
}

.sub-card {
    background: #FFFAF5;
    border: 1px solid #FDEEE1;
    border-radius: 12px;
    padding: 12px 14px;
    margin-bottom: 10px;
}
.footer {
    text-align: center;
    color: #6B7280;
    font-size: 12px;
    margin-top: 30px;
    padding-top: 20px;
    border-top: 1px solid #ECECEC;
}
</style>
""", unsafe_allow_html=True)

# =====================================================
# FUNCIÓN PRINCIPAL
# =====================================================

def mostrar_recomendaciones():
    estilo = st.session_state.get("resultado", "Divergente")

    recomendaciones = {

        # =====================================================
        # ESTILO DIVERGENTE
        # =====================================================

        "Divergente": {

            "descripcion": "Como aprendiz divergente, te beneficias al conectar la teoría con experiencias reales y analizar los problemas desde diferentes perspectivas.",

            "estrategias": [
                (
                    "Aprendizaje colaborativo",
                    "Participa en discusiones grupales, debates y trabajo en equipo. Compartir ideas y escuchar diferentes puntos de vista enriquece tu comprensión.",
                    ICON_TEAM
                ),
                (
                    "Estudio de casos reales",
                    "Analiza situaciones reales donde se apliquen las Ecuaciones Diferenciales. Relacionar la teoría con contextos reales facilitará tu aprendizaje.",
                    ICON_SEARCH
                ),
                (
                    "Mapas conceptuales",
                    "Organiza la información visualmente. Los mapas conceptuales te ayudan a relacionar conceptos y ver el panorama completo.",
                    ICON_MAP
                ),
                (
                    "Reflexión y síntesis",
                    "Después de cada tema, sintetiza lo aprendido con tus propias palabras y reflexiona sobre cómo aplicarlo a nuevas situaciones.",
                    ICON_NOTE
                )
            ],

            "recursos": [
                (
                    "Video: Visión geométrica de las ecuaciones diferenciales",
                    "Visualización del comportamiento de las soluciones.",
                    ICON_PLAY,
                    "https://www.ocw.mit.edu/courses/18-03-differential-equations-spring-2010/video_galleries/video-lectures/"
                ),
                (
                    "Artículo: Introducción a las ecuaciones diferenciales",
                    "Conceptos y aplicaciones de las ecuaciones diferenciales.",
                    ICON_DOC,
                    "https://www.open.edu/openlearn/science-maths-technology/introduction-differential-equations/content-section-0"
                ),
                (
                    "Actividad interactiva: Campo de pendientes",
                    "Explora visualmente las soluciones de una ecuación diferencial.",
                    ICON_INTERACTIVE,
                    "https://www.geogebra.org/m/ggWUWEZe"
                ),
                (
                    "Guía de ejercicios: Problem Sets",
                    "Problemas de ecuaciones diferenciales para reforzar el análisis.",
                    ICON_BOOK,
                    "https://www.ocw.mit.edu/courses/18-03-differential-equations-spring-2010/pages/assignments/"
                )
            ]
        },

        # =====================================================
        # ESTILO ASIMILADOR
        # =====================================================

        "Asimilador": {

            "descripcion": "Tu estilo de aprendizaje se caracteriza por comprender mejor modelos teóricos y conceptos abstractos estructurados.",

            "estrategias": [
                (
                    "Mapas conceptuales",
                    "Utiliza mapas conceptuales antes de resolver ejercicios para relacionar los conceptos principales.",
                    ICON_MAP
                ),
                (
                    "Resúmenes teóricos",
                    "Construye resúmenes de cada tema trabajado y analiza las relaciones entre conceptos y procedimientos.",
                    ICON_NOTE
                ),
                (
                    "Organización conceptual",
                    "Clasifica los métodos de solución y establece relaciones entre sus características y aplicaciones.",
                    ICON_BOOK
                ),
                (
                    "Análisis de procedimientos",
                    "Compara diferentes métodos de solución para identificar sus ventajas y condiciones de aplicación.",
                    ICON_SEARCH
                )
            ],

            "recursos": [
                (
                    "Video: Clases de Differential Equations",
                    "Explicaciones estructuradas sobre conceptos y métodos.",
                    ICON_PLAY,
                    "https://www.ocw.mit.edu/courses/18-03-differential-equations-spring-2010/video_galleries/video-lectures/"
                ),
                (
                    "Artículo: Introducción a las ecuaciones diferenciales",
                    "Material estructurado sobre métodos y aplicaciones.",
                    ICON_DOC,
                    "https://www.open.edu/openlearn/science-maths-technology/introduction-differential-equations/content-section-0"
                ),
                (
                    "Actividad interactiva: Campo de pendientes",
                    "Relaciona la representación gráfica con el comportamiento de las soluciones.",
                    ICON_INTERACTIVE,
                    "https://www.geogebra.org/m/qYENU3ZB"
                ),
                (
                    "Guía: Lecture Notes",
                    "Notas de clase sobre conceptos y métodos de ecuaciones diferenciales.",
                    ICON_BOOK,
                    "https://www.ocw.mit.edu/courses/18-03-differential-equations-spring-2010/resources/lecture-notes/"
                )
            ]
        },

        # =====================================================
        # ESTILO CONVERGENTE
        # =====================================================

        "Convergente": {

            "descripcion": "Te orientas hacia la aplicación práctica del conocimiento y la resolución eficiente de problemas técnicos.",

            "estrategias": [
                (
                    "Práctica constante",
                    "Resuelve ejercicios paso a paso para consolidar los procedimientos de solución.",
                    ICON_SEARCH
                ),
                (
                    "Proyectos técnicos",
                    "Desarrolla problemas aplicados de ingeniería que requieran utilizar ecuaciones diferenciales.",
                    ICON_TEAM
                ),
                (
                    "Comprobación de resultados",
                    "Verifica las soluciones obtenidas y analiza si responden adecuadamente al problema planteado.",
                    ICON_NOTE
                ),
                (
                    "Aplicación de métodos",
                    "Selecciona el método de solución más adecuado según las características de cada ecuación.",
                    ICON_BOOK
                )
            ],

            "recursos": [
                (
                    "Video: Método numérico de Euler",
                    "Resolución y aplicación de un método numérico.",
                    ICON_PLAY,
                    "https://www.ocw.mit.edu/courses/18-03-differential-equations-spring-2010/video_galleries/video-lectures/"
                ),
                (
                    "Artículo: Lecture Notes de Differential Equations",
                    "Métodos analíticos, gráficos y numéricos.",
                    ICON_DOC,
                    "https://www.ocw.mit.edu/courses/18-03-differential-equations-spring-2010/pages/lecture-notes/"
                ),
                (
                    "Actividad interactiva: Método de Euler",
                    "Modifica parámetros y observa el comportamiento de la aproximación.",
                    ICON_INTERACTIVE,
                    "https://www.geogebra.org/m/pcnda2e3"
                ),
                (
                    "Guía de ejercicios: Assignments",
                    "Ejercicios y problemas de aplicación de ecuaciones diferenciales.",
                    ICON_BOOK,
                    "https://www.ocw.mit.edu/courses/18-03-differential-equations-spring-2010/pages/assignments/"
                )
            ]
        },

        # =====================================================
        # ESTILO ACOMODADOR
        # =====================================================

        "Acomodador": {

            "descripcion": "Prefieres aprender haciendo mediante actividades prácticas, experimentales y dinámicas.",

            "estrategias": [
                (
                    "Ensayo y error",
                    "Aprende mediante retos prácticos en los que puedas probar diferentes procedimientos y comparar resultados.",
                    ICON_SEARCH
                ),
                (
                    "Proyectos de aula",
                    "Participa activamente en actividades y proyectos relacionados con situaciones reales.",
                    ICON_TEAM
                ),
                (
                    "Experimentación",
                    "Modifica condiciones y parámetros para observar directamente cómo cambia el comportamiento de una solución.",
                    ICON_INTERACTIVE
                ),
                (
                    "Resolución de problemas",
                    "Aplica los conceptos aprendidos a situaciones concretas y contextualizadas.",
                    ICON_BOOK
                )
            ],

            "recursos": [
                (
                    "Video: Métodos gráficos y numéricos",
                    "Explora diferentes formas de aproximar y visualizar soluciones.",
                    ICON_PLAY,
                    "https://opencw.aprende.org/resources/res-18-009-learn-differential-equations-up-close-with-gilbert-strang-and-cleve-moler-fall-2015/differential-equations-and-linear-algebra/"
                ),
                (
                    "Artículo: Aplicaciones de las ecuaciones diferenciales",
                    "Ejemplos de utilización de ecuaciones diferenciales en diferentes contextos.",
                    ICON_DOC,
                    "https://www.open.edu/openlearn/science-maths-technology/introduction-differential-equations/content-section-0"
                ),
                (
                    "Actividad interactiva: Explorando una EDO",
                    "Modifica condiciones iniciales y observa el campo direccional y la solución.",
                    ICON_INTERACTIVE,
                    "https://www.geogebra.org/m/dQM1cKDe"
                ),
                (
                    "Guía: Recitations",
                    "Problemas prácticos sobre modelos y métodos de ecuaciones diferenciales.",
                    ICON_BOOK,
                    "https://opencw.aprende.org/courses/mathematics/18-03-differential-equations-spring-2010/recitations/"
                )
            ]
        }
    }

    datos = recomendaciones.get(estilo, recomendaciones["Divergente"])

    render_stepper()

    # =====================================================
    # TÍTULO
    # =====================================================

    st.markdown("""
    <div style="text-align:center; margin-bottom:30px;">
        <h2 style="color:#1F2D4D; font-size:30px; font-weight:800; margin-bottom:6px;">
            Recomendaciones pedagógicas personalizadas 
        </h2>
        <p style="color:#6B7280; font-size:15px;">
            A partir de tu estilo de aprendizaje identificado, te ofrecemos estrategias y recursos que pueden potenciar tu aprendizaje en Ecuaciones Diferenciales.
        </p>
    </div>
    """, unsafe_allow_html=True)

    # =====================================================
    # TRES COLUMNAS PRINCIPALES (ALTURAS IGUALADAS EXACTAS)
    # =====================================================

    col1, col2, col3 = st.columns([1, 1.3, 1], gap="large")

    # Columna 1: Estilo Identificado
    with col1:
        with st.container(border=True):
            st.markdown(f"""
            <div style="text-align: center; display: flex; flex-direction: column; justify-content: center; height: 100%; padding: 10px 0;">
                <div style="font-size: 11px; font-weight: 700; color: #6B7280; letter-spacing: 0.5px; margin-bottom: 10px;">
                    TU ESTILO DE APRENDIZAJE
                </div>
                <div style="font-size: 30px; font-weight: 900; color: #F58220; margin-bottom: 20px; letter-spacing: -0.5px;">
                    {estilo.upper()}
                </div>
                <div style="background: #FFF8F2; border-radius: 50%; width: 130px; height: 130px; margin: 0 auto 20px auto; display: flex; align-items: center; justify-content: center; border: 1px solid #FDEEE1;">
                    <svg width="60" height="60" viewBox="0 0 24 24" fill="none" stroke="#F58220" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
                        <path d="M9.5 2A2.5 2.5 0 0 1 12 4.5v15a2.5 2.5 0 0 1-4.96.44 2.5 2.5 0 0 1-2.96-3.08 3 3 0 0 1-.34-5.58 2.5 2.5 0 0 1 1.32-4.24 2.5 2.5 0 0 1 3.44-2.54Z"/>
                        <path d="M14.5 2A2.5 2.5 0 0 0 12 4.5v15a2.5 2.5 0 0 0 4.96.44 2.5 2.5 0 0 0 2.96-3.08 3 3 0 0 0 .34-5.58 2.5 2.5 0 0 0-1.32-4.24 2.5 2.5 0 0 0-3.44-2.54Z"/>
                    </svg>
                </div>
                <div style="font-size: 11px; font-weight: 700; color: #6B7280; margin-bottom: 4px;">
                    PROBABILIDAD ESTIMADA
                </div>
                <div style="font-size: 30px; font-weight: 800; color: #10B981; margin-bottom: 4px;">
                    90%
                </div>
                <div style="font-size: 13px; color: #10B981; font-weight: 600;">
                    ✓ Resultado orientativo
                </div>
            </div>
            """, unsafe_allow_html=True)

    # Columna 2: Estrategias pedagógicas sugeridas
    with col2:
        with st.container(border=True):
            st.markdown(f"""
            <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 12px;">
                <div style="background: #FFF6ED; padding: 8px; border-radius: 8px; display: flex;">{ICON_LIGHT}</div>
                <h3 style="margin: 0; font-size: 18px; font-weight: 800; color: #1F2D4D;">Estrategias pedagógicas sugeridas para ti</h3>
            </div>
            <p style="color: #4B5563; font-size: 13.5px; line-height: 1.5; margin-bottom: 16px;">
                {datos["descripcion"]}
            </p>
            """, unsafe_allow_html=True)

            for titulo, desc, icono in datos["estrategias"]:
                st.markdown(f"""
                <div class="sub-card">
                    <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 4px;">
                        <div style="display: flex; align-items: center;">{icono}</div>
                        <div style="font-weight: 700; color: #1F2D4D; font-size: 14px;">{titulo}</div>
                    </div>
                    <div style="color: #4B5563; font-size: 13px; line-height: 1.4; padding-left: 32px;">{desc}</div>
                </div>
                """, unsafe_allow_html=True)

    # Columna 3: Recursos recomendados
    with col3:
        with st.container(border=True):
            st.markdown(f"""
            <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 12px;">
                <div style="background: #FFF6ED; padding: 8px; border-radius: 8px; display: flex;">{ICON_BOOK}</div>
                <h3 style="margin: 0; font-size: 18px; font-weight: 800; color: #1F2D4D;">Recursos recomendados</h3>
            </div>
            <p style="color:#4B5563; font-size:13.5px; line-height:1.5; margin-bottom:16px;">
                Materiales externos seleccionados para complementar tu proceso de aprendizaje en Ecuaciones Diferenciales.
            </p>
            """, unsafe_allow_html=True)

            for titulo, desc, icono, url in datos["recursos"]:
                # IMPORTANTE: todo el HTML va en una sola línea (sin saltos de línea
                # ni indentación interna). textwrap.dedent() NO garantiza dejar todas
                # las líneas en 0 espacios cuando hay niveles de anidación distintos,
                # y Markdown convierte en "bloque de código" cualquier línea que quede
                # con 4+ espacios de indentación, lo que hacía que el HTML se mostrara
                # como texto crudo en vez de renderizarse.
                html_recurso = (
                    '<div class="sub-card">'
                    '<div style="display:flex; align-items:flex-start; gap:10px;">'
                    f'<div style="display:flex; align-items:center; margin-top:2px;">{icono}</div>'
                    '<div>'
                    f'<div style="font-weight:700; color:#1F2D4D; font-size:13.5px; margin-bottom:3px;">'
                    f'<a href="{url}" target="_blank" style="color:#1F2D4D; text-decoration:none;">{titulo}</a>'
                    '</div>'
                    f'<div style="color:#6B7280; font-size:12.5px; line-height:1.4; margin-bottom:5px;">{desc}</div>'
                    f'<a href="{url}" target="_blank" style="color:#F58220; font-size:11.5px; font-weight:700; text-decoration:none;">↗ Abrir recurso</a>'
                    '</div>'
                    '</div>'
                    '</div>'
                )
                st.markdown(html_recurso, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # =====================================================
    # MENSAJE DE AGRADECIMIENTO ANTES DE LOS BOTONES
    # =====================================================

    st.markdown("""
    <div style="background: #FFF8F2; border: 1px solid #FDEEE1; border-radius: 12px; padding: 20px; text-align: center; margin-bottom: 25px;">
        <h4 style="color: #F58220; font-size: 18px; font-weight: 800; margin-bottom: 6px;">¡Gracias por completar la evaluación!</h4>
        <p style="color: #4B5563; font-size: 14px; margin: 0; line-height: 1.5;">
            Esperamos que estas recomendaciones personalizadas te acompañen y potencien con éxito tu proceso de aprendizaje en Ecuaciones Diferenciales.
        </p>
    </div>
    """, unsafe_allow_html=True)

    # =====================================================
    # BOTONES DE NAVEGACIÓN
    # =====================================================

    col_b1, col_b2 = st.columns(2, gap="large")

    with col_b1:
        if st.button("← Volver a resultados", use_container_width=True):
            st.session_state.page = "resultado"
            st.rerun()

    with col_b2:
        if st.button("Nueva evaluación", use_container_width=True, type="primary"):
            st.session_state.page = "bienvenida"
            st.session_state.pregunta_actual = 0
            st.session_state.respuestas = {}
            st.session_state.resultado = None
            st.session_state.probabilidades = None
            st.session_state.datos_estudiante = {}
            st.rerun()

    # =====================================================
    # FOOTER
    # =====================================================

    st.markdown("""
    <div class="footer">
        Universidad Autónoma de Bucaramanga | Facultad de Ingenierías | Maestría en Ciencia de Datos
    </div>
    """, unsafe_allow_html=True)
