import os
import sys
# DON'T CHANGE THIS !!!
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS

app = Flask(__name__, static_folder=os.path.join(os.path.dirname(__file__), 'static'))
app.config['SECRET_KEY'] = 'asdf#FGSgvasgf$5$WGT'
CORS(app)

# Base de dados expandida com 25+ profissões
PROFISSOES_DATABASE = {
    # TECNOLOGIA
    "cientista_dados": {
        "nome": "Cientista de Dados",
        "categoria": "Tecnologia",
        "salario": "R$ 8.000 - R$ 25.000",
        "demanda": "Alta demanda",
        "crescimento": "Crescimento de 35% até 2030",
        "descricao": "Analisa grandes volumes de dados para extrair insights valiosos para empresas.",
        "habilidades": ["Python", "SQL", "Machine Learning", "Estatística", "Power BI"],
        "perfil": ["analitico", "tecnico"],
        "pontuacao_minima": 15
    },
    "desenvolvedor_ia": {
        "nome": "Desenvolvedor de IA",
        "categoria": "Tecnologia", 
        "salario": "R$ 10.000 - R$ 30.000",
        "demanda": "Altíssima demanda",
        "crescimento": "Crescimento de 60% até 2030",
        "descricao": "Desenvolve sistemas de inteligência artificial e machine learning.",
        "habilidades": ["Python", "TensorFlow", "PyTorch", "Deep Learning", "Neural Networks"],
        "perfil": ["tecnico", "inovador"],
        "pontuacao_minima": 16
    },
    "engenheiro_cybersecurity": {
        "nome": "Engenheiro de Cibersegurança",
        "categoria": "Tecnologia",
        "salario": "R$ 9.000 - R$ 28.000", 
        "demanda": "Alta demanda",
        "crescimento": "Crescimento de 45% até 2030",
        "descricao": "Protege sistemas e dados contra ameaças cibernéticas.",
        "habilidades": ["Ethical Hacking", "Firewall", "Criptografia", "Análise de Vulnerabilidades"],
        "perfil": ["analitico", "tecnico"],
        "pontuacao_minima": 14
    },
    "arquiteto_cloud": {
        "nome": "Arquiteto de Cloud",
        "categoria": "Tecnologia",
        "salario": "R$ 12.000 - R$ 35.000",
        "demanda": "Alta demanda", 
        "crescimento": "Crescimento de 40% até 2030",
        "descricao": "Projeta e implementa soluções em nuvem para empresas.",
        "habilidades": ["AWS", "Azure", "Google Cloud", "Kubernetes", "DevOps"],
        "perfil": ["tecnico", "estrategico"],
        "pontuacao_minima": 15
    },
    "desenvolvedor_blockchain": {
        "nome": "Desenvolvedor Blockchain",
        "categoria": "Tecnologia",
        "salario": "R$ 11.000 - R$ 32.000",
        "demanda": "Crescente",
        "crescimento": "Crescimento de 50% até 2030", 
        "descricao": "Desenvolve aplicações descentralizadas e contratos inteligentes.",
        "habilidades": ["Solidity", "Web3", "Smart Contracts", "Ethereum", "Criptografia"],
        "perfil": ["tecnico", "inovador"],
        "pontuacao_minima": 16
    },

    # CRIATIVIDADE & DESIGN
    "designer_ux": {
        "nome": "Designer UX/UI",
        "categoria": "Criatividade",
        "salario": "R$ 6.000 - R$ 18.000",
        "demanda": "Alta demanda",
        "crescimento": "Crescimento de 30% até 2030",
        "descricao": "Cria experiências digitais intuitivas e interfaces atrativas.",
        "habilidades": ["Figma", "Adobe XD", "Prototipagem", "Design Thinking", "Usabilidade"],
        "perfil": ["criativo", "empatico"],
        "pontuacao_minima": 13
    },
    "criador_conteudo": {
        "nome": "Criador de Conteúdo Digital",
        "categoria": "Criatividade",
        "salario": "R$ 4.000 - R$ 20.000",
        "demanda": "Altíssima demanda",
        "crescimento": "Crescimento de 55% até 2030",
        "descricao": "Produz conteúdo para redes sociais, blogs e plataformas digitais.",
        "habilidades": ["Copywriting", "SEO", "Redes Sociais", "Edição de Vídeo", "Analytics"],
        "perfil": ["criativo", "comunicativo"],
        "pontuacao_minima": 12
    },
    "motion_designer": {
        "nome": "Motion Designer",
        "categoria": "Criatividade",
        "salario": "R$ 5.000 - R$ 16.000",
        "demanda": "Crescente",
        "crescimento": "Crescimento de 35% até 2030",
        "descricao": "Cria animações e motion graphics para mídia digital.",
        "habilidades": ["After Effects", "Cinema 4D", "Animação", "Design Gráfico", "Storytelling"],
        "perfil": ["criativo", "tecnico"],
        "pontuacao_minima": 13
    },
    "game_designer": {
        "nome": "Game Designer",
        "categoria": "Criatividade",
        "salario": "R$ 6.000 - R$ 22.000",
        "demanda": "Alta demanda",
        "crescimento": "Crescimento de 40% até 2030",
        "descricao": "Desenvolve conceitos, mecânicas e narrativas para jogos digitais.",
        "habilidades": ["Unity", "Unreal Engine", "Game Design", "Programação", "Arte Digital"],
        "perfil": ["criativo", "tecnico"],
        "pontuacao_minima": 14
    },

    # NEGÓCIOS & ESTRATÉGIA
    "analista_business": {
        "nome": "Analista de Business Intelligence",
        "categoria": "Negócios",
        "salario": "R$ 6.000 - R$ 18.000",
        "demanda": "Crescimento constante",
        "crescimento": "Crescimento de 25% até 2030",
        "descricao": "Transforma dados em informações estratégicas para tomada de decisões.",
        "habilidades": ["Power BI", "Excel Avançado", "SQL", "Análise de Dados", "Tableau"],
        "perfil": ["analitico", "estrategico"],
        "pontuacao_minima": 13
    },
    "especialista_esg": {
        "nome": "Especialista em ESG",
        "categoria": "Negócios",
        "salario": "R$ 8.000 - R$ 25.000",
        "demanda": "Altíssima demanda",
        "crescimento": "Crescimento de 70% até 2030",
        "descricao": "Desenvolve estratégias de sustentabilidade e responsabilidade social corporativa.",
        "habilidades": ["Sustentabilidade", "Compliance", "Relatórios ESG", "Gestão Ambiental"],
        "perfil": ["estrategico", "sustentavel"],
        "pontuacao_minima": 14
    },
    "growth_hacker": {
        "nome": "Growth Hacker",
        "categoria": "Negócios",
        "salario": "R$ 7.000 - R$ 22.000",
        "demanda": "Alta demanda",
        "crescimento": "Crescimento de 45% até 2030",
        "descricao": "Acelera o crescimento de empresas através de estratégias inovadoras.",
        "habilidades": ["Marketing Digital", "Analytics", "A/B Testing", "Growth Mindset", "Automação"],
        "perfil": ["estrategico", "inovador"],
        "pontuacao_minima": 15
    },
    "product_manager": {
        "nome": "Product Manager",
        "categoria": "Negócios",
        "salario": "R$ 10.000 - R$ 30.000",
        "demanda": "Alta demanda",
        "crescimento": "Crescimento de 35% até 2030",
        "descricao": "Gerencia o desenvolvimento e estratégia de produtos digitais.",
        "habilidades": ["Product Management", "Agile", "Scrum", "Analytics", "UX Research"],
        "perfil": ["estrategico", "lideranca"],
        "pontuacao_minima": 16
    },

    # SAÚDE & CIÊNCIAS
    "bioinformata": {
        "nome": "Bioinformata",
        "categoria": "Ciências",
        "salario": "R$ 8.000 - R$ 24.000",
        "demanda": "Crescente",
        "crescimento": "Crescimento de 40% até 2030",
        "descricao": "Aplica computação e estatística para analisar dados biológicos.",
        "habilidades": ["Python", "R", "Biologia Molecular", "Estatística", "Genômica"],
        "perfil": ["analitico", "cientifico"],
        "pontuacao_minima": 15
    },
    "terapeuta_digital": {
        "nome": "Terapeuta Digital",
        "categoria": "Saúde",
        "salario": "R$ 5.000 - R$ 15.000",
        "demanda": "Alta demanda",
        "crescimento": "Crescimento de 50% até 2030",
        "descricao": "Oferece terapia e suporte psicológico através de plataformas digitais.",
        "habilidades": ["Psicologia", "Terapia Online", "Tecnologia", "Comunicação", "Empatia"],
        "perfil": ["empatico", "social"],
        "pontuacao_minima": 12
    },
    "especialista_telemedicina": {
        "nome": "Especialista em Telemedicina",
        "categoria": "Saúde",
        "salario": "R$ 12.000 - R$ 35.000",
        "demanda": "Altíssima demanda",
        "crescimento": "Crescimento de 60% até 2030",
        "descricao": "Fornece cuidados médicos remotos através de tecnologias digitais.",
        "habilidades": ["Medicina", "Tecnologia Médica", "Diagnóstico Remoto", "Comunicação"],
        "perfil": ["cientifico", "empatico"],
        "pontuacao_minima": 16
    },

    # SUSTENTABILIDADE & ENERGIA
    "engenheiro_energia_renovavel": {
        "nome": "Engenheiro de Energia Renovável",
        "categoria": "Sustentabilidade",
        "salario": "R$ 9.000 - R$ 26.000",
        "demanda": "Alta demanda",
        "crescimento": "Crescimento de 50% até 2030",
        "descricao": "Desenvolve projetos de energia solar, eólica e outras fontes renováveis.",
        "habilidades": ["Energia Solar", "Energia Eólica", "Sustentabilidade", "Engenharia", "Projetos"],
        "perfil": ["tecnico", "sustentavel"],
        "pontuacao_minima": 15
    },
    "consultor_carbono": {
        "nome": "Consultor de Créditos de Carbono",
        "categoria": "Sustentabilidade",
        "salario": "R$ 8.000 - R$ 22.000",
        "demanda": "Crescente rapidamente",
        "crescimento": "Crescimento de 65% até 2030",
        "descricao": "Ajuda empresas a reduzir emissões e comercializar créditos de carbono.",
        "habilidades": ["Sustentabilidade", "Mercado de Carbono", "Auditoria Ambiental", "Regulamentação"],
        "perfil": ["estrategico", "sustentavel"],
        "pontuacao_minima": 14
    },

    # EDUCAÇÃO & IMPACTO SOCIAL
    "designer_instrucional": {
        "nome": "Designer Instrucional",
        "categoria": "Educação",
        "salario": "R$ 5.000 - R$ 14.000",
        "demanda": "Alta demanda",
        "crescimento": "Crescimento de 40% até 2030",
        "descricao": "Desenvolve experiências de aprendizagem online e materiais educacionais.",
        "habilidades": ["Pedagogia", "EAD", "Tecnologia Educacional", "Design", "Psicologia da Aprendizagem"],
        "perfil": ["educativo", "criativo"],
        "pontuacao_minima": 13
    },
    "especialista_diversidade": {
        "nome": "Especialista em Diversidade e Inclusão",
        "categoria": "Impacto Social",
        "salario": "R$ 7.000 - R$ 20.000",
        "demanda": "Crescente",
        "crescimento": "Crescimento de 55% até 2030",
        "descricao": "Desenvolve políticas e programas de diversidade e inclusão nas organizações.",
        "habilidades": ["Diversidade", "Inclusão", "RH", "Psicologia Organizacional", "Comunicação"],
        "perfil": ["social", "empatico"],
        "pontuacao_minima": 13
    },

    # ECONOMIA DIGITAL
    "trader_crypto": {
        "nome": "Trader de Criptomoedas",
        "categoria": "Finanças Digitais",
        "salario": "R$ 6.000 - R$ 50.000",
        "demanda": "Volátil mas crescente",
        "crescimento": "Crescimento de 35% até 2030",
        "descricao": "Negocia criptomoedas e ativos digitais nos mercados financeiros.",
        "habilidades": ["Trading", "Análise Técnica", "Blockchain", "Gestão de Risco", "Mercado Financeiro"],
        "perfil": ["analitico", "estrategico"],
        "pontuacao_minima": 14
    },
    "especialista_nft": {
        "nome": "Especialista em NFTs e Metaverso",
        "categoria": "Economia Digital",
        "salario": "R$ 8.000 - R$ 25.000",
        "demanda": "Emergente",
        "crescimento": "Crescimento de 80% até 2030",
        "descricao": "Desenvolve estratégias e projetos no metaverso e economia de NFTs.",
        "habilidades": ["NFTs", "Metaverso", "Blockchain", "Arte Digital", "Marketing Digital"],
        "perfil": ["inovador", "criativo"],
        "pontuacao_minima": 15
    },

    # AUTOMAÇÃO & ROBÓTICA
    "engenheiro_robotica": {
        "nome": "Engenheiro de Robótica",
        "categoria": "Automação",
        "salario": "R$ 10.000 - R$ 28.000",
        "demanda": "Alta demanda",
        "crescimento": "Crescimento de 45% até 2030",
        "descricao": "Desenvolve robôs e sistemas automatizados para indústrias.",
        "habilidades": ["Robótica", "Automação", "Programação", "Mecatrônica", "IA"],
        "perfil": ["tecnico", "inovador"],
        "pontuacao_minima": 16
    },
    "especialista_rpa": {
        "nome": "Especialista em RPA",
        "categoria": "Automação",
        "salario": "R$ 8.000 - R$ 22.000",
        "demanda": "Alta demanda",
        "crescimento": "Crescimento de 40% até 2030",
        "descricao": "Automatiza processos empresariais usando robôs de software.",
        "habilidades": ["RPA", "UiPath", "Blue Prism", "Automação", "Análise de Processos"],
        "perfil": ["analitico", "tecnico"],
        "pontuacao_minima": 14
    },

    # SAÚDE AVANÇADA
    "analista_dados_saude": {
        "nome": "Analista de Dados em Saúde",
        "categoria": "Saúde",
        "salario": "R$ 7.000 - R$ 20.000",
        "demanda": "Alta demanda",
        "crescimento": "Crescimento de 45% até 2030",
        "descricao": "Analisa grandes volumes de dados médicos para melhorar tratamentos e prevenir doenças.",
        "habilidades": ["Análise de Dados", "SQL", "Python", "Saúde Pública", "Estatística"],
        "perfil": ["analitico", "cientifico"],
        "pontuacao_minima": 14
    },
    "engenheiro_biomedico": {
        "nome": "Engenheiro Biomédico",
        "categoria": "Saúde",
        "salario": "R$ 8.000 - R$ 24.000",
        "demanda": "Crescente",
        "crescimento": "Crescimento de 38% até 2030",
        "descricao": "Desenvolve equipamentos médicos, próteses e tecnologias assistivas.",
        "habilidades": ["Engenharia", "Eletrônica", "Biomedicina", "Inovação", "Tecnologia Médica"],
        "perfil": ["tecnico", "cientifico"],
        "pontuacao_minima": 15
    },
    "especialista_longevidade": {
        "nome": "Especialista em Longevidade",
        "categoria": "Saúde",
        "salario": "R$ 6.000 - R$ 18.000",
        "demanda": "Emergente",
        "crescimento": "Crescimento de 55% até 2030",
        "descricao": "Foca em estratégias para prolongar a vida saudável e o bem-estar na terceira idade.",
        "habilidades": ["Gerontologia", "Nutrição", "Medicina Preventiva", "Bem-Estar", "Pesquisa"],
        "perfil": ["cientifico", "empatico"],
        "pontuacao_minima": 13
    },
    "consultor_genetico": {
        "nome": "Consultor Genético",
        "categoria": "Saúde",
        "salario": "R$ 9.000 - R$ 26.000",
        "demanda": "Crescente",
        "crescimento": "Crescimento de 42% até 2030",
        "descricao": "Interpreta testes genéticos e orienta pacientes sobre riscos e prevenção de doenças hereditárias.",
        "habilidades": ["Genética", "Biologia Molecular", "Aconselhamento", "Medicina", "Comunicação"],
        "perfil": ["cientifico", "empatico"],
        "pontuacao_minima": 15
    },

    # ARTES E MÍDIA DIGITAL
    "produtor_podcast": {
        "nome": "Produtor de Podcast",
        "categoria": "Criatividade",
        "salario": "R$ 4.000 - R$ 16.000",
        "demanda": "Alta demanda",
        "crescimento": "Crescimento de 50% até 2030",
        "descricao": "Cria e produz conteúdo em áudio para plataformas de streaming.",
        "habilidades": ["Edição de Áudio", "Roteiro", "Comunicação", "Marketing", "Storytelling"],
        "perfil": ["criativo", "comunicativo"],
        "pontuacao_minima": 12
    },
    "sound_designer": {
        "nome": "Sound Designer",
        "categoria": "Criatividade",
        "salario": "R$ 5.000 - R$ 18.000",
        "demanda": "Crescente",
        "crescimento": "Crescimento de 35% até 2030",
        "descricao": "Desenvolve design de som para games, aplicativos e produções audiovisuais.",
        "habilidades": ["Sound Design", "Edição de Áudio", "Música", "Games", "Criatividade"],
        "perfil": ["criativo", "tecnico"],
        "pontuacao_minima": 13
    },
    "designer_avatar": {
        "nome": "Designer de Avatar e Moda Virtual",
        "categoria": "Criatividade",
        "salario": "R$ 5.000 - R$ 20.000",
        "demanda": "Emergente",
        "crescimento": "Crescimento de 70% até 2030",
        "descricao": "Projeta avatares e roupas digitais para uso em metaversos e jogos.",
        "habilidades": ["Design 3D", "Moda", "Metaverso", "Blender", "Arte Digital"],
        "perfil": ["criativo", "inovador"],
        "pontuacao_minima": 14
    },

    # EDUCAÇÃO DIGITAL
    "especialista_aprendizado_personalizado": {
        "nome": "Especialista em Aprendizado Personalizado",
        "categoria": "Educação",
        "salario": "R$ 6.000 - R$ 16.000",
        "demanda": "Crescente",
        "crescimento": "Crescimento de 45% até 2030",
        "descricao": "Desenvolve trilhas de ensino adaptadas ao ritmo e estilo de cada aluno.",
        "habilidades": ["Pedagogia", "IA em Educação", "Tecnologia Educacional", "Psicologia", "Análise de Dados"],
        "perfil": ["educativo", "analitico"],
        "pontuacao_minima": 13
    },
    "instrutor_vr_educacao": {
        "nome": "Instrutor de Realidade Virtual para Educação",
        "categoria": "Educação",
        "salario": "R$ 7.000 - R$ 20.000",
        "demanda": "Emergente",
        "crescimento": "Crescimento de 60% até 2030",
        "descricao": "Cria experiências imersivas de aprendizado usando VR e AR.",
        "habilidades": ["Realidade Virtual", "Pedagogia", "Unity", "Design de Experiência", "Tecnologia"],
        "perfil": ["educativo", "tecnico"],
        "pontuacao_minima": 14
    },
    "professor_etica_digital": {
        "nome": "Professor de Ética Digital",
        "categoria": "Educação",
        "salario": "R$ 5.000 - R$ 14.000",
        "demanda": "Crescente",
        "crescimento": "Crescimento de 40% até 2030",
        "descricao": "Ensina sobre uso responsável de tecnologia e cidadania digital.",
        "habilidades": ["Pedagogia", "Ética", "Tecnologia", "Comunicação", "Segurança Digital"],
        "perfil": ["educativo", "social"],
        "pontuacao_minima": 12
    }
}

