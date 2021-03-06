#Algumas variáveis que servirão para manipulação de dados

result = []
classe = {}
med = []

def ui():

    #Primeiro parâmetro do dicionário nome do aluno, ou apenas 'nome' é uma string que recebe uma entrada de usuário

    classe['Aluno'] = str(input('Nome do aluno: ')) 

    '''Como o ano letivo é definido por 4 bimestres é necessário 4 entradas de usuário para cada bimestre como um ponto flutuante
    pois, as notas nem sempre são numeros inteiros '''

    nota1 = float(input('Insira a primeira nota: '))
    nota2 = float(input('Insira a segunda nota: '))
    nota3 = float(input('Insira a terceira nota: '))
    nota4 = float(input('Insira a quarta nota: '))
    
    ''' Inserimos as 4 notas na lista med para mais a frente calcularmos a média que é a soma da lista dividida pelo tamanho
    sum(lista)/len(lista) '''

    med.append(nota1)
    med.append(nota2)
    med.append(nota3)
    med.append(nota4)
    classe['Média'] = sum(med)/len(med)
    
    #O resultado é adicionado a lista result como uma cópia do dicionário classe

    result.append(classe.copy())

    ''' tl1 é o teste de logica 1 o nome não faz muito sentido mas no fim é um resultado if-else se true roda todo 
    o programa do inicio para adicionar mais alunos e médias e se false printa o resultado'''
    


    tl1 = str(input('Cadastrar mais um aluno? S/N '))
    if tl1.lower() == 's':
        ui()


        ''' A lista é então organizada com uma função lambda (poderia se usar uma função 'def' comum, mas para fins de poupar espaço e desenvolver 
    as minhas habilidades de programação usei a função lambda que é uma def de sintaxe diferente) de paramentro val 
    (valor já que quero exibir o aluno com a maior média) e o reverse true faz com que seja do maior para o menor'''

    sorted_list = sorted(result, key=lambda val: val['Média'], reverse=True)

    #Por fim a lista organizada é exibida com o valor de índice zero que é o primeiro e maior da lista

    tl2 = str(input('Mostrar aluno com maior média? S/N'))
    if tl2.lower() == 's':
         print(sorted_list[0])
    else:
        print('Insira uma informação valida!')
        pass    
    #E é dada a opção de exibir toda a classe

    tl3 = str(input('Exibir todos alunos e médias? S/N'))
    if tl3.lower() == 's':
        print(result)    
    else:
        print('Insira uma informação valida!')
        pass
        
    exit()
    
ui()
