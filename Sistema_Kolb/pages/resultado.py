import streamlit as st
import numpy as np

# =====================================================
# ICONOS SVG (sin emojis) - estilo linea
# width/height fijos EN el propio SVG para evitar problemas de escalado
# =====================================================
ICON_AWARD = '<svg width="34" height="34" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="8" r="7"></circle><polyline points="8.21 13.89 7 23 12 20 17 23 15.79 13.88"></polyline></svg>'
ICON_INFO = '<svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"></circle><line x1="12" y1="16" x2="12" y2="12"></line><line x1="12" y1="8" x2="12.01" y2="8"></line></svg>'
ICON_BARCHART = '<svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="18" y1="20" x2="18" y2="10"></line><line x1="12" y1="20" x2="12" y2="4"></line><line x1="6" y1="20" x2="6" y2="14"></line></svg>'
ICON_CHECK = '<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"></path><polyline points="22 4 12 14.01 9 11.01"></polyline></svg>'


def _icon(svg, color):
    return f'<span style="display:inline-flex; color:{color}; flex-shrink:0;">{svg}</span>'


# =====================================================
# STEPPER (barra de pasos superior) - reutilizable
# =====================================================
def render_stepper(paso_actual):
    pasos = ["Información", "Cuestionario", "Resultados", "Recomendaciones"]
    items = ""
    for i, nombre in enumerate(pasos, start=1):
        activo_o_completo = i <= paso_actual
        color_circulo = "#F58220" if activo_o_completo else "#E5E7EB"
        color_texto_circulo = "#FFFFFF" if activo_o_completo else "#9CA3AF"
        color_label = "#1F2D4D" if activo_o_completo else "#9CA3AF"
        peso_label = "700" if i == paso_actual else "600"
        items += f'<div style="display:flex; flex-direction:column; align-items:center; flex-shrink:0;"><div style="width:32px; height:32px; border-radius:50%; background-color:{color_circulo}; color:{color_texto_circulo}; display:flex; align-items:center; justify-content:center; font-weight:700; font-size:14px;">{i}</div><div style="font-size:12px; font-weight:{peso_label}; color:{color_label}; margin-top:6px; white-space:nowrap;">{nombre}</div></div>'
        if i < len(pasos):
            color_linea = "#F58220" if i < paso_actual else "#E5E7EB"
            items += f'<div style="flex:1; height:3px; background-color:{color_linea}; margin: 0 10px 22px 10px;"></div>'
    st.markdown(f'<div style="display:flex; align-items:flex-start; margin-bottom:30px;">{items}</div>', unsafe_allow_html=True)


# =====================================================
# ESTILOS CSS
# =====================================================
st.markdown("""
<style>
    .card-container {
        background-color: #FFFEFC;
        border: 1px solid #E5E7EB;
        border-radius: 16px;
        padding: 28px 24px;
        min-height: 340px;
        height: 100%;
        box-shadow: 0 1px 3px rgba(0,0,0,0.04);
        display: flex;
        flex-direction: column;
    }
    .card-container-middle {
        background-color: #FFFEFC;
        border: 1px solid #E5E7EB;
        border-radius: 16px;
        padding: 34px;
        min-height: 340px;
        height: 100%;
        box-shadow: 0 1px 3px rgba(0,0,0,0.04);
        display: flex;
        flex-direction: column;
    }
    .icon-circle {
        width: 58px;
        height: 58px;
        border-radius: 14px;
        background-color: #FDEEE1;
        display: flex;
        align-items: center;
        justify-content: center;
        margin: 0 auto 14px auto;
        overflow: hidden;
        flex-shrink: 0;
    }
    .icon-circle-left {
        width: 58px;
        height: 58px;
        border-radius: 12px;
        background-color: #FDEEE1;
        display: flex;
        align-items: center;
        justify-content: center;
        margin: 0 auto 18px auto;
        overflow: hidden;
        flex-shrink: 0;
    }
    .info-box-custom {
        background-color: #F0F4F8;
        border: 1px solid #D1D5DB;
        border-radius: 10px;
        padding: 16px;
        margin-top: 20px;
        margin-bottom: 20px;
        color: #1F2D4D;
        font-size: 14px;
    }
    .footer-text {
        text-align: center;
        color: #6B7280;
        font-size: 12px;
        margin-top: 30px;
        border-top: 1px solid #E5E7EB;
        padding-top: 15px;
    }
    div.stButton > button {
        border-radius: 10px !important;
        font-weight: 600 !important;
        padding: 0.6rem 1rem !important;
        border: 1px solid #D1D5DB !important;
        transition: all 0.15s ease-in-out;
    }
    div.stButton > button[kind="secondary"] {
        background-color: #FFFFFF !important;
        color: #374151 !important;
    }
    div.stButton > button[kind="secondary"]:hover {
        border-color: #F58220 !important;
        color: #F58220 !important;
    }
    div.stButton > button[kind="primary"] {
        background-color: #F58220 !important;
        color: #FFFFFF !important;
        border: none !important;
    }
    div.stButton > button[kind="primary"]:hover {
        background-color: #DB711A !important;
    }
</style>
""", unsafe_allow_html=True)


