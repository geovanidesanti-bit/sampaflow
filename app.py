import streamlit as st
from streamlit_mic_recorder import mic_recorder

# Configuração da Página
st.set_page_config(
    page_title="SampaFlow - Ecossistema Inteligente",
    page_icon="⚡",
    layout="centered",
)

# Injeção de CSS Customizado (Dark Glassmorphism, Neon & Barra Fixa Inferior)
st.markdown(
    """
    <style>
    .stApp {
        background-color: #080b11;
        color: #f3f4f6;
        font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
    }
    header {visibility: hidden;}
    
    .top-bar {
        display: flex;
        justify-content: space-between;
        align-items: center;
        color: #9ca3af;
        font-size: 13px;
        margin-bottom: 15px;
        padding: 0 5px;
    }

    .logo-container {
        text-align: center;
        margin-bottom: 15px;
    }
    .logo-title {
        font-size: 32px;
        font-weight: 900;
        letter-spacing: -1px;
        background: linear-gradient(90deg, #00F59B 0%, #00D2FF 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        display: inline-block;
    }

    .neon-card {
        background: rgba(17, 24, 39, 0.75);
        border: 1px solid rgba(0, 245, 155, 0.4);
        backdrop-filter: blur(12px);
        border-radius: 16px;
        padding: 16px 18px;
        margin-bottom: 16px;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.5);
    }

    .flow-ai-footer {
        background: rgba(8, 11, 17, 0.95);
        border-top: 1px solid rgba(0, 245, 155, 0.3);
        padding: 12px 10px;
        text-align: center;
        margin-top: 20px;
        border-radius: 16px 16px 0 0;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Inicialização de Variáveis de Sessão
if "pagina_atual" not in st.session_state:
    st.session_state.pagina_atual = "Home"

if "usuario_logado" not in st.session_state:
    st.session_state.usuario_logado = {
        "nome": "Patrícia Lima",
        "cargo": "Executiva de Parcerias",
        "linkedin": "https://linkedin.com/in/patricialima",
    }

# Função padrão para a barra superior em todas as telas
def render_top_bar(titulo_pagina="Showcase"):
    st.markdown(
        f"""
        <div class="top-bar">
            <span>⚡ SampaFlow &nbsp;|&nbsp; <b>{titulo_pagina}</b></span>
            <span>📍 Jardins &nbsp; 🌧️ 21°C</span>
        </div>
        """,
        unsafe_allow_html=True,
    )

# Função padrão para o rodapé fixo do Flow AI em todas as telas
def render_flow_ai_footer():
    st.markdown("---")
    st.markdown(
        """
        <div class="flow-ai-footer">
            <span style="color: #00F59B; font-weight: bold; font-size: 14px;">🎙️ FLOW AI BUTTON</span><br>
            <span style="color: #9ca3af; font-size: 11px;">TOQUE P/ FALAR</span>
        </div>
        """,
        unsafe_allow_html=True,
    )
    mic_recorder(
        start_prompt="🔴 Iniciar Gravação de Voz",
        stop_prompt="⏹️ Parar & Processar IA",
        key=f"mic_{st.session_state.pagina_atual}",
    )

# ----------------- TELA: HOME (Dashboard Principal) -----------------
if st.session_state.pagina_atual == "Home":
    render_top_bar("Showcase")

    st.markdown(
        """
        <div class="logo-container">
            <span class="logo-title">SAMPAFLOW</span>
        </div>
    """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div class="neon-card" style="text-align: center; border-color: rgba(0, 213, 255, 0.4);">
            <span style="font-size: 22px;">💬</span>
            <div style="color: #00D2FF; font-weight: 600; font-size: 14px; margin-top: 4px;">FLOW AI ACTIVE</div>
            <div style="color: #9ca3af; font-size: 12px;">Pronto para curadoria preditiva e imersiva</div>
        </div>
    """,
        unsafe_allow_html=True,
    )

    if st.button("🤝  **SAMPA MATCH**\n\n*(Radar Biz)*", use_container_width=True):
        st.session_state.pagina_atual = "Sampa Match"
        st.rerun()

    if st.button("📍  **GPS INDOOR**\n\n*(Navegar Estandes)*", use_container_width=True):
        st.session_state.pagina_atual = "GPS Indoor"
        st.rerun()

    if st.button("🛍️  **COMPRAS & GASTRONOMIA**\n\n*(Popular | Luxo)*", use_container_width=True):
        st.session_state.pagina_atual = "Compras Dual"
        st.rerun()

    if st.button("💼  **SAMPA WORK**\n\n*(Jobs)*", use_container_width=True):
        st.session_state.pagina_atual = "Sampa Work"
        st.rerun()

    render_flow_ai_footer()

