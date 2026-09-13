import streamlit as st
from streamlit_mic_recorder import mic_recorder

# Configuração da Página
st.set_page_config(
    page_title="SampaFlow - Ecossistema Inteligente",
    page_icon="⚡",
    layout="centered",
)

# Injeção de CSS Customizado (Dark Glassmorphism & Neon)
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
        font-size: 14px;
        margin-bottom: 20px;
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
    .logo-icon {
        color: #00F59B;
        font-size: 28px;
        vertical-align: middle;
    }

    .flow-ai-box {
        background: rgba(255, 255, 255, 0.03);
        border: 1px solid rgba(0, 245, 155, 0.3);
        backdrop-filter: blur(12px);
        border-radius: 16px;
        padding: 12px;
        text-align: center;
        margin-bottom: 25px;
        box-shadow: 0 0 15px rgba(0, 245, 155, 0.1);
    }
    .flow-ai-text {
        color: #00F59B;
        font-weight: 600;
        font-size: 14px;
        margin-top: 5px;
    }

    .neon-card {
        background: rgba(17, 24, 39, 0.7);
        border: 1px solid rgba(0, 245, 155, 0.4);
        backdrop-filter: blur(10px);
        border-radius: 14px;
        padding: 18px 20px;
        margin-bottom: 14px;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.4);
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
        "nome": "Geovani Maciel",
        "cargo": "CEO & Fundador",
        "linkedin": "https://linkedin.com/in/geovanimaciel",
        "bio": "Desenvolvedor de ecossistemas inteligentes em São Paulo.",
    }

if "ultimo_comando" not in st.session_state:
    st.session_state.ultimo_comando = None

# ----------------- TELA: HOME (Interface Principal) -----------------
if st.session_state.pagina_atual == "Home":

    # Barra Superior
    st.markdown(
        """
        <div class="top-bar">
            <span>Showcase</span>
            <span>📍 Jardins &nbsp; 🌧️ 21°C</span>
        </div>
    """,
        unsafe_allow_html=True,
    )

    # Logo SampaFlow
    st.markdown(
        """
        <div class="logo-container">
            <span class="logo-icon">⚡</span>
            <span class="logo-title">SAMPAFLOW</span>
        </div>
    """,
        unsafe_allow_html=True,
    )

    # Bloco Flow AI Active
    st.markdown(
        """
        <div class="flow-ai-box">
            <div style="font-size: 20px;">💬</div>
            <div class="flow-ai-text">FLOW AI ACTIVE - PRONTO PARA BUSCA</div>
        </div>
    """,
        unsafe_allow_html=True,
    )

    # ----------------- BOTÕES DE MÓDULOS -----------------

    if st.button("🤝  **SAMPA MATCH**\n\n*(Radar Biz)*", use_container_width=True):
        st.session_state.pagina_atual = "Sampa Match"
        st.rerun()

    if st.button(
        "📍  **GPS INDOOR**\n\n*(Navegar Estandes)*", use_container_width=True
    ):
        st.session_state.pagina_atual = "GPS Indoor"
        st.rerun()

    if st.button(
        "🛍️  **COMPRAS & GASTRONOMIA**\n\n*(Restaurantes, Armazéns e Lojas)*",
        use_container_width=True,
    ):
        st.session_state.pagina_atual = "Compras Dual"
        st.rerun()

    if st.button("💼  **SAMPA WORK**\n\n*(Jobs)*", use_container_width=True):
        st.session_state.pagina_atual = "Sampa Work"
        st.rerun()

    st.markdown("<br>", unsafe_allow_html=True)
    if st.button(
        "👤  **MEU PERFIL & LINKEDIN**", use_container_width=True
    ):
        st.session_state.pagina_atual = "Perfil"
        st.rerun()

    # ----------------- SEÇÃO DO FLOW AI BUTTON (VOZ) -----------------
    st.markdown("---")
    st.markdown(
        "<h4 style='color: #00F59B; text-align: center;'>🎙️ FLOW AI BUTTON (TOQUE P/ FALAR)</h4>",
        unsafe_allow_html=True,
    )
    st.markdown(
        "<p style='color: #9ca3af; text-align: center; font-size: 13px;'>Grave seu comando de voz para pesquisar restaurantes, armazéns, locais ou vagas instantaneamente.</p>",
        unsafe_allow_html=True,
    )

    # Componente de gravação de áudio do microfone
    audio_data = mic_recorder(
        start_prompt="🔴 Iniciar Gravação",
        stop_prompt="⏹️ Parar e Processar",
        key="flow_ai_mic",
    )

    if audio_data:
        st.success(
            "🎙️ Áudio capturado com sucesso! A IA (Flow AI) processou seu comando de voz."
        )
        # Simulando uma busca inteligente baseada em voz (ex: buscando armazéns ou restaurantes)
        st.session_state.ultimo_comando = (
            "Busca por comando de voz: Restaurantes e Armazéns em São Paulo"
        )
        st.session_state.pagina_atual = "Resultados Voz"
        st.rerun()

