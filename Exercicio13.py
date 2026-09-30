#Joao paulo Santos silva
porc_reprovados_c = float(input("digite a % de alunos reprovadosna turma c:"))
porc_reprovados_d = float(input("digite a % de aprovados na turma D:"))

#A
reprovados_c = (perc_reprovados_c / 100)

#B
porc_reprovados_d = 100 - porc_reprovados_d
reprovados_d =  20 * (porc_reprovados_d / 100)

#C
total_reprovados = reprovados_c + reprovados_d
porc_total = (total_reprovados /80)

print (f"a) alunos reprovados na turma C: {reprovados_c:.0f}")
print (f"b) alunos reprovados na turma D: {reprovados_d:.0f}")
print (f"c) porcentagem total de alunos reprovados: {porc_total:.1f}%")