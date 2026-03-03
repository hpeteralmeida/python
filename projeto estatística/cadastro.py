quantidade_pessoas = int(input("Quantas pessoas você quer cadastrar? "))
contador = 0
nomes = []
idades = []
cursos = []
while quantidade_pessoas > contador:
  
  print("=" * 40)
  nome = str(input("Insira o nome da pessoa: ")).strip().upper()
  idade = int(input("Insira a idade da pessoa: ").strip())
  curso = str(input("Insira o nome do curso dessa pessoa: ")).strip().upper()
  print("=" * 40)

  nomes.append(nome)
  idades.append(idade)
  cursos.append(curso)
  
  contador += 1
  
print(nomes)
print(idades)
print(cursos)