# 15 Perguntas expandidas para análise mais precisa
PERGUNTAS = [
    {
        "id": 1,
        "pergunta": "Em um projeto em grupo, você prefere:",
        "opcoes": [
            {"texto": "Liderar e coordenar as atividades", "perfis": ["lideranca", "estrategico"]},
            {"texto": "Pesquisar e analisar informações", "perfis": ["analitico", "cientifico"]},
            {"texto": "Criar apresentações e materiais visuais", "perfis": ["criativo", "comunicativo"]},
            {"texto": "Mediar conflitos e manter a harmonia", "perfis": ["empatico", "social"]},
            {"texto": "Implementar soluções técnicas", "perfis": ["tecnico", "inovador"]}
        ]
    },
    {
        "id": 2,
        "pergunta": "Qual ambiente de trabalho é mais atrativo para você?",
        "opcoes": [
            {"texto": "Escritório corporativo com equipes", "perfis": ["lideranca", "estrategico"]},
            {"texto": "Laboratório ou centro de pesquisa", "perfis": ["cientifico", "analitico"]},
            {"texto": "Estúdio criativo ou agência", "perfis": ["criativo", "inovador"]},
            {"texto": "Hospital, escola ou ONG", "perfis": ["social", "empatico"]},
            {"texto": "Empresa de tecnologia ou startup", "perfis": ["tecnico", "inovador"]}
        ]
    },
    {
        "id": 3,
        "pergunta": "Qual habilidade você gostaria de desenvolver mais?",
        "opcoes": [
            {"texto": "Liderança e gestão de pessoas", "perfis": ["lideranca", "estrategico"]},
            {"texto": "Pensamento crítico e resolução de problemas", "perfis": ["analitico", "cientifico"]},
            {"texto": "Criatividade e inovação", "perfis": ["criativo", "inovador"]},
            {"texto": "Comunicação e empatia", "perfis": ["empatico", "comunicativo"]},
            {"texto": "Programação e automação", "perfis": ["tecnico", "inovador"]}
        ]
    },
    {
        "id": 4,
        "pergunta": "Qual tipo de desafio mais te motiva?",
        "opcoes": [
            {"texto": "Criar um negócio do zero", "perfis": ["lideranca", "estrategico"]},
            {"texto": "Descobrir padrões em dados complexos", "perfis": ["analitico", "cientifico"]},
            {"texto": "Desenvolver uma campanha viral", "perfis": ["criativo", "comunicativo"]},
            {"texto": "Transformar a vida de uma comunidade", "perfis": ["social", "empatico"]},
            {"texto": "Construir uma aplicação inovadora", "perfis": ["tecnico", "inovador"]}
        ]
    },
    {
        "id": 5,
        "pergunta": "Como você prefere aprender coisas novas?",
        "opcoes": [
            {"texto": "Fazendo cursos de negócios e networking", "perfis": ["lideranca", "estrategico"]},
            {"texto": "Lendo pesquisas e estudos científicos", "perfis": ["cientifico", "analitico"]},
            {"texto": "Experimentando e criando projetos", "perfis": ["criativo", "inovador"]},
            {"texto": "Conversando com pessoas e trocando experiências", "perfis": ["social", "comunicativo"]},
            {"texto": "Praticando e testando na prática", "perfis": ["tecnico", "inovador"]}
        ]
    },
    {
        "id": 6,
        "pergunta": "Qual resultado mais te daria satisfação?",
        "opcoes": [
            {"texto": "Construir uma empresa de sucesso", "perfis": ["lideranca", "estrategico"]},
            {"texto": "Publicar uma descoberta científica", "perfis": ["cientifico", "analitico"]},
            {"texto": "Ver sua arte sendo admirada por milhões", "perfis": ["criativo", "comunicativo"]},
            {"texto": "Ajudar alguém a superar um problema", "perfis": ["empatico", "social"]},
            {"texto": "Criar uma tecnologia que mude o mundo", "perfis": ["tecnico", "inovador"]}
        ]
    },
    {
        "id": 7,
        "pergunta": "Qual área de conhecimento mais desperta sua curiosidade?",
        "opcoes": [
            {"texto": "Economia e mercado financeiro", "perfis": ["estrategico", "analitico"]},
            {"texto": "Ciências e matemática", "perfis": ["cientifico", "analitico"]},
            {"texto": "Arte, design e comunicação", "perfis": ["criativo", "comunicativo"]},
            {"texto": "Psicologia e comportamento humano", "perfis": ["empatico", "social"]},
            {"texto": "Tecnologia e inovação", "perfis": ["tecnico", "inovador"]}
        ]
    },
    {
        "id": 8,
        "pergunta": "Em qual situação você se sente mais confortável?",
        "opcoes": [
            {"texto": "Apresentando uma ideia para investidores", "perfis": ["lideranca", "comunicativo"]},
            {"texto": "Analisando dados para tomar uma decisão", "perfis": ["analitico", "estrategico"]},
            {"texto": "Criando algo do zero", "perfis": ["criativo", "inovador"]},
            {"texto": "Ajudando alguém em dificuldade", "perfis": ["empatico", "social"]},
            {"texto": "Resolvendo um problema técnico complexo", "perfis": ["tecnico", "analitico"]}
        ]
    },
    {
        "id": 9,
        "pergunta": "Qual impacto você gostaria de causar no mundo?",
        "opcoes": [
            {"texto": "Gerar empregos e movimentar a economia", "perfis": ["lideranca", "estrategico"]},
            {"texto": "Avançar o conhecimento científico", "perfis": ["cientifico", "analitico"]},
            {"texto": "Inspirar e emocionar pessoas", "perfis": ["criativo", "comunicativo"]},
            {"texto": "Reduzir desigualdades sociais", "perfis": ["social", "empatico"]},
            {"texto": "Automatizar processos e facilitar a vida", "perfis": ["tecnico", "inovador"]}
        ]
    },
    {
        "id": 10,
        "pergunta": "Qual motivação é mais importante para você?",
        "opcoes": [
            {"texto": "Reconhecimento e liderança", "perfis": ["lideranca", "estrategico"]},
            {"texto": "Descoberta e conhecimento", "perfis": ["cientifico", "analitico"]},
            {"texto": "Expressão e criatividade", "perfis": ["criativo", "comunicativo"]},
            {"texto": "Conexão e ajuda ao próximo", "perfis": ["empatico", "social"]},
            {"texto": "Inovação e eficiência", "perfis": ["tecnico", "inovador"]}
        ]
    },
    {
        "id": 11,
        "pergunta": "Como você lida com mudanças e incertezas?",
        "opcoes": [
            {"texto": "Vejo como oportunidades de crescimento", "perfis": ["lideranca", "inovador"]},
            {"texto": "Analiso dados para reduzir riscos", "perfis": ["analitico", "estrategico"]},
            {"texto": "Uso criatividade para encontrar soluções", "perfis": ["criativo", "inovador"]},
            {"texto": "Busco apoio e colaboração com outros", "perfis": ["social", "empatico"]},
            {"texto": "Desenvolvo sistemas para lidar com elas", "perfis": ["tecnico", "estrategico"]}
        ]
    },
    {
        "id": 12,
        "pergunta": "Qual tipo de problema você mais gosta de resolver?",
        "opcoes": [
            {"texto": "Desafios estratégicos de negócios", "perfis": ["estrategico", "lideranca"]},
            {"texto": "Enigmas científicos ou matemáticos", "perfis": ["cientifico", "analitico"]},
            {"texto": "Problemas que exigem soluções criativas", "perfis": ["criativo", "inovador"]},
            {"texto": "Conflitos interpessoais ou sociais", "perfis": ["empatico", "social"]},
            {"texto": "Bugs de sistema ou falhas técnicas", "perfis": ["tecnico", "analitico"]}
        ]
    },
    {
        "id": 13,
        "pergunta": "Qual aspecto do trabalho mais te energiza?",
        "opcoes": [
            {"texto": "Liderar equipes e tomar decisões importantes", "perfis": ["lideranca", "estrategico"]},
            {"texto": "Descobrir insights através de análise", "perfis": ["analitico", "cientifico"]},
            {"texto": "Criar algo único e original", "perfis": ["criativo", "inovador"]},
            {"texto": "Fazer diferença na vida das pessoas", "perfis": ["social", "empatico"]},
            {"texto": "Otimizar processos e sistemas", "perfis": ["tecnico", "estrategico"]}
        ]
    },
    {
        "id": 14,
        "pergunta": "Como você prefere trabalhar em equipe?",
        "opcoes": [
            {"texto": "Coordenando e direcionando o grupo", "perfis": ["lideranca", "estrategico"]},
            {"texto": "Fornecendo análises e dados precisos", "perfis": ["analitico", "cientifico"]},
            {"texto": "Contribuindo com ideias inovadoras", "perfis": ["criativo", "inovador"]},
            {"texto": "Facilitando comunicação e colaboração", "perfis": ["empatico", "comunicativo"]},
            {"texto": "Implementando soluções técnicas", "perfis": ["tecnico", "inovador"]}
        ]
    },
    {
        "id": 15,
        "pergunta": "Qual tema relacionado ao futuro mais te interessa?",
        "opcoes": [
            {"texto": "Empreendedorismo e novos modelos de negócio", "perfis": ["lideranca", "estrategico"]},
            {"texto": "Avanços científicos e descobertas", "perfis": ["cientifico", "analitico"]},
            {"texto": "Realidade virtual e experiências imersivas", "perfis": ["criativo", "tecnico"]},
            {"texto": "Sustentabilidade e impacto social", "perfis": ["sustentavel", "social"]},
            {"texto": "Inteligência artificial e automação", "perfis": ["tecnico", "inovador"]}
        ]
    }
]

