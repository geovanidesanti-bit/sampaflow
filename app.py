import streamlit as st
from streamlit_mic_recorder import mic_recorder

# Configuração da Página
st.set_page_config(
    page_title="SampaFlow - Ecossistema Inteligente",
    page_icon="⚡",
    layout="centered",
)

# Injeção de CSS Customizado - Dark Glassmorphism & Animações
st.markdown(
    """
    <style>
    .stApp {
        background-color: #05080e;
        background-image: 
            linear-gradient(rgba(0, 245, 155, 0.03) 1px, transparent 1px),
            linear-gradient(90deg, rgba(0, 213, 255, 0.03) 1px, transparent 1px),
            radial-gradient(circle at 50% 20%, rgba(0, 213, 255, 0.08) 0%, transparent 60%),
            radial-gradient(circle at 20% 80%, rgba(0, 245, 155, 0.06) 0%, transparent 50%);
        background-size: 40px 40px, 40px 40px, 100% 100%, 100% 100%;
        color: #f3f4f6;
        font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
    }
    header {visibility: hidden;}
    
    .ticker-container {
        width: 100%;
        overflow: hidden;
        background: rgba(0, 213, 255, 0.12);
        border: 1px solid rgba(0, 213, 255, 0.4);
        border-radius: 8px;
        padding: 6px 0;
        margin-bottom: 12px;
        white-space: nowrap;
    }
    .ticker-text {
        display: inline-block;
        padding-left: 100%;
        animation: marquee 22s linear infinite;
        color: #00D2FF;
        font-size: 12px;
        font-weight: 600;
    }
    @keyframes marquee {
        0%   { transform: translate(0, 0); }
        100% { transform: translate(-100%, 0); }
    }

    .top-bar {
        display: flex;
        justify-content: space-between;
        align-items: center;
        color: #9ca3af;
        font-size: 13px;
        margin-bottom: 10px;
        padding: 0 5px;
    }

    .logo-container {
        text-align: center;
        margin-bottom: 12px;
    }
    .logo-title {
        font-size: 30px;
        font-weight: 900;
        letter-spacing: -1px;
        background: linear-gradient(90deg, #00F59B 0%, #00D2FF 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        display: inline-block;
    }

    .profile-card-header {
        background: rgba(10, 15, 26, 0.95);
        border: 1px solid rgba(0, 245, 155, 0.5);
        border-radius: 14px;
        padding: 14px 16px;
        margin-bottom: 15px;
        display: flex;
        align-items: center;
        justify-content: space-between;
    }

    .neon-card {
        background: rgba(10, 15, 26, 0.92);
        border: 1px solid rgba(0, 245, 155, 0.45);
        backdrop-filter: blur(16px);
        border-radius: 16px;
        padding: 16px 18px;
        margin-bottom: 14px;
    }
    
    .neon-card-cyan {
        background: rgba(10, 15, 26, 0.92);
        border: 1px solid rgba(0, 213, 255, 0.45);
        backdrop-filter: blur(16px);
        border-radius: 16px;
        padding: 16px 18px;
        margin-bottom: 14px;
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
        background: rgba(13, 19, 33, 0.95) !important;
        color: #00F59B !important;
        border: 1px solid rgba(0, 245, 155, 0.6) !important;
        border-radius: 12px !important;
        font-weight: 700 !important;
        padding: 10px 16px !important;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Inicialização segura de todas as variáveis de sessão
if "pagina_atual" not in st.session_state:
    st.session_state.pagina_atual = "Home"

if "historico_ia" not in st.session_state:
    st.session_state.historico_ia = []

if "dados_usuario" not in st.session_state:
    st.session_state.dados_usuario = {
        "nome": "Geovani Santi",
        "cargo": "Gestão Comercial & Tech Leader",
        "linkedin": "linkedin.com/in/geovani-santi",
        "whatsapp": "(11) 99999-9999",
        "tipo": "Exibidor / Consultor B2B",
        "empresa": "SampaFlow Consulting",
        "estrelas": "⭐ 5.0 (48 avaliações)"
    }

if "dados_motorista" not in st.session_state:
    st.session_state.dados_motorista = {
        "nome": "Geovani Santi",
        "carro": "Renault Kwid 2020 Prata",
        "saldo_pix": 120.00,
        "faturamento_total": 450.00
    }

if "evento_selecionado" not in st.session_state:
    st.session_state.evento_selecionado = {
        "pavilhao": "Expo Center Norte",
        "nome": "Feira Internacional de TI & Cloud 2026",
        "tipo": "Feira de TI & Inovação B2B",
        "data": "18 a 21 de Outubro",
        "desc": "O maior ponto de encontro de infraestrutura digital."
    }

if "corrida_atual" not in st.session_state:
    st.session_state.corrida_atual = {
        "ativa": True,
        "origem": "Expo Center Norte (Pavilhão A)",
        "destino": "Rua Augusta, 1500 — Jardins",
        "valor": 48.50,
        "distancia": "4.2 km (8 min)",
        "passageiro": "Mariana Costa (Nota ⭐ 4.9)"
    }

def render_top_bar(titulo_pagina="SampaFlow"):
    st.markdown(
        """
        <div class="ticker-container">
            <div class="ticker-text">
                ⚡ SampaFlow Info: São Paulo • 15 de Setembro de 2026 • 🌧️ 21°C • Tempo Chuvoso • Ótimo dia para um caldo quente nos restaurantes parceiros! ☕🍲
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.markdown(
        f"""
        <div class="top-bar">
            <span>⚡ SampaFlow &nbsp;|&nbsp; <b>{titulo_pagina}</b></span>
            <span>📍 São Paulo &nbsp; 🌧️ 21°C</span>
        </div>
        """,
        unsafe_allow_html=True,
    )

def render_flow_ai_footer():
    st.markdown("---")
    audio_gravado = mic_recorder(
        start_prompt="🔴 Iniciar Gravação de Voz",
        stop_prompt="⏹️ Parar & Processar IA",
        key=f"mic_{st.session_state.pagina_atual}",
    )
    
    if audio_gravado:
        resposta_texto = "✨ [Flow AI Command Processed]: Sincronização executada com sucesso."
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

# Roteador de Páginas Blindado contra Erros
pagina = st.session_state.pagina_atual

if pagina == "Home":
    render_top_bar("Hub Central SP")
    st.markdown(
        """
        <div class="logo-container">
            <span class="logo-title">SAMPAFLOW</span>
            <div style="color: #9ca3af; font-size: 12px; margin-top: 4px;">Ecossistema Urbano Preditivo & Inteligência de Fluxo</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    user = st.session_state.dados_usuario
    st.markdown(
        f"""
        <div class="profile-card-header">
            <div>
                <div style="color: #00F59B; font-weight: bold; font-size: 15px;">👤 {user['nome']} <span style="font-size:12px; color:#00D2FF;">({user['estrelas']})</span></div>
                <div style="color: #f3f4f6; font-size: 12px; margin-top: 2px;">{user['cargo']} • {user['empresa']}</div>
            </div>
            <div>
                <span style="background: rgba(0,245,155,0.15); color: #00F59B; border: 1px solid rgba(0,245,155,0.4); padding: 4px 10px; border-radius: 8px; font-size: 11px; font-weight: bold;">VERIFICADO</span>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    col_u1, col_u2 = st.columns(2)
    with col_u1:
        if st.button("🚗 Portal do Motorista (Radar)", use_container_width=True):
            st.session_state.pagina_atual = "Portal Motorista"
            st.rerun()
    with col_u2:
        if st.button("✏️ Editar Perfil", use_container_width=True):
            st.session_state.pagina_atual = "Cadastro Usuario"
            st.rerun()

    st.markdown("### 🏛️ Menu de Eventos & Exposições em São Paulo")
    if st.button("🚀 Acessar Painel do Evento Atual", use_container_width=True):
        st.session_state.pagina_atual = "Dashboard Evento"
        st.rerun()

    st.markdown("### 🌐 Módulos Principais")
    if st.button("🤝 SAMPA MATCH — Radar & Conexões", use_container_width=True):
        st.session_state.pagina_atual = "Sampa Match Geral"
        st.rerun()
    if st.button("📍 GPS INDOOR — Mapa Tático", use_container_width=True):
        st.session_state.pagina_atual = "GPS Indoor"
        st.rerun()
    if st.button("🛍️ GASTRONOMIA — Caldos para Dias Chuvosos", use_container_width=True):
        st.session_state.pagina_atual = "Compras Dual"
        st.rerun()
    if st.button("💼 SAMPA WORK — Oportunidades", use_container_width=True):
        st.session_state.pagina_atual = "Sampa Work"
        st.rerun()

    render_flow_ai_footer()

elif pagina == "Cadastro Usuario":
    render_top_bar("Perfil & Credenciamento")
    with st.form("form_cad"):
        nome_input = st.text_input("Nome Completo", st.session_state.dados_usuario["nome"])
        cargo_input = st.text_input("Cargo / Bio Resumida", st.session_state.dados_usuario["cargo"])
        if st.form_submit_button("✅ Salvar"):
            st.session_state.dados_usuario["nome"] = nome_input
            st.session_state.dados_usuario["cargo"] = cargo_input
            st.success("Atualizado!")
            st.session_state.pagina_atual = "Home"
            st.rerun()
    if st.button("⬅️ Voltar"):
        st.session_state.pagina_atual = "Home"
        st.rerun()
    render_flow_ai_footer()

elif pagina == "Dashboard Evento":
    ev = st.session_state.evento_selecionado
    render_top_bar(ev['pavilhao'])
    st.markdown(
        f"""
        <div class="neon-card">
            <div style="color: #00F59B; font-weight: bold; font-size: 16px;">🏢 {ev['nome']}</div>
            <div style="color: #00D2FF; font-size: 13px; margin: 4px 0;">📍 <b>Local:</b> {ev['pavilhao']}</div>
            <p style="color: #d1d5db; font-size: 12px;">{ev['desc']}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    if st.button("⬅️ Voltar"):
        st.session_state.pagina_atual = "Home"
        st.rerun()
    render_flow_ai_footer()

elif pagina == "Sampa Match Geral":
    render_top_bar("SAMPA MATCH")
    st.markdown(
        """
        <div class="neon-card">
            <div style="color: #00F59B; font-weight: bold;">Ana Mendes (⭐ 4.9)</div>
            <div style="color: #00D2FF; font-size: 13px;">📍 Analista Tech — 50m de distância</div>
        </div>
        """,
        unsafe_allow_html=True,
    )
    if st.button("⬅️ Voltar"):
        st.session_state.pagina_atual = "Home"
        st.rerun()
    render_flow_ai_footer()

elif pagina == "GPS Indoor":
    render_top_bar("GPS INDOOR")
    st.markdown(
        """
        <div class="neon-card-cyan">
            <b>📍 Localização em Tempo Real Ativa</b><br>
            Siga em frente pelo corredor norte.
        </div>
        """,
        unsafe_allow_html=True,
    )
    if st.button("⬅️ Voltar"):
        st.session_state.pagina_atual = "Home"
        st.rerun()
    render_flow_ai_footer()

elif pagina == "Compras Dual":
    render_top_bar("Gastronomia & Caldos")
    st.markdown(
        """
        <div class="neon-card">
            <div style="color: #00F59B; font-weight: bold;">☕ Café Girondino (Caldo Verde & Cremes)</div>
            <div style="color: #f3f4f6; font-size: 13px;">⭐ Nota: 4.9 | 📍 Centro de São Paulo</div>
        </div>
        """,
        unsafe_allow_html=True,
    )
    if st.button("🍽️ Reservar Mesa com Caldo Quente"):
        st.success("Mesa reservada com sucesso para os dias chuvosos!")
    if st.button("⬅️ Voltar"):
        st.session_state.pagina_atual = "Home"
        st.rerun()
    render_flow_ai_footer()

elif pagina == "Sampa Work":
    render_top_bar("Sampa Work")
    st.markdown(
        """
        <div class="neon-card">
            <div style="color: #00D2FF; font-weight: bold;">Concierge Executivo — Hotel Fasano</div>
            <div style="color: #d1d5db; font-size: 12px;">Compatibilidade com seu perfil 5 estrelas: 96%</div>
        </div>
        """,
        unsafe_allow_html=True,
    )
    if st.button("⬅️ Voltar"):
        st.session_state.pagina_atual = "Home"
        st.rerun()
    render_flow_ai_footer()

elif pagina == "Portal Motorista":
    render_top_bar("Portal do Motorista")
    mot = st.session_state.dados_motorista
    st.markdown(
        f"""
        <div class="neon-card-cyan">
            <b>Motorista:</b> {mot['nome']} ({mot['carro']}) ⭐ 5.0<br>
            <b>Faturamento:</b> R$ {mot['faturamento_total']:.2f} | <b>Saldo Pix:</b> R$ {mot['saldo_pix']:.2f}
        </div>
        """,
        unsafe_allow_html=True,
    )

    corrida = st.session_state.corrida_atual
    if corrida["ativa"]:
        st.markdown(
            f"""
            <div class="neon-card" style="border: 1px solid rgba(0,213,255,0.8); text-align: center;">
                <div style="color: #00D2FF; font-weight: bold; font-size: 16px;">🔔 NOVA SOLICITAÇÃO NO RADAR!</div>
                <div style="font-size: 15px; color: #ffffff; font-weight: bold;">R$ {corrida['valor']:.2f} ({corrida['distancia']})</div>
                <div style="font-size: 13px; color: #d1d5db;">👤 {corrida['passageiro']}</div>
                <div style="font-size: 12px; color: #9ca3af;">📍 Embarque: {corrida['origem']}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )
        col1, col2 = st.columns(2)
        with col1:
            if st.button("✅ Aceitar"):
                st.success("Corrida aceita!")
                st.session_state.dados_motorista["faturamento_total"] += corrida["valor"]
                st.session_state.corrida_atual["ativa"] = False
                st.rerun()
        with col2:
            if st.button("❌ Rejeitar"):
                st.warning("Rejeitado.")
                st.session_state.corrida_atual["ativa"] = False
                st.rerun()
    else:
        st.info("📡 Radar buscando novas chamadas...")
        if st.button("🔄 Simular Nova Chamada"):
            st.session_state.corrida_atual["ativa"] = True
            st.rerun()

    if st.button("⬅️ Voltar"):
        st.session_state.pagina_atual = "Home"
        st.rerun()
    render_flow_ai_footer()
    
