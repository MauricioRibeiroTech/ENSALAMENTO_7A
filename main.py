import streamlit as st
import base64
from fpdf import FPDF
import requests
import os

# --- CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(
    page_title="Mapa da Sala de Aula do 7A",
    page_icon="🏫",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- DEFINIÇÕES DE GRUPOS ---
GROUP_CONFIG = {
    1: {"color": "#FF6B6B", "emoji": "🍎"}, # Vermelho
    2: {"color": "#4ECDC4", "emoji": "💧"}, # Verde Água
    3: {"color": "#45B7D1", "emoji": "🚀"}, # Azul
    4: {"color": "#FED766", "emoji": "🌟"}, # Amarelo
    5: {"color": "#9B59B6", "emoji": "🍇"}, # Roxo
    6: {"color": "#F29E4C", "emoji": "🍊"}  # Laranja
}

# --- INICIALIZAÇÃO DO ESTADO DA SESSÃO ---
if 'students' not in st.session_state:
    st.session_state.students = []
if 'map_generated' not in st.session_state:
    st.session_state.map_generated = False

# --- FUNÇÃO DE GERAÇÃO DE PDF ---
def create_pdf_report(students_list):
    """Gera um relatório PDF elegante com a lista de alunos por grupo."""
    
    # Baixar uma fonte que suporte emojis (essencial para funcionar na nuvem)
    font_url = "https://github.com/google/fonts/raw/main/apache/dejavusans/DejaVuSans.ttf"
    font_file = "DejaVuSans.ttf"
    try:
        if not os.path.exists(font_file):
            response = requests.get(font_url)
            response.raise_for_status()
            with open(font_file, "wb") as f:
                f.write(response.content)
    except requests.exceptions.RequestException as e:
        st.error(f"Falha ao baixar a fonte necessária para o PDF: {e}")
        return None

    pdf = FPDF()
    pdf.add_page()
    
    # Adicionar a fonte baixada ao PDF
    pdf.add_font('DejaVu', '', font_file, uni=True)
    
    # Título do Documento
    pdf.set_font('DejaVu', size=20)
    pdf.cell(0, 15, "Ensalamento Interativo - 7º Ano A do HD", new_x="LMARGIN", new_y="NEXT", align='C')
    pdf.ln(10)

    # Loop pelos grupos e alunos
    for group_id, config in GROUP_CONFIG.items():
        students_in_group = [s for s in students_list if s['group'] == group_id]
        
        if students_in_group:
            # Título do Grupo
            pdf.set_font('DejaVu', size=16)
            pdf.cell(0, 12, f"Grupo {group_id} {config['emoji']}", new_x="LMARGIN", new_y="NEXT")
            
            # Lista de Alunos no Grupo
            pdf.set_font('DejaVu', size=12)
            for student in students_in_group:
                student_emoji = "👦" if student['gender'] == "Menino" else "👧"
                pdf.cell(0, 8, f"    {student_emoji}  {student['name']}", new_x="LMARGIN", new_y="NEXT")
            
            pdf.ln(8) # Espaço entre os grupos
        
    return pdf.output(dest='S').encode('latin-1')


# --- FUNÇÕES AUXILIARES ---
def add_student(name, group, gender):
    if name:
        if any(student['name'].lower() == name.lower() for student in st.session_state.students):
            st.sidebar.warning(f"O aluno '{name}' já está na lista.")
        else:
            st.session_state.students.append({"name": name, "group": group, "gender": gender})
            st.sidebar.success(f"'{name}' adicionado ao Grupo {group}!")
            st.session_state.map_generated = False
    else:
        st.sidebar.error("Por favor, insira o nome do aluno.")

def clear_students():
    st.session_state.students = []
    st.session_state.map_generated = False

