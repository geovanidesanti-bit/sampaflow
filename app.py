import streamlit as st
from streamlit_mic_recorder 
import mic_recorder

# Configuração da Página
st.set_page_config(
    page_title="SampaFlow - Ecossistema Inteligente",
    page_icon="⚡",
    layout="centered",
)

# Injeção de CSS Customizado - Dark Glassmorphism com Fundo Urbano Tático & Animações
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
    
    /* Barra de Notícia Rolando (Marquee) no Topo */
    .ticker-container {
        width: 100%;
        overflow: hidden;
        background: rgba(0, 213, 255, 0.12);
        border: 1px solid rgba(0, 213, 255, 0.4);
        border-radius: 8px;
        padding: 6px 0;
        margin-bottom: 12px;
        white-space: nowrap;
        box-shadow: 0 0 10px rgba(0, 213, 255, 0.2);
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
        filter: drop-shadow(0 0 15px rgba(0, 245, 155, 0.4));
    }

    /* Perfil Estilo LinkedIn Compacto na Home */
    .profile-card-header {
        background: rgba(10, 15, 26, 0.95);
        border: 1px solid rgba(0, 245, 155, 0.5);
        border-radius: 14px;
        padding: 14px 16px;
        margin-bottom: 15px;
        display: flex;
        align-items: center;
        justify-content: space-between;
        box-shadow: 0 4px 20px rgba(0,0,0,0.6);
    }

    .neon-card {
        background: rgba(10, 15, 26, 0.92);
        border: 1px solid rgba(0, 245, 155, 0.45);
        backdrop-filter: blur(16px);
        border-radius: 16px;
        padding: 16px 18px;
        margin-bottom: 14px;
        box-shadow: 0 8px 24px rgba(0, 0, 0, 0.7);
    }
    
    .neon-card-cyan {
        background: rgba(10, 15, 26, 0.92);
        border: 1px solid rgba(0, 213, 255, 0.45);
        backdrop-filter: blur(16px);
        border-radius: 16px;
        padding: 16px 18px;
        margin-bottom: 14px;
        box-shadow: 0 8px 24px rgba(0, 0, 0, 0.7);
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
        transition: all 0.3s ease;
    }
    .stButton > button:hover {
        background: rgba(0, 245, 155, 0.2) !important;
        border-color: #00F59B !important;
        color: #ffffff !important;
        box-shadow: 0 0 15px rgba(0, 245, 155, 0.4);
    }

    .flow-ai-footer {
        background: rgba(5, 8, 14, 0.98);
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

# Inicialização de Variáveis de Sessão globais
if "pagina_atual" not in st.session_state:
    st.session_state.pagina_atual = "Home"

if "historico_ia" not in st.session_state:
    st.session_state.historico_ia = []

if "usuario_logado" not in st.session_state:
    st.session_state.usuario_logado = True  # Deixamos True para exibir o perfil simulado estilo LinkedIn de pronto
    st.session_state.dados_usuario = {
        "nome": "Geovani Santi",
        "cargo": "Gestão Comercial & Tech Leader",
        "linkedin": "linkedin.com/in/geovani-santi",
        "whatsapp": "(11) 99999-9999",
        "tipo": "Exibidor / Consultor B2B",
        "empresa": "SampaFlow Consulting",
        "nicho": "Tecnologia & Varejo",
        "estrelas": "⭐ 5.0 (48 avaliações)"
    }

if "motorista_logado" not in st.session_state:
    st.session_state.motorista_logado = True
    st.session_state.dados_motorista = {
        "nome": "Geovani Santi",
        "carro": "Renault Kwid 2020 Prata",
        "saldo_pix": 120.00,
        "faturamento_total": 450.00
    }

if "evento_selecionado" not in st.session_state:
    st.session_state.evento_selecionado = None

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
    # Mensagem propagando estilo outdoor digital rolando no topo
    st.markdown(
        """
        <div class="ticker-container">
            <div class="ticker-text">
                ⚡ SampaFlow Info: São Paulo • 15 de Setembro de 2026 • 🌧️ 21°C • Tempo Chuvoso • Ótimo dia para um caldo quente nos restaurantes parceiros do Centro e Jardins! ☕🍲
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
    st.markdown(
        """
        <div class="flow-ai-footer">
            <span style="color: #00F59B; font-weight: bold; font-size: 14px;">🎙️ FLOW AI BUTTON</span><br>
            <span style="color: #9ca3af; font-size: 11px;">TOQUE P/ FALAR OU CONSULTAR O ECOSSISTEMA</span>
        </div>
        """,
        unsafe_allow_html=True,
    )
    
    audio_gravado = mic_recorder(
        start_prompt="🔴 Iniciar Gravação de Voz",
        stop_prompt="⏹️ Parar & Processar IA",
        key=f"mic_{st.session_state.pagina_atual}",
    )
    
    if audio_gravado:
        resposta_texto = "✨ [Flow AI Command Processed]: Sincronização de rotas, radar de motoristas e feiras ativas executada com sucesso."
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
# TELA 1: HOME - PERFIL 5 ESTRELAS, MENU DE EVENTOS E MÓDULOS
# ---------------------------------------------------------
if st.session_state.pagina_atual == "Home":
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

    # 1. Perfil Estilo LinkedIn com Nota 5 Estrelas no Topo
    user = st.session_state.dados_usuario
    st.markdown(
        f"""
        <div class="profile-card-header">
            <div>
                <div style="color: #00F59B; font-weight: bold; font-size: 15px;">👤 {user['nome']} <span style="font-size:12px; color:#00D2FF;">({user['estrelas']})</span></div>
                <div style="color: #f3f4f6; font-size: 12px; margin-top: 2px;">{user['cargo']} • {user['empresa']}</div>
                <div style="color: #9ca3af; font-size: 11px; margin-top: 2px;">🔗 {user['linkedin']} | 📱 {user['whatsapp']}</div>
            </div>
            <div>
                <span style="background: rgba(0,245,155,0.15); color: #00F59B; border: 1px solid rgba(0,245,155,0.4); padding: 4px 10px; border-radius: 8px; font-size: 11px; font-weight: bold;">VERIFICADO</span>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Atalhos rápidos de acesso
    col_u1, col_u2 = st.columns(2)
    with col_u1:
        if st.button("🚗 Portal do Motorista (Radar)", use_container_width=True):
            st.session_state.pagina_atual = "Portal Motorista"
            st.rerun()
    with col_u2:
        if st.button("✏️ Editar Perfil LinkedIn", use_container_width=True):
            st.session_state.pagina_atual = "Cadastro Usuario"
            st.rerun()

    # 2. Menu de Eventos (Dropdown / Seletor de Feiras e Exposições)
    st.markdown("### 🏛️ Menu de Eventos & Exposições em São Paulo")
    
    pavilhoes_eventos = [
        {
            "id": "expocenter_norte",
            "pavilhao": "Expo Center Norte",
            "nome": "Feira Internacional de TI & Cloud 2026",
            "tipo": "Feira de TI & Inovação B2B",
            "data": "18 a 21 de Outubro",
            "desc": "O maior ponto de encontro de infraestrutura digital, cibersegurança e cloud computing da América Latina."
        },
        {
            "id": "transamerica",
            "pavilhao": "Transamérica Expo Center",
            "nome": "Sampa Logistics & Supply Chain Expo",
            "tipo": "Feira de Logística & Indústria 4.0",
            "data": "25 a 28 de Outubro",
            "desc": "Conectando gigantes do transporte, automação industrial, armazéns inteligentes e parceiros logísticos."
        },
        {
            "id": "imigrantes",
            "pavilhao": "São Paulo Expo (Imigrantes)",
            "nome": "Global Health & MedTech Brazil",
            "tipo": "Feira de Saúde & Tecnologia Médica",
            "data": "05 a 08 de Novembro",
            "desc": "Inovações em equipamentos hospitalares, telessaúde e conexões diretas com redes farmacêuticas."
        }
    ]

    # Menu seletor estilo dropdown para abrir o evento escolhido
    nombres_eventos = [f"{ev['pavilhao']} — {ev['nome']}" for ev in pavilhoes_eventos]
    evento_escolhido_menu = st.selectbox("📂 Selecione o Evento no Menu de Exposições:", nombres_eventos)
    
    # Identifica qual foi selecionado no selectbox
    idx_selecionado = nombres_eventos.index(evento_escolhido_menu)
    ev_atual = pavilhoes_eventos[idx_selecionado]

    st.markdown(
        f"""
        <div class="neon-card">
            <div style="color: #00F59B; font-weight: bold; font-size: 15px;">🏢 {ev_atual['pavilhao']}</div>
            <div style="color: #00D2FF; font-size: 14px; font-weight: bold; margin: 4px 0;">{ev_atual['nome']}</div>
            <div style="color: #f3f4f6; font-size: 12px; margin-bottom: 4px;">🏷️ <b>Tipo:</b> {ev_atual['tipo']} &nbsp;|&nbsp; 📅 {ev_atual['data']}</div>
            <p style="color: #d1d5db; font-size: 12px; line-height: 1.4; margin-top: 4px;">{ev_atual['desc']}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    if st.button(f"🚀 Acessar Ecossistema do Evento Selecionado", use_container_width=True):
        st.session_state.evento_selecionado = ev_atual
        st.session_state.pagina_atual = "Dashboard Evento"
        st.rerun()

    st.markdown("### 🌐 Módulos Principais do Ecossistema")
    
    if st.button("🤝  **SAMPA MATCH** — Radar Biz & Conexões Gerais", use_container_width=True):
        st.session_state.pagina_atual = "Sampa Match Geral"
        st.rerun()

    if st.button("📍  **GPS INDOOR** — Mapa Tático & Localização", use_container_width=True):
        st.session_state.pagina_atual = "GPS Indoor"
        st.rerun()

    if st.button("🛍️  **GASTRONOMIA & RESERVAS** — Restaurantes & Caldos (Dias Chuvosos)", use_container_width=True):
        st.session_state.pagina_atual = "Compras Dual"
        st.rerun()

    if st.button("💼  **SAMPA WORK** — Jobs & Oportunidades Executivas", use_container_width=True):
        st.session_state.pagina_atual = "Sampa Work"
        st.rerun()

    render_flow_ai_footer()

# ---------------------------------------------------------
# TELA 2: CADASTRO DO USUÁRIO
# ---------------------------------------------------------
elif st.session_state.pagina_atual == "Cadastro Usuario":
    render_top_bar("Perfil & Credenciamento")

    st.markdown(
        """
        <div class="neon-card-cyan">
            <div style="color: #00D2FF; font-weight: bold; font-size: 15px; margin-bottom: 6px;">🔗 CADASTRO VIA LINKEDIN & RETENÇÃO</div>
            <p style="font-size: 13px; color: #d1d5db;">Atualize seus dados profissionais para refletir sua nota 5 estrelas e bio executiva no app.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    with st.form("form_cadastro_usuario"):
        st.markdown("### Credenciais Profissionais")
        nome_input = st.text_input("Nome Completo", st.session_state.dados_usuario["nome"])
        cargo_input = st.text_input("Cargo / Bio Resumida (Estilo LinkedIn)", st.session_state.dados_usuario["cargo"])
        linkedin_url = st.text_input("🔗 Link do Perfil do LinkedIn", st.session_state.dados_usuario["linkedin"])
        whatsapp_celular = st.text_input("📱 Celular (WhatsApp) para Alertas e Retenção", st.session_state.dados_usuario["whatsapp"])
        
        tipo_participante = st.selectbox("Você participa como:", ["Exibidor / Consultor B2B", "Visitante / Comprador Geral"])
        empresa_estande = st.text_input("🏢 Nome da sua Empresa", st.session_state.dados_usuario["empresa"])
        
        submitted = st.form_submit_button("✅ Salvar Alterações de Perfil")
        if submitted:
            st.session_state.dados_usuario.update({
                "nome": nome_input,
                "cargo": cargo_input,
                "linkedin": linkedin_url,
                "whatsapp": whatsapp_celular,
                "tipo": tipo_participante,
                "empresa": empresa_estande
            })
            st.success("🎉 Perfil atualizado com sucesso!")
            st.session_state.pagina_atual = "Home"
            st.rerun()

    if st.button("⬅️ Voltar ao Início", use_container_width=True):
        st.session_state.pagina_atual = "Home"
        st.rerun()

    render_flow_ai_footer()

# ---------------------------------------------------------
# TELA 3: DASHBOARD DO EVENTO SELECIONADO
# ---------------------------------------------------------
elif st.session_state.pagina_atual == "Dashboard Evento":
    ev = st.session_state.evento_selecionado
    render_top_bar(ev['pavilhao'] if ev else "Evento SP")

    st.markdown(
        f"""
        <div class="neon-card">
            <div style="color: #00F59B; font-weight: bold; font-size: 16px;">🏢 {ev['nome'] if ev else 'Feira Sampa'}</div>
            <div style="color: #00D2FF; font-size: 13px; margin: 4px 0;">📍 <b>Local:</b> {ev['pavilhao'] if ev else ''}</div>
            <p style="color: #d1d5db; font-size: 12px; margin-top: 6px;">{ev['desc'] if ev else ''}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    aba_escolhida = st.radio("Navegação do Evento:", ["🤝 Match & Conexões B2B", "🏢 Empresas do Estande", "📸 Feed Oficial"], horizontal=True)

    if aba_escolhida == "🤝 Match & Conexões B2B":
        st.markdown("### ⚡ Radar de Matches Inteligentes (Nota 5 Estrelas)")
        
        perfis_match = [
            {"nome": "Marcos Vinicius", "cargo": "Head de Inovação (⭐ 4.9)", "empresa": "CloudNet Brasil", "nicho": "Tecnologia & Software B2B"},
            {"nome": "Juliana Paes", "cargo": "Diretora de Contratos (⭐ 5.0)", "empresa": "Global Supply Ltda", "nicho": "Logística & Supply Chain"}
        ]

        for p in perfis_match:
            st.markdown(
                f"""
                <div class="neon-card-cyan">
                    <div style="color: #ffffff; font-weight: bold; font-size: 14px;">{p['nome']} — <span style="color: #00D2FF; font-size: 12px;">{p['cargo']}</span></div>
                    <div style="color: #00F59B; font-size: 12px; margin: 2px 0;">🏢 {p['empresa']} &nbsp;|&nbsp; 🏷️ {p['nicho']}</div>
                </div>
                """,
                unsafe_allow_html=True,
            )
            col_m1, col_m2 = st.columns(2)
            with col_m1:
                if st.button(f"💚 Curtir", key=f"like_{p['nome']}"):
                    st.success(f"Like enviado para {p['nome']}!")
            with col_m2:
                if st.button(f"🤝 Conectar", key=f"match_{p['nome']}"):
                    st.success(f"Match B2B estabelecido com {p['nome']}!")

    elif aba_escolhida == "🏢 Empresas do Estande":
        st.markdown("### 📋 Diretório de Empresas Expositoras")
        st.markdown("* **TechInnovate Cloud** (Tecnologia) — *Estande 42*")
        st.markdown("* **Sampa Cargo Express** (Logística) — *Estande 15*")

    elif aba_escolhida == "📸 Feed Oficial":
        st.markdown("### 📸 Feed de Momentos do Pavilhão")
        st.markdown(
            """
            <div class="neon-card">
                <div style="color: #00F59B; font-weight: bold; font-size: 13px;">🏢 Geovani Santi <span style="color:#00D2FF; font-size:11px;">(⭐ 5.0)</span></div>
                <p style="font-size: 12px; color: #d1d5db; margin-top: 4px;">Apresentando as soluções de inteligência de fluxo no Expo Center Norte. Venha tomar um café!</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("⬅️ Voltar ao Início", use_container_width=True):
        st.session_state.pagina_atual = "Home"
        st.rerun()

    render_flow_ai_footer()

# ---------------------------------------------------------
# TELA 4: SAMPA MATCH GERAL
# ---------------------------------------------------------
elif st.session_state.pagina_atual == "Sampa Match Geral":
    render_top_bar("SAMPA MATCH: Radar & Áudio")

    st.markdown(
        """
        <div class="neon-card" style="text-align: center;">
            <div style="color: #00F59B; font-weight: bold; font-size: 14px; margin-bottom: 8px;">🎧 GUIA DE ÁUDIO IMERSIVO: CENTRO HISTÓRICO</div>
            <div style="font-size: 13px; color: #ffffff; font-weight: bold; margin-bottom: 4px;">Café Girondino</div>
            <div style="font-size: 11px; color: #9ca3af; margin-bottom: 12px;">Fundado em 1554, o coração da metrópole guarda séculos de histórias...</div>
            <div style="background: rgba(0,245,155,0.08); border-radius: 10px; padding: 15px; border: 1px solid rgba(0,245,155,0.3);">
                <span style="font-size: 20px; color: #00F59B
