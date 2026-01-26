# Referências, mutabilidade, e memória

# Variáveis: variável é atribuída a um objeto, não o contrário. 

# == e is: 

### O operador == compara valores de objetos, enquanto o is compara suas identidades

### se você estiver comparando uma variável com um singleton (um objeto único) faz mais sentido usar is.

# Método __del__

### Existe um método especial __del__, mas ele não causa a remoção de uma instância e não deve ser invocado em seu código. O método __del__ é invocado pelo interpretador Python quando a instância está prestes a ser destruída, para dar a ela a chance de liberar recursos externos. 

# Objetos em Python: Todo objeto em Python tem uma identidade, um tipo e um valor. Apenas o valor do objeto pode mudar ao longo do tempo