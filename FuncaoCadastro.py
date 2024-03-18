import Menu


def cadastrar_pessoa(**kwargs):
    email = kwargs.get('email', None)

    # Validação do email
    if email is None:
        email = input("Digite o email: ")

    onde_arroba = email.find("@")
    onde_ponto = email.find(".")
    verific = email[:onde_arroba]

    if onde_arroba == -1 or onde_ponto == -1 or verific in Menu.cadastros:
        print("\nE-mail inválido!")
        return cadastrar_pessoa()

    # Nome
    nome = kwargs.get('nome', None)
    if nome is None:
        nome = input("Digite o nome: ")

    # Verifica se a pessoa já está cadastrada
    for pessoa in Menu.cadastros:
        if pessoa["email"] == email:
            print("Já está cadastrada!")
            return

    # Se a pessoa não estiver cadastrada, adiciona ao cadastro
    Menu.cadastros.append({"email": email, "nome": nome})
    print("Pessoa cadastrada com sucesso!")
    return Menu.main()


if __name__ == "__main__":
    cadastrar_pessoa()