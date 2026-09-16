import streamlit as st
from streamlit_mic_recorder import mic_recorder
from datetime import datetime
import random
import string

# Configuração da Página
st.set_page_config(
    page_title="SampaFlow - Ecossistema Inteligente",
    page_icon="⚡",
    layout="centered",
)

# --- INICIALIZAÇÃO SEGURA DE VARIÁVEIS DE SESSÃO ---
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
        "empresa": "Samsung Brasil",
        "estande": "Estande 12 — Pavilhão Transamérica",
        "produto_destaque": "Smartphone Samsung Galaxy (Novidade)",
        "estrelas": "⭐ 5.0 (48 avaliações)"
    }

if "dados_motorista" not in st.session_state:
    st.session_state.dados_motorista = {
        "nome": "Geovani Santi",
        "carro": "Renault Kwid Zen 2020 Prata",
        "placa": "ABC-1D23",
        "saldo_pix": 180.50,
        "faturamento_total": 540.00,
        "corridas_realizadas": 14,
        "avaliacao": "⭐ 4.92 (312 avaliações)"
    }

if "evento_selecionado" not in st.session_state:
    st.session_state.evento_selecionado = {
        "pavilhao": "Transamérica Expo Center",
        "nome": "Sampa Tech & Mobile Summit 2026",
        "tipo": "Feira de Tecnologia & Eletrônicos B2B",
        "data": "15 a 18 de Setembro de 2026",
        "desc": "O maior evento de inovação mobile e lançamentos de dispositivos da América Latina.",
        "empresas_cadastradas": 340,
        "pessoas_trabalhando": 1250,
        "visitantes_online": 8420
    }

if "cupom_gerado" not in st.session_state:
    st.session_state.cupom_gerado = None

