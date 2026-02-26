# Demonstração de um dos jeitos de criar filas em pyhton: as listas
# Esse método não é recomendável, mas é válido saber como funciona.

# As filas funcionam no sistema FIFO - First In First Out


# Primeiro criamos uma fila vazia usando []:
fila = []

# A função .append() adiciona elementos dentro da lista
fila.append('A')
print(fila)
fila.append('B')
print(fila)
fila.append('C')
print(fila)
# Até aqui, temos uma lista ['A', 'B', 'C'], mostrando passo a passo os elementos sendo adicionados


# A função .pop() retira elementos da lista. Dentro dos parenteses, o índice pode ser referenciado
fila.pop(0)

# Em listas, o índice começa em 0, sendo assim, uma lista com 5 elementos vai até o índice 4
#   0    1    2    3    4
# ['A', 'B', 'C', 'D', 'E']
print(fila)
# Aqui temos, agora, uma lista ['B', 'C']
# O elemento 'A' foi removido e agora o elemento 'B', passa a ser o índice 0
# O método de listas não é recomendavél  pois, em listas grandes, a ordenança de índices tende a gerar um problema de performance
