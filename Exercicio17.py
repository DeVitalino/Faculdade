#Mateus Vitalino
print("TURMAS")

total_alunos = int(input("Digite o número total de alunos da série: "))

turma1 = total_alunos // 3
turma2 = total_alunos // 3
turma3 = total_alunos // 3

resto = total_alunos % 3

if resto == 1:
    turma1 += 1
elif resto == 2:
    turma1 += 1
    turma2 += 1

print("ALUNOS")
print(f"Turma A: {turma1} alunos")
print(f"Turma B: {turma2} alunos")
print(f"Turma C: {turma3} alunos")
