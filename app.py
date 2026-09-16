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

# Injeção de CSS Customizado - Incluindo Estilização para Menu Inferior Estilo App
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

def gerar_resposta_ia_contextual(pagina, input_usuario=""):
    return f"🤖 [Flow AI]: Sincronização urbana ativa para o módulo '{pagina}'. Tudo operando com máxima precisão em São Paulo!"

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

def render_bottom_app_bar():
    """Barra de navegação flutuante inferior estilo aplicativo de mobilidade/super app"""
    st.markdown("---")
    st.markdown("<div style='text-align: center; color: #9ca3af; font-size: 11px; margin-bottom: 6px;'>🧭 NAVEGAÇÃO RÁPIDA ENTRE MÓDULOS</div>", unsafe_allow_html=True)
    
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        if st.button("🏠 Home", use_container_width=True, key="bar_home"):
            st.session_state.pagina_atual = "Home"
            st.rerun()
    with c2:
        if st.button("🚗 Motorista", use_container_width=True, key="bar_mot"):
            st.session_state.pagina_atual = "Portal Motorista"
            st.rerun()
    with c3:
        if st.button("🍷 Date", use_container_width=True, key="bar_date"):
            st.session_state.pagina_atual = "Sampa Date"
            st.rerun()
    with c4:
        if st.button("🚀 Evento", use_container_width=True, key="bar_ev"):
            st.session_state.pagina_atual = "Dashboard Evento"
            st.rerun()

    c5, c6, c7, c8 = st.columns(4)
    with c5:
        if st.button("🤝 Match", use_container_width=True, key="bar_match"):
            st.session_state.pagina_atual = "Sampa Match Geral"
            st.rerun()
    with c6:
        if st.button("📍 GPS", use_container_width=True, key="bar_gps"):
            st.session_state.pagina_atual = "GPS Indoor"
            st.rerun()
    with c7:
        if st.button("🛍️ Gastron.", use_container_width=True, key="bar_gast"):
            st.session_state.pagina_atual = "Compras Dual"
            st.rerun()
    with c8:
        if st.button("🎭 Cultura", use_container_width=True, key="bar_cult"):
            st.session_state.pagina_atual = "Passeios e Cultura"
            st.rerun()

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
    
    render_bottom_app_bar()

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

    render_flow_ai_footer()

