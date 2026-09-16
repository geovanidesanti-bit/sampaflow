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
        animation: marquee 24s linear infinite;
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
    .radar-dot {
        display: inline-block;
        width: 10px;
        height: 10px;
        background-color: #00F59B;
        border-radius: 50%;
        box-shadow: 0 0 10px #00F59B;
        margin: 0 4px;
        animation: pulse 1.5s infinite;
    }
    @keyframes pulse {
        0% { transform: scale(0.95); box-shadow: 0 0 0 0 rgba(0, 245, 155, 0.7); }
        70% { transform: scale(1.1); box-shadow: 0 0 0 8px rgba(0, 245, 155, 0); }
        100% { transform: scale(0.95); box-shadow: 0 0 0 0 rgba(0, 245, 155, 0); }
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

# Inicialização segura de variáveis de sessão
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
        "produto_destaque": "Smartphone Samsung Galaxy A03 (Novidade)",
        "especificacoes": "Tela Infinity-V de 6.5'', Câmera Dupla de 48MP, Bateria de 5000mAh e Processador Octa-Core.",
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
        "pavilhao": "Transamérica Expo Center",
        "nome": "Sampa Tech & Mobile Summit 2026",
        "tipo": "Feira de Tecnologia & Eletrônicos B2B",
        "data": "18 a 21 de Outubro",
        "desc": "O maior evento de inovação mobile e lançamentos de dispositivos da América Latina."
    }

if "corrida_atual" not in st.session_state:
    st.session_state.corrida_atual = {
        "ativa": True,
        "origem": "Transamérica Expo Center",
        "destino": "Av. Paulista, 1000 — Bela Vista",
        "valor": 55.00,
        "distancia": "5.5 km (10 min)",
        "passageiro": "Carlos Eduardo (Nota ⭐ 4.9)"
    }

if "cupom_gerado" not in st.session_state:
    st.session_state.cupom_gerado = None

if "lista_matches" not in st.session_state:
    st.session_state.lista_matches = [
        {"nome": "Ana Mendes", "empresa": "Samsung Partner", "estande": "Estande 15", "status": "Conectado & Café Agendado"}
    ]

def gerar_resposta_ia_contextual(pagina, input_usuario=""):
    """Motor de IA inteligente que gera respostas com base na página atual e contexto urbano."""
    if pagina == "Home":
        return "🤖 [Flow AI]: Olá! O hub central está operando em capacidade máxima. Noite perfeita em São Paulo com 22°C. O módulo 'Sampa Date' está ativo para planejar seu encontro!"
    elif pagina == "Sampa Date":
        return "🤖 [Flow AI]: Analisando o perfil do date + clima de 22°C: Locais com iluminação baixa, massas artesanais e carta de vinhos selecionados garantem 100% de sucesso sem surpresas na conta."
    elif pagina == "Dashboard Evento":
        return f"🤖 [Flow AI]: Analisando o {st.session_state.evento_selecionado['pavilhao']}: Pico de tráfego detectado no corredor principal. O estande da {st.session_state.dados_usuario['empresa']} possui alta conversão!"
    elif pagina == "Compras Dual":
        return "🤖 [Flow AI]: Sugestão inteligente: Com 22°C, os restaurantes parceiros com mesas ao ar livre e aconchego estão com alta procura. Seu cupom de 10% está pronto!"
    elif pagina == "Passeios e Cultura":
        return "🤖 [Flow AI]: Roteiro cultural otimizado: Museus e centros cobertos abertos com cafeterias charmosas para curtir a noite de São Paulo."
    elif pagina == "Portal Motorista":
        return "🤖 [Flow AI]: Radar tático de trânsito: Alta demanda de passageiros saindo de eventos e restaurantes. Tarifas dinâmicas ativas!"
    else:
        return f"🤖 [Flow AI]: Comando processado com sucesso para a seção '{pagina}'. Sincronização realizada!"

