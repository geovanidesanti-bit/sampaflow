import streamlit as st

# Configuração da Página
st.set_page_config(
    page_title="SampaFlow - Ecossistema Inteligente",
    page_icon="⚡",
    layout="centered",
)

# Injeção de CSS Customizado - Dark Glassmorphism, Letreiro Dinâmico & Radar Tático
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
    
    /* Letreiro Animado estilo Propaganda */
    .marquee-container {
        background: rgba(0, 213, 255, 0.1);
        border: 1px solid rgba(0, 213, 255, 0.4);
        border-radius: 10px;
        overflow: hidden;
        white-space: nowrap;
        box-sizing: border-box;
        margin-bottom: 15px;
        padding: 8px 0;
    }
    .marquee-text {
        display: inline-block;
        padding-left: 100%;
        animation: marquee 18s linear infinite;
        color: #00D2FF;
        font-size: 13px;
        font-weight: bold;
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
        filter: drop-shadow(0 0 15px rgba(0, 245, 155, 0.4));
    }

    .neon-card {
        background: rgba(10, 15, 26, 0.92);
        border: 1px solid rgba(0, 245, 155, 0.45);
        backdrop-filter: blur(16px);
        border-radius: 16px;
        padding: 18px 20px;
        margin-bottom: 16px;
        box-shadow: 0 8px 24px rgba(0, 0, 0, 0.7);
    }
    
    .neon-card-cyan {
        background: rgba(10, 15, 26, 0.92);
        border: 1px solid rgba(0, 213, 255, 0.45);
        backdrop-filter: blur(16px);
        border-radius: 16px;
        padding: 18px 20px;
        margin-bottom: 16px;
        box-shadow: 0 8px 24px rgba(0, 0, 0, 0.7);
    }

    .ride-request-box {
        background: rgba(0, 245, 155, 0.08);
        border: 2px solid #00F59B;
        border-radius: 14px;
        padding: 16px;
        margin-bottom: 15px;
        box-shadow: 0 0 20px rgba(0, 245, 155, 0.3);
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
        padding: 12px 18px !important;
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
    st.session_state.usuario_logado = False
    st.session_state.dados_usuario = {}

if "motorista_logado" not in st.session_state:
    st.session_state.motorista_logado = False
    st.session_state.dados_motorista = {}

if "evento_selecionado" not in st.session_state:
    st.session_state.evento_selecionado = None

if "corrida_ativa" not in st.session_state:
    st.session_state.corrida_ativa = {
        "ativa": True,
        "passageiro": "Mariana Souza (Diretora de Contratos)",
        "origem": "Expo Center Norte — Pavilhão A",
        "destino": "Hotel Fasano (Jardins)",
        "valor": 78.50,
        "distancia": "4.2 km (12 min)"
    }

def render_top_bar(titulo_pagina="SampaFlow"):
    st.markdown(
        f"""
        <div class="top-bar">
            <span>⚡ SampaFlow &nbsp;|&nbsp; <b>{titulo_pagina}</b></span>
            <span>📍 São Paulo</span>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.markdown(
        """
        <div class="marquee-container">
            <div class="marquee-text">
                ⚡ SÃO PAULO | Terça-feira, 15 de Setembro de 2026 | 🌧️ 19°C — Clima chuvoso na metrópole. Perfeito para um caldo quente no Café Girondino ou um jantar reservado no The Sãopaulista Undercurrent! 🍷🍜
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

def render_flow_ai_footer():
    st.markdown("---")
    st.markdown(
        """
        <div class="flow-ai-footer">
            <span style="color: #00F59B; font-weight: bold; font-size: 14px;">🎙️ FLOW AI AUDIO INTERACTION</span><br>
            <span style="color: #9ca3af; font-size: 11px;">GRAVE SUA VOZ OU COMANDO PARA CONSULTAR O ECOSSISTEMA</span>
        </div>
        """,
        unsafe_allow_html=True,
    )
    
    # Substituído por st.audio_input nativo para evitar erros de dependência externa
    audio_gravado = st.audio_input("Grave seu comando de voz para a Flow AI", key=f"audio_input_{st.session_state.pagina_atual}")
    
    if audio_gravado:
        resposta_texto = "✨ [Flow AI Command Processed]: Rota recalculada, match corporativo validado e radar sincronizado com sucesso via áudio."
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
# TELA 1: HOME - HUB DE EVENTOS E PERFIS EM DESTAQUE
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

    col_u1, col_u2 = st.columns(2)
    with col_u1:
        if st.button("🚗 Portal do Motorista", use_container_width=True):
            st.session_state.pagina_atual = "Portal Motorista"
            st.rerun()
    with col_u2:
        if st.button("👤 Cadastro / Perfil LinkedIn", use_container_width=True):
            st.session_state.pagina_atual = "Cadastro Usuario"
            st.rerun()

    st.markdown("### 🏛️ Menu de Grandes Pavilhões & Feiras de SP")
    if st.button("📂 Abrir Diretório Geral de Exposições & Feiras", use_container_width=True):
        st.session_state.pagina_atual = "Lista Eventos"
        st.rerun()

    st.markdown("### ⭐ Perfis em Destaque no Ecossistema (Networking)")
    
    perfis_home = [
        {
            "nome": "Camila Vasconcelos",
            "cargo": "Head de Inovação & Transformação Digital",
            "bio": "Especialista em ecossistemas B2B e IA aplicada à indústria 4.0. Conectando marcas globais em São Paulo.",
            "rating": "★★★★★ (4.9 / 180 conexões)"
        },
        {
            "nome": "Dr. Eduardo Monteiro",
            "cargo": "Sócio Fundador | Venture Capital & MedTech",
            "bio": "Investidor focado em scale-ups de tecnologia médica e infraestrutura digital. Palestrante no São Paulo Expo.",
            "rating": "★★★★★ (5.0 / 215 conexões)"
        }
    ]

    for p in perfis_home:
        st.markdown(
            f"""
            <div class="neon-card-cyan">
                <div style="display: flex; justify-content: space-between; align-items: center;">
                    <span style="color: #ffffff; font-weight: bold; font-size: 15px;">{p['nome']}</span>
                    <span style="color: #00F59B; font-size: 13px;">{p['rating']}</span>
                </div>
                <div style="color: #00D2FF; font-size: 13px; margin: 3px 0; font-weight: bold;">{p['cargo']}</div>
                <p style="color: #d1d5db; font-size: 12px; line-height: 1.4; margin-top: 6px;">{p['bio']}</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown("### 🌐 Módulos Principais do Ecossistema")
    
    if st.button("🤝  **SAMPA MATCH** — Radar Biz & Conexões Gerais", use_container_width=True):
        st.session_state.pagina_atual = "Sampa Match Geral"
        st.rerun()

    if st.button("📍  **GPS INDOOR** — Mapa Tático & Localização", use_container_width=True):
        st.session_state.pagina_atual = "GPS Indoor"
        st.rerun()

    if st.button("🛍️  **GASTRONOMIA & RESERVAS** — Restaurantes com Seletor de Horário", use_container_width=True):
        st.session_state.pagina_atual = "Compras Dual"
        st.rerun()

    if st.button("💼  **SAMPA WORK** — Jobs & Oportunidades Executivas", use_container_width=True):
        st.session_state.pagina_atual = "Sampa Work"
        st.rerun()

    render_flow_ai_footer()

# ---------------------------------------------------------
# TELA 1.1: LISTA DE EVENTOS E EXPOSIÇÕES (MENU DEDICADO)
# ---------------------------------------------------------
elif st.session_state.pagina_atual == "Lista Eventos":
    render_top_bar("Diretório de Feiras & Expos")

    st.markdown("### 🏛️ Todas as Exposições & Feiras Ativas em São Paulo")
    st.markdown("<p style='font-size:12px; color:#9ca3af;'>Selecione abaixo o evento para entrar no ecossistema específico do pavilhão.</p>", unsafe_allow_html=True)

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

    for ev in pavilhoes_eventos:
        st.markdown(
            f"""
            <div class="neon-card">
                <div style="color: #00F59B; font-weight: bold; font-size: 15px;">🏢 {ev['pavilhao']}</div>
                <div style="color: #00D2FF; font-size: 14px; font-weight: bold; margin: 4px 0;">{ev['nome']}</div>
                <div style="color: #f3f4f6; font-size: 12px; margin-bottom: 4px;">🏷️ <b>Tipo:</b> {ev['tipo']} &nbsp;|&nbsp; 📅 {ev['data']}</div>
                <p style="color: #d1d5db; font-size: 12px; line-height: 1.4; margin-top: 4px;">{ev['desc']}</p>
            </div>
            """,
            unsafe_allow_html=True,
        )
        if st.button(f"🚀 Entrar no Ecossistema: {ev['pavilhao']}", key=f"menu_ev_{ev['id']}", use_container_width=True):
            st.session_state.evento_selecionado = ev
            st.session_state.pagina_atual = "Dashboard Evento"
            st.rerun()

    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("⬅️ Voltar ao Início", use_container_width=True):
        st.session_state.pagina_atual = "Home"
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
            <p style="font-size: 13px; color: #d1d5db;">Conecte sua conta profissional para carregar seus dados e garantir mensagens diretas e networking seguro.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    with st.form("form_cadastro_usuario"):
        st.markdown("### Credenciais Profissionais")
        linkedin_url = st.text_input("🔗 Link do Perfil do LinkedIn", "https://linkedin.com/in/seu-perfil")
        whatsapp_celular = st.text_input("📱 Celular (WhatsApp) para Alertas e Retenção", "(11) 99999-9999")
        
        st.markdown("### Perfil de Participação no Evento")
        tipo_participante = st.selectbox("Você participa como:", ["Exibidor / Empresa no Estande", "Visitante / Comprador Geral"])
        
        empresa_estande = ""
        nicho_parceria = ""
        if tipo_participante == "Exibidor / Empresa no Estande":
            empresa_estande = st.text_input("🏢 Confirme o Nome da sua Empresa / Estande", "Ex: TechSolutions Global")
            nicho_parceria = st.selectbox("Nicho Específico para Parcerias e Contratos B2B:", [
                "Tecnologia & Software B2B", 
                "Logística & Supply Chain", 
                "Saúde & MedTech", 
                "Investimentos & Venture Capital", 
                "Consultoria & Serviços Executivos"
            ])
        
        uploaded_foto = st.file_uploader("📸 Suba sua Foto de Perfil (Avatar)", type=["png", "jpg", "jpeg"])
        
        submitted = st.form_submit_button("✅ Concluir Cadastro & Entrar no App")
        if submitted:
            st.session_state.usuario_logado = True
            st.session_state.dados_usuario = {
                "linkedin": linkedin_url,
                "whatsapp": whatsapp_celular,
                "tipo": tipo_participante,
                "empresa": empresa_estande,
                "nicho": nicho_parceria,
                "foto": uploaded_foto
            }
            st.success("🎉 Cadastro realizado com sucesso! Seus dados foram sincronizados.")
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

    if not st.session_state.usuario_logado:
        st.warning("⚠️ Você ainda não concluiu seu cadastro profissional. Cadastre-se para habilitar conexões e postagens!")
        if st.button("👉 Fazer Cadastro Agora", use_container_width=True):
            st.session_state.pagina_atual = "Cadastro Usuario"
            st.rerun()
    else:
        user = st.session_state.dados_usuario
        st.markdown(
            f"""
            <div style="background: rgba(0,245,155,0.08); padding: 10px 15px; border-radius: 10px; border: 1px solid rgba(0,245,155,0.3); margin-bottom: 15px; font-size: 13px;">
                👤 <b>Logado como:</b> {user['tipo']} | 📱 {user['whatsapp']} {f"| 🏢 {user['empresa']}" if user['empresa'] else ""}
            </div>
            """,
            unsafe_allow_html=True,
        )

    aba_escolhida = st.radio("Navegação do Evento:", ["🤝 Match & Conexões B2B", "🏢 Empresas do Estande & Nichos", "📸 Publicações & Feed"], horizontal=True)

    if aba_escolhida == "🤝 Match & Conexões B2B":
        st.markdown("### ⚡ Radar de Matches Inteligentes")
        st.markdown("<p style='font-size:12px; color:#9ca3af;'>Conecte-se com expositores e profissionais alinhados ao seu nicho.</p>", unsafe_allow_html=True)

        perfis_match = [
            {"nome": "Marcos Vinicius", "cargo": "Head de Inovação", "empresa": "CloudNet Brasil", "nicho": "Tecnologia & Software B2B"},
            {"nome": "Juliana Paes", "cargo": "Diretora de Contratos", "empresa": "Global Supply Ltda", "nicho": "Logística & Supply Chain"},
            {"nome": "Dr. Roberto Sampaio", "cargo": "CEO & Fundador", "empresa": "MedTech Solutions", "nicho": "Saúde & MedTech"}
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
                if st.button(f"💚 Curtir / Like", key=f"like_{p['nome']}"):
                    st.success(f"Você enviou um Like para {p['nome']}!")
            with col_m2:
                if st.button(f"🤝 Conectar (Match)", key=f"match_{p['nome']}"):
                    st.success(f"Solicitação de Match B2B enviada com sucesso para {p['nome']} via WhatsApp/LinkedIn!")

    elif aba_escolhida == "🏢 Empresas do Estande & Nichos":
        st.markdown("### 📋 Cadastro de Empresas do Estande & Nichos de Parceria")
        st.markdown("<p style='font-size:12px; color:#9ca3af;'>Cadastre sua empresa expositora ou 
