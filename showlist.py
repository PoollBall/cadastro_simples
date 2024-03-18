import Menu

def mostrarlista():
    print("{:<20} {:<20}".format("Email", "Nome"))
    print("-" * 40)
    for cadastro in Menu.cadastros:
        print("{:<20} {:<20}".format(cadastro['email'], cadastro['nome']))








if __name__ == "__main__":
    mostrarlista()