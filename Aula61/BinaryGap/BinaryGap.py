class BinaryGap:

    def countBinaryGap(num):
        binary = format(num , "b")
        print("O maior intervalo binário de :" + binary)
        intervalo = False
        contador = 0
        ultimo = ''
        gap_binario = 0

        for numero in binary:
            if ultimo == '':
                ultimo = str(numero)
            else :
                if numero == '0':
                    if ultimo == '1':
                        contador += 1
                        ultimo = '0'
                        intervalo = True
                    else:
                        if ultimo == '0':
                            if contador > 0 :
                                contador += 1
                                ultimo = '0'
                            else:
                                if contador == 0:
                                    ultimo = '0'

                if numero == '1':
                    if intervalo == True :
                        if ultimo == '0':
                            if contador > gap_binario:
                                gap_binario = contador
                            contador = 0
                            ultimo = '1'
                            intervalo == False


                    if intervalo == False:
                        if ultimo == '0':
                            ultimo = '1'

                        elif ultimo == '1':
                            ultimo = '1'


        return gap_binario


    print(countBinaryGap(1041))
    # print(countBinaryGap(300))
    # print(countBinaryGap(250))
    # print(countBinaryGap(17))
    # print(countBinaryGap(44))
    # print(countBinaryGap(69))
    # print(countBinaryGap(123123))