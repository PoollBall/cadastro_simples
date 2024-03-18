# segunda tentativa:
# Lista para armazenar os cadastros
import FuncaoCadastro
import showlist


cadastros = []


def main():
    while True:
        print("\n1. Cadastrar Pessoa")
        print("2. Mostrar a Lista de Cadastros")
        print("3. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            sucesso = FuncaoCadastro.cadastrar_pessoa()
            if not sucesso:
                continue  # Retorna ao início do programa
        elif opcao == "2":
            showlist.mostrarlista()
            continue
        elif opcao == "3":
            print("Saindo...")
            break

        else:
            print("Opção inválida. Por favor, escolha novamente.")


if __name__ == "__main__":
    main()