def calcular_perfil(respostas):
    """Calcula o perfil baseado nas respostas do usuário"""
    pontuacao_perfis = {
        "lideranca": 0,
        "estrategico": 0,
        "analitico": 0,
        "cientifico": 0,
        "criativo": 0,
        "comunicativo": 0,
        "empatico": 0,
        "social": 0,
        "tecnico": 0,
        "inovador": 0,
        "educativo": 0,
        "sustentavel": 0
    }
    
    # Conta pontos para cada perfil baseado nas respostas
    for resposta in respostas:
        pergunta_id = resposta['pergunta_id']
        opcao_escolhida = resposta['opcao']
        
        # Encontra a pergunta correspondente
        pergunta = next((p for p in PERGUNTAS if p['id'] == pergunta_id), None)
        if pergunta and opcao_escolhida < len(pergunta['opcoes']):
            perfis_opcao = pergunta['opcoes'][opcao_escolhida]['perfis']
            for perfil in perfis_opcao:
                if perfil in pontuacao_perfis:
                    pontuacao_perfis[perfil] += 1
    
    # Determina o perfil principal
    perfil_principal = max(pontuacao_perfis, key=pontuacao_perfis.get)
    
    # Mapeia perfis para nomes amigáveis
    nomes_perfis = {
        "lideranca": "Líder",
        "estrategico": "Estratégico", 
        "analitico": "Analítico",
        "cientifico": "Científico",
        "criativo": "Criativo",
        "comunicativo": "Comunicativo",
        "empatico": "Empático",
        "social": "Social",
        "tecnico": "Técnico",
        "inovador": "Inovador",
        "educativo": "Educativo",
        "sustentavel": "Sustentável"
    }
    
    return {
        "perfil_principal": nomes_perfis.get(perfil_principal, "Analítico"),
        "pontuacao": pontuacao_perfis,
        "perfil_codigo": perfil_principal
    }

