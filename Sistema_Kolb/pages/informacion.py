import streamlit as st

def mostrar_informacion():

    # =====================================================
    # CSS LOCAL DE ESTA PÁGINA (CON ESPACIADO REDUCIDO)
    # =====================================================
    st.markdown("""
    <style>
    .hero-box{
        background: linear-gradient(90deg,#FFF8F2 0%, #FFFFFF 100%);
        border: 1px solid #F2E6D9;
        border-radius: 20px;
        padding: 24px;
        margin-bottom: 20px;
    }
    .hero-icon{
        width: 64px;
        height: 64px;
        border-radius: 16px;
        background: #FEF1E7;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 30px;
    }
    .hero-title{
        color: #1F2D4D;
        font-size: 30px;
        font-weight: 800;
        margin-bottom: 4px;
    }
    .hero-subtitle{
        color: #606C80;
        font-size: 16px;
        line-height: 1.5;
    }
    .privacy-box{
        display: flex;
        align-items: flex-start;
        gap: 14px;
        margin-top: 15px;
        padding-top: 15px;
        border-top: 1px solid #E7EAF3;
    }
    
    /* Estilos de inputs */
    .stNumberInput input, .stSelectbox [data-baseweb="select"] {
        background-color: #F8FAFC !important;
        border: 1.5px solid #E2E8F0 !important;
        border-radius: 12px !important;
    }
    .stNumberInput input:focus, .stNumberInput input:hover,
    .stSelectbox [data-baseweb="select"]:hover,
    .stSelectbox [data-baseweb="select"]:focus-within {
        border-color: #F58220 !important;
        background-color: #FFFFFF !important;
        box-shadow: 0 0 0 3px rgba(245, 130, 32, 0.12) !important;
    }
    
    /* Contenedor principal estilizado con padding inferior más compacto */
    [data-testid="stVerticalBlockBorderWrapper"] {
        border: 1.5px solid #E2E8F0 !important;
        box-shadow: 0 12px 30px -10px rgba(31, 45, 77, 0.08) !important;
        background: linear-gradient(180deg, #FFFFFF 0%, #FAFAFC 100%) !important;
        padding: 15px 20px 20px 20px !important;
    }
    </style>
    """, unsafe_allow_html=True)

    # =====================================================
    # STEPPER
    # =====================================================
    st.markdown("""
        <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:20px;">
            <div style="text-align:center;flex:1;">
                <div style="width:34px; height:34px; background:#F58220; color:white; border-radius:50%; display:flex; align-items:center; justify-content:center; margin:auto; font-weight:700;">1</div>
                <div style="margin-top:6px; color:#1F2D4D; font-weight:700; font-size:14px;">Información</div>
            </div>
            <div style="flex:2;height:2px;background:#E7EAF3;"></div>
            <div style="text-align:center;flex:1;">
                <div style="width:34px; height:34px; background:#EEF2F8; color:#8A94A8; border-radius:50%; display:flex; align-items:center; justify-content:center; margin:auto; font-weight:700;">2</div>
                <div style="margin-top:6px; color:#8A94A8; font-size:14px;">Cuestionario</div>
            </div>
            <div style="flex:2;height:2px;background:#E7EAF3;"></div>
            <div style="text-align:center;flex:1;">
                <div style="width:34px; height:34px; background:#EEF2F8; color:#8A94A8; border-radius:50%; display:flex; align-items:center; justify-content:center; margin:auto; font-weight:700;">3</div>
                <div style="margin-top:6px; color:#8A94A8; font-size:14px;">Resultados</div>
            </div>
            <div style="flex:2;height:2px;background:#E7EAF3;"></div>
            <div style="text-align:center;flex:1;">
                <div style="width:34px; height:34px; background:#EEF2F8; color:#8A94A8; border-radius:50%; display:flex; align-items:center; justify-content:center; margin:auto; font-weight:700;">4</div>
                <div style="margin-top:6px; color:#8A94A8; font-size:14px;">Recomendaciones</div>
            </div>
        </div>
    """, unsafe_allow_html=True)

    # =====================================================
    # TARJETA PRINCIPAL
    # =====================================================
    with st.container(border=True):
        st.markdown("""
            <div class="hero-box">
                <div style="display:flex;align-items:center;gap:18px;">
                    <div class="hero-icon">
                        <svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="#F58220" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path><circle cx="12" cy="7" r="4"></circle></svg>
                    </div>
                    <div>
                        <div class="hero-title">Información del estudiante</div>
                        <div class="hero-subtitle">Por favor ingresa los siguientes datos antes de continuar con la evaluación del estilo de aprendizaje.</div>
                    </div>
                </div>
            </div>
        """, unsafe_allow_html=True)

        # =====================================================
        # FORMULARIO
        # =====================================================
        col1, col2 = st.columns(2, gap="large")

        with col1:
            st.markdown("""
                <div style="display:flex; align-items:center; gap:10px; margin-bottom:8px;">
                    <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#F58220" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"></circle><polyline points="12 6 12 12 16 14"></polyline></svg>
                    <span style="color:#1F2D4D; font-weight:700; font-size:17px;">Edad</span>
                </div>
            """, unsafe_allow_html=True)

            edad = st.number_input("", min_value=15, max_value=80, step=1, label_visibility="collapsed")

            st.markdown("<div style='height:15px'></div>", unsafe_allow_html=True)

            st.markdown("""
                <div style="display:flex; align-items:center; gap:10px; margin-bottom:8px;">
                    <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#F58220" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2z"></path><path d="M22 3h-6a4 4 0 0 0-4 4v14a3 3 0 0 1 3-3h7z"></path></svg>
                    <span style="color:#1F2D4D; font-weight:700; font-size:17px;">Tipo de colegio</span>
                </div>
            """, unsafe_allow_html=True)

            colegio = st.selectbox("", ["Público", "Privado"], label_visibility="collapsed")

        with col2:
            st.markdown("""
                <div style="display:flex; align-items:center; gap:10px; margin-bottom:8px;">
                    <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#F58220" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path><circle cx="12" cy="7" r="4"></circle></svg>
                    <span style="color:#1F2D4D; font-weight:700; font-size:17px;">Género</span>
                </div>
            """, unsafe_allow_html=True)

            genero = st.selectbox("", ["Masculino", "Femenino"], label_visibility="collapsed")

            st.markdown("<div style='height:15px'></div>", unsafe_allow_html=True)

            st.markdown("""
                <div style="display:flex; align-items:center; gap:10px; margin-bottom:8px;">
                    <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#F58220" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline><line x1="16" y1="13" x2="8" y2="13"></line><line x1="16" y1="17" x2="8" y2="17"></line><polyline points="10 9 9 9 8 9"></polyline></svg>
                    <span style="color:#1F2D4D; font-weight:700; font-size:17px;">Promedio académico actual</span>
                </div>
            """, unsafe_allow_html=True)

            promedio = st.number_input("", min_value=0.0, max_value=5.0, step=0.1, format="%.1f", label_visibility="collapsed")
            st.caption("Escala de 0.0 a 5.0")

        # =====================================================
        # NOTA DE PRIVACIDAD
        # =====================================================
        st.markdown("""
            <div class="privacy-box">
                <div style="width:38px; height:38px; border-radius:10px; background:#EEF5FB; display:flex; align-items:center; justify-content:center;">
                    <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#2563EB" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="11" width="18" height="11" rx="2" ry="2"></rect><path d="M7 11V7a5 5 0 0 1 10 0v4"></path></svg>
                </div>
                <div>
                    <div style="color:#1F2D4D; font-weight:700; margin-bottom:2px; font-size:14px;">Confidencialidad de la información</div>
                    <div style="color:#6B7280; font-size:13px; line-height:1.5;">
                        Los datos suministrados serán utilizados únicamente para realizar la clasificación del estilo de aprendizaje dentro del prototipo y no serán almacenados con fines diferentes a esta investigación.
                    </div>
                </div>
            </div>
        """, unsafe_allow_html=True)

        st.markdown("<div style='height:20px'></div>", unsafe_allow_html=True)

        # =====================================================
        # BOTONES
        # =====================================================
        volver_col, continuar_col = st.columns(2, gap="medium")

        with volver_col:
            if st.button("← Volver", use_container_width=True):
                st.session_state.page = "bienvenida"
                st.rerun()

        with continuar_col:
            if st.button("Continuar →", use_container_width=True, type="primary"):
                st.session_state.datos_estudiante = {
                    "EDAD": edad,
                    "GENERO": genero,
                    "COLEGIO": colegio,
                    "PROMEDIO ACADEMICO ACTUAL": promedio
                }
                st.session_state.page = "cuestionario"
                st.rerun()

    # =====================================================
    # FOOTER
    # =====================================================
    st.caption("© 2026 Universidad Autónoma de Bucaramanga · Facultad de Ingenierías · Maestría en Ciencia de Datos")