import logging
import csv
import random
import time
from datetime import datetime

# --- Configuração 1: Log Geral do Sistema ---
# Cria um arquivo .log tradicional
logging.basicConfig(filename='sistema_seguranca.log', level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

# --- Configuração 2: Arquivo CSV para Relatório ---
# Necessário para o item "Visualização dos arquivos .csv de saída" do PDF
ARQUIVO_CSV = 'relatorio_logs.csv'

def inicializar_csv():
    """Cria o cabeçalho do CSV se o arquivo ainda não existir."""
    try:
        # Tenta criar o arquivo (modo 'x'). Se já existe, ignora.
        with open(ARQUIVO_CSV, 'x', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(["Data_Hora", "Nivel", "Evento", "Detalhes", "IP_Origem"])
    except FileExistsError:
        pass

def registrar_evento(nivel, evento, detalhes, ip):
    """Função central que grava tanto no LOG quanto no CSV."""
    
    # 1. Grava no arquivo de texto (.log)
    msg = f"{evento} - {detalhes} - IP: {ip}"
    if nivel == "INFO":
        logging.info(msg)
    elif nivel == "WARNING":
        logging.warning(msg)
    elif nivel == "ERROR":
        logging.error(msg)
    
    # 2. Grava no arquivo de planilha (.csv)
    with open(ARQUIVO_CSV, 'a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        # Registra data atual automaticamente
        writer.writerow([datetime.now().strftime("%Y-%m-%d %H:%M:%S"), nivel, evento, detalhes, ip])

def simular_atividades():
    """Gera os dados falsos para cumprir os requisitos do trabalho."""
    ips = ["192.168.1.10", "10.0.0.5", "172.16.0.1", "45.33.22.11"]

    print("--- 🛡️  Iniciando Simulação de Monitoramento de Segurança 🛡️ ---")
    time.sleep(1)

    # Requisito: Tentativas de login inválidas 
    print(f"[{datetime.now()}] Simulando ataque de Força Bruta (Brute Force)...")
    for _ in range(3):
        ip = random.choice(ips)
        registrar_evento("WARNING", "FALHA_LOGIN", "Senha incorreta para usuario admin", ip)
        time.sleep(0.5)

    # Requisito: Modificações em arquivos críticos 
    print(f"[{datetime.now()}] Simulando alteração de integridade de arquivo...")
    registrar_evento("ERROR", "MODIFICACAO_CRITICA", "Arquivo /etc/passwd alterado", "10.0.0.200")
    time.sleep(1)

    # Requisito: Execuções não autorizadas 
    print(f"[{datetime.now()}] Simulando execução de script malicioso...")
    registrar_evento("WARNING", "EXECUCAO_SUSPEITA", "Script powershell.exe executado em /tmp", "192.168.1.15")
    
    # Evento normal para contraste
    registrar_evento("INFO", "LOGIN_SUCESSO", "Usuario admin logado com sucesso", "192.168.1.10")
    
    print("---------------------------------------------------------------")
    print(f"✅ Simulação concluída. Verifique o arquivo '{ARQUIVO_CSV}'.")

if __name__ == "__main__":
    inicializar_csv()
    simular_atividades()