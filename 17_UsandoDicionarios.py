# ALUNOS APROVADOS OU REPROVADOS USANDO DICIONARIOS:

nome = str(input('NOME: '))
media = float(input('MEDIA: '))
alunos = {'NOME': f'{nome}', 'MEDIA': f'{media}'}

for k, v in alunos.items():                           # para keys e values nos alunos.itens 
    print(f' - {k} É IGUAL A {v.upper()} ')           # print a chave é igual ao valor

if media >= 7:
    print('A SITUACAO DO ALUNO É APROVADO')
elif media < 7 and media > 5:
    print('A SITUACAO DO ALUNO É EM RECUPERACAO')
else:
    print('A SITUACAO DO ALUNO É REPROVADO')