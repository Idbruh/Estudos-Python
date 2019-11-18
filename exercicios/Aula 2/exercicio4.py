#--- Exercicio 4  - Variávies e impressão com interpolacão de string
#--- Imprima a tela de um itinerário de viagem
#--- O itinerário deve conter o ponto de partida e de destino
#--- Entre os dois pontos deve conter no minimo 10 pontos de parada
#--- Cada item deve conter data, hora e descrição
#--- O itineário deve conter cabeçalho com o título da viagem
#--- Os dados de cada ponto devem estar em variáveis
#--- Deve ser usado os caracteres de tabulação, quebra de linha e a função Format()

itinerario = ('Casa > Shopping Park Europeu 20 min')

partida = ('Rua João Pessoa')
destino = ('Shopping Park Europeu')

bus1 = ('Aguarde por onibus 30 ou 31 e viaje até o Terminal Proheb: 5 min')
bus2 = ('Aguarde por onibus 605:Terminal Proeb/ Rodoviária/ Park Europeu/ Terminal Fortaleza: 12 min')
viagem = ('Viaje até Ponto Shopping Park Europeu; \nExibindo paradas para 605; \nTerminal Proeb - Plataforma 605-616; \nRua Antônio Da Veiga, 701-849; \nRua Antônio Da Veiga, 171; \nAvenida Martin Luther, 1602-1704; \nPonto - Policlínica; \nPonto - Rodoviária De Blumenau; \nPonto Shopping Park Europeu C/B \nCaminhe até: Shopping Park Europeu: 3 min')

print(f'\nItinerário: {itinerario}\nPartida: {partida} \nDestino: {destino}\n \nTrajeto\n \n{bus1}\n{bus2} \n{viagem}\n \nVocê chegou no destino: {destino}\n')