def recomendar_profissoes(perfil_resultado):
    """Recomenda profissões baseadas no perfil do usuário"""
    perfil_codigo = perfil_resultado['perfil_codigo']
    pontuacao_perfis = perfil_resultado['pontuacao']
    
    profissoes_recomendadas = []
    
    # Busca profissões que combinam com o perfil
    for codigo, profissao in PROFISSOES_DATABASE.items():
        pontuacao_profissao = 0
        
        # Calcula compatibilidade baseada nos perfis da profissão
        for perfil_prof in profissao['perfil']:
            if perfil_prof in pontuacao_perfis:
                pontuacao_profissao += pontuacao_perfis[perfil_prof]
        
        # Adiciona bônus se o perfil principal combina
        if perfil_codigo in profissao['perfil']:
            pontuacao_profissao += 3
            
        # Só recomenda se atingir pontuação mínima
        if pontuacao_profissao >= profissao.get('pontuacao_minima', 10):
            profissoes_recomendadas.append({
                **profissao,
                'compatibilidade': pontuacao_profissao
            })
    
    # Ordena por compatibilidade e retorna top 3
    profissoes_recomendadas.sort(key=lambda x: x['compatibilidade'], reverse=True)
    return profissoes_recomendadas[:3]

@app.route('/api/perguntas', methods=['GET'])
def get_perguntas():
    """Retorna as perguntas do quiz"""
    return jsonify(PERGUNTAS)

