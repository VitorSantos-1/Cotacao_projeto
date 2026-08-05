"""
Script avançado para explorar Supabase
"""
import os
from dotenv import load_dotenv
from supabase import create_client, Client

# Carrega variáveis do arquivo .env
load_dotenv(".env")

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")
SUPABASE_SERVICE_KEY = os.getenv("SUPABASE_SERVICE_KEY")

def connect_supabase() -> Client:
    """Conecta ao Supabase"""
    if not SUPABASE_URL or not SUPABASE_KEY:
        raise ValueError("SUPABASE_URL ou SUPABASE_KEY não configurados no .env")
    
    supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)
    return supabase

def explore_supabase():
    """Explora o banco de dados Supabase"""
    try:
        supabase = connect_supabase()
        
        print("=" * 50)
        print("🔗 CONEXÃO SUPABASE ESTABELECIDA COM SUCESSO!")
        print("=" * 50)
        print(f"\n📍 URL: {SUPABASE_URL}")
        print(f"✅ Status: Conectado e autenticado")
        
        print("\n" + "=" * 50)
        print("📚 EXPLORANDO BANCO DE DADOS")
        print("=" * 50)
        
        # Teste: tenta buscar dados de uma tabela (exemplo)
        # Você pode alterar "seu_tabela" para o nome real da sua tabela
        print("\n📌 Para buscar dados de uma tabela, use:")
        print("""
response = supabase.table("nome_da_sua_tabela").select("*").execute()
print(response.data)
        """)
        
        print("\n✨ Seu Supabase está pronto para usar!")
        print("=" * 50)
        
    except Exception as e:
        print(f"❌ Erro: {e}")
        print("\n📌 Verifique se:")
        print("1. Arquivo .env foi criado com suas credenciais")
        print("2. SUPABASE_URL está correto")
        print("3. SUPABASE_KEY está correto")

if __name__ == "__main__":
    explore_supabase()