# Injeção de CSS Customizado - Dark Glassmorphism & Radar Style
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
        animation: marquee 26s linear infinite;
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

    .waze-radar-box {
        background: radial-gradient(circle, rgba(0,213,255,0.12) 0%, rgba(5,8,14,0.95) 80%);
        border: 1px solid rgba(0, 213, 255, 0.6);
        border-radius: 16px;
        padding: 20px;
        text-align: center;
        position: relative;
        overflow: hidden;
        margin-bottom: 15px;
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

# --- MENU LATERAL DE SEGURANÇA ---
with st.sidebar:
    st.markdown("### ⚡ Navegação SampaFlow")
    if st.button("🏠 Voltar ao Hub Central", use_container_width=True, key="sb_home"):
        st.session_state.pagina_atual = "Home"
        st.rerun()
    if st.button("🍷 Sampa Date", use_container_width=True, key="sb_date"):
        st.session_state.pagina_atual = "Sampa Date"
        st.rerun()
    if st.button("🚀 Painel do Evento", use_container_width=True, key="sb_evento"):
        st.session_state.pagina_atual = "Dashboard Evento"
        st.rerun()
    if st.button("🤝 Sampa Match / Meet", use_container_width=True, key="sb_match"):
        st.session_state.pagina_atual = "Sampa Match Geral"
        st.rerun()
    if st.button("🚗 Portal do Motorista", use_container_width=True, key="sb_motorista"):
        st.session_state.pagina_atual = "Portal Motorista"
        st.rerun()
    if st.button("📍 GPS Indoor", use_container_width=True, key="sb_gps"):
        st.session_state.pagina_atual = "GPS Indoor"
        st.rerun()
    if st.button("🛍️ Gastronomia & Cupons", use_container_width=True, key="sb_gast"):
        st.session_state.pagina_atual = "Compras Dual"
        st.rerun()
    if st.button("🎭 Passeios & Cultura", use_container_width=True, key="sb_cult"):
        st.session_state.pagina_atual = "Passeios e Cultura"
        st.rerun()
    if st.button("✏️ Editar Perfil", use_container_width=True, key="sb_perfil"):
        st.session_state.pagina_atual = "Cadastro Usuario"
        st.rerun()
    st.markdown("---")
    st.caption("SampaFlow v2.9 • SP 2026")

def gerar_resposta_ia_contextual(pagina, input_usuario=""):
    if pagina == "Home":
        return "🤖 [Flow AI]: Hub central operando em capacidade máxima. São Paulo com 22°C e clima excelente!"
    elif pagina == "Sampa Date":
        return "🤖 [Flow AI]: Roteiro gastronômico cruzado com sucesso. Famiglia Mancini na Rua Avanhandava é a escolha ideal para hoje."
    elif pagina == "Dashboard Evento":
        return "🤖 [Flow AI]: Transamérica Expo Center ao vivo: Fluxo intenso e 8.420 visitantes ativos circulando nos corredores."
    elif pagina == "Sampa Match Geral":
        return "🤖 [Flow AI]: Sampa Match ativo! Detectados executivos com alta sinergia comercial no seu setor."
    elif pagina == "Portal Motorista":
        return "🤖 [Flow AI]: Radar de mobilidade ativado: Alta concentração de chamadas saindo do Transamérica e polos corporativos com tarifa dinâmica."
    elif pagina == "Passeios e Cultura":
        return "🤖 [Flow AI]: Dicas culturais carregadas: Parques abertos, exposições noturnas no MASP e Pinacoteca selecionadas para aproveitar os 22°C."
    else:
        return f"🤖 [Flow AI]: Sincronização realizada para '{pagina}'."

def render_top_bar(titulo_pagina="SampaFlow"):
    st.markdown(
        """
        <div class="ticker-container">
            <div class="ticker-text">
                ⚡ SampaFlow Info: São Paulo • 15 de Setembro de 2026 • 🌙 22°C • Noite Agradável • Transamérica Expo Center com 8.420 visitantes ativos • 10% OFF em restaurantes parceiros! 🍷✨
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.markdown(
        f"""
        <div class="top-bar">
            <span>⚡ SampaFlow &nbsp;|&nbsp; <b>{titulo_pagina}</b></span>
            <span>📍 São Paulo &nbsp; 🌙 22°C</span>
        </div>
        """,
        unsafe_allow_html=True,
    )

def render_flow_ai_footer():
    st.markdown("---")
    audio_gravado = mic_recorder(
        start_prompt="🔴 Iniciar Gravação de Voz (IA Real)",
        stop_prompt="⏹️ Processar Comando de Voz",
        key=f"mic_{st.session_state.pagina_atual}",
    )
    
    if audio_gravado:
        resposta_texto = gerar_resposta_ia_contextual(st.session_state.pagina_atual, "Comando de voz")
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
                    <b>{ultima["resposta"]}</b>
                </div>
                """,
                unsafe_allow_html=True,
            )

# --- ROTEADOR DE PÁGINAS ---
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
                <div style="color: #f3f4f6; font-size: 12px; margin-top: 2px;">{user['cargo']} • <b>{user['empresa']}</b></div>
                <div style="color: #00D2FF; font-size: 11px; margin-top: 2px;">📍 {user['estande']}</div>
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
        if st.button("🚗 Portal do Motorista", use_container_width=True, key="btn_h_mot"):
            st.session_state.pagina_atual = "Portal Motorista"
            st.rerun()
    with col_u2:
        if st.button("✏️ Editar Perfil", use_container_width=True, key="btn_h_cad"):
            st.session_state.pagina_atual = "Cadastro Usuario"
            st.rerun()

    st.markdown("### 🏛️ Menu Principal & Novidades")
    if st.button("🍷 SAMPA DATE — O Guia do Encontro", use_container_width=True, key="btn_h_date"):
        st.session_state.pagina_atual = "Sampa Date"
        st.rerun()
    if st.button("🚀 Painel do Evento (Transamérica ao Vivo)", use_container_width=True, key="btn_h_ev"):
        st.session_state.pagina_atual = "Dashboard Evento"
        st.rerun()

    st.markdown("### 🌐 Outros Módulos & Inteligência Urbana")
    if st.button("🤝 SAMPA MATCH / MEET — Radar B2B", use_container_width=True, key="btn_h_match"):
        st.session_state.pagina_atual = "Sampa Match Geral"
        st.rerun()
    if st.button("📍 GPS INDOOR — Mapa Tático", use_container_width=True, key="btn_h_gps"):
        st.session_state.pagina_atual = "GPS Indoor"
        st.rerun()
    if st.button("🛍️ GASTRONOMIA — 300 Restaurantes (10% OFF)", use_container_width=True, key="btn_h_gast"):
        st.session_state.pagina_atual = "Compras Dual"
        st.rerun()
    if st.button("🎭 PASSEIOS & CULTURA — O que fazer em SP", use_container_width=True, key="btn_h_cult"):
        st.session_state.pagina_atual = "Passeios e Cultura"
        st.rerun()

    render_flow_ai_footer()

elif pagina == "Sampa Date":
    render_top_bar("Sampa Date — O Guia do Encontro Perfeito")
    
    st.markdown(
        """
        <div class="neon-card">
            <div style="color: #00F59B; font-weight: bold; font-size: 16px;">🍷 Planeje o Date Perfeito sem Errar e sem Surpresas!</div>
            <p style="font-size: 12px; color: #d1d5db; margin-top: 6px; line-height: 1.4;">
                Está fazendo <b>22°C</b> agora à noite em São Paulo — uma temperatura deliciosa para sair! Conte para o nosso assistente como é a sua companhia, o estilo dela e o que ela gosta. O SampaFlow vai indicar o restaurante sob medida, os pratos de maior sucesso e o *gasto médio estimado para o casal*.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    with st.form("form_sampa_date"):
        st.markdown("#### 📝 Descreva a sua companhia para a IA calibrar o local:")
        estilo_parceira = st.selectbox(
            "1. Como ela se veste / Qual o estilo predominante?",
            [
                "Elegante / Sofisticada (Gosta de lugares refinados)",
                "Casual / Descontraída (Ambientes rústicos e aconchegantes)",
                "Moderna / Alternativa (Bares descolados e conceituais)",
                "Romântica / Clássica (Luz de velas e boa música)"
            ]
        )
        
        experiencia_previa = st.selectbox(
            "2. Ela já conhece os clássicos tradicionais de São Paulo (Ex: Bixiga / Centro)?",
            [
                "Nunca foi / Pouco hábito com os clássicos tradicionais",
                "Já conhece alguns pontos turísticos principais",
                "É apaixonada pela história e gastronomia paulistana"
            ]
        )

        tipo_cozinha_date = st.selectbox(
            "3. Qual culinária tem mais a ver com a ocasião de hoje?",
            [
                "Italiana Tradicional & Massas Artesanais (Ex: Famiglia Mancini)",
                "Bistrô Francês & Vinhos Selecionados",
                "Japonesa Contemporânea & Drinks de Autor",
                "Culinária Contemporânea Paulista"
            ]
        )

        btn_gerar_date = st.form_submit_button("✨ Revelar a Sugestão Perfeita para o Date")

    if btn_gerar_date or st.session_state.get("sugeriu_date", False):
        st.session_state.sugeriu_date = True
        st.markdown("---")
        st.markdown("### 🏆 Sugestão Exclusiva do SampaFlow:")
        
        st.markdown(
            """
            <div class="neon-card-cyan" style="border: 1px solid #00F59B;">
                <div style="color: #00F59B; font-weight: bold; font-size: 16px;">🍝 Destino Sugerido: Famiglia Mancini (Bela Vista)</div>
                <div style="color: #00D2FF; font-size: 13px; margin: 4px 0;">📍 <b>Endereço:</b> Rua Avanhandava, 81 — Centro, São Paulo</div>
                <div style="color: #ffffff; font-size: 13px; margin-top: 8px;"><b>🌡️ Clima no Momento:</b> 22°C (Perfeito para caminhar pela iluminação charmosa da Rua Avanhandava).</div>
                
                <div style="background: rgba(0,245,155,0.1); border: 1px solid rgba(0,245,155,0.4); border-radius: 10px; padding: 12px; margin-top: 12px;">
                    <span style="color: #00F59B; font-weight: bold; font-size: 14px;">💰 Previsão Real de Gastos para o Casal:</span><br>
                    <span style="color: #ffffff; font-size: 13px;">Média de <b>R$ 220 a R$ 320</b> (Inclui couvert renomado, prato principal para compartilhar e bebidas).</span>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        if st.button("🎁 Gerar Cupom de 10% OFF para o Restaurante", key="btn_cupom_date"):
            hash_date = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
            st.session_state.cupom_gerado = f"SAMPA-DATE-{hash_date}-10OFF"
            st.success(f"Cupom gerado com sucesso: {st.session_state.cupom_gerado} (Apresente no estabelecimento parceiro)")

    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("⬅️ Voltar ao Início", use_container_width=True, key="btn_back_date"):
        st.session_state.pagina_atual = "Home"
        st.rerun()
    render_flow_ai_footer()

elif pagina == "Dashboard Evento":
    ev = st.session_state.evento_selecionado
    render_top_bar(ev['pavilhao'])
    
    st.markdown(
        f"""
        <div class="neon-card">
            <div style="color: #00F59B; font-weight: bold; font-size: 18px;">🏢 {ev['nome']}</div>
            <div style="color: #00D2FF; font-size: 13px; margin-top: 4px;">📍 {ev['pavilhao']} • {ev['data']}</div>
            <p style="color: #d1d5db; font-size: 12px; margin-top: 8px; line-height: 1.4;">{ev['desc']}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("### 📊 Indicadores em Tempo Real (Transamérica Online)")
    
    col_e1, col_e2, col_e3 = st.columns(3)
    with col_e1:
        st.markdown(
            f"""
            <div class="neon-card-cyan" style="text-align: center; padding: 12px;">
                <div style="color: #9ca3af; font-size: 11px;">EMPRESAS</div>
                <div style="color: #00F59B; font-size: 22px; font-weight: bold;">{ev['empresas_cadastradas']}</div>
                <div style="color: #00D2FF; font-size: 10px;">Expositores Ativos</div>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with col_e2:
        st.markdown(
            f"""
            <div class="neon-card-cyan" style="text-align: center; padding: 12px;">
                <div style="color: #9ca3af; font-size: 11px;">EQUIPE & STAFF</div>
                <div style="color: #00F59B; font-size: 22px; font-weight: bold;">{ev['pessoas_trabalhando']}</div>
                <div style="color: #00D2FF; font-size: 10px;">Trabalhando no Pavilhão</div>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with col_e3:
        st.markdown(
            f"""
            <div class="neon-card-cyan" style="text-align: center; padding: 12px;">
                <div style="color: #9ca3af; font-size: 11px;">VISITANTES</div>
                <div style="color: #00F59B; font-size: 22px; font-weight: bold;">{ev['visitantes_online']}</div>
                <div style="color: #00D2FF; font-size: 10px;">Online Circulando</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown(
        """
        <div class="neon-card">
            <div style="color: #00F59B; font-weight: bold; font-size: 14px;">🔥 Destaque do Estande Atual</div>
            <div style="color: #ffffff; font-size: 13px; margin-top: 6px;">
                <b>Estande 12 — Samsung Brasil:</b> Fluxo intenso de visitantes interessados no ecossistema de smartphones e integração mobile corporativa.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    if st.button("⬅️ Voltar ao Início", use_container_width=True, key="btn_back_ev"):
        st.session_state.pagina_atual = "Home"
        st.rerun()
    render_flow_ai_footer()

elif pagina == "Sampa Match Geral":
    render_top_bar("SAMPA MATCH / MEET — Networking B2B")
    
    st.markdown(
        """
        <div class="neon-card">
            <div style="color: #00F59B; font-weight: bold; font-size: 16px;">🤝 Conexões Inteligentes em Grandes Feiras</div>
            <p style="font-size: 12px; color: #d1d5db; margin-top: 6px; line-height: 1.4;">
                O Sampa Match cruza o seu perfil profissional com o de outros decisores presentes no Transamérica Expo Center. Conecte-se, troque contatos e agende cafés de negócios instantaneamente.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("### 👥 Perfis com Sinergia Próximos de Você:")
    
    matches = [
        {"nome": "Ana Mendes", "cargo": "Head de Parcerias", "empresa": "Samsung Partner", "estande": "Estande 15", "status": "Próximo (15m)"},
        {"nome": "Carlos Eduardo", "cargo": "Diretor de Tecnologia", "empresa": "Inovação SP Tech", "estande": "Estande 22", "status": "Reunião Livre às 14h"},
        {"nome": "Juliana Lima", "cargo": "Gerente de Expansão", "empresa": "Varejo Inteligente Brasil", "estande": "Estande 08", "status": "Online no Pavilhão"}
    ]

    for m in matches:
        st.markdown(
            f"""
            <div class="neon-card-cyan">
                <div style="color: #00F59B; font-weight: bold; font-size: 14px;">{m['nome']} ({m['cargo']})</div>
                <div style="color: #f3f4f6; font-size: 12px; margin-top: 2px;">🏢 <b>{m['empresa']}</b> • 📍 {m['estande']}</div>
                <div style="color: #00D2FF; font-size: 11px; margin-top: 4px;">📡 Status: <b>{m['status']}</b></div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    if st.button("☕ Agendar Café / Conexão Rápida", key="btn_cafe_match"):
        st.success("Convite de networking enviado com sucesso para a rede de parceiros no evento!")

    if st.button("⬅️ Voltar ao Início", use_container_width=True, key="btn_back_match"):
        st.session_state.pagina_atual = "Home"
        st.rerun()
    render_flow_ai_footer()

elif pagina == "GPS Indoor":
    render_top_bar("GPS INDOOR & Mapa Tático")
    st.markdown(
        """
        <div class="waze-radar-box">
            <div style="color: #00D2FF; font-weight: bold; font-size: 16px;">🗺️ Navegação Interna — Transamérica Expo Center</div>
            <p style="color: #9ca3af; font-size: 12px; margin-top: 8px;">
                Sua localização atual: <b>Estande 12 (Corredor Principal B)</b>.<br>
                Tráfego de visitantes no setor: <b>Alto / Fluido</b>.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    
    st.markdown("### 📍 Pontos de Interesse Próximos:")
    st.markdown(
        """
        <div class="neon-card">
            <div style="color: #00F59B; font-weight: bold;">☕ Lounge VIP de Cafés & Networking</div>
            <div style="color: #d1d5db; font-size: 12px;">A apenas 30 metros à sua esquerda (Corredor B).</div>
        </div>
        <div class="neon-card">
            <div style="color: #00F59B; font-weight: bold;">🚻 Sanitários & Central de Atendimento</div>
            <div style="color: #d1d5db; font-size: 12px;">Localizados na Ala Norte do Pavilhão.</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    if st.button("⬅️ Voltar ao Início", use_container_width=True, key="btn_back_gps"):
        st.session_state.pagina_atual = "Home"
        st.rerun()
    render_flow_ai_footer()

elif pagina == "Compras Dual":
    render_top_bar("Gastronomia & Compras — 10% OFF")
    st.markdown(
        """
        <div class="neon-card">
            <div style="color: #00F59B; font-weight: bold; font-size: 16px;">🛍️ Rede de Descontos Exclusivos em São Paulo</div>
            <p style="font-size: 12px; color: #d1d5db; margin-top: 6px;">
                Explore centenas de restaurantes parceiros nos principais polos gastronômicos (Itaim Bibi, Pinheiros, Jardins e Centro) com cupons instantâneos de 10% OFF.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    restaurantes_parceiros = [
        {"nome": "Fasano (Jardins)", "culinaria": "Italiana Alta Gastronomia", "desconto": "10% OFF com SampaFlow"},
        {"nome": "A Casa do Porco (Centro)", "culinaria": "Culinária Brasileira Premiada", "desconto": "10% OFF na Fila Preferencial"},
        {"nome": "Rubaiyat (Itaim Bibi)", "culinaria": "Carnes Nobres & Cortes Especiais", "desconto": "10% OFF no Almoço Executivo"}
    ]

    for r in restaurantes_parceiros:
        st.markdown(
            f"""
            <div class="neon-card-cyan">
                <div style="color: #00F59B; font-weight: bold; font-size: 14px;">🍽️ {r['nome']}</div>
                <div style="color: #f3f4f6; font-size: 12px; margin-top: 2px;">{r['culinaria']}</div>
                <div style="color: #00D2FF; font-size: 11px; margin-top: 4px;">🏷️ <b>{r['desconto']}</b></div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    if st.button("⬅️ Voltar ao Início", use_container_width=True, key="btn_back_gast"):
        st.session_state.pagina_atual = "Home"
        st.rerun()
    render_flow_ai_footer()

elif pagina == "Passeios e Cultura":
    render_top_bar("Passeios & Cultura — O que fazer em SP")
    st.markdown(
        """
        <div class="neon-card">
            <div style="color: #00F59B; font-weight: bold; font-size: 16px;">🎭 Roteiros Culturais, Parques e Museus em SP</div>
            <p style="font-size: 12px; color: #d1d5db; margin-top: 6px; line-height: 1.4;">
                Aproveite o melhor de São Paulo com sugestões baseadas no clima atual (<b>22°C</b>) e na sua localização próxima aos grandes centros de inovação e lazer.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("### 🌳 Parques & Áreas Verdes Recomendados")
    st.markdown(
        """
        <div class="neon-card-cyan">
            <div style="color: #00F59B; font-weight: bold; font-size: 14px;">🌿 Parque Ibirapuera</div>
            <div style="color: #f3f4f6; font-size: 12px; margin-top: 2px;">O coração verde de São Paulo. Ótimo para caminhadas ao anoitecer, contemplação do Planetário e arquitetura de Oscar Niemeyer.</div>
        </div>
        <div class="neon-card-cyan">
            <div style="color: #00F59B; font-weight: bold; font-size: 14px;">🌳 Parque Villa-Lobos (Zona Oeste)</div>
            <div style="color: #f3f4f6; font-size: 12px; margin-top: 2px;">Excelente infraestrutura para ciclovias, patins e apresentações ao ar livre na concha acústica.</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("### 🏛️ Museus & Exposições em Destaque")
    st.markdown(
        """
        <div class="neon-card-cyan">
            <div style="color: #00F59B; font-weight: bold; font-size: 14px;">🖼️ MASP (Museu de Arte de São Paulo) — Av. Paulista</div>
            <div style="color: #f3f4f6; font-size: 12px; margin-top: 2px;">Famoso pelos cavaletes de vidro e acervo internacional de grandes mestres da pintura. Aberto até mais tarde em dias úteis selecionados.</div>
        </div>
        <div class="neon-card-cyan">
            <div style="color: #00F59B; font-weight: bold; font-size: 14px;">🏛️ Pinacoteca de São Paulo (Praça da Luz)</div>
            <div style="color: #f3f4f6; font-size: 12px; margin-top: 2px;">O museu de arte mais antigo da capital, reunindo esculturas e pinturas históricas em um prédio deslumbrante de tijolos à vista.</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    if st.button("⬅️ Voltar ao Início", use_container_width=True, key="btn_back_cult"):
        st.session_state.pagina_atual = "Home"
        st.rerun()
    render_flow_ai_footer()

elif pagina == "Cadastro Usuario":
    render_top_bar("Editar Perfil Profissional")
    with st.form("form_cad"):
        nome_input = st.text_input("Nome Completo", st.session_state.dados_usuario["nome"])
        cargo_input = st.text_input("Cargo", st.session_state.dados_usuario["cargo"])
        empresa_input = st.text_input("Empresa", st.session_state.dados_usuario["empresa"])
        estande_input = st.text_input("Estande", st.session_state.dados_usuario["estande"])
        
        if st.form_submit_button("✅ Salvar Alterações"):
            st.session_state.dados_usuario.update({
                "nome": nome_input, "cargo": cargo_input, "empresa": empresa_input, "estande": estande_input
            })
            st.success("Perfil atualizado com sucesso!")
            st.session_state.pagina_atual = "Home"
            st.rerun()
            
    if st.button("⬅️ Voltar ao Início", use_container_width=True, key="btn_back_cad"):
        st.session_state.pagina_atual = "Home"
        st.rerun()
    render_flow_ai_footer()

elif pagina == "Portal Motorista":
    render_top_bar("Portal do Motorista & Mobilidade")
    mot = st.session_state.dados_motorista
    
    st.markdown(
        f"""
        <div class="neon-card-cyan">
            <div style="color: #00F59B; font-weight: bold; font-size: 15px;">🚗 {mot['nome']} ({mot['carro']} • Placa: {mot['placa']})</div>
            <div style="color: #00D2FF; font-size: 13px; margin-top: 6px;">💰 Saldo Disponível via Pix: <b>R$ {mot['saldo_pix']:.2f}</b></div>
            <div style="color: #ffffff; font-size: 12px; margin-top: 2px;">📈 Faturamento Total do Dia: <b>R$ {mot['faturamento_total']:.2f}</b> ({mot['corridas_realizadas']} corridas)</div>
            <div style="color: #facc15; font-size: 12px; margin-top: 2px;">Avaliação dos Passageiros: {mot['avaliacao']}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("### 📡 Radar Tático de Corridas (Saindo de Grandes Eventos)")
    st.markdown(
        """
        <div class="neon-card">
            <div style="color: #00F59B; font-size: 14px; font-weight: bold;">🏢 Transamérica Expo Center ➔ Bela Vista</div>
            <div style="color: #00D2FF; font-size: 12px; margin-top: 4px;">Tarifa Dinâmica Ativa (2.4x) • <b>Valor Estimado: R$ 55,00 a R$ 68,00</b></div>
            <div style="color: #9ca3af; font-size: 11px; margin-top: 2px;">Distância estimada: 12.4 km • Tempo até o passageiro: 4 mins</div>
        </div>
        <div class="neon-card">
            <div style="color: #00F59B; font-size: 14px; font-weight: bold;">🍷 Itaim Bibi (Polo Gastronômico) ➔ Pinheiros</div>
            <div style="color: #00D2FF; font-size: 12px; margin-top: 4px;">Alta demanda de casais saindo de restaurantes • <b>Valor Estimado: R$ 38,00</b></div>
            <div style="color: #9ca3af; font-size: 11px; margin-top: 2px;">Distância estimada: 5.8 km</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    if st.button("💵 Solicitar Saque via Pix Instantâneo"):
        st.success(f"Saque de R$ {mot['saldo_pix']:.2f} solicitado com sucesso para a chave cadastrada!")

    if st.button("⬅️ Voltar ao Início", use_container_width=True, key="btn_back_mot"):
        st.session_state.pagina_atual = "Home"
        st.rerun()
    render_flow_ai_footer()
