## 🏫 Mapa da Sala de Aula Interativo 🎨
Bem-vindo ao projeto Mapa da Sala de Aula Interativo! Esta é uma aplicação web desenvolvida com Streamlit para ajudar educadores a organizar e visualizar a disposição dos alunos em sala de aula de forma rápida, bonita e personalizável.
A ferramenta permite criar grupos, adicionar alunos com identificação de gênero (menino/menina) e gerar um mapa visual que pode ser salvo como uma imagem de alta qualidade, pronta para impressão.

## ✨ Funcionalidades Principais
Painel de Controle Intuitivo: Adicione, gerencie e limpe a lista de alunos através de uma barra lateral simples.
Criação de Grupos: Atribua cada aluno a um dos seis grupos pré-definidos, cada um com uma cor e um emoji de identificação.
Personalização por Gênero: Escolha entre "Menino" (👦) e "Menina" (👧) para cada aluno, personalizando o mapa visual.
Geração Automática do Mapa: Com um único clique, organize todos os alunos em um mapa visual elegante, com os estudantes agrupados por equipe.
Layout Otimizado: O mapa é exibido em um layout de duas colunas para melhor aproveitamento do espaço em telas largas.
Visual de "Carteira": Cada aluno é representado por um card estilizado que simula uma carteira escolar.
Exportação para PNG: Salve o mapa da sala gerado como um arquivo de imagem .png de alta resolução, ideal para impressão, compartilhamento ou arquivamento digital.

## 📸 Screenshot da Aplicação
![Imagem de <Screenshot da aplicação em funcionamento>]
(Substitua esta seção por um print da sua aplicação)

## 🛠️ Tecnologias Utilizadas
Python 3
Streamlit: Framework principal para a criação da aplicação web.
streamlit-js-eval: Biblioteca para executar JavaScript no navegador e habilitar o download da imagem.
HTML/CSS: Para a estilização personalizada dos cards de alunos.
JavaScript (html2canvas): Biblioteca utilizada para "fotografar" a área do mapa e convertê-la em uma imagem.

## 🚀 Como Executar o Projeto
Siga os passos abaixo para executar a aplicação em sua máquina local.
Pré-requisitos
Python 3.8 ou superior instalado.
```bash
pip (gerenciador de pacotes do Python).
```
Instalação e Execução
Clone o repositório:
```bash
git clone https://github.com/seu-usuario/nome-do-repositorio.git
cd nome-do-repositorio
```
Crie um ambiente virtual (recomendado):
```bash
python -m venv venv
source venv/bin/activate  # No Windows, use: venv\Scripts\activate
```


Instale as dependências:
Crie um arquivo chamado requirements.txt com o seguinte conteúdo:
```bash
streamlit
streamlit_js_eval
```

Em seguida, instale as bibliotecas com o comando:
```bash
pip install -r requirements.txt
```


Execute a aplicação Streamlit ( No terminal, execute o comando)
```bash
streamlit run mapa_sala_app.py
```

A aplicação será aberta automaticamente no seu navegador padrão!
📝 Licença
Este projeto está sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.
