import streamlit as st
from streamlit_mic_recorder import mic_recorder

# Configuração da Página
st.set_page_config(
    page_title="SampaFlow - Ecossistema Inteligente",
    page_icon="⚡",
    layout="centered",
)

# Injeção de CSS Customizado - Dark Glassmorphism com Contraste Perfeito
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
        background: rgba(13, 19, 33, 0.95);
        border: 1px solid rgba(0, 245, 155, 0.5);
        backdrop-filter: blur(16px);
        border-radius: 16px;
        padding: 18px 20px;
        margin-bottom: 16px;
        box-shadow: 0 8px 24px rgba(0, 0, 0, 0.6);
    }
    
    .neon-card-cyan {
        background: rgba(13, 19, 33, 0.95);
        border: 1px solid rgba(0, 213, 255, 0.5);
        backdrop-filter: blur(16px);
        border-radius: 16px;
        padding: 18px 20px;
        margin-bottom: 16px;
        box-shadow: 0 8px 24px rgba(0, 0, 0, 0.6);
    }

    .ai-response-box {
        background: rgba(0, 213, 255, 0.08);
        border: 1px solid rgba(0, 213, 255, 0.6);
        border-radius: 12px;
        padding: 14px;
        margin-bottom: 15px;
        color: #00D2FF;
        font-size: 13px;
    }

    .stButton > button {
        background: rgba(17, 24, 39, 0.95) !important;
        color: #00F59B !important;
        border: 1px solid rgba(0, 245, 155, 0.6) !important;
        border-radius: 12px !important;
        font-weight: 700 !important;
        padding: 12px 18px !important;
        transition: all 0.3s ease;
    }
    .stButton > button:hover {
        background: rgba(0, 245, 155, 0.15) !important;
        border-color: #00F59B !important;
        color: #ffffff !important;
    }

    .flow-ai-footer {
        background: rgba(8, 11, 17, 0.98);
        border-top: 1px solid rgba(0, 245, 155, 0.4);
        padding: 14px 10px;
        text-align: center;
        margin-top: 25px;
        border-radius: 18px 18px 0 0;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Inicialização de Variáveis de Sessão
if "pagina_atual" not in st.session_state:
    st.session_state.pagina_atual = "Home"

if "historico_ia" not in st.session_state:
    st.session_state.historico_ia = []

if "reproduzindo_audio" not in st.session_state:
    st.session_state.reproduzindo_audio = False

def render_top_bar(titulo_pagina="Showcase"):
    st.markdown(
        f"""
        <div class="top-bar">
            <span>⚡ SampaFlow &nbsp;|&nbsp; <b>{titulo_pagina}</b></span>
            <span>📍 Jardins &nbsp; 🌧️ 21°C (Chuva Fraca)</span>
        </div>
        """,
        unsafe_allow_html=True,
    )

def render_flow_ai_footer():
    st.markdown("---")
    st.markdown(
        """
        <div class="flow-ai-footer">
            <span style="color: #00F59B; font-weight: bold; font-size: 14px;">🎙️ FLOW AI BUTTON</span><br>
            <span style="color: #9ca3af; font-size: 11px;">TOQUE P/ FALAR OU COMANDAR O MAPA</span>
        </div>
        """,
        unsafe_allow_html=True,
    )
    
    # Captura inteligente de voz com resposta interativa da IA
    audio_gravado = mic_recorder(
        start_prompt="🔴 Iniciar Gravação de Voz",
        stop_prompt="⏹️ Parar & Processar IA",
        key=f"mic_{st.session_state.pagina_atual}",
    )
    
    if audio_gravado:
        resposta_texto = "✨ [Flow AI Command Processed]: Comando de voz decodificado com sucesso! Ajustando rotas urbanas, filtrando restaurantes parceiros com nota > 4.7 e sincronizando o mapa tático 3D."
        st.session_state.historico_ia.append({
            "pagina": st.session_state.pagina_atual,
            "resposta": resposta_texto
        })
        st.rerun()

    if st.session_state.historico_ia:
        ultima = st.session_state.historico_ia[-1]
        if ultima["pagina"] == st.session_state.pagina_atual:
            st.markdown(
                f"""
                <div class="ai-response-box">
                    <b>🤖 Flow AI Response:</b><br>{ultima["resposta"]}
                </div>
                """,
                unsafe_allow_html=True,
            )

# ---------------------------------------------------------
# TELA: HOME (Dashboard Completo)
# ---------------------------------------------------------
if st.session_state.pagina_atual == "Home":
    render_top_bar("Showcase Central")

    st.markdown(
        """
        <div class="logo-container">
            <span class="logo-title">SAMPAFLOW</span>
            <div style="color: #9ca3af; font-size: 12px; margin-top: 4px;">Ecossistema Urbano Preditivo & Inteligência de Fluxo</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Bloco do Mapa 3D Tático
    st.markdown(
        """
        <div class="neon-card-cyan">
            <div style="color: #00D2FF; font-weight: bold; font-size: 14px; margin-bottom: 6px;">🗺️ MAPA 3D TÁTICO & ECOSSISTEMA</div>
            <div style="font-size: 12px; color: #d1d5db; margin-bottom: 8px;">
                Localização em tempo real: <b>Centro Histórico ➔ Jardins ➔ Berrini Business</b>
            </div>
            <div style="background: rgba(0,0,0,0.5); border-radius: 8px; padding: 12px; text-align: center; border: 1px dashed rgba(0,213,255,0.4);">
                <span style="color: #00F59B; font-size: 12px; font-weight: bold;">🟢 Rota Otimizada Ativa via Flow AI (Tráfego Fluido)</span>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Modo Chuva & Previsão de Demanda
    st.markdown(
        """
        <div class="neon-card">
            <div style="color: #00F59B; font-weight: bold; font-size: 14px; margin-bottom: 4px;">🌧️ RAIN MODE & PREVISÃO DE DEMANDA</div>
            <div style="font-size: 12px; color: #d1d5db; line-height: 1.4;">
                <b>Temperatura São Paulo:</b> 21°C com precipitação leve nos Jardins.<br>
                <b>Demanda Urbana Preditiva:</b> Pico de circulação em vaults gastronômicos cobertos e hubs de inovação esperado entre 18h e 22h.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("### Módulos Principais")
    
    if st.button("🤝  **SAMPA MATCH** — Radar Biz & Conexões", use_container_width=True):
        st.session_state.pagina_atual = "Sampa Match"
        st.rerun()

    if st.button("📍  **GPS INDOOR** — Mapa Tático & Localização", use_container_width=True):
        st.session_state.pagina_atual = "GPS Indoor"
        st.rerun()

    if st.button("🛍️  **COMPRAS & GASTRONOMIA** — Restaurantes Parceiros & Vaults", use_container_width=True):
        st.session_state.pagina_atual = "Compras Dual"
        st.rerun()

    if st.button("💼  **SAMPA WORK** — Jobs & Oportunidades Executivas", use_container_width=True):
        st.session_state.pagina_atual = "Sampa Work"
        st.rerun()

    render_flow_ai_footer()

# ---------------------------------------------------------
# TELA: SAMPA MATCH (Radar Biz & Player de Áudio Histórico)
# ---------------------------------------------------------
elif st.session_state.pagina_atual == "Sampa Match":
    render_top_bar("SAMPA MATCH: Radar Biz")

    # Bloco idêntico ao seu print com o player imersivo do Café Girondino
    st.markdown(
        """
        <div class="neon-card" style="text-align: center;">
            <div style="color: #00F59B; font-weight: bold; font-size: 14px; margin-bottom: 8px;">🎧 GUIA DE ÁUDIO IMERSIVO: CENTRO HISTÓRICO</div>
            <div style="font-size: 13px; color: #ffffff; font-weight: bold; margin-bottom: 4px;">Café Girondino</div>
            <div style="font-size: 11px; color: #9ca3af; margin-bottom: 12px;">Fundado em 1554, o coração da metrópole guarda séculos de histórias...</div>
            <div style="background: rgba(0,245,155,0.08); border-radius: 10px; padding: 15px; border: 1px solid rgba(0,245,155,0.3);">
                <span style="font-size: 24px; color: #00F59B;">||| |||| | |||||| || | ||||</span><br>
                <span style="font-size: 12px; color: #00D2FF; margin-top: 6px; display: block;">▶️ Reproduzindo Trilha Histórica (01:45 / 03:20)</span>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div class="neon-card">
            <div style="color: #ffffff; font-weight: bold; font-size: 15px;">Ana Mendes</div>
            <div style="color: #00D2FF; font-size: 13px; margin: 2px 0;">📍 Sr. Analyst, Tech Solutions — 50m away</div>
            <p style="color: #d1d5db; font-size: 12px; margin-top: 6px;">Interesses em comum: Inovação B2B, Inteligência Artificial.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    col1, col2 = st.columns(2)
    with col1:
        if st.button("✨ Connect", key="c_ana", use_container_width=True):
            st.success("Conexão solicitada com Ana Mendes!")
    with col2:
        if st.button("🍷 Book VIP", key="b_ana", use_container_width=True):
            st.success("Reserva VIP solicitada!")

    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("⬅️ Voltar ao Início", use_container_width=True):
        st.session_state.pagina_atual = "Home"
        st.rerun()

    render_flow_ai_footer()

# ---------------------------------------------------------
# TELA: GPS INDOOR (Mapa 3D & Localização de Pessoas e Estandes)
# ---------------------------------------------------------
elif st.session_state.pagina_atual == "GPS Indoor":
    render_top_bar("GPS INDOOR: Mapa 3D Tático")
    
    st.markdown(
        """
        <div class="neon-card-cyan">
            <div style="color: #00D2FF; font-weight: bold; font-size: 15px; margin-bottom: 6px;">🗺️ MAPA 3D DE LOCALIZAÇÃO EM TEMPO REAL</div>
            <p style="font-size: 13px; color: #d1d5db;">Rastreamento ativo de participantes e pontos de interesse na zona.</p>
            <div style="background: rgba(0,213,255,0.08); padding: 15px; border-radius: 10px; border: 1px solid rgba(0,213,255,0.3); margin-top: 10px;">
                <b style="color: #00F59B;">📍 Ponto Atual:</b> Pavilhão Principal (Expo Floor A)<br>
                <b style="color: #00F59B;">🎯 Destino Rastreado:</b> Estande TechInnovate (Apenas 15m de distância)<br>
                <span style="font-size: 12px; color: #9ca3af; margin-top: 6px; display: block;">➔ Siga em frente pelo corredor norte e vire à esquerda.</span>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    if st.button("⬅️ Voltar ao Início", use_container_width=True):
        st.session_state.pagina_atual = "Home"
        st.rerun()

    render_flow_ai_footer()

# ---------------------------------------------------------
# TELA: COMPRAS & GASTRONOMIA (Restaurantes Parceiros, Localização, Notas e RTC)
# ---------------------------------------------------------
elif st.session_state.pagina_atual == "Compras Dual":
    render_top_bar("GASTRONOMIA & RESTAURANTES")

    st.markdown(
        """
        <div class="neon-card">
            <div style="color: #00F59B; font-weight: bold; font-size: 16px;">☕ Café Girondino (Centro Histórico)</div>
            <div style="color: #f3f4f6; font-size: 13px; margin: 4px 0;">⭐ <b>4.9</b> &nbsp;|&nbsp; 📍 Rua Boa Vista, 365 — Centro Histórico &nbsp;|&nbsp; 🕒 <b>RTC: 12 min</b></div>
            <p style="color: #d1d5db; font-size: 12px; line-height: 1.4; margin-top: 6px;">Café histórico tradicional com ambiente requintado e curadoria de áudio imersiva ativa pelo SampaFlow.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    if st.button("🍽️ Reservar Mesa (Café Girondino)", key="res_gir", use_container_width=True):
        st.success("Reserva confirmada com prioridade executiva!")

    st.markdown(
        """
        <div class="neon-card" style="margin-top: 15px;">
            <div style="color: #00F59B; font-weight: bold; font-size: 16px;">🍷 The Sãopaulista Undercurrent</div>
            <div style="color: #f3f4f6; font-size: 13px; margin: 4px 0;">⭐ <b>4.8</b> &nbsp;|&nbsp; 📍 Jardins (Vault Secreto) &nbsp;|&nbsp; 🕒 <b>RTC: 8 min</b></div>
            <p style="color: #d1d5db; font-size: 12px; line-height: 1.4; margin-top: 6px;">A hidden vault born from a forgotten coffee-baron catacomb. Flow AI predicts a high historical intrigue score.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    if st.button("🍽️ Reservar Mesa no Vault", key="res_vault", use_container_width=True):
        st.success("Mesa reservada com sucesso no Vault Secreto!")

    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("⬅️ Voltar ao Início", use_container_width=True):
        st.session_state.pagina_atual = "Home"
        st.rerun()

    render_flow_ai_footer()

# ---------------------------------------------------------
# TELA: SAMPA WORK
# ---------------------------------------------------------
elif st.session_state.pagina_atual == "Sampa Work":
    render_top_bar("SAMPA WORK: Jobs")

    st.markdown(
        """
        <div class="neon-card">
            <div style="color: #00D2FF; font-weight: bold; font-size: 15px;">💼 Concierge Executivo de Luxo</div>
            <p style="font-size: 13px; color: #d1d5db; margin-top: 6px;">Hotel Fasano Jardins — R$ 12.000 / mês</p>
            <p style="font-size: 12px; color: #9ca3af; margin-top: 4px;">Compatibilidade com seu perfil executivo calculada em 96% pela Flow AI.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    if st.button("⬅️ Voltar ao Início", use_container_width=True):
        st.session_state.pagina_atual = "Home"
        st.rerun()

    render_flow_ai_footer()
