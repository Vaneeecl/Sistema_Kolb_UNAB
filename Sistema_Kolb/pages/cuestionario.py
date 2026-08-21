import streamlit as st
from utils.prediccion import predecir_estilo

# ==========================================================
# PREGUNTAS DEL CUESTIONARIO
# ==========================================================

preguntas = [
    {
        "codigo": "EC2",
        "dimension": "Experiencia Concreta (EC)",
        "titulo": "RECEPTIVAMENTE",
        "texto": "Estoy concentrado plenamente en lo que sucede y disponible para recoger la mayor cantidad de elementos posible."
    },
    {
        "codigo": "EC3",
        "dimension": "Experiencia Concreta (EC)",
        "titulo": "SINTIENDO",
        "texto": "Pongo atención a lo que siento espontáneamente y a lo que soy dentro de la situación."
    },
    {
        "codigo": "EC4",
        "dimension": "Experiencia Concreta (EC)",
        "titulo": "ACEPTANDO",
        "texto": "Acepto la situación tal como se presenta y procuro adaptarme a ella."
    },
    {
        "codigo": "EC5",
        "dimension": "Experiencia Concreta (EC)",
        "titulo": "INTUITIVAMENTE",
        "texto": "Confío en mis intuiciones y primeras impresiones para comprender una situación."
    },
    {
        "codigo": "EC7",
        "dimension": "Experiencia Concreta (EC)",
        "titulo": "EXPERIMENTANDO",
        "texto": "Prefiero aprender involucrándome directamente en la experiencia."
    },
    {
        "codigo": "EC8",
        "dimension": "Experiencia Concreta (EC)",
        "titulo": "VIVIENDO",
        "texto": "Aprendo mejor cuando participo activamente en las situaciones."
    },
    {
        "codigo": "OR1",
        "dimension": "Observación Reflexiva (OR)",
        "titulo": "OBSERVANDO",
        "texto": "Analizo cuidadosamente lo que ocurre antes de sacar conclusiones."
    },
    {
        "codigo": "OR2",
        "dimension": "Observación Reflexiva (OR)",
        "titulo": "REFLEXIONANDO",
        "texto": "Prefiero pensar detenidamente sobre una experiencia antes de actuar."
    },
    {
        "codigo": "OR3",
        "dimension": "Observación Reflexiva (OR)",
        "titulo": "ESCUCHANDO",
        "texto": "Aprendo observando y escuchando a los demás."
    },
    {
        "codigo": "OR5",
        "dimension": "Observación Reflexiva (OR)",
        "titulo": "ANALIZANDO",
        "texto": "Me gusta revisar diferentes perspectivas antes de tomar decisiones."
    },
    {
        "codigo": "OR7",
        "dimension": "Observación Reflexiva (OR)",
        "titulo": "PENSANDO",
        "texto": "Dedico tiempo a comprender una situación antes de intervenir."
    },
    {
        "codigo": "CA1",
        "dimension": "Conceptualización Abstracta (CA)",
        "titulo": "RAZONANDO",
        "texto": "Prefiero organizar las ideas mediante conceptos y teorías."
    },
    {
        "codigo": "CA3",
        "dimension": "Conceptualización Abstracta (CA)",
        "titulo": "LÓGICAMENTE",
        "texto": "Me siento cómodo utilizando el razonamiento lógico para aprender."
    },
    {
        "codigo": "CA5",
        "dimension": "Conceptualización Abstracta (CA)",
        "titulo": "TEORIZANDO",
        "texto": "Disfruto comprender los principios que explican una situación."
    },
    {
        "codigo": "EA1",
        "dimension": "Experimentación Activa (EA)",
        "titulo": "ACTUANDO",
        "texto": "Prefiero poner rápidamente en práctica las ideas."
    },
    {
        "codigo": "EA2",
        "dimension": "Experimentación Activa (EA)",
        "titulo": "HACIENDO",
        "texto": "Aprendo mejor cuando realizo actividades prácticas."
    },
    {
        "codigo": "EA7",
        "dimension": "Experimentación Activa (EA)",
        "titulo": "APLICANDO",
        "texto": "Me gusta comprobar inmediatamente si una idea funciona."
    },
    {
        "codigo": "EA8",
        "dimension": "Experimentación Activa (EA)",
        "titulo": "EJECUTANDO",
        "texto": "Prefiero aprender realizando tareas concretas."
    },
    {
        "codigo": "EA9",
        "dimension": "Experimentación Activa (EA)",
        "titulo": "PRACTICANDO",
        "texto": "Consolido mi aprendizaje cuando puedo practicar lo aprendido."
    }
]