def mostrar_resultado():
    estilo_predicho = st.session_state.get("resultado", "Asimilador")
    probabilidades_brutas = st.session_state.get("probabilidades", None)

    clases_modelo = [
        "Acomodador",
        "Asimilador",
        "Convergente",
        "Divergente"
    ]

    if isinstance(probabilidades_brutas, (list, np.ndarray)):
        probs = {clases_modelo[i]: float(probabilidades_brutas[i]) * 100 for i in range(len(probabilidades_brutas))}
    elif isinstance(probabilidades_brutas, dict):
        probs = probabilidades_brutas
    else:
        probs = {"Asimilador": 91.0, "Convergente": 5.0, "Divergente": 3.0, "Acomodador": 1.0}

    estilo_predicho = str(estilo_predicho).title()
    probabilidad_estimada = probs[estilo_predicho]

    descripciones_por_estilo = {
        "Asimilador": "Los estudiantes con este resultado tienden a preferir la conceptualización abstracta y la observación reflexiva. Generalmente comprenden con facilidad los fundamentos teóricos antes de abordar su aplicación práctica y disfrutan del análisis lógico de la información.",
        "Divergente": "Los estudiantes con este resultado tienden a preferir la experiencia concreta y la observación reflexiva. Suelen ver las situaciones desde distintas perspectivas, disfrutan generar ideas y se motivan al relacionar la teoría con experiencias reales.",
        "Convergente": "Los estudiantes con este resultado tienden a preferir la conceptualización abstracta y la experimentación activa. Se orientan a la aplicación práctica de ideas, prefieren tareas técnicas y buscan soluciones concretas a los problemas.",
        "Acomodador": "Los estudiantes con este resultado tienden a preferir la experiencia concreta y la experimentación activa. Aprenden principalmente mediante la práctica, se adaptan con facilidad a situaciones nuevas y prefieren la acción antes que el análisis extenso."
    }
    descripcion_actual = descripciones_por_estilo.get(estilo_predicho, descripciones_por_estilo["Asimilador"])

    # =====================================================
    # BARRA DE PASOS (paso 3: Resultados)
    # =====================================================
    render_stepper(3)

    # =====================================================
    # TITULO PRINCIPAL
    # =====================================================
    st.markdown("""
    <div style="text-align: center; margin-bottom: 30px;">
        <h2 style="color: #1F2D4D; font-weight: 800; font-size: 30px;">Resultado de la clasificación</h2>
        <p style="color: #4B5563; font-size: 15px; margin-top: 5px;">El sistema ha procesado la información suministrada y presenta el estilo de aprendizaje identificado.</p>
    </div>
    """, unsafe_allow_html=True)

    col1, spacer1, col2, spacer2, col3 = st.columns([1, 0.08, 1, 0.08, 1])

    with col1:
        st.markdown(f"""
        <div class="card-container" style="text-align: center; justify-content: center;">
            <div class="icon-circle">{_icon(ICON_AWARD, '#F58220')}</div>
            <div style="font-size: 13px; font-weight: 700; color: #6B7280; text-transform: uppercase; letter-spacing: 0.3px; margin-bottom: 8px;">
                Estilo de aprendizaje identificado
            </div>
            <div style="font-size: 42px; font-weight: 900; letter-spacing: -1px; color: #F58220; margin-bottom: 20px;">
                {str(estilo_predicho).upper()}
            </div>
            <div style="font-size: 12px; font-weight: 700; color: #6B7280; text-transform: uppercase;">
                Probabilidad estimada
            </div>
            <div style="font-size: 36px; font-weight: 800; color: #10B981; margin-top: 2px;">
                {probabilidad_estimada:.0f}%
            </div>
            <div style="font-size: 13px; color: #10B981; font-weight: 600; margin-top: 6px; display:flex; align-items:center; justify-content:center; gap:5px;">
                {_icon(ICON_CHECK, '#10B981')} Resultado orientativo
            </div>
            <div style="
                font-size: 11px;
                color: #6B7280;
                line-height: 1.4;
                margin-top: 10px;
                text-align: center;">
                Este valor representa la probabilidad estimada
                por el modelo y debe interpretarse de manera orientativa, 
                considerando el tamaño muestral del estudio.
            </div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown(f"""
        <div class="card-container-middle">
            <div class="icon-circle-left">{_icon(ICON_INFO, '#F58220')}</div>
            <div style="
                font-size:22px;
                font-weight:800;
                color:#1F2D4D;
                margin-bottom:18px;
                text-align:center;">
                ¿Qué significa este resultado?
            </div>
            <div style="
                font-size:18px;
                color:#4B5563;
                line-height:2.05;
                text-align:justify;
                font-weight:400;">
                {descripcion_actual}
            </div>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        sorted_probs = sorted(probs.items(), key=lambda item: item[1], reverse=True)
        row_h = 42
        chart_w = 380
        bar_max = 290
        svg_h = row_h * len(sorted_probs) + 20
        rects = ""
        for i, (est, val) in enumerate(sorted_probs):
            es_ganador = (i == 0)
            color_txt = "#F58220" if es_ganador else "#6B7280"
            weight_txt = "700" if es_ganador else "500"
            color_bar = "#F58220" if es_ganador else "#FBCFA0"
            y_label = row_h * i + 13
            y_bar = row_h * i + 20
            bar_w = max((val / 100) * bar_max, 2)
            rects += f'<text x="0" y="{y_label}" font-size="12.5" font-weight="{weight_txt}" fill="{color_txt}" font-family="Inter, sans-serif">{est}</text>'
            rects += f'<text x="{chart_w}" y="{y_label}" font-size="12.5" font-weight="{weight_txt}" fill="{color_txt}" text-anchor="end" font-family="Inter, sans-serif">{val:.0f}%</text>'
            rects += f'<rect x="0" y="{y_bar}" width="{bar_max}" height="8" rx="4" fill="#F1F1F1"></rect>'
            rects += f'<rect x="0" y="{y_bar}" width="{bar_w}" height="8" rx="4" fill="{color_bar}"></rect>'
        svg_chart = f'<svg viewBox="0 0 {chart_w} {svg_h}" width="100%" height="{svg_h}" xmlns="http://www.w3.org/2000/svg">{rects}</svg>'
        st.markdown(f"""
        <div class="card-container">
            <div class="icon-circle-left">{_icon(ICON_BARCHART, '#F58220')}</div>
            <div style="font-size: 22px; font-weight: 800; color: #1F2D4D; margin-bottom: 18px; text-align: center;">
                Probabilidad por estilo
            </div>
            {svg_chart}
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<div style='height: 20px;'></div>", unsafe_allow_html=True)

    col_b1, col_b2 = st.columns(2, gap="medium")
    with col_b1:
        if st.button("Nueva evaluación", use_container_width=True, key="btn_nueva_evaluacion"):
            st.session_state.page = "cuestionario"
            st.rerun()
    with col_b2:
        if st.button("Ver recomendaciones pedagógicas", use_container_width=True, type="primary", key="btn_ver_recomendaciones"):
            st.session_state.page = "recomendaciones"
            st.rerun()

    st.markdown("""
    <div class="footer-text">
        Universidad Autónoma de Bucaramanga | Facultad de Ingenierías | Maestría en Ciencia de Datos
    </div>
    """, unsafe_allow_html=True)