@app.route('/api/resultado', methods=['POST'])
def calcular_resultado():
    """Calcula o resultado do quiz baseado nas respostas"""
    try:
        data = request.get_json()
        respostas = data.get('respostas', [])
        
        if len(respostas) != 15:
            return jsonify({'error': 'Número inválido de respostas'}), 400
        
        # Calcula o perfil do usuário
        perfil_resultado = calcular_perfil(respostas)
        
        # Recomenda profissões
        profissoes_recomendadas = recomendar_profissoes(perfil_resultado)
        
        # Descrições dos perfis
        descricoes_perfis = {
            "Líder": "Você tem facilidade para liderar equipes, tomar decisões estratégicas e inspirar outras pessoas.",
            "Estratégico": "Você pensa de forma sistêmica, planeja a longo prazo e tem visão de negócios.",
            "Analítico": "Você tem facilidade para analisar dados, identificar padrões e tomar decisões baseadas em evidências.",
            "Científico": "Você é curioso, metódico e gosta de descobrir como as coisas funcionam.",
            "Criativo": "Você tem imaginação, originalidade e gosta de criar coisas novas e inovadoras.",
            "Comunicativo": "Você se expressa bem, conecta-se facilmente com pessoas e tem facilidade para transmitir ideias.",
            "Empático": "Você compreende as emoções dos outros e tem facilidade para ajudar e apoiar pessoas.",
            "Social": "Você se preocupa com questões sociais e tem motivação para causar impacto positivo na sociedade.",
            "Técnico": "Você gosta de trabalhar com tecnologia, resolver problemas complexos e implementar soluções.",
            "Inovador": "Você está sempre buscando novas formas de fazer as coisas e tem facilidade para se adaptar a mudanças.",
            "Educativo": "Você gosta de ensinar, compartilhar conhecimento e ajudar outros a aprender.",
            "Sustentável": "Você se preocupa com o meio ambiente e sustentabilidade."
        }
        
        resultado = {
            'perfil_principal': perfil_resultado['perfil_principal'],
            'descricao_perfil': descricoes_perfis.get(perfil_resultado['perfil_principal'], ''),
            'profissoes_recomendadas': profissoes_recomendadas
        }
        
        return jsonify(resultado)
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve(path):
    static_folder_path = app.static_folder
    if static_folder_path is None:
            return "Static folder not configured", 404

    if path != "" and os.path.exists(os.path.join(static_folder_path, path)):
        return send_from_directory(static_folder_path, path)
    else:
        index_path = os.path.join(static_folder_path, 'index.html')
        if os.path.exists(index_path):
            return send_from_directory(static_folder_path, 'index.html')
        else:
            return "index.html not found", 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

