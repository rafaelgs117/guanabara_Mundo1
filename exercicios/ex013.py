#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário com 15% de aumento

salario = float(input('Digite o salário do funcionário: R$'))
aumento = 0.15 #15% de aumento 15/100 = 0.15
novo_salario = salario + (salario * aumento) #novo salário é igual ao salário atual mais o aumento

print('O salário atual é R${:.2f} e o novo salário com 15% de aumento é R${:.2f}'.format(salario, novo_salario))