# --- BARRA LATERAL (SIDEBAR) ---
with st.sidebar:
    st.header("🧑‍🎓 Painel de Controle")
    with st.form("add_student_form", clear_on_submit=True):
        st.subheader("Adicionar Novo Aluno")
        student_name = st.text_input("Nome do Aluno", placeholder="Ex: Ana Silva")
        col1, col2 = st.columns(2)
        with col1:
            student_group = st.selectbox("Grupo", options=list(GROUP_CONFIG.keys()), format_func=lambda g: f"Grupo {g} {GROUP_CONFIG[g]['emoji']}")
        with col2:
            student_gender = st.selectbox("Gênero", ["Menino", "Menina"])
        if st.form_submit_button("Adicionar à Turma"):
            add_student(student_name, student_group, student_gender)
    st.divider()
    st.subheader("📋 Alunos na Turma")
    if not st.session_state.students:
        st.info("Nenhum aluno foi adicionado ainda.")
    else:
        for group_id, config in GROUP_CONFIG.items():
            students_in_group = [s['name'] for s in st.session_state.students if s['group'] == group_id]
            if students_in_group:
                with st.expander(f"**Grupo {group_id} {config['emoji']}** ({len(students_in_group)} alunos)"):
                    for student_data in st.session_state.students:
                        if student_data['group'] == group_id:
                            emoji = "👦" if student_data['gender'] == "Menino" else "👧"
                            st.write(f"- {student_data['name']} {emoji}")
    if st.session_state.students:
        st.divider()
        if st.button("🗑️ Limpar Todos os Alunos", use_container_width=True):
            clear_students()
            st.rerun()

# --- ÁREA PRINCIPAL ---
st.title("Ensalamento Interativo do 7º Ano A do HD")
st.markdown("Adicione os alunos na barra lateral e clique no botão abaixo para criar um layout organizado por grupos!")

if st.button("✨ Gerar / Organizar Ensalamento", type="primary", use_container_width=True):
    if not st.session_state.students:
        st.error("Você precisa adicionar pelo menos um aluno para gerar o mapa da sala!")
    else:
        st.session_state.map_generated = True

if st.session_state.map_generated:
    st.subheader("Aqui está a turma organizada por grupos!")
    # A visualização do mapa na tela continua a mesma
    st.markdown('<div id="classroom-map" style="background-color: white; padding: 20px; border-radius: 10px;">', unsafe_allow_html=True)
    main_cols = st.columns(2, gap="large")
    for i, (group_id, group_info_config) in enumerate(GROUP_CONFIG.items()):
        target_col = main_cols[i % 2]
        with target_col:
            students_in_group = [s for s in st.session_state.students if s['group'] == group_id]
            if students_in_group:
                st.markdown(f"<h5><span style='color:{group_info_config['color']};'>Grupo {group_id} {group_info_config['emoji']}</span></h5>", unsafe_allow_html=True)
                num_columns = 3
                num_rows = (len(students_in_group) + num_columns - 1) // num_columns
                for row in range(num_rows):
                    desk_cols = st.columns(num_columns)
                    for col_index in range(num_columns):
                        student_index = row * num_columns + col_index
                        if student_index < len(students_in_group):
                            student = students_in_group[student_index]
                            group_info = GROUP_CONFIG[student['group']]
                            student_emoji = "👦" if student['gender'] == "Menino" else "👧"
                            with desk_cols[col_index]:
                                st.markdown(f'<div style="background-color: {group_info["color"]}; border-radius: 8px; padding: 15px 10px; text-align: center; color: white; font-family: sans-serif; min-height: 120px; display: flex; flex-direction: column; justify-content: center; align-items: center; box-shadow: 0 4px 6px rgba(0,0,0,0.1); border-top: 15px solid rgba(0,0,0,0.2); margin-bottom: 10px;"><p style="font-size: 2.5em; margin: 0; line-height: 1;">{student_emoji}</p><h6 style="margin-top: 5px; margin-bottom: 0px; font-weight: bold; word-wrap: break-word;">{student["name"]}</h6></div>', unsafe_allow_html=True)
                st.markdown("<br>", unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    st.divider()

    # --- LÓGICA DE DOWNLOAD DE PDF ---
    with st.spinner("Preparando PDF..."):
        pdf_data = create_pdf_report(st.session_state.students)
    
    if pdf_data:
        st.download_button(
            label="📄 Baixar Relatório PDF",
            data=pdf_data,
            file_name="ensalamento_turma.pdf",
            mime="application/pdf",
            use_container_width=True,
            type="primary"
        )
else:
    st.info("Clique no botão 'Gerar Ensalamento' para visualizar o mapa.")

