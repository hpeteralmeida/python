while True:
    quantidade_pessoas = input("Quantas pessoas você quer cadastrar? ")
    if quantidade_pessoas != '' and quantidade_pessoas.isnumeric():
       quantidade_pessoas = int(quantidade_pessoas)
       break

contador = 0
nomes = []
idades = []
cursos = []
while quantidade_pessoas > contador:
  
    print("=" * 40)
    while True:
        nome = input("Insira o nome da pessoa: ").strip().upper()
        if nome != '' and nome.isalpha():
            nome = str(nome)
            nomes.append(nome)
            break
    while True:
        idade = input("Insira a idade da pessoa: ").strip()
        if idade != '' and idade.isnumeric():
            idade = int(idade)
            idades.append(idade)
            break
    while True:
        curso = input("Insira o nome do curso dessa pessoa: ").strip().upper()
        if curso != '' and curso.isalpha():
            curso = str(curso)
            cursos.append(curso)
            break
    contador += 1
  
print(nomes)
print(idades)
print(cursos)
