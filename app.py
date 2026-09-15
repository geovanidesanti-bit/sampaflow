import streamlit as st
from streamlit_mic_recorder import mic_recorder

# Configuração da Página
st.set_page_config(
    page_title="SampaFlow - Ecossistema Inteligente",
    page_icon="⚡",
    layout="centered",
)

# Injeção de CSS Customizado - Dark Glassmorphism com Fundo Urbano Tático
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

def render_top_bar(titulo_pagina="SampaFlow"):
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
        resposta_texto = "✨ [Flow AI Command Processed]: Sincronização de pavilhões, leads B2B e painel de motoristas processados via inteligência preditiva."
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
# TELA 1: HOME - HUB DE EVENTOS E TODOS OS MÓDULOS
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

    # Atalhos rápidos de acesso
    col_u1, col_u2 = st.columns(2)
    with col_u1:
        if st.button("🚗 Portal do Motorista", use_container_width=True):
            st.session_state.pagina_atual = "Portal Motorista"
            st.rerun()
    with col_u2:
        if st.button("👤 Cadastro / Perfil LinkedIn", use_container_width=True):
            st.session_state.pagina_atual = "Cadastro Usuario"
            st.rerun()

    st.markdown("### 🏛️ Grandes Pavilhões & Feiras de São Paulo")

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
        if st.button(f"🚀 Entrar no Ecossistema: {ev['pavilhao']}", key=f"btn_{ev['id']}", use_container_width=True):
            st.session_state.evento_selecionado = ev
            st.session_state.pagina_atual = "Dashboard Evento"
            st.rerun()

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
        st.markdown("<p style='font-size:12px; color:#9ca3af;'>Cadastre sua empresa expositora ou busque parcerias contratuais por nicho específico.</p>", unsafe_allow_html=True)

        with st.form("form_cad_empresa_estande"):
            nome_empresa = st.text_input("Nome da Empresa Expositora", "Ex: TechInnovate Pavilhão A")
            nicho_alvo = st.selectbox("Nicho Específico para Contratos", ["Tecnologia", "Logística", "Saúde", "Varejo", "Energia"])
            descricao_parceria = st.text_area("O que sua empresa busca em parcerias B2B?", "Ex: Buscamos fornecedores de software em nuvem e integradores de logística...")
            btn_pub_empresa = st.form_submit_button("✨ Publicar Empresa no Estande")
            if btn_pub_empresa:
                st.success(f"Empresa '{nome_empresa}' cadastrada com sucesso no diretório do pavilhão!")

        st.markdown("---")
        st.markdown("#### 🔍 Empresas Exibidoras Cadastradas no Pavilhão")
        st.markdown("""
        * **TechInnovate Cloud** (Tecnologia) — *Busca integradores B2B*
        * **Sampa Cargo Express** (Logística) — *Busca armazéns e frotas parceiras*
        * **MedTech Diagnósticos** (Saúde) — *Busca hospitais e clínicas*
        """)

    elif aba_escolhida == "📸 Publicações & Feed":
        st.markdown("### 📸 Feed de Fotos & Momentos do Evento")
        
        if st.session_state.usuario_logado and st.session_state.dados_usuario["tipo"] == "Exibidor / Empresa no Estande":
            with st.form("form_post_feed"):
                legenda_foto = st.text_input("Escreva uma legenda para sua publicação", "Visite nosso estande no pavilhão principal!")
                foto_feed = st.file_uploader("Enviar Foto do Estande / Novidade", type=["png", "jpg", "jpeg"])
                enviar_post = st.form_submit_button("🚀 Publicar no Feed do Evento")
                if enviar_post:
                    st.success("📸 Foto publicada com sucesso no feed geral!")
        else:
            st.info("💡 Apenas usuários cadastrados como **Exibidor / Empresa no Estande** podem publicar fotos oficiais no feed. Visitantes podem interagir e dar likes.")

        st.markdown("---")
        st.markdown(
            """
            <div class="neon-card">
                <div style="color: #00F59B; font-weight: bold; font-size: 13px;">🏢 TechInnovate Cloud <span style="color:#9ca3af; font-size:11px;">(Exibidor)</span></div>
                <p style="font-size: 12px; color: #d1d5db; margin-top: 4px;">Lançamento oficial da nossa plataforma de IA no Expo Center Norte! Venha conferir o estande 42.</p>
                <div style="background: rgba(0,213,255,0.05); height: 100px; border-radius: 8px; text-align: center; padding-top: 35px; color: #00D2FF; font-size: 12px; border: 1px dashed rgba(0,213,255,0.3); margin-top: 8px;">
                    🖼️ [Foto Oficial do Estande Carregada]
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("⬅️ Voltar aos Pavilhões", use_container_width=True):
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
# TELA 5: GPS INDOOR
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
# TELA 6: COMPRAS & GASTRONOMIA
# ---------------------------------------------------------
elif st.session_state.pagina_atual == "Compras Dual":
    render_top_bar("GASTRONOMIA & RESTAURANTES")

    horarios_disponiveis = ["18:30", "19:00", "19:30", "20:00", "20:30", "21:00", "21:30", "22:00"]

    st.markdown(
        """
        <div class="neon-card">
            <div style="color: #00F59B; font-weight: bold; font-size: 16px;">☕ Café Girondino</div>
            <div style="color: #f3f4f6; font-size: 13px; margin: 4px 0;">⭐ <b>Nota: 4.9</b> &nbsp;|&nbsp; 📍 Rua Boa Vista, 365 — Centro &nbsp;|&nbsp; 🕒 <b>RTC: 12 min</b></div>
            <p style="color: #d1d5db; font-size: 12px; line-height: 1.4; margin-top: 6px;">Café histórico tradicional com curadoria de áudio imersiva ativa.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    horario_gir = st.selectbox("Selecione o Horário (Café Girondino)", horarios_disponiveis, key="sel_gir")
    if st.button(f"🍽️ Reservar para às {horario_gir} (Café Girondino)", key="res_gir", use_container_width=True):
        st.success(f"Mesa confirmada no Café Girondino para às {horario_gir}!")

    st.markdown(
        """
        <div class="neon-card" style="margin-top: 20px;">
            <div style="color: #00F59B; font-weight: bold; font-size: 16px;">🍷 The Sãopaulista Undercurrent</div>
            <div style="color: #f3f4f6; font-size: 13px; margin: 4px 0;">⭐ <b>Nota: 4.8</b> &nbsp;|&nbsp; 📍 Al. dos Anapurus, 1430 — Jardins &nbsp;|&nbsp; 🕒 <b>RTC: 8 min</b></div>
            <p style="color: #d1d5db; font-size: 12px; line-height: 1.4; margin-top: 6px;">A hidden vault born from a forgotten coffee-baron catacomb.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    horario_vault = st.selectbox("Selecione o Horário (The Sãopaulista)", horarios_disponiveis, key="sel_vault")
    if st.button(f"🍽️ Reservar para às {horario_vault} no Vault", key="res_vault", use_container_width=True):
        st.success(f"Mesa confirmada no The Sãopaulista Undercurrent para às {horario_vault}!")

    st.markdown(
        """
        <div class="neon-card" style="margin-top: 20px;">
            <div style="color: #00F59B; font-weight: bold; font-size: 16px;">🥩 Figueira Rubaiyat</div>
            <div style="color: #f3f4f6; font-size: 13px; margin: 4px 0;">⭐ <b>Nota: 4.9</b> &nbsp;|&nbsp; 📍 R. Haddock Lobo, 1738 — Jardins &nbsp;|&nbsp; 🕒 <b>RTC: 15 min</b></div>
            <p style="color: #d1d5db; font-size: 12px; line-height: 1.4; margin-top: 6px;">Gastronomia de alta classe integrada ao ecossistema executivo.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    horario_fig = st.selectbox("Selecione o Horário (Figueira Rubaiyat)", horarios_disponiveis, key="sel_fig")
    if st.button(f"🍽️ Reservar para às {horario_fig} (Figueira)", key="res_fig", use_container_width=True):
        st.success(f"Mesa confirmada na Figueira Rubaiyat para às {horario_fig}!")

    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("⬅️ Voltar ao Início", use_container_width=True):
        st.session_state.pagina_atual = "Home"
        st.rerun()

    render_flow_ai_footer()

# ---------------------------------------------------------
# TELA 7: SAMPA WORK
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

# ---------------------------------------------------------
# TELA 8: PORTAL DO MOTORISTA
# ---------------------------------------------------------
elif st.session_state.pagina_atual == "Portal Motorista":
    render_top_bar("Portal do Motorista SampaDrive")

    st.markdown(
        """
        <div class="neon-card-cyan">
            <div style="color: #00D2FF; font-weight: bold; font-size: 15px; margin-bottom: 6px;">🚗 CADASTRO & PAINEL DE MOTORISTA EXECUTIVO</div>
            <p style="font-size: 13px; color: #d1d5db;">Cadastre sua foto, documento do veículo e CNH em PDF. Após validação instantânea, fique online para aceitar corridas com taxa fixa de 10%.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    if not st.session_state.motorista_logado:
        with st.form("form_cad_motorista"):
            st.markdown("### Credenciamento de Motorista")
            nome_mot = st.text_input("Nome Completo do Motorista", "Carlos Silva")
            tel_mot = st.text_input("Telefone / WhatsApp", "(11) 98888-7777")
            modelo_carro = st.text_input("Modelo e Placa do Veículo", "Toyota Corolla Prata — ABC-1234")
            
            foto_mot = st.file_uploader("📸 Foto de Perfil do Motorista", type=["png", "jpg", "jpeg"])
            doc_carro = st.file_uploader("📄 Documento do Carro (CRLV em PDF)", type=["pdf"])
            cnh_pdf = st.file_uploader("📄 CNH em PDF", type=["pdf"])
            
            btn_cad_mot = st.form_submit_button("🚀 Enviar Documentos para Aprovação")
            if btn_cad_mot:
                st.session_state.motorista_logado = True
                st.session_state.dados_motorista = {
                    "nome": nome_mot,
                    "carro": modelo_carro,
                    "saldo_pix": 50.00,
                    "faturamento_total": 0.00
                }
                st.success("🎉 Cadastro aprovado automaticamente pela IA! Você já está liberado para ficar online.")
                st.rerun()
    else:
        mot = st.session_state.dados_motorista
        st.markdown(
            f"""
            <div style="background: rgba(0,245,155,0.08); padding: 15px; border-radius: 12px; border: 1px solid rgba(0,245,155,0.4); margin-bottom: 15px;">
                <b style="color: #00F59B;">Status:</b> ✅ Online & Ativo<br>
                <b>Motorista:</b> {mot['nome']} ({mot['carro']})<br>
                <b>Faturamento Total em Corridas:</b> R$ {mot['faturamento_total']:.2f}<br>
                <b>Taxa da Plataforma (10%):</b> R$ {mot['faturamento_total'] * 0.10:.2f}<br>
                <b>Saldo de Recarga Pix:</b> R$ {mot['saldo_pix']:.2f}
            </div>
            """,
            unsafe_allow_html=True,
        )

        st.markdown("### 💰 Recarga de Saldo via Pix (Taxa de Corridas)")
        st.markdown("<p style='font-size:12px; color:#9ca3af;'>Gere seu Pix instantâneo para manter o saldo de repasse das taxas de 10% (ex: se faturar R$ 500, a taxa de 10% é R$ 50).</p>", unsafe_allow_html=True)

        valor_recarga = st.number_input("Valor da Recarga Pix (R$)", min_value=10.0, max_value=500.0, value=50.0, step=10.0)
        if st.button("📱 Gerar QR Code Pix", use_container_width=True):
            st.markdown(
                f"""
                <div style="background: rgba(0,213,255,0.08); border: 1px solid rgba(0,213,255,0.5); padding: 15px; border-radius: 10px; text-align: center; margin-top: 10px;">
                    <b style="color: #00D2FF;">📱 QR Code Pix Gerado com Sucesso!</b><br>
                    <span style="font-size: 13px; color: #f3f4f6;">Valor: <b>R$ {valor_recarga:.2f}</b></span><br>
                    <code style="background: #000; padding: 4px 8px; border-radius: 4px; font-size: 11px; display: block; margin-top: 8px;">00020126580014br.gov.bcb.pix...sampaflow-recarga-pix</code>
                    <span style="font-size: 11px; color: #00F59B; margin-top: 6px; display: block;">🟢 Pagamento aprovado instantaneamente! Saldo atualizado.</span>
                </div>
                """,
                unsafe_allow_html=True,
            )
            st.session_state.dados_motorista["saldo_pix"] += valor_recarga

        st.markdown("---")
        st.markdown("### 🚘 Simulação de Corrida Recebida")
        if st.button("Simular Nova Corrida (Ex: Expo Center Norte ➔ Jardins)", use_container_width=True):
            valor_corrida = 80.00
            taxa_devida = valor_corrida * 0.10
            st.success(f"🛎️ Corrida Aceita!\n\n**Destino:** Jardins / Hotel Fasano\n**Valor da Corrida:** R$ {valor_corrida:.2f}\n**Taxa da Plataforma (10%):** R$ {taxa_devida:.2f}\n\n*O saldo foi debitado da sua carteira e o faturamento atualizado.*")
            st.session_state.dados_motorista["faturamento_total"] += valor_corrida

    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("⬅️ Voltar ao Início", use_container_width=True):
        st.session_state.pagina_atual = "Home"
        st.rerun()

    render_flow_ai_footer()
