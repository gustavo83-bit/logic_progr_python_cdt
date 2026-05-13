import os
import json


def configurar_sistema():
    if not os.path.exists("uploads_projetos"):
        os.makedirs("uploads_projetos")


def listar_projetos():
    arquivos = [f for f in os.listdir("uploads_projetos") if f.endswith(".json")]

    print('\n' + '=' * 40)
    print('   PROJETOS CADASTRADOS')
    print('=' * 40)

    if not arquivos:
        print("Nenhum projeto cadastrado.")
        return []

    for i, arquivo in enumerate(arquivos, start=1):
        nome_exibicao = arquivo.replace("projeto_", "").replace(".json", "").replace("_", " ")
        print(f"{i}. {nome_exibicao.title()}")

    return arquivos


def gerenciar_projeto():
    arquivos = listar_projetos()

    if not arquivos:
        return

    try:
        escolha = int(input("\nEscolha o número do projeto para gerenciar (ou 0 para voltar): "))

        if escolha == 0:
            return

        nome_arquivo = arquivos[escolha - 1]
        caminho = f"uploads_projetos/{nome_arquivo}"

        # 1. LER o projeto atual
        with open(caminho, "r", encoding="utf-8") as f:
            dados = json.load(f)

        print(f"\n--- Dados Atuais ---")
        print(f"Aluno: {dados['aluno']}")
        print(f"Projeto: {dados['projeto']}")

        # 2. ALTERAR
        confirmar = input("\nDeseja alterar as informações do projeto? (s/n): ").lower()

        if confirmar == "s":
            dados['aluno'] = input(f"Novo nome [{dados['aluno']}]: ") or dados['aluno']
            dados['projeto'] = input(f"Novo resumo [{dados['projeto']}]: ") or dados['projeto']

            # 3. SOBRESCREVER
            with open(caminho, "w", encoding="utf-8") as f:
                json.dump(dados, f, indent=4, ensure_ascii=False)

            print("\n[SUCESSO] Projeto atualizado com sucesso!")

    except (ValueError, IndexError):
       
        print("[ERRO] Escolha inválida. Voltando ao menu.")


    def fazer_upload_json():
        print('\n'+ '='*40)

        print('  NOVO UPLOD DE PROJETO')

        print('='*40)

        nome_aluno = input("Nome do aluno:").strip()

        resumo = input("Resumo do projeto:")


        dados = {"aluno":nome_aluno, "projeto":resumo}

        nome_fich = nome_aluno = nome_aluno.replace(" ", "_").lower()