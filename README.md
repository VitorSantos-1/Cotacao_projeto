# Sistema de Cotação de Fornecedores (PostgreSQL / Supabase)

Back-end de um sistema de cotação de preços com fornecedores, construído em PostgreSQL/Supabase com Row
Level Security, triggers, views de análise e controle de acesso por papéis (vendedor, comprador e
admin). O projeto demonstra modelagem relacional e segurança de dados no nível do banco — não apenas na
aplicação — que é o que separa um protótipo de um sistema confiável para múltiplos usuários.

> **Nota de confidencialidade:** todos os dados presentes neste repositório (planilhas, seeds,
> exemplos) são fictícios, gerados aleatoriamente apenas para demonstração. Os dados reais da operação
> são confidenciais e estão protegidos — nenhum dado real, credencial ou informação de terceiros foi
> incluído aqui.

---

## Visão Geral

O sistema organiza o processo de cotação entre quem oferta (vendedores/fornecedores) e quem compra. A
segurança por linha (RLS) garante que cada vendedor só enxergue as próprias cotações, enquanto o
comprador compara todas através de uma view de análise que centraliza os cálculos. Uma camada em Python
integra e migra o catálogo. Toda a lógica sensível — isolamento de dados e comparação — vive no banco, o
que reduz a superfície de erro da aplicação.

## Contexto de Negócio

Cotar com vários fornecedores em planilhas ou e-mails gera confusão: preços se misturam, um vendedor vê
a proposta do outro e a comparação final é feita à mão. Isso compromete tanto a isonomia do processo
quanto a qualidade da decisão de compra. Estruturar a cotação em um banco com regras de acesso e uma
view de comparação devolve controle, sigilo entre concorrentes e uma base objetiva para escolher o
melhor preço.

## O Problema que Resolve

- **Falta de sigilo entre fornecedores** que cotam o mesmo item.
- **Comparação manual** de propostas, lenta e sujeita a erro.
- **Ausência de controle de acesso por papel** (quem vê e faz o quê).
- **Cadastro de catálogo disperso**, sem uma base única.

## Público e Decisões Apoiadas

- **Vendedor/Fornecedor:** envia cotações vendo apenas as próprias (isolado por RLS).
- **Comprador:** compara propostas pela view de análise e decide o melhor preço.
- **Admin:** gerencia usuários e catálogo.

## Impacto e Valor Gerado

- Garante sigilo entre concorrentes por segurança no nível do banco (RLS).
- Automatiza a comparação de propostas com uma view de análise dedicada.
- Padroniza o cadastro e a migração do catálogo via integração Python.
- Cria um processo de cotação auditável e controlado por papéis.

---

## Arquitetura e Abordagem Técnica

```text
Vendedor  -> envia cotações (RLS isola por vendedor)
Comprador -> compara pela VIEW de análise -> decide o melhor preço
Admin     -> gerencia usuários e catálogo
```

- **Modelagem relacional** completa: perfis, fornecedores, categorias, produtos e cotações
  (`sql/01_tabelas.sql`).
- **Row Level Security** (`sql/03_rls.sql`): cada vendedor só enxerga as próprias cotações.
- **Trigger** (`sql/02_trigger_perfil.sql`): cria o perfil do usuário automaticamente no cadastro.
- **View de análise do comprador** (`sql/05_view_analise.sql`): centraliza os cálculos de comparação.
- **Integração em Python** (`scripts/`): usa o cliente `supabase-py` para conexão e migração do catálogo.

## Stack

PostgreSQL - Supabase - Python (supabase-py) - SQL - Row Level Security - Triggers - Views - HTML.

## Como Aplicar

```bash
# no editor SQL do Supabase, rode em ordem:
# sql/01_tabelas.sql -> 02_trigger_perfil.sql -> 03_rls.sql -> 04_dados_iniciais.sql -> 05_view_analise.sql

# integração Python:
pip install supabase python-dotenv
copy .env.example .env      # preencha SUPABASE_URL / KEY
python scripts/connect_supabase.py
```

## Estrutura do Projeto

```text
sql/01_tabelas.sql          -> Modelagem relacional (perfis, fornecedores, produtos, cotações)
sql/02_trigger_perfil.sql   -> Trigger de criação automática de perfil
sql/03_rls.sql              -> Políticas de Row Level Security
sql/04_dados_iniciais.sql   -> Dados iniciais (fictícios)
sql/05_view_analise.sql     -> View de comparação de cotações (comprador)
scripts/                    -> Integração Python (conexão, exploração, migração do catálogo)
frontend/beta.html          -> Interface de demonstração
```

## Autor

José Vitor Santos Pinheiro — Análise de Dados e Inteligência Comercial (Varejo, Indústria e Distribuição).
Contato: vytorsantt@gmail.com
