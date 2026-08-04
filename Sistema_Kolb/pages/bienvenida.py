from pathlib import Path
import streamlit as st

# =====================================================
# RUTA BASE DEL PROYECTO (independiente del directorio de trabajo)
# Este archivo vive en: <raiz_proyecto>/pages/bienvenida.py
# Por eso .parent.parent apunta a <raiz_proyecto>, igual que en utils/prediccion.py
# =====================================================
BASE_DIR = Path(__file__).resolve().parent.parent
ASSETS_DIR = BASE_DIR / "assets"


def mostrar_bienvenida():

    # =====================================================
    # CONTENIDO PRINCIPAL
    # =====================================================

    izquierda, derecha = st.columns([0.95, 1.05], gap="medium")

    # =====================================================
    # COLUMNA IZQUIERDA
    # =====================================================

    with izquierda:

        # LOGO
        logo = ASSETS_DIR / "Logo_UNAB.png"
        if logo.exists():
            st.image(str(logo), width=160)
        else:
            st.warning(f"No se encontró la imagen: {logo}")

        # TÍTULO UNIFICADO Y HOMOGÉNEO
        st.markdown(
            """
            <div style="line-height:1.2; margin-top:12px; margin-bottom:16px;">
                <span style="
                    color:#1F2D4D;
                    font-size:27px;
                    font-weight:800;">
                    Sistema de Apoyo a la Clasificación del Estilo de Aprendizaje según el Modelo de Kolb 
                </span>
                <span style="
                    color:#F58220;
                    font-size:27px;
                    font-weight:800;">
                    en Estudiantes de Ecuaciones Diferenciales
                </span>
            </div>
            """,
            unsafe_allow_html=True,
        )

        st.markdown("<h3 style='margin-top:0px; margin-bottom:6px; font-size:22px;'>Bienvenido</h3>", unsafe_allow_html=True)

        st.markdown(
            """
            <p style="font-size: 17px; line-height: 1.6; color: #4B5563; margin-bottom: 20px;">
                Este prototipo emplea un modelo de <b>Regresión Logística Optimizada</b> para clasificar el estilo de aprendizaje de los estudiantes y proporcionar estrategias pedagógicas orientativas que apoyen el proceso de enseñanza y aprendizaje.
            </p>
            """,
            unsafe_allow_html=True
        )

        with st.container(border=True):
            st.markdown(
                """
                <div style="display: flex; align-items: center; gap: 16px; border-left: 4px solid #F58220; padding-left: 14px; padding-top: 4px; padding-bottom: 4px;">
                    <div style="background-color: #FEF3EC; padding: 12px; border-radius: 12px; display: flex; align-items: center; justify-content: center;">
                        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#F58220" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
                            <path d="M18 20V10"></path>
                            <path d="M12 20V4"></path>
                            <path d="M6 20v-6"></path>
                        </svg>
                    </div>
                    <div>
                        <h4 style="color: #1F2D4D; margin: 0 0 6px 0; font-size: 19px; font-weight: 700;">Modelo de Kolb</h4>
                        <p style="color: #4B5563; margin: 0; font-size: 16px; line-height: 1.5;">
                            Cuestionario de <b>19 ítems</b> que evalúan las cuatro dimensiones del aprendizaje experiencial.
                        </p>
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )

        st.markdown("<div style='margin-bottom: 12px;'></div>", unsafe_allow_html=True)

        with st.container(border=True):
            st.markdown(
                """
                <div style="display: flex; align-items: center; gap: 16px; border-left: 4px solid #1F2D4D; padding-left: 14px; padding-top: 4px; padding-bottom: 4px;">
                    <div style="background-color: #EBF1F8; padding: 12px; border-radius: 12px; display: flex; align-items: center; justify-content: center;">
                        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#1F2D4D" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
                            <path d="M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2z"></path>
                            <path d="M22 3h-6a4 4 0 0 0-4 4v14a3 3 0 0 1 3-3h7z"></path>
                        </svg>
                    </div>
                    <div>
                        <h4 style="color: #1F2D4D; margin: 0 0 6px 0; font-size: 19px; font-weight: 700;">Apoyo pedagógico</h4>
                        <p style="color: #4B5563; margin: 0; font-size: 16px; line-height: 1.5;">
                            Obtén recomendaciones para fortalecer el aprendizaje en Ecuaciones diferenciales.
                        </p>
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )

        st.markdown("<div style='margin-bottom: 16px;'></div>", unsafe_allow_html=True)

        if st.button("Comenzar evaluación", use_container_width=True, type="primary"):
            st.session_state.page = "informacion"
            st.rerun()

    # ============================================
    # COLUMNA DERECHA
    # ============================================

    with derecha:

        imagen = ASSETS_DIR / "Campus_UNAB.jpg"

        if imagen.exists():
            st.image(str(imagen), use_container_width=True)
        else:
            st.warning(f"No se encontró la imagen: {imagen}")

    st.caption(
        "© 2026 Universidad Autónoma de Bucaramanga · Facultad de Ingenierías · Maestría en Ciencia de Datos"
    )
