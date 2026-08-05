-- BLOCO 4, Dados iniciais (categorias e primeiro admin)
--------------------------------------------------------

-- Categorias base (você pode adicionar mais depois)
INSERT INTO public.categorias (nome) VALUES
  ('Frios'),
  ('Frango'),
  ('Grãos'),
  ('Laticínios'),
  ('Bebidas'),
  ('Limpeza'),
  ('Descartáveis'),
  ('Hortifruti'),
  ('Carnes'),
  ('Mercearia');

-- IMPORTANTE: depois de criar sua conta no sistema,
-- rode esse comando trocando o email pelo seu
-- para se tornar admin e ativar sua conta:
UPDATE public.perfis
SET role = 'admin', ativo = true
WHERE id = (
  SELECT id FROM auth.users WHERE email = 'SEU_EMAIL_AQUI@email.com'
);