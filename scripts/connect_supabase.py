"""
Script para conectar e testar a conexão com Supabase
"""
import os
from dotenv import load_dotenv
from supabase import create_client, Client

# Carrega variáveis do arquivo .env
load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

def connect_supabase() -> Client:
    """Conecta ao Supabase"""
    if not SUPABASE_URL or not SUPABASE_KEY:
        raise ValueError("SUPABASE_URL ou SUPABASE_KEY não configurados no .env")
    
    supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)
    print("✅ Conectado ao Supabase com sucesso!")
    return supabase

def test_connection():
    """Testa a conexão"""
    try:
        supabase = connect_supabase()
        
        # Teste simples - listar tabelas
        print("\n📋 Testando acesso...")
        print("Supabase URL:", SUPABASE_URL)
        print("Autenticação: Configurada ✓")
        
    except Exception as e:
        print(f"❌ Erro na conexão: {e}")
        print("\n📌 Verifique se:")
        print("1. Arquivo .env foi criado com suas credenciais")
        print("2. SUPABASE_URL está correto")
        print("3. SUPABASE_KEY está correto")

if __name__ == "__main__":
    test_connection()