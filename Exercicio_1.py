salario=float(input("Digite seu salário:"))
horas= int(input("Digite suas horas semanais trabalhadas:"))
horas_trabalhadas_mensais= horas*4
print(f"Você recebe {salario/horas_trabalhadas_mensais:.2f} por hora trabalhada")