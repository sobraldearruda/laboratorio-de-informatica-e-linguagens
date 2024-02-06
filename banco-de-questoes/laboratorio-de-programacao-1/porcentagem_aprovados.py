## UFCG
## Ciência da Computação
## Programação I / Laboratório de Programação I
## Rafael de Arruda Sobral
## Percentagem de aprovados

print("Análise da Turma")
print("===")
approved = int(input("Número de aprovados? "))
failed = int(input("Número de reprovados? "))
students = approved + failed
approved_percent = (approved * 100) / students
failed_percent = (failed * 100) / students
print("---")
print(f"Total de alunos na turma: {students}")
print(f"Aprovados: {approved} = {approved_percent:.1f}%")
print(f"Reprovados: {failed} = {failed_percent:.1f}%")
