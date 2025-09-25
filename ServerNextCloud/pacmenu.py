#!/usr/bin/env python3

############################################### BIBLIOTECAS NECESSARIAS ######################################################
import csv, subprocess
from pathlib import Path

############################################### VARIAVEIS DE DIRETORIOS/ARQ ##################################################
# dir seguro
dir_seguro = Path("/home/nextcloud-projetos/configs_occ/")

# Caminho para o seu CSV
CSV_FILE = "usuarios.csv"

# Caminho do PHP OCC no Nextcloud
#OCC_CMD = ["sudo", "-u", "www-data", "php", "/var/www/nextcloud/occ"] no baremetal
OCC_CMD = ["docker", "exec", "-u", "www-data", "nextcloud_app", "php", "/var/www/html/occ"]

############################################### FUNCOES AUTOMATIZADAS #######################################################
def criar_usuario(user_id, display_name, group, email):
    """
    Executa o comando occ user:add para criar um usuário.
    """
    cmd = OCC_CMD + [
        "user:add", user_id,
        f'--display-name={display_name}',
        f'--group={group}',
        f'--email={email}',
        "--generate-password"
    ]

    try:
        resultado = subprocess.run(cmd, capture_output=True, text=True, check=True)
        print(f"[OK] Usuário {user_id} criado com sucesso!")
        print(resultado.stdout)
        
    except subprocess.CalledProcessError as e:
        print(f"[ERRO] Falha ao criar usuario {user_id}:")
        print(e.stderr)

def print_logo():
    print("""
    ==========================================
                    PACMENU
    ==========================================
    """)

def menu():
    try:
        while True:
            print_logo()
            print(
            """
            1 - Cadastro de usuarios em massa
            2 - Listar 'IPs bloqueados'
            2 - Remover 'Bloqueio de IP'
            3 - Atualizar indices no banco de dados
	    4 - Sair	
            """
            )
            print("Escolha uma das seguintes opcoes: ", end='')
            
            escolha = int(input())

            if escolha == 1:
                print("Digite o nome do documento: ",end='')
                name_file = input().strip()+".csv"
                file_csv = dir_seguro/name_file
                
                obter_doc(file_csv)
                break

	

            #elif escolha == 2:
            #elif escolha == 3
            elif escolha == 4:
                break

            else:
                print("ERRO: opcao invalida.")
                break
        
    except ValueError as e:
        print(f"Ocorreu um erro: {e}")

############################################### FUNCAO PRINCIPAL #######################################################
def obter_doc(name_file):
    with open(name_file, newline='', encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile, delimiter=",")  # separador vai ser ","
        for row in reader:
            user_id = row["user_id"].strip()
            display_name = row["display_name"].strip()
            group = row["group"].strip()
            email = row["email"].strip()

            criar_usuario(user_id, display_name, group, email)

def main():
    menu()

if __name__ == "__main__":
    main()