def render_top_bar(titulo_pagina="SampaFlow"):
    st.markdown(
        """
        <div class="ticker-container">
            <div class="ticker-text">
                ⚡ SampaFlow Info: São Paulo • 15 de Setembro de 2026 • 🌙 22°C • Noite Agradável • Perfeita para um Sampa Date inesquecível com 10% OFF nos melhores restaurantes! 🍷✨
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
        resposta_texto = gerar_resposta_ia_contextual(st.session_state.pagina_atual, "Comando de voz do usuário")
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

# Roteador de Páginas
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
        if st.button("🚗 Portal do Motorista (Radar)", use_container_width=True):
            st.session_state.pagina_atual = "Portal Motorista"
            st.rerun()
    with col_u2:
        if st.button("✏️ Editar Perfil", use_container_width=True):
            st.session_state.pagina_atual = "Cadastro Usuario"
            st.rerun()

    st.markdown("### 🏛️ Menu Principal & Novidades")
    if st.button("🍷 SAMPA DATE — O Guia do Encontro Perfeito", use_container_width=True):
        st.session_state.pagina_atual = "Sampa Date"
        st.rerun()
    if st.button("🚀 Acessar Painel do Evento Atual", use_container_width=True):
        st.session_state.pagina_atual = "Dashboard Evento"
        st.rerun()

    st.markdown("### 🌐 Outros Módulos")
    if st.button("🤝 SAMPA MATCH — Radar & Conexões B2B", use_container_width=True):
        st.session_state.pagina_atual = "Sampa Match Geral"
        st.rerun()
    if st.button("📍 GPS INDOOR — Mapa Tático", use_container_width=True):
        st.session_state.pagina_atual = "GPS Indoor"
        st.rerun()
    if st.button("🛍️ GASTRONOMIA — 300 Restaurantes (10% OFF)", use_container_width=True):
        st.session_state.pagina_atual = "Compras Dual"
        st.rerun()
    if st.button("🎭 PASSEIOS & CULTURA — O que fazer em SP Hoje?", use_container_width=True):
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
                Está fazendo <b>22°C</b> agora à noite em São Paulo — uma temperatura deliciosa para sair! 
                Conte para o nosso assistente como é a sua companhia, o estilo dela e o que ela gosta. O SampaFlow vai indicar o restaurante sob medida, os pratos de maior sucesso e o **gasto médio estimado para o casal** para você ir totalmente preparado.
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
                "Elegante / Sofisticada (Gosta de lugares refinados e boa iluminação)",
                "Casual / Descontraída (Prefere lugares aconchegantes, rústicos ou animados)",
                "Moderna / Alternativa (Curte arte, centros históricos e bares conceituais)",
                "Romântica / Clássica (Adora jantar à luz de velas, massas e vinhos)"
            ]
        )
        
        experiencia_previa = st.selectbox(
            "2. Ela já conhece os clássicos tradicionais de São Paulo (ex: Bixiga / Centro)?",
            [
                "Nunca foi / Pouco hábito com os clássicos tradicionais",
                "Já conhece um pouco, mas adora novidades",
                "É super fã de comida tradicional e porções fartas"
            ]
        )

        tipo_cozinha_date = st.selectbox(
            "3. Qual culinária tem mais a ver com a ocasião de hoje?",
            [
                "Italiana Tradicional & Massas Artesanais (Ex: Famiglia Mancini)",
                "Contemporânea & Bistrô Francês / Íntimo",
                "Japonesa Sofisticada & Drinks Exclusivos",
                "Comida Mineira ou Brasileira Afetiva"
            ]
        )

        btn_gerar_date = st.form_submit_button("✨ Revelar a Sugestão Perfeita para o Date")

    if btn_gerar_date or "sugeriu_date" in st.session_state:
        st.session_state.sugeriu_date = True
        
        st.markdown("---")
        st.markdown("### 🏆 Sugestão Exclusiva do SampaFlow para Hoje à Noite:")
        
        if "Italiana" in tipo_cozinha_date:
            st.markdown(
                """
                <div class="neon-card-cyan" style="border: 1px solid #00F59B;">
                    <div style="color: #00F59B; font-weight: bold; font-size: 16px;">🍝 Destino Sugerido: Famiglia Mancini (Bela Vista / Centro)</div>
                    <div style="color: #00D2FF; font-size: 13px; margin: 4px 0;">📍 <b>Endereço:</b> Rua Avanhandava, 81 — Centro (Região iluminada e segura)</div>
                    <div style="color: #ffffff; font-size: 13px; margin-top: 8px;"><b>🌡️ Condição Climática:</b> 22°C (Perfeito para caminhar na charmosa e iluminada Rua Avanhandava após o jantar).</div>
                    
                    <hr style="border-color: rgba(0,213,255,0.2); margin: 10px 0;">
                    <div style="color: #f3f4f6; font-size: 12px;">
                        <b>🎯 Por que vai impressionar a gata?</b><br>
                        O ambiente é icônico, repleto de antiguidades e com uma atmosfera acolhedora espetacular. Como ela não tem o hábito de frequentar os clássicos paulistanos, o visual imersivo vai surpreendê-la positivamente.
                    </div>
                    
                    <div style="margin-top: 10px; color: #f3f4f6; font-size: 12px;">
                        <b>🍲 Pratos Recomendados para Pedir:</b><br>
                        • Fettuccine artesanal com molho de camarão e ervas finas.<br>
                        • Escalope à Parmegiana (famoso pela fartura e sabor inigualável).
                    </div>
                    
                    <div style="background: rgba(0,245,155,0.1); border: 1px solid rgba(0,245,155,0.4); border-radius: 10px; padding: 10px; margin-top: 12px;">
                        <span style="color: #00F59B; font-weight: bold; font-size: 14px;">💰 Previsão de Gastos para o Casal:</span><br>
                        <span style="color: #ffffff; font-size: 13px;">Média de <b>R$ 220 a R$ 300</b> (incluindo prato principal bem servido para compartilhar, bebidas não alcoólicas/vinho da casa e serviço). Você já vai sabendo exatamente quanto programar na carteira!</span>
                    </div>
                </div>
                """,
                unsafe_allow_html=True,
            )
        else:
            st.markdown(
                """
                <div class="neon-card-cyan" style="border: 1px solid #00F59B;">
                    <div style="color: #00F59B; font-weight: bold; font-size: 16px;">🍷 Destino Sugerido: Bistrô Al Mare & Rooftop (Itaim Bibi)</div>
                    <div style="color: #00D2FF; font-size: 13px; margin: 4px 0;">📍 <b>Endereço:</b> Rua Brisamar, 220 — Itaim Bibi</div>
                    <div style="color: #ffffff; font-size: 13px; margin-top: 8px;"><b>🌡️ Condição Climática:</b> 22°C (Clima agradabilíssimo para mesas na varanda iluminada).</div>
                    
                    <hr style="border-color: rgba(0,213,255,0.2); margin: 10px 0;">
                    <div style="color: #f3f4f6; font-size: 12px;">
                        <b>🎯 Por que vai impressionar a gata?</b><br>
                        Ambiente extremamente charmoso, música ambiente suave e atendimento impecável. Ideal para conversas longas e momentos marcantes.
                    </div>
                    
                    <div style="margin-top: 10px; color: #f3f4f6; font-size: 12px;">
                        <b>🍲 Pratos Recomendados para Pedir:</b><br>
                        • Risoto de Funghi com filé mignon grelhado.<br>
                        • Taças de vinho tinto selecionado pelo sommelier.
                    </div>
                    
                    <div style="background: rgba(0,245,155,0.1); border: 1px solid rgba(0,245,155,0.4); border-radius: 10px; padding: 10px; margin-top: 12px;">
                        <span style="color: #00F59B; font-weight: bold; font-size: 14px;">💰 Previsão de Gastos para o Casal:</span><br>
                        <span style="color: #ffffff; font-size: 13px;">Média de <b>R$ 250 a R$ 350</b> (incluindo entrada, prato principal para dois e bebidas). Zero surpresas na hora de fechar a conta!</span>
                    </div>
                </div>
                """,
                unsafe_allow_html=True,
            )

        if st.button("🎁 Gerar Cupom de 10% OFF para este Date"):
            hash_date = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
            st.session_state.cupom_gerado = f"SAMPA-DATE-{hash_date}-10OFF"
            st.success(f"Cupom gerado com sucesso: {st.session_state.cupom_gerado} (Válido no restaurante escolhido!)")

    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("⬅️ Voltar ao Início"):
        st.session_state
