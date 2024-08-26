'''
    Um professor precisa sortear bombons para diversos alunos.
    Esses alunos serão sorteados randômicamente.
    O número deve corresponder ao número do diário.
'''

import random

while True: 
    sprteio_turma = random.randint(1,27)
    opcao = input("Deseja sortear outro nome (s/n)").lower().strip()
    
    if opcao!= "s" :
        print("Encerrando o sorteio")
        break
    