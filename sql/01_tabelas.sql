-- BLOCO 1, Tabelas principais
------------------------------

-- PERFIS DE USUÁRIO (extensão da auth do Supabase)
CREATE TABLE public.perfis (
  id UUID REFERENCES auth.users(id) ON DELETE CASCADE PRIMARY KEY,
  nome TEXT NOT NULL,
  telefone TEXT,
  role TEXT NOT NULL DEFAULT 'vendedor' CHECK (role IN ('vendedor', 'comprador', 'admin')),
  ativo BOOLEAN NOT NULL DEFAULT false,
  created_at TIMESTAMPTZ DEFAULT NOW()
);

-- FORNECEDORES
CREATE TABLE public.fornecedores (
  id UUID DEFAULT gen_random_uuid() PRIMARY KEY,
  nome TEXT NOT NULL,
  user_id UUID REFERENCES public.perfis(id) ON DELETE SET NULL,
  ativo BOOLEAN DEFAULT true,
  created_at TIMESTAMPTZ DEFAULT NOW()
);

-- CATEGORIAS
CREATE TABLE public.categorias (
  id UUID DEFAULT gen_random_uuid() PRIMARY KEY,
  nome TEXT NOT NULL UNIQUE,
  created_at TIMESTAMPTZ DEFAULT NOW()
);

-- PRODUTOS PADRONIZADOS
CREATE TABLE public.produtos (
  id UUID DEFAULT gen_random_uuid() PRIMARY KEY,
  nome TEXT NOT NULL,
  nome_normalizado TEXT NOT NULL,
  categoria_id UUID REFERENCES public.categorias(id),
  unidade_base TEXT NOT NULL DEFAULT 'un',
  preco_venda NUMERIC(10,4),
  custo_atual NUMERIC(10,4),
  ativo BOOLEAN DEFAULT true,
  created_at TIMESTAMPTZ DEFAULT NOW()
);

-- COTAÇÕES
CREATE TABLE public.cotacoes (
  id UUID DEFAULT gen_random_uuid() PRIMARY KEY,
  fornecedor_id UUID REFERENCES public.fornecedores(id) NOT NULL,
  produto_id UUID REFERENCES public.produtos(id) NOT NULL,
  user_id UUID REFERENCES public.perfis(id) NOT NULL,
  data_cotacao DATE NOT NULL DEFAULT CURRENT_DATE,
  fator_embalagem NUMERIC(10,4) NOT NULL,
  preco_embalagem NUMERIC(10,4) NOT NULL,
  preco_unitario NUMERIC(10,4) GENERATED ALWAYS AS (preco_embalagem  fator_embalagem) STORED,
  condicao_acima NUMERIC(10,4),
  preco_acima NUMERIC(10,4),
  mercadologico TEXT,
  observacoes TEXT,
  status TEXT DEFAULT 'pendente' CHECK (status IN ('pendente', 'em_analise', 'aprovado', 'reprovado')),
  created_at TIMESTAMPTZ DEFAULT NOW()
);

-- SUGESTÕES DE PRODUTOS (sistema inteligente)
CREATE TABLE public.sugestoes_produto (
  id UUID DEFAULT gen_random_uuid() PRIMARY KEY,
  nome_digitado TEXT NOT NULL,
  produto_sugerido_id UUID REFERENCES public.produtos(id),
  aprovado BOOLEAN DEFAULT false,
  created_by UUID REFERENCES public.perfis(id),
  created_at TIMESTAMPTZ DEFAULT NOW()
);