# ==========================================================
# OPCIONES DE RESPUESTA
# ==========================================================

opciones = [
    "Me identifica totalmente",
    "Me identifica con frecuencia",
    "Me identifica poco",
    "No me identifica"
]

svg_iconos = [
    '''<div style="width: 38px; height: 38px; border-radius: 50%; background: #FFF8F2; display: flex; align-items: center; justify-content: center; margin: 0 auto 6px auto; border: 1px solid #F2E6D9;"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#F58220" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"></circle><circle cx="12" cy="12" r="6"></circle><circle cx="12" cy="12" r="2"></circle></svg></div>''',
    '''<div style="width: 38px; height: 38px; border-radius: 50%; background: #FFF8F2; display: flex; align-items: center; justify-content: center; margin: 0 auto 6px auto; border: 1px solid #F2E6D9;"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#F58220" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"></polygon></svg></div>''',
    '''<div style="width: 38px; height: 38px; border-radius: 50%; background: #FFF8F2; display: flex; align-items: center; justify-content: center; margin: 0 auto 6px auto; border: 1px solid #F2E6D9;"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#F58220" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"></circle><path d="M8 14s1.5 2 4 2 4-2 4-2"></path><line x1="9" y1="9" x2="9.01" y2="9"></line><line x1="15" y1="9" x2="15.01" y2="9"></line></svg></div>''',
    '''<div style="width: 38px; height: 38px; border-radius: 50%; background: #FFF8F2; display: flex; align-items: center; justify-content: center; margin: 0 auto 6px auto; border: 1px solid #F2E6D9;"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#F58220" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"></circle><line x1="15" y1="9" x2="9" y2="15"></line><line x1="9" y1="9" x2="15" y2="15"></line></svg></div>'''
]

# ==========================================================
# INICIALIZAR SESSION STATE
# ==========================================================

if "pregunta_actual" not in st.session_state:
    st.session_state.pregunta_actual = 0

if "respuestas" not in st.session_state or not isinstance(st.session_state.respuestas, dict):
    st.session_state.respuestas = {}

# ==========================================================
# FUNCIÓN PRINCIPAL
# ==========================================================

