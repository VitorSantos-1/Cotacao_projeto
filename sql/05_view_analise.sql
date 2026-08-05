-- BLOCO 5, View de análise do comprador (o coração dos cálculos)
-----------------------------------------------------------------

CREATE OR REPLACE VIEW public.analise_cotacoes AS
SELECT
  c.id,
  c.data_cotacao,
  c.status,
  c.observacoes,
  c.mercadologico,
  c.condicao_acima,
  c.preco_acima,
  c.fator_embalagem,
  c.preco_embalagem,
  c.preco_unitario,

  -- Produto
  p.id AS produto_id,
  p.nome AS produto,
  p.unidade_base,
  p.preco_venda,
  p.custo_atual,

  -- Categoria
  cat.nome AS categoria,

  -- Fornecedor
  f.id AS fornecedor_id,
  f.nome AS fornecedor,

  -- Melhor preço entre todos os fornecedores para este produto
  MIN(c2.preco_unitario) OVER (PARTITION BY c.produto_id) AS melhor_preco,

  -- Nossa margem atual: (preco_venda - custo_atual) / preco_venda
  CASE
    WHEN p.preco_venda > 0
    THEN ROUND(((p.preco_venda - p.custo_atual) / p.preco_venda) * 100, 2)
    ELSE NULL
  END AS nossa_margem_atual_pct,

  -- Margem do fornecedor: (preco_venda - preco_unitario_fornecedor) / preco_venda
  CASE
    WHEN p.preco_venda > 0
    THEN ROUND(((p.preco_venda - c.preco_unitario) / p.preco_venda) * 100, 2)
    ELSE NULL
  END AS margem_fornecedor_pct,

  -- Diferença entre as margens
  CASE
    WHEN p.preco_venda > 0
    THEN ROUND(
      (((p.preco_venda - c.preco_unitario) / p.preco_venda) -
       ((p.preco_venda - p.custo_atual) / p.preco_venda)) * 100,
      2
    )
    ELSE NULL
  END AS diferenca_margens_pct,

  -- Diferença do nosso custo com o do fornecedor (R$)
  ROUND(p.custo_atual - c.preco_unitario, 4) AS diferenca_custo_rs,

  -- Diferença do preço do fornecedor com o melhor preço (R$)
  ROUND(c.preco_unitario - MIN(c2.preco_unitario) OVER (PARTITION BY c.produto_id), 4)
    AS diferenca_melhor_preco_rs

FROM public.cotacoes c
JOIN public.produtos p ON c.produto_id = p.id
JOIN public.categorias cat ON p.categoria_id = cat.id
JOIN public.fornecedores f ON c.fornecedor_id = f.id
JOIN public.cotacoes c2 ON c2.produto_id = c.produto_id;