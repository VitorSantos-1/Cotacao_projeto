-- BLOCO 3, Row Level Security (a blindagem entre vendedores)
-------------------------------------------------------------

-- Ativa RLS em todas as tabelas
ALTER TABLE public.perfis ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.fornecedores ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.categorias ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.produtos ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.cotacoes ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.sugestoes_produto ENABLE ROW LEVEL SECURITY;

-- ==========================================
-- POLÍTICAS: PERFIS
-- ==========================================
-- Usuário vê e edita apenas o próprio perfil
CREATE POLICY "perfil_proprio" ON public.perfis
  FOR ALL USING (auth.uid() = id);

-- Admin vê todos os perfis
CREATE POLICY "admin_ve_todos_perfis" ON public.perfis
  FOR ALL USING (
    EXISTS (
      SELECT 1 FROM public.perfis p
      WHERE p.id = auth.uid() AND p.role = 'admin'
    )
  );

-- ==========================================
-- POLÍTICAS: FORNECEDORES
-- ==========================================
-- Vendedor vê apenas o próprio fornecedor
CREATE POLICY "vendedor_ve_proprio_fornecedor" ON public.fornecedores
  FOR SELECT USING (user_id = auth.uid());

-- Comprador e Admin veem todos
CREATE POLICY "comprador_admin_ve_fornecedores" ON public.fornecedores
  FOR ALL USING (
    EXISTS (
      SELECT 1 FROM public.perfis p
      WHERE p.id = auth.uid() AND p.role IN ('comprador', 'admin')
    )
  );

-- ==========================================
-- POLÍTICAS: CATEGORIAS E PRODUTOS
-- ==========================================
-- Todos os usuários ativos leem categorias e produtos (para preencher o form)
CREATE POLICY "todos_leem_categorias" ON public.categorias
  FOR SELECT USING (
    EXISTS (SELECT 1 FROM public.perfis p WHERE p.id = auth.uid() AND p.ativo = true)
  );

CREATE POLICY "todos_leem_produtos" ON public.produtos
  FOR SELECT USING (
    EXISTS (SELECT 1 FROM public.perfis p WHERE p.id = auth.uid() AND p.ativo = true)
  );

-- Somente comprador/admin gerencia produtos e categorias
CREATE POLICY "comprador_admin_gerencia_produtos" ON public.produtos
  FOR ALL USING (
    EXISTS (
      SELECT 1 FROM public.perfis p
      WHERE p.id = auth.uid() AND p.role IN ('comprador', 'admin')
    )
  );

CREATE POLICY "comprador_admin_gerencia_categorias" ON public.categorias
  FOR ALL USING (
    EXISTS (
      SELECT 1 FROM public.perfis p
      WHERE p.id = auth.uid() AND p.role IN ('comprador', 'admin')
    )
  );

-- ==========================================
-- POLÍTICAS: COTAÇÕES (o mais crítico)
-- ==========================================
-- Vendedor insere cotações
CREATE POLICY "vendedor_insere_cotacao" ON public.cotacoes
  FOR INSERT WITH CHECK (
    auth.uid() = user_id AND
    EXISTS (SELECT 1 FROM public.perfis p WHERE p.id = auth.uid() AND p.ativo = true)
  );

-- Vendedor vê APENAS as próprias cotações
CREATE POLICY "vendedor_ve_proprias_cotacoes" ON public.cotacoes
  FOR SELECT USING (
    auth.uid() = user_id AND
    EXISTS (
      SELECT 1 FROM public.perfis p WHERE p.id = auth.uid() AND p.role = 'vendedor'
    )
  );

-- Comprador e Admin veem TODAS as cotações
CREATE POLICY "comprador_admin_ve_cotacoes" ON public.cotacoes
  FOR ALL USING (
    EXISTS (
      SELECT 1 FROM public.perfis p
      WHERE p.id = auth.uid() AND p.role IN ('comprador', 'admin')
    )
  );

-- ==========================================
-- POLÍTICAS: SUGESTÕES DE PRODUTO
-- ==========================================
CREATE POLICY "vendedor_cria_sugestao" ON public.sugestoes_produto
  FOR INSERT WITH CHECK (auth.uid() = created_by);

CREATE POLICY "comprador_admin_gerencia_sugestoes" ON public.sugestoes_produto
  FOR ALL USING (
    EXISTS (
      SELECT 1 FROM public.perfis p
      WHERE p.id = auth.uid() AND p.role IN ('comprador', 'admin')
    )
  );