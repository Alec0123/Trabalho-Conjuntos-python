#Alexandre Theo Kogut BCC

#Faça um codigo que leia dados de um TXT e realize operações de conjuntos, sendo elas união, interseção, diferença e plano cartesiano.

#Lendo o txt
text = open("n4.txt", "r")

#Lendo a quantidade de operações
a = text.readline().split(",")
l1 = []
l1.append(int(a[0]))

#Contador pro while
cont = l1[0]

#Laço de repetição da quantidade de operações
while cont > 0:

    #Lendo e transformando em numero a letra referente a operação
    b = text.readline().rstrip('\n')
    l2 = []
    l2.append(ord(b[0]))

    #If da União
    if l2 == [85]:

        #Transformando as 2 linhas a baixo da letra de operação em lista e tirando o caractere \n
        l3 = text.readline()
        l3 = l3.rstrip('\n')
        list1 = l3.split(", ")

        l4 = text.readline()
        l4 = l4.rstrip('\n')
        list2 = l4.split(", ")

        #Operação de União
        list3 = []
        for i in list1:
            list3.append(i)
        for i in list2:
            if i not in list3:
                list3.append(i)
        #Diminuindo o valor do contador
        cont = cont - 1

        #Print da operação
        print("União:", end="")
        print("Conjunto1:", end="")
        print(list1, end="")
        print(",", end="")
        print("Conjunto2:", end="")
        print(list2, end="")
        print(".", end="")
        print("Resultado:", end="")
        print(list3)

    #If da Interseção
    elif l2 == [73]:
        l3 = text.readline()
        l3 = l3.rstrip('\n')
        list1 = l3.split(", ")

        l4 = text.readline()
        l4 = l4.rstrip('\n')
        list2 = l4.split(", ")

        #Operação de interseção
        list3 = []
        for i in list1:
            if i in list2:
                list3.append(i)
        cont = cont - 1

        print("Interseção:", end="")
        print("Conjunto1:", end="")
        print(list1, end="")
        print(",", end="")
        print("Conjunto2:", end="")
        print(list2, end="")
        print(".", end="")
        print("Resultado:", end="")
        print(list3)

    #If da Diferença
    elif l2 == [68]:
        l3 = text.readline()
        l3 = l3.rstrip('\n')
        list1 = l3.split(", ")

        l4 = text.readline()
        l4 = l4.rstrip('\n')
        list2 = l4.split(", ")

        #Operação de diferença
        list3 = []
        for i in list1:
            if i not in list2:
                list3.append(i)
        for i in list1:
            if i not in list2:
                list3.append(i)
        cont = cont - 1

        print("Diferença:", end="")
        print("Conjunto1:", end="")
        print(list1, end="")
        print(",", end="")
        print("Conjunto2:", end="")
        print(list2, end="")
        print(".", end="")
        print("Resultado:", end="")
        print(list3)

   #If do plano cartesiano
    elif l2 == [67]:
        l3 = text.readline()
        l3 = l3.rstrip('\n')
        list1 = l3.split(", ")

        l4 = text.readline()
        l4 = l4.rstrip('\n')
        list2 = l4.split(", ")

        #Operação do produto cartesiano
        list3 = []
        for i in list1:
            for l in list2:
                list3.append((i, l))
        cont = cont - 1

        print("Produto Cartesiano:", end="")
        print("Conjunto1:", end="")
        print(list1, end="")
        print(",", end="")
        print("Conjunto2:", end="")
        print(list2, end="")
        print(".", end="")
        print("Resultado:", end="")
        print(list3)