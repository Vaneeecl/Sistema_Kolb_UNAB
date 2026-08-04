import streamlit as st
from pathlib import Path

# =====================================================
# CONFIGURACIÓN DE LA PÁGINA
# =====================================================

st.set_page_config(
    page_title="Sistema Kolb",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# =====================================================
# CARGAR HOJA DE ESTILOS
# =====================================================

css_file = Path("style.css")

if css_file.exists():
    with open(css_file, "r", encoding="utf-8") as css:
        st.markdown(
            f"<style>{css.read()}</style>",
            unsafe_allow_html=True
        )

# =====================================================
# OCULTAR ELEMENTOS DE STREAMLIT
# =====================================================

st.markdown(
    """
    <style>

    #MainMenu{
        visibility:hidden;
    }

    footer{
        visibility:hidden;
    }

    header{
        visibility:hidden;
    }

    [data-testid="stSidebar"]{
        display:none;
    }

    </style>
    """,
    unsafe_allow_html=True
)

# =====================================================
# SESSION STATE
# =====================================================

if "page" not in st.session_state:
    st.session_state.page = "bienvenida"

if "pregunta_actual" not in st.session_state:
    st.session_state.pregunta_actual = 0

if "datos_estudiante" not in st.session_state:
    st.session_state.datos_estudiante = {}

if "respuestas" not in st.session_state:
    st.session_state.respuestas = {}

if "resultado" not in st.session_state:
    st.session_state.resultado = None

if "probabilidades" not in st.session_state:
    st.session_state.probabilidades = None

# =====================================================
# IMPORTAR PÁGINAS
# =====================================================

from pages.bienvenida import mostrar_bienvenida
from pages.informacion import mostrar_informacion
from pages.cuestionario import mostrar_cuestionario
from pages.resultado import mostrar_resultado
from pages.recomendaciones import mostrar_recomendaciones

# =====================================================
# NAVEGACIÓN Y ROUTER DE LA APLICACIÓN
# =====================================================

pagina = st.session_state.page

if pagina == "bienvenida":
    mostrar_bienvenida()

elif pagina == "informacion":
    mostrar_informacion()

elif pagina == "cuestionario":
    mostrar_cuestionario()

elif pagina == "resultado":
    mostrar_resultado()

elif pagina == "recomendaciones":
    mostrar_recomendaciones()

else:
    st.session_state.page = "bienvenida"
    st.rerun()