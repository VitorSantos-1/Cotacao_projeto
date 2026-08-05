import json
import re

file_path = 'index copy.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

match = re.search(r'(<script id="catalogo-data" type="application/json">\s*)(.*?)(\s*</script>)', content, re.DOTALL)
if not match:
    print("Catalog not found")
    exit(1)

prefix = match.group(1)
data_str = match.group(2)
suffix = match.group(3)

catalog = json.loads(data_str)

# Map existing items to new categories
def map_category(item):
    cat = item.get("Categoria", "")
    sub = item.get("Subcategoria", "")
    prod = item.get("Produto", "")
    
    # 1. Analista de Dados
    # 2. Analista de BI
    # 3. Engenheiro de Dados
    # 4. Cientista de Dados
    # 5. Automação vba, js, python...
    # 6. Engenharia de IA
    # 7. Planilhas Profissionais
    # 8. Projetos de BI
    # 9. Consultoria em Dados
    
    text = f"{cat} {sub} {prod}".lower()
    
    if "planilha" in text or "excel" in text:
        return "Planilhas Profissionais"
    elif "automa" in text or "rpa" in text or "vba" in text or "python" in text:
        return "Automação"
    elif "ia" in text or "inteligência artificial" in text or "llm" in text or "gpt" in text or "machine learning" in text:
        if "engenharia" in text or "ops" in text or "deploy" in text:
            return "Engenharia de IA"
        return "Cientista de Dados"
    elif "dashboard" in text or "power bi" in text or "tableau" in text or "looker" in text:
        if "projeto" in text or "end-to-end" in text or "implantação" in text:
            return "Projetos de BI"
        return "Analista de BI"
    elif "engenharia de dados" in text or "pipeline" in text or "data warehouse" in text or "etl" in text or "dbt" in text:
        return "Engenheiro de Dados"
    elif "ciência de dados" in text or "modelo" in text or "predição" in text or "churn" in text:
        return "Cientista de Dados"
    elif "consultoria" in text or "diagnóstico" in text or "estratégia" in text or "governança" in text or "roadmap" in text:
        return "Consultoria em Dados"
    elif "análise" in text or "exploratória" in text or "estudo" in text:
        return "Analista de Dados"
    
    # Default fallbacks
    if "bi" in text:
        return "Analista de BI"
    return "Consultoria em Dados"

for item in catalog:
    item["Categoria"] = map_category(item)