# ----------------- TELA: SAMPA MATCH (Radar & Conexões) -----------------
elif st.session_state.pagina_atual == "Sampa Match":
    render_top_bar("SAMPA MATCH: Radar Biz")

    st.markdown(
        """
        <div class="neon-card" style="text-align: center;">
            <div style="color: #00F59B; font-weight: bold; margin-bottom: 8px;">📡 RADAR 360° ATIVO</div>
            <div style="font-size: 13px; color: #9ca3af; margin-bottom: 12px;">Detectando profissionais e estandes em tempo real no evento.</div>
            <div style="background: rgba(0,0,0,0.4); border-radius: 10px; padding: 20px; border: 1px dashed rgba(0,245,155,0.3);">
                <span style="font-size: 32px;">🎯</span><br>
                <span style="color: #00D2FF; font-size: 12px;">142 participantes online na sua zona (Expo Floor A)</span>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div class="neon-card">
            <b>Ana Mendes</b><br>
            <span style="color: #00D2FF; font-size: 13px;">📍 Sr. Analyst, Tech Solutions — 50m away</span><br>
            <p style="color: #9ca3af; font-size: 12px; margin-top: 6px;">Interesses em comum: Inovação B2B, Inteligência Artificial.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    col1, col2 = st.columns(2)
    with col1:
        if st.button("✨ Connect", key="conn_ana", use_container_width=True):
            st.success("Conexão solicitada!")
    with col2:
        if st.button("🍷 Book VIP", key="book_ana", use_container_width=True):
            st.success("Reserva solicitada!")

    st.markdown(
        """
        <div class="neon-card" style="margin-top: 15px;">
            <b>Carlos Ribeiro</b><br>
            <span style="color: #00D2FF; font-size: 13px;">📍 Global Dev — 120m away</span><br>
            <p style="color: #9ca3af; font-size: 12px; margin-top: 6px;">Interesses em comum: Arquitetura Cloud, Redes.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    col3, col4 = st.columns(2)
    with col3:
        if st.button("✨ Connect", key="conn_carlos", use_container_width=True):
            st.success("Conexão solicitada!")
    with col4:
        if st.button("🍷 Book VIP", key="book_carlos", use_container_width=True):
            st.success("Reserva solicitada!")

    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("⬅️ Voltar ao Início", use_container_width=True):
        st.session_state.pagina_atual = "Home"
        st.rerun()

    render_flow_ai_footer()

# ----------------- TELA: GPS INDOOR -----------------
elif st.session_state.pagina_atual == "GPS Indoor":
    render_top_bar("GPS INDOOR: Mapa 3D")
    
    st.markdown(
        """
        <div class="neon-card">
            <div style="color: #00D2FF; font-weight: bold; margin-bottom: 6px;">🗺️ NAVEGAÇÃO TÁTICA INTERNA</div>
            <p style="font-size: 13px; color: #9ca3af;">Destino selecionado: <b>Estande TechInnovate (Pavilhão B)</b></p>
            <div style="background: rgba(0,213,255,0.05); padding: 15px; border-radius: 8px; border: 1px solid rgba(0,213,255,0.2); text-align: center;">
                <span style="color: #00F59B; font-weight: bold;">➔ Siga em frente por 15 metros</span><br>
                <span style="font-size: 12px; color: #9ca3af;">Virar à esquerda no corredor principal</span>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    if st.button("⬅️ Voltar ao Início", use_container_width=True):
        st.session_state.pagina_atual = "Home"
        st.rerun()

    render_flow_ai_footer()

# ----------------- TELA: COMPRAS & GASTRONOMIA -----------------
elif st.session_state.pagina_atual == "Compras Dual":
    render_top_bar("GASTRONOMIA & VAULTS")

    st.markdown(
        """
        <div class="neon-card">
            <div style="color: #00F59B; font-weight: bold; font-size: 16px;">THE SÃOPAULISTA UNDERCURRENT</div>
            <div style="color: #f3f4f6; font-size: 13px; margin: 6px 0;">⭐⭐⭐⭐⭐ 4.8</div>
            <p style="color: #9ca3af; font-size: 12px;">A hidden vault born from a forgotten coffee-baron catacomb. Flow AI predicts a high historical intrigue score for Patrícia Lima.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    if st.button("🍽️ RESERVE MINHA MESA", use_container_width=True):
        st.success("Mesa reservada com sucesso no Vault Secreto!")

    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("⬅️ Voltar ao Início", use_container_width=True):
        st.session_state.pagina_atual = "Home"
        st.rerun()

    render_flow_ai_footer()

# ----------------- TELA: SAMPA WORK -----------------
elif st.session_state.pagina_atual == "Sampa Work":
    render_top_bar("SAMPA WORK: Jobs")

    st.markdown(
        """
        <div class="neon-card">
            <div style="color: #00D2FF; font-weight: bold;">💼 Concierge Executivo de Luxo</div>
            <p style="font-size: 12px; color: #9ca3af; margin-top: 5px;">Hotel Fasano Jardins — R$ 12.000 / mês</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    if st.button("⬅️ Voltar ao Início", use_container_width=True):
        st.session_state.pagina_atual = "Home"
        st.rerun()

    render_flow_ai_footer()
