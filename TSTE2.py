#primeira tentativa:

nome = input("Digite seu nome completo \n")
cpf = input("Digite seu CPF \n")

listaNomes = [nome]
listaCPF = [cpf]
for cpf in listaCPF:
    if cpf == listaCPF:
        print("Você ja tem uma conta")
    else:
        pass


nome = nome.strip()
cpf = cpf.strip()
cpf = cpf.replace(".", "")
cpf = cpf.replace("-", "")

if len(cpf) == 11 and cpf.isnumeric():
    email = input("Digite seu e-mail mais usado \n")
    email = email.strip()
    onde_arroba = email.find("@")
    pre_arroba = email[:onde_arroba]
    pos_arroba = email[onde_arroba:]
    onde_ponto = email.find(".")

else:
    print("Revise seus dados")

if (".") not in pos_arroba:
    print("Revise os dados informados")

else:
    print(f"Seu nome {nome}, Seu CPF {cpf}, Seu e-mail {email}.\n {pre_arroba}, {pos_arroba}")


print(f"\nSalvo no banco de dados:\n{listaNomes}\n e {listaCPF}")
print(",".join(listaNomes))
print("\n".join(listaCPF))
print("/".join(listaNomes))
