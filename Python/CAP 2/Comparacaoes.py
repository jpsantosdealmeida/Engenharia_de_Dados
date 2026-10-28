
'''

Quero que você defina as seguintes variáveis, inicialmente todas como False, a ideia aqui não é de se importar com os valores dentro dessas variáveis, mas sim como montar condicionais.

possui_passaporte = False

passagem_comprada = False

menor_de_idade = False

E Crie as seguintes condições usando o que acabou de ver e imprima o resultado na tela. Tente fazer cada condição e depois veja a solução no final deste aula.


'''

# operadores lógicos = ==,>=,<=,!=,<,> etc...
# operadores booleanos = and,not,or

possui_passaporte = False

passagem_comprada = False

menor_de_idade = False

# Uma pessoa só pode viajar se possuir  passaporte E tiver a passagem comprada E não for menor de idade
print(possui_passaporte and passagem_comprada and not menor_de_idade )
# Uma pessoa só pode viajar se possuir passaporte ou tiver a passagem comprada e não for menor de idade
print(possui_passaporte or (passagem_comprada and not menor_de_idade ))
# Uma pessoa só pode viajar se não possuir passaporte ou tiver a passagem comprada e não for menor de idade
print(possui_passaporte == False or (passagem_comprada and not menor_de_idade ))
# Uma pessoa não pode viajar se não possuir passaporte ou não tiver a passagem comprada e for menor de idade
print(possui_passaporte == False or (passagem_comprada == False and menor_de_idade ))