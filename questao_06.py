#6. Escreva uma expressão que será utilizada para decidir se um aluno foi ou não aprovado. 
# Para ser aprovado, todas as médias do aluno devem ser maiores que 7. 
# Considere que o aluno cursa apenas três matérias, e que a nota de cada uma está armazenada nas 
# seguintes variáveis: matéria1, matéria2 e matéria3.
materia1 = float(input("Informe a media da materia1:"))
materia2 = float(input("Informe a media da materia2:"))
materia3 = float(input("Informe a media da materia3:"))
if materia1 >= 7 and materia2 >= 7 and materia3 >= 7:
    print("Você foi aprovado")
else:
    print("Você foi reprovado :D ")