elif pagina == "Sampa Date":
    render_top_bar("Sampa Date — O Guia do Encontro Perfeito")
    
    st.markdown(
        """
        <div class="neon-card">
            <div style="color: #00F59B; font-weight: bold; font-size: 16px;">🍷 Planeje o Date Perfeito sem Errar e sem Surpresas!</div>
            <p style="font-size: 12px; color: #d1d5db; margin-top: 6px; line-height: 1.4;">
                Está fazendo <b>22°C</b> agora à noite em São Paulo — uma temperatura deliciosa para sair! Conte para o nosso assistente como é a sua companhia e o SampaFlow indicará o restaurante ideal.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    with st.form("form_sampa_date"):
        st.selectbox("1. Como ela se veste / Qual o estilo predominante?", ["Elegante / Sofisticada", "Casual / Descontraída", "Moderna / Alternativa"])
        st.selectbox("2. Experiência com os clássicos de São Paulo?", ["Nunca foi / Pouco hábito", "Já conhece alguns", "Apaixonada pela história paulistana"])
        st.selectbox("3. Qual culinária tem mais a ver com o momento?", ["Italiana Tradicional", "Bistrô Francês", "Japonesa Contemporânea"])
        btn_gerar_date = st.form_submit_button("✨ Revelar a Sugestão Perfeita para o Date")

    if btn_gerar_date or st.session_state.get("sugeriu_date", False):
        st.session_state.sugeriu_date = True
        st.markdown(
            """
            <div class="neon-card-cyan" style="border: 1px solid #00F59B; margin-top: 10px;">
                <div style="color: #00F59B; font-weight: bold; font-size: 15px;">🍝 Famiglia Mancini (Bela Vista)</div>
                <div style="color: #00D2FF; font-size: 12px; margin: 4px 0;">📍 Rua Avanhandava, 81 — Centro, São Paulo</div>
                <div style="color: #ffffff; font-size: 12px;">Previsão média para o casal: <b>R$ 220 a R$ 320</b>. Clima ótimo de 22°C para caminhar pela rua iluminada.</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    render_flow_ai_footer()

elif pagina == "Dashboard Evento":
    ev = st.session_state.evento_selecionado
    render_top_bar(ev['pavilhao'])
    st.markdown(
        f"""
        <div class="neon-card">
            <div style="color: #00F59B; font-weight: bold; font-size: 18px;">🏢 {ev['nome']}</div>
            <div style="color: #00D2FF; font-size: 13px; margin-top: 4px;">📍 {ev['pavilhao']} • {ev['data']}</div>
            <p style="color: #d1d5db; font-size: 12px; margin-top: 8px;">{ev['desc']}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    render_flow_ai_footer()

elif pagina == "Sampa Match Geral":
    render_top_bar("SAMPA MATCH — Networking B2B")
    st.markdown(
        """
        <div class="neon-card">
            <div style="color: #00F59B; font-weight: bold; font-size: 16px;">🤝 Conexões Inteligentes em Grandes Feiras</div>
            <p style="font-size: 12px; color: #d1d5db; margin-top: 6px;">Conecte-se com decisores presentes no Transamérica Expo Center.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    render_flow_ai_footer()

elif pagina == "GPS Indoor":
    render_top_bar("GPS INDOOR & Mapa Tático")
    st.markdown(
        """
        <div class="waze-radar-box">
            <div style="color: #00D2FF; font-weight: bold; font-size: 16px;">🗺️ Navegação Interna — Transamérica Expo Center</div>
            <p style="color: #9ca3af; font-size: 12px; margin-top: 8px;">Sua localização: <b>Estande 12 (Corredor Principal B)</b>.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    render_flow_ai_footer()

elif pagina == "Compras Dual":
    render_top_bar("Gastronomia & Compras — 10% OFF")
    st.markdown(
        """
        <div class="neon-card">
            <div style="color: #00F59B; font-weight: bold; font-size: 16px;">🛍️ Descontos Exclusivos em São Paulo</div>
            <p style="font-size: 12px; color: #d1d5db; margin-top: 6px;">Cupons de 10% OFF nos principais restaurantes parceiros.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    render_flow_ai_footer()

elif pagina == "Passeios e Cultura":
    render_top_bar("Passeios & Cultura — O que fazer em SP")
    st.markdown(
        """
        <div class="neon-card">
            <div style="color: #00F59B; font-weight: bold; font-size: 16px;">🎭 Roteiros Culturais & Parques (22°C)</div>
            <p style="font-size: 12px; color: #d1d5db; margin-top: 6px;">Parque Ibirapuera, MASP e Pinacoteca em destaque para hoje.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    render_flow_ai_footer()

elif pagina == "Cadastro Usuario":
    render_top_bar("Editar Perfil Profissional")
    with st.form("form_cad"):
        nome_input = st.text_input("Nome Completo", st.session_state.dados_usuario["nome"])
        cargo_input = st.text_input("Cargo", st.session_state.dados_usuario["cargo"])
        if st.form_submit_button("✅ Salvar Alterações"):
            st.session_state.dados_usuario.update({"nome": nome_input, "cargo": cargo_input})
            st.success("Perfil atualizado com sucesso!")
            st.rerun()
    render_flow_ai_footer()

elif pagina == "Portal Motorista":
    render_top_bar("Portal do Motorista & Chamada Estilo App")
    mot = st.session_state.dados_motorista
    
    # Interface inspirada no print do app de passageiro / motorista com mapa simulado e barra de busca de destino
    st.markdown(
        f"""
        <div class="neon-card-cyan" style="border: 1px solid #00D2FF; text-align: center; padding: 12px;">
            <div style="color: #00F59B; font-weight: bold; font-size: 14px;">📍 Painel de Chamada & Radar de Corridas</div>
            <div style="color: #ffffff; font-size: 12px; margin-top: 4px;">Simulação de Solicitação de Corrida para Passageiros no SampaFlow</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    with st.form("form_chamada_passageiro"):
        st.markdown("🔍 **Para onde vamos?** (Simulação de Corrida)")
        destino_input = st.text_input("Endereço de Destino:", "Avenida Paulista, 1000 — Bela Vista")
        forma_pagamento = st.selectbox("Forma de Pagamento:", ["Pix Instantâneo (10% OFF)", "Cartão de Crédito SampaPay", "Dinheiro"])
        
        btn_chamar = st.form_submit_button("🚗 Chamar Motorista Próximo Agora")

    if btn_chamar:
        st.success(f"Corrida solicitada com sucesso para **{destino_input}**! Rota calculada com tarifa dinâmica ativa (2.4x).")

    st.markdown("---")
    st.markdown(
        f"""
        <div class="neon-card">
            <div style="color: #00F59B; font-weight: bold; font-size: 14px;">🚗 Seus Dados de Motorista Ativos</div>
            <div style="color: #f3f4f6; font-size: 12px; margin-top: 4px;">Veículo: <b>{mot['carro']}</b> ({mot['placa']})</div>
            <div style="color: #00D2FF; font-size: 12px; margin-top: 2px;">Saldo Pix Disponível: <b>R$ {mot['saldo_pix']:.2f}</b> | Faturamento: <b>R$ {mot['faturamento_total']:.2f}</b></div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    if st.button("💵 Solicitar Saque via Pix Instantâneo"):
        st.success(f"Saque de R$ {mot['saldo_pix']:.2f} transferido via Pix com sucesso!")

    render_flow_ai_footer()
    