def mostrar_cuestionario():
    indice = st.session_state.pregunta_actual
    pregunta = preguntas[indice]
    porcentaje = int(((indice + 1) / len(preguntas)) * 100)

    # ==========================================================
    # ESTILOS CSS
    # ==========================================================
    st.markdown(
        """
        <style>
        .block-container {
            padding-top: 1rem;
            padding-bottom: 2rem;
        }
        .main-card {
            background: #FFFFFF;
            border: 1px solid #E5E7EB;
            border-radius: 14px;
            padding: 20px 24px;
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);
        }
        .header-title {
            font-size: 30px;
            font-weight: 800;
            letter-spacing: -0.5px;
            color: #1F2D4D;
        }
        .header-subtitle {
            font-size: 16px;
            color: #6B7280;
            margin-top: 2px;
        }
        .badge-guardado {
            background: #FFF8F2;
            border: 1px solid #F2E6D9;
            border-radius: 8px;
            padding: 6px 12px;
            font-size: 13px;
            color: #F58220;
            font-weight: 600;
            text-align: center;
        }
        .banda-dimension {
            background: #FFF8F2;
            border: 1px solid #F2E6D9;
            border-radius: 8px;
            padding: 6px 12px;
            color: #F58220;
            font-weight: 700;
            font-size: 13px;
            display: flex;
            align-items: center;
            gap: 6px;
        }
        .codigo-tag {
            background: #FFF8F2;
            color: #F58220;
            padding: 4px 10px;
            border-radius: 6px;
            font-weight: 800;
            font-size: 16px;
            border: 1px solid #F2E6D9;
        }
        .pregunta-titulo {
            color: #1F2D4D;
            font-size: 22px;
            font-weight: 800;
            margin-left: 10px;
        }
        .pregunta-texto {
            color: #4B5563;
            font-size: 17px;
            font-style: italic;
            line-height: 1.4;
            margin-top: 8px;
        }
        .pregunta-pregunta {
            color: #1F2D4D;
            font-size: 15px;
            font-weight: 700;
            margin-top: 12px;
            margin-bottom: 8px;
        }
        div[data-testid="column"] .stButton button {
            background: transparent !important;
            border: 2px solid transparent !important;
            box-shadow: none !important;
            width: 100% !important;
            height: 130px !important;
            min-height: 130px !important;
            border-radius: 10px !important;
            padding: 0px !important;
            color: transparent !important;
            cursor: pointer !important;
        }
        div[data-testid="column"] .stButton button:hover {
            background: rgba(245, 130, 32, 0.04) !important;
            border: 2px solid rgba(245, 130, 32, 0.20) !important;
        }
        div[data-testid="stHorizontalBlock"] > div:not(:nth-child(2)) .stButton button {
            min-height: 42px !important;
            height: 42px !important;
            border-radius: 8px !important;
            font-weight: 600;
            color: inherit !important;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # ==========================================================
    # STEPPER SUPERIOR
    # ==========================================================
    st.markdown(
        """
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 14px; padding: 0 10px;">
            <div style="text-align:center; flex:1;">
                <div style="width: 24px; height: 24px; background: #F58220; color: white; border-radius: 50%; display: flex; align-items: center; justify-content: center; margin: auto; font-size: 10px; font-weight: 700;">✓</div>
                <div style="margin-top: 2px; color: #F58220; font-size: 11px; font-weight: 600;">Información</div>
            </div>
            <div style="flex: 2; height: 2px; background: #F58220;"></div>
            <div style="text-align:center; flex:1;">
                <div style="width: 24px; height: 24px; background: #F58220; color: white; border-radius: 50%; display: flex; align-items: center; justify-content: center; margin: auto; font-size: 10px; font-weight: 700;">2</div>
                <div style="margin-top: 2px; color: #1F2D4D; font-weight: 700; font-size: 11px;">Cuestionario</div>
            </div>
            <div style="flex: 2; height: 2px; background: #E5E7EB;"></div>
            <div style="text-align:center; flex:1;">
                <div style="width: 24px; height: 24px; background: #F3F4F6; color: #9CA3AF; border-radius: 50%; display: flex; align-items: center; justify-content: center; margin: auto; font-size: 10px; font-weight: 700;">3</div>
                <div style="margin-top: 2px; color: #9CA3AF; font-size: 11px;">Resultados</div>
            </div>
            <div style="flex: 2; height: 2px; background: #E5E7EB;"></div>
            <div style="text-align:center; flex:1;">
                <div style="width: 24px; height: 24px; background: #F3F4F6; color: #9CA3AF; border-radius: 50%; display: flex; align-items: center; justify-content: center; margin: auto; font-size: 10px; font-weight: 700;">4</div>
                <div style="margin-top: 2px; color: #9CA3AF; font-size: 11px;">Recomendaciones</div>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    # ==========================================================
    # CONTENEDOR PRINCIPAL
    # ==========================================================
    with st.container():
        st.markdown('<div class="main-card">', unsafe_allow_html=True)

        # Header
        col_h1, col_h2 = st.columns([5, 2])
        with col_h1:
            st.markdown(
                """
                <div style="display: flex; align-items: center; gap: 14px;">
                    <div style="background: #FFF8F2; border: 1px solid #F2E6D9; padding: 12px; border-radius: 12px; display: flex; align-items: center; justify-content: center;">
                        <svg width="36" height="36" viewBox="0 0 24 24" fill="none" stroke="#F58220" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline><line x1="16" y1="13" x2="8" y2="13"></line><line x1="16" y1="17" x2="8" y2="17"></line><polyline points="10 9 9 9 8 9"></polyline></svg>
                    </div>
                    <div>
                        <div class="header-title">Cuestionario del Modelo de Kolb</div>
                        <div class="header-subtitle">Responde cada afirmación según tu experiencia.</div>
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )
        with col_h2:
            st.markdown('<div class="badge-guardado">🔒 Guardado automático</div>', unsafe_allow_html=True)

        st.markdown("<div style='height: 8px;'></div>", unsafe_allow_html=True)

        # Barra de Progreso
        st.markdown(
            f"""
            <div style="display: flex; justify-content: space-between; font-size: 12px; color: #4B5563; margin-bottom: 4px;">
                <span>Pregunta <b>{indice+1}</b> de <b>{len(preguntas)}</b></span>
                <span><b>{porcentaje}%</b> completado</span>
            </div>
            <div style="width: 100%; background-color: #E5E7EB; border-radius: 9999px; height: 8px; overflow: hidden;">
                <div style="width: {porcentaje}%; background-color: #F58220; height: 100%; border-radius: 9999px; transition: width 0.4s ease;"></div>
            </div>
            """,
            unsafe_allow_html=True
        )

        st.markdown("<hr style='margin: 12px 0; border: none; border-top: 1px solid #E5E7EB;'>", unsafe_allow_html=True)

        # ==========================================================
        # NÚMERO DE DIMENSIÓN ACTUAL
        # ==========================================================
        if indice < 6:
            numero_dimension = 1
        elif indice < 11:
            numero_dimension = 2
        elif indice < 14:
            numero_dimension = 3
        else:
            numero_dimension = 4

        # ==========================================================
        # BANDA SUPERIOR DE DIMENSIONES
        # ==========================================================
        st.markdown(
            f"""
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
                <div class="banda-dimension">
                    <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#F58220" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path><circle cx="12" cy="7" r="4"></circle></svg>
                    {pregunta["dimension"]}
                </div>
                <div style="color: #6B7280; font-size: 11px; text-align: right;">Dimensión {numero_dimension} de 4</div>
            </div>
            """,
            unsafe_allow_html=True
        )

        # Tarjeta de la Afirmación
        st.markdown(
            f"""
            <div style="background: #FFFDFB; border: 1px solid #F2E6D9; border-radius: 12px; padding: 14px 18px; margin-bottom: 10px;">
                <div style="display: flex; align-items: center;">
                    <span class="codigo-tag">{pregunta["codigo"]}</span>
                    <span class="pregunta-titulo">{pregunta["titulo"]}</span>
                </div>
                <div class="pregunta-texto">
                    "{pregunta["texto"]}"
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

        st.markdown('<div class="pregunta-pregunta">¿Qué tanto te identifica esta afirmación?</div>', unsafe_allow_html=True)

        # ==========================================================
        # TARJETAS DE OPCIONES INTERACTIVAS
        # ==========================================================
        respuesta_actual = st.session_state.respuestas.get(
            pregunta["codigo"],
            None
        )
        
        cols = st.columns(4)

        for i, opcion in enumerate(opciones):
            with cols[i]:
                seleccionado = (respuesta_actual == opcion)

                # Colores según selección
                if seleccionado:
                    borde_tarjeta = "#F58220"
                    fondo_tarjeta = "#FFF8F2"
                    sombra_tarjeta = "0 3px 10px rgba(245, 130, 32, 0.12)"
                else:
                    borde_tarjeta = "#E5E7EB"
                    fondo_tarjeta = "#FFFFFF"
                    sombra_tarjeta = "none"

                # Radio visual
                if seleccionado:
                    radio_html = """
                    <div style="
                        width:16px;
                        height:16px;
                        border-radius:50%;
                        border:2px solid #F58220;
                        display:flex;
                        align-items:center;
                        justify-content:center;
                        margin:6px auto 0 auto;
                        box-sizing:border-box;
                    ">
                        <div style="
                            width:8px;
                            height:8px;
                            border-radius:50%;
                            background:#F58220;
                        "></div>
                    </div>
                    """
                else:
                    radio_html = """
                    <div style="
                        width:16px;
                        height:16px;
                        border-radius:50%;
                        border:2px solid #D1D5DB;
                        margin:6px auto 0 auto;
                        box-sizing:border-box;
                    "></div>
                    """

                # Tarjeta visual
                contenido_tarjeta = f"""
                <div style="
                    background-color:{fondo_tarjeta};
                    border:2px solid {borde_tarjeta};
                    border-radius:10px;
                    padding:10px 4px;
                    text-align:center;
                    min-height:130px;
                    box-sizing:border-box;
                    display:flex;
                    flex-direction:column;
                    justify-content:space-between;
                    box-shadow:{sombra_tarjeta};
                    pointer-events:none;
                ">

                    <div>
                        {svg_iconos[i]}

                        <div style="
                            font-size:12px;
                            font-weight:600;
                            color:#374151;
                            line-height:1.2;
                        ">
                            {opcion}
                        </div>
                    </div>

                    <div>
                        {radio_html}
                    </div>

                </div>
                """
                
                # Botón real de Streamlit
                if st.button(
                    "",
                    key=f"card_btn_{indice}_{i}",
                    help=f"Seleccionar: {opcion}",
                    use_container_width=True
                ):
                    st.session_state.respuestas[pregunta["codigo"]] = opcion
                    st.rerun()
                
                # Mostrar la tarjeta sobre el botón
                st.markdown(
                    f"""
                    <div style="
                        margin-top:-130px;
                        position:relative;
                        z-index:2;
                        pointer-events:none;
                    ">
                        {contenido_tarjeta}
                    </div>
                    """,
                    unsafe_allow_html=True
                )

        st.markdown("<div style='height: 8px;'></div>", unsafe_allow_html=True)

        # ==========================================================
        # BOTONES DE NAVEGACIÓN INFERIORES
        # ==========================================================
        col_b1, col_b2, col_b3 = st.columns([1, 1.5, 1])

        with col_b1:
            if st.button("← Anterior", use_container_width=True, disabled=(indice == 0)):
                st.session_state.pregunta_actual -= 1
                st.rerun()

        with col_b2:
            st.markdown(
                """
                <div style="text-align: center; color: #6B7280; font-size: 11px; padding-top: 6px;">
                    🔒 Tu progreso se guarda automáticamente<br>Puedes salir y continuar cuando lo desees.
                </div>
                """,
                unsafe_allow_html=True
            )

        with col_b3:
            texto_boton = "Finalizar →" if indice == len(preguntas) - 1 else "Siguiente →"

            if st.button(texto_boton, use_container_width=True, type="primary"):

                # ==========================================================
                # VALIDACIÓN OBLIGATORIA DE LA RESPUESTA
                # ==========================================================

                respuesta_actual = st.session_state.respuestas.get(
                    pregunta["codigo"],
                    None
                )

                if respuesta_actual is None:

                    st.warning(
                        "⚠️ Por favor, selecciona una respuesta antes de continuar."
                    )

                elif indice == len(preguntas) - 1:

                    # ======================================================
                    # DATOS PERSONALES
                    # ======================================================

                    datos = st.session_state.datos_estudiante

                    # ======================================================
                    # RESPUESTAS DEL CUESTIONARIO
                    # ======================================================

                    respuestas = st.session_state.respuestas

                    # ======================================================
                    # EJECUTAR EL MODELO
                    # ======================================================

                    estilo, probabilidades = predecir_estilo(
                        datos,
                        respuestas
                    )

                    # ======================================================
                    # GUARDAR RESULTADOS
                    # ======================================================

                    st.session_state.resultado = estilo
                    st.session_state.probabilidades = probabilidades

                    # ======================================================
                    # IR A RESULTADOS
                    # ======================================================

                    st.session_state.page = "resultado"
                    st.rerun()

                else:

                    # ======================================================
                    # AVANZAR A LA SIGUIENTE PREGUNTA
                    # ======================================================

                    st.session_state.pregunta_actual += 1
                    st.rerun()

        st.markdown('</div>', unsafe_allow_html=True)

    # ==========================================================
    # CUADRO INFERIOR (TEXTO ORIGINAL CON LA BOMBILLA)
    # ==========================================================
    st.markdown("<div style='height: 8px;'></div>", unsafe_allow_html=True)
    
    with st.container():
        st.markdown(
            """
            <div style="background: #FFF8F2; border: 1px solid #F2E6D9; border-radius: 12px; padding: 12px 18px; position: relative; overflow: hidden; display: flex; align-items: center; justify-content: space-between;">
                <div style="display: flex; align-items: center; gap: 14px; z-index: 2;">
                    <div style="background: #FFFFFF; border: 1px solid #F2E6D9; padding: 8px; border-radius: 10px; display: flex; align-items: center; justify-content: center;">
                        <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#F58220" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M15 14c.2-1 .7-1.7 1.5-2.5 1-.9 1.5-2.2 1.5-3.5A6 6 0 0 0 6 8c0 1 .2 2.2 1.5 3.5.8.7 1.3 1.5 1.5 2.5"></path><path d="M9 18h6"></path><path d="M10 22h4"></path></svg>
                    </div>
                    <div style="font-size: 13px; color: #4B5563; line-height: 1.3;">
                        <b style="color: #1F2D4D; font-size: 13.5px;">Estás respondiendo preguntas sobre cómo experimentas situaciones nuevas.</b><br>
                        No hay respuestas correctas o incorrectas. Guíate por tu experiencia.
                    </div>
                </div>
                <div style="opacity: 0.1; position: absolute; right: 20px; z-index: 1;">
                    <svg width="70" height="70" viewBox="0 0 24 24" fill="none" stroke="#F58220" stroke-width="1" stroke-linecap="round" stroke-linejoin="round"><path d="M9.5 2A2.5 2.5 0 0 1 12 4.5v15a2.5 2.5 0 0 1-4.96.44 2.5 2.5 0 0 1-2.96-3.08 3 3 0 0 1-.34-5.58 2.5 2.5 0 0 1 1.32-4.24 2.5 2.5 0 0 1 3.44-3.54A2.5 2.5 0 0 1 9.5 2Z"></path><path d="M14.5 2A2.5 2.5 0 0 0 12 4.5v15a2.5 2.5 0 0 0 4.96.44 2.5 2.5 0 0 0 2.96-3.08 3 3 0 0 0 .34-5.58 2.5 2.5 0 0 0-1.32-4.24 2.5 2.5 0 0 0-3.44-3.54A2.5 2.5 0 0 0 14.5 2Z"></path></svg>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown("<div style='text-align: center; color: #9CA3AF; font-size: 11px; margin-top: 8px;'>Universidad Autónoma de Bucaramanga | Facultad de Ingenierías | Maestría en Ciencia de Datos</div>", unsafe_allow_html=True)