# ----------------- TELA DE RESULTADOS DA BUSCA POR VOZ -----------------
elif st.session_state.pagina_atual == "Resultados Voz":
    st.markdown(
        "<h2 style='color: #00F59B;'>🔍 Resultados da Pesquisa por Voz</h2>",
        unsafe_allow_html=True,
    )
    st.info(f"Comando interpretado: *{st.session_state.ultimo_comando}*")

    st.markdown("### 🍽️ Restaurantes e Armazéns Encontrados na Região:")

    st.markdown(
        """
        <div class="neon-card">
            <b>1. Armazém & Mercadão Gourmet Paulistano</b><br>
            <span style='color: #00D2FF;'>📍 Rua Augusta, Jardins - 350m de você</span><br>
            <p style='color: #9ca3af; font-size: 13px; margin-top: 5px;'>Especializado em queijos artesanais, embutidos e adega subterrânea.</p>
            <button style='background-color:#00F59B; color:black; border:none; padding:6px 12px; border-radius:4px; font-weight:bold;'>Iniciar Rota</button>
            <button style='background-color:#00D2FF; color:black; border:none; padding:6px 12px; border-radius:4px; font-weight:bold; margin-left:8px;'>Reservar Mesa</button>
        </div>
        
        <div class="neon-card">
            <b>2. Boteco & Vault Secreto do Chef</b><br>
            <span style='color: #00D2FF;'>📍 Vila Madalena - 1.2km de você</span><br>
            <p style='color: #9ca3af; font-size: 13px; margin-top: 5px;'>Gastronomia fusão com curadoria de pratos preditivos baseados no seu perfil.</p>
            <button style='background-color:#00F59B; color:black; border:none; padding:6px 12px; border-radius:4px; font-weight:bold;'>Iniciar Rota</button>
            <button style='background-color:#00D2FF; color:black; border:none; padding:6px 12px; border-radius:4px; font-weight:bold; margin-left:8px;'>Reservar Mesa</button>
        </div>
    """,
        unsafe_allow_html=True,
    )

    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("⬅️ Voltar ao Início"):
        st.session_state.pagina_atual = "Home"
        st.rerun()

# ----------------- TELA: PERFIL E LINKEDIN -----------------
elif st.session_state.pagina_atual == "Perfil":
    st.markdown(
        "<h2 style='color: #00F59B;'>👤 Cadastro & Perfil Profissional</h2>",
        unsafe_allow_html=True,
    )
    with st.form("form_perfil"):
        nome_input = st.text_input(
            "Seu Nome Completo", value=st.session_state.usuario_logado["nome"]
        )
        cargo_input = st.text_input(
            "Cargo / Profissão", value=st.session_state.usuario_logado["cargo"]
        )
        linkedin_input = st.text_input(
            "Link do LinkedIn", value=st.session_state.usuario_logado["linkedin"]
        )
        bio_input = st.text_area(
            "Bio / Resumo do Trabalho",
            value=st.session_state.usuario_logado["bio"],
        )
        salvar = st.form_submit_button("💾 Salvar Informações")
        if salvar:
            st.session_state.usuario_logado["nome"] = nome_input
            st.session_state.usuario_logado["cargo"] = cargo_input
            st.session_state.usuario_logado["linkedin"] = linkedin_input
            st.session_state.usuario_logado["bio"] = bio_input
            st.success("✅ Informações atualizadas com sucesso!")

    st.markdown("---")
    if st.button("⬅️ Voltar ao Início"):
        st.session_state.pagina_atual = "Home"
        st.rerun()

# ----------------- OUTRAS TELAS DE MÓDULOS -----------------
elif st.session_state.pagina_atual == "Sampa Match":
    st.markdown(
        "<h2 style='color: #00F59B;'>🤝 Sampa Match (Radar Biz)</h2>",
        unsafe_allow_html=True,
    )
    st.info(
        f"Perfil Ativo: **{st.session_state.usuario_logado['nome']}** | 🔗 [LinkedIn]({st.session_state.usuario_logado['linkedin']})"
    )
    if st.button("⬅️ Voltar ao Início"):
        st.session_state.pagina_atual = "Home"
        st.rerun()

elif st.session_state.pagina_atual == "GPS Indoor":
    st.markdown(
        "<h2 style='color: #00D2FF;'>📍 GPS Indoor & Mapeamento 3D</h2>",
        unsafe_allow_html=True,
    )
    st.success("Destino atual: **BOOTH B42: TechInnovate Global**")
    if st.button("⬅️ Voltar ao Início"):
        st.session_state.pagina_atual = "Home"
        st.rerun()

elif st.session_state.pagina_atual == "Compras Dual":
    st.markdown(
        "<h2 style='color: #00F59B;'>🛍️ Compras & Gastronomia</h2>",
        unsafe_allow_html=True,
    )
    st.write(
        "Explore armazéns, restaurantes, vaults subterrâneos e rotas customizadas em São Paulo."
    )
    if st.button("⬅️ Voltar ao Início"):
        st.session_state.pagina_atual = "Home"
        st.rerun()

elif st.session_state.pagina_atual == "Sampa Work":
    st.markdown(
        "<h2 style='color: #00D2FF;'>💼 Sampa Work (Vagas & Jobs)</h2>",
        unsafe_allow_html=True,
    )
    st.write("• **Concierge de Luxo** - Hotel Fasano Jardins (R$ 12.000/mês)")
    if st.button("⬅️ Voltar ao Início"):
        st.session_state.pagina_atual = "Home"
        st.rerun()
