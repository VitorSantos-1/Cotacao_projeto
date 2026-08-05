# 💰 Sistema de Cotação de Fornecedores (PostgreSQL / Supabase)

Back-end de um sistema de **cotação de preços com fornecedores**, construído em **PostgreSQL/Supabase** com
**Row Level Security**, **triggers**, **views de análise** e **controle de acesso por papéis** (vendedor / comprador / admin).

> ⚠️ **Aviso sobre os dados**
> Todos os dados presentes neste repositório (planilhas, seeds, exemplos) são **fictícios** e foram
> **gerados aleatoriamente apenas para demonstração**. Os dados reais da operação em que o projeto
> foi utilizado são **confidenciais e estão protegidos** — nenhum dado real, credencial ou informação
> de terceiros foi incluído aqui.

## 🎯 Destaques
- **Modelagem relacional** completa: perfis, fornecedores, categorias, produtos e cotações (`sql/01_tabelas.sql`).
- **Segurança por linha (RLS)**: cada vendedor só enxerga as próprias cotações (`sql/03_rls.sql`).
- **Trigger** que cria o perfil do usuário automaticamente no cadastro (`sql/02_trigger_perfil.sql`).
- **View de análise do comprador** — o "coração" dos cálculos de comparação (`sql/05_view_analise.sql`).
- **Camada de integração em Python** (`scripts/`) usando o cliente `supabase-py` para conexão e **migração do catálogo**.

## 🏗️ Papéis e fluxo
```
Vendedor  ─► envia cotações (RLS isola por vendedor)
Comprador ─► compara via VIEW de análise  ─► decide melhor preço
Admin     ─► gerencia usuários e catálogo
```

## 🧑‍💻 Stack
`PostgreSQL` · `Supabase` · `Python (supabase-py)` · `SQL` · `RLS` · `Triggers` · `Views` · `HTML`

## ▶️ Como aplicar
```bash
# no editor SQL do Supabase, rode em ordem:
sql/01_tabelas.sql → 02_trigger_perfil.sql → 03_rls.sql → 04_dados_iniciais.sql → 05_view_analise.sql
# integração Python:
pip install supabase python-dotenv
copy .env.example .env      # preencha SUPABASE_URL / KEY
python scripts/connect_supabase.py
```

---

### 🧰 Competências demonstradas
`PostgreSQL` · `Row Level Security` · `Triggers & Views` · `Modelagem Relacional` · `Supabase`

### 👤 Autor
**José Vitor Santos Pinheiro** — Analista de Dados / BI / Ciência de Dados
· vytorsantt@gmail.com