# Let's add some NEW cards to populate the categories
new_items = [
    # Analista de Dados
    {
        "Categoria": "Analista de Dados",
        "Subcategoria": "Análise Exploratória",
        "Produto": "Análise Exploratória de Vendas",
        "Descrição": "Mergulho profundo nos dados de vendas para identificar tendências, sazonalidades e anomalias ocultas nos resultados da sua empresa.",
        "Entregáveis": "Relatório em PDF com insights visuais; Apresentação executiva; Base de dados limpa.",
        "Prazo típico": "1 a 2 semanas",
        "Preço mín (R$)": 1500,
        "Preço máx (R$)": 3000,
        "Modelo de preço": "Projeto",
        "Complexidade": "Baixa",
        "Tecnologias principais": "Python; Pandas; SQL",
        "Imagem": "https://source.unsplash.com/featured/800x500?data,analysis"
    },
    {
        "Categoria": "Analista de Dados",
        "Subcategoria": "Limpeza de Dados",
        "Produto": "Saneamento e Estruturação de Base de Dados",
        "Descrição": "Serviço dedicado a limpar bases de dados sujas, tratar valores nulos e padronizar registros para torná-los prontos para análises e modelagem.",
        "Entregáveis": "Dataset estruturado; Documentação de regras de negócio aplicadas; Script de limpeza.",
        "Prazo típico": "1 a 3 semanas",
        "Preço mín (R$)": 1000,
        "Preço máx (R$)": 2500,
        "Modelo de preço": "Projeto",
        "Complexidade": "Média",
        "Tecnologias principais": "Python; SQL; Excel",
        "Imagem": "https://source.unsplash.com/featured/800x500?clean,data"
    },
    # Analista de BI
    {
        "Categoria": "Analista de BI",
        "Subcategoria": "Manutenção",
        "Produto": "Suporte e Manutenção de Dashboards",
        "Descrição": "Serviço de suporte contínuo para atualizar, corrigir bugs e adicionar novas visões a dashboards Power BI ou Tableau existentes.",
        "Entregáveis": "SLA de atendimento; Atualizações de relatórios; Correções de DAX/M.",
        "Prazo típico": "Recorrente",
        "Preço mín (R$)": 800,
        "Preço máx (R$)": 2000,
        "Modelo de preço": "Mensal",
        "Complexidade": "Baixa",
        "Tecnologias principais": "Power BI; DAX; Tableau",
        "Imagem": "https://source.unsplash.com/featured/800x500?dashboard,support"
    },
    # Engenheiro de Dados
    {
        "Categoria": "Engenheiro de Dados",
        "Subcategoria": "Pipelines ETL",
        "Produto": "Desenvolvimento de Pipeline ETL Customizado",
        "Descrição": "Criação de fluxos de dados automatizados para extrair informações de APIs externas ou bancos de dados, transformar e carregar no seu Data Warehouse.",
        "Entregáveis": "Código do pipeline; Orquestração configurada (Airflow/Prefect); Documentação técnica.",
        "Prazo típico": "3 a 5 semanas",
        "Preço mín (R$)": 4000,
        "Preço máx (R$)": 8000,
        "Modelo de preço": "Projeto",
        "Complexidade": "Média",
        "Tecnologias principais": "Python; Apache Airflow; SQL",
        "Imagem": "https://source.unsplash.com/featured/800x500?database,pipeline"
    },
    # Cientista de Dados
    {
        "Categoria": "Cientista de Dados",
        "Subcategoria": "Previsão",
        "Produto": "Modelo de Previsão de Demanda",
        "Descrição": "Desenvolvimento de modelos de Machine Learning (Séries Temporais) para prever a demanda futura de produtos, otimizando o estoque e evitando rupturas.",
        "Entregáveis": "Modelo treinado; Relatório de acurácia; Script de predição em lote.",
        "Prazo típico": "4 a 6 semanas",
        "Preço mín (R$)": 6000,
        "Preço máx (R$)": 12000,
        "Modelo de preço": "Projeto",
        "Complexidade": "Alta",
        "Tecnologias principais": "Python; scikit-learn; Prophet",
        "Imagem": "https://source.unsplash.com/featured/800x500?forecast,chart"
    },
    # Automação
    {
        "Categoria": "Automação",
        "Subcategoria": "RPA",
        "Produto": "Automação de Tarefas Repetitivas (RPA)",
        "Descrição": "Criação de robôs para automatizar a extração de dados de portais, preenchimento de formulários e rotinas diárias massantes, usando Python ou ferramentas RPA.",
        "Entregáveis": "Script executável; Manual de uso; Tratamento de erros.",
        "Prazo típico": "2 a 4 semanas",
        "Preço mín (R$)": 2500,
        "Preço máx (R$)": 6000,
        "Modelo de preço": "Projeto",
        "Complexidade": "Média",
        "Tecnologias principais": "Python; Selenium; UiPath",
        "Imagem": "https://source.unsplash.com/featured/800x500?robot,automation"
    },
    {
        "Categoria": "Automação",
        "Subcategoria": "VBA",
        "Produto": "Macros e Automação no Excel (VBA)",
        "Descrição": "Desenvolvimento de rotinas em VBA para automatizar a geração de relatórios complexos, formatação de planilhas e integração com outros aplicativos Office.",
        "Entregáveis": "Planilha com código VBA embarcado; Botões de execução na interface.",
        "Prazo típico": "1 a 2 semanas",
        "Preço mín (R$)": 800,
        "Preço máx (R$)": 2500,
        "Modelo de preço": "Projeto",
        "Complexidade": "Baixa",
        "Tecnologias principais": "Excel; VBA",
        "Imagem": "https://source.unsplash.com/featured/800x500?excel,macro"
    },
    # Engenharia de IA
    {
        "Categoria": "Engenharia de IA",
        "Subcategoria": "LLM",
        "Produto": "Implementação de RAG com LLMs Privados",
        "Descrição": "Criação de um sistema de Perguntas e Respostas baseado em Retrieval-Augmented Generation (RAG) usando a base de conhecimento interna da empresa.",
        "Entregáveis": "API de consulta; Interface de Chat; Banco de Dados Vetorial configurado.",
        "Prazo típico": "4 a 8 semanas",
        "Preço mín (R$)": 8000,
        "Preço máx (R$)": 15000,
        "Modelo de preço": "Projeto",
        "Complexidade": "Alta",
        "Tecnologias principais": "LangChain; OpenAI; Pinecone; Python",
        "Imagem": "https://source.unsplash.com/featured/800x500?artificial,intelligence"
    },
    # Planilhas Profissionais
    {
        "Categoria": "Planilhas Profissionais",
        "Subcategoria": "Controle Financeiro",
        "Produto": "Planilha de Fluxo de Caixa Avançado",
        "Descrição": "Uma ferramenta robusta em Excel/Google Sheets para controle total de entradas e saídas, projeção de caixa e análise de DRE, com dashboards integrados.",
        "Entregáveis": "Arquivo Excel/Sheets pronto para uso; Vídeo tutorial de preenchimento.",
        "Prazo típico": "1 semana",
        "Preço mín (R$)": 500,
        "Preço máx (R$)": 1200,
        "Modelo de preço": "Produto Único",
        "Complexidade": "Baixa",
        "Tecnologias principais": "Microsoft Excel; Google Sheets",
        "Imagem": "https://source.unsplash.com/featured/800x500?finance,spreadsheet"
    },
    # Projetos de BI
    {
        "Categoria": "Projetos de BI",
        "Subcategoria": "Implementação End-to-End",
        "Produto": "Projeto Completo de Business Intelligence",
        "Descrição": "Desde a modelagem do Data Warehouse até a entrega de painéis de indicadores (KPIs) para todas as áreas do negócio, garantindo uma fonte única de verdade.",
        "Entregáveis": "Data Warehouse modelado; Dashboards no Power BI; Treinamento para usuários.",
        "Prazo típico": "2 a 3 meses",
        "Preço mín (R$)": 15000,
        "Preço máx (R$)": 30000,
        "Modelo de preço": "Projeto",
        "Complexidade": "Alta",
        "Tecnologias principais": "SQL; Power BI; Azure/AWS",
        "Imagem": "https://source.unsplash.com/featured/800x500?business,metrics"
    },
    # Consultoria em Dados
    {
        "Categoria": "Consultoria em Dados",
        "Subcategoria": "Arquitetura",
        "Produto": "Desenho de Arquitetura de Dados em Nuvem",
        "Descrição": "Assessoria especializada para definir a melhor arquitetura de dados (Data Lake, Data Mesh, etc) na nuvem (AWS/GCP/Azure) para sua necessidade e budget.",
        "Entregáveis": "Diagrama de arquitetura; Estimativa de custos de cloud; Recomendações de ferramentas.",
        "Prazo típico": "2 a 4 semanas",
        "Preço mín (R$)": 5000,
        "Preço máx (R$)": 10000,
        "Modelo de preço": "Projeto",
        "Complexidade": "Média",
        "Tecnologias principais": "AWS; GCP; Azure",
        "Imagem": "https://source.unsplash.com/featured/800x500?cloud,architecture"
    }
]

catalog.extend(new_items)

# Add a specific function to map "Automação" instead of adding "vba, js, python..." to every card.
# The user said "Automação vba, js, python..." - we can map the category strictly to "Automação". 
# The UI will group them nicely.

new_data_str = json.dumps(catalog, indent=2, ensure_ascii=False)
new_content = content[:match.start(2)] + new_data_str + content[match.end(2):]

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(new_content)

print(f"Migration completed. New catalog size: {len(catalog)}")
