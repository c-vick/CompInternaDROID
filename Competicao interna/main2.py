from ev3dev2.motor import andar_em_metros, andar_livre, giro_livre, Stop as parar, TurnDirectionAng as girar_90_180
from ev3dev2.sensor import getColor as le_cor, getDistanceIR as le_distancia
import ev3dev2.globalDefs as glob
import ev3dev2.sim as sim
import time

CorEsquerda = glob.color_sensor_Left
CorDireita = glob.color_sensor_Right
SensorUsFrente = glob.us_front
SensorUsEsquerda = glob.us_left
frente = glob.frente
tras = glob.tras
horario = glob.horario
antihorario = glob.antihorario

#################################################################################

# Nomes dos Sensores:
# Ultrassom:
# 	SensorUsFrente
#	SensorUsEsquerda
# Cor:
#	CorEsquerda
#	CorDireita

# PRETO = 0
# VERMELHO = 1
# AMARELO = 2
# VERDE = 3
# AZUL = 5
# BRANCO = 6

# Funções movimento:
#	andar_em_metros(direção, velocidade, metros)
#	andar_livre(direção, velocidade)
#	giro_livre(orientação, velocidade)
#	parar()
#	girar_90_180(orientação, ângulo)
#
# Funções sensores:
#	le_cor(sensor)
#	le_distancia(sensor)


# ESCREVER SEU CÓDIGO AQUI:
#################################################################################

# andar_em_metros(frente,5,0.31)
# print(le_cor(CorEsquerda))
# print(le_distancia(SensorUsEsquerda))

# giro_livre(horario,5)
# time.sleep(1)
# parar()

# print(le_cor(CorEsquerda))
# time.sleep(2)

# print("Finalizado")


cores = []
cores.append(6)

for i in range (4): #le as cores e salva em uma lista
    while le_cor(CorEsquerda) == cores[i] and le_cor(CorDireita) == cores[i]: #verifica os dois sensores, talvez possa verificar só um
        andar_livre(frente, 3)
    parar()
    cores.append(le_cor(CorEsquerda))
print(cores) #teste

if cores[1] == glob.VERDE and cores[2] == glob.VERMELHO and cores[3] == glob.AZUL:
    path = 1
elif cores[1] == glob.VERMELHO and cores[2] == glob.AMARELO and cores[3] == glob.VERDE:
    path = 2
elif cores[1] == glob.AZUL and cores[2] == glob.VERDE and cores[3] == glob.AMARELO:
    path = 3
elif cores[1] == glob.VERMELHO and cores[2] == glob.AZUL and cores[3] == glob.AMARELO:
    path = 4
elif cores[1] == glob.AMARELO and cores[2] == glob.VERDE and cores[3] == glob.AZUL:
    path = 5
elif cores[1] == glob.AZUL and cores[2] == glob.VERMELHO and cores[3] == glob.VERDE: #podia ser um else
    path = 6
print(path) #teste

while le_distancia(SensorUsEsquerda) != 1: #andar até o vão na parede
    andar_livre(frente, 3)
time.sleep(0.2) #esperar um pouco para não bater o lado esquerdo quando for passar pelo vão
parar()

# giro_livre(antihorario, 0.5) #girar para passar pelo vão
# time.sleep(1.32)
# parar()
girar_90_180(antihorario, 90) #girar para passar pelo vão

while le_distancia(SensorUsFrente) > 0.45: #andar até estar perto o suficiente da parede para que o sensor us esquerdo consiga detectar a parede
    andar_livre(frente, 3)
parar()

girar_90_180(horario, 90) #girar 90º para a direita

while le_distancia(SensorUsEsquerda) != 1: #andar até o fim da parede
    andar_livre(tras, 3)
andar_em_metros(frente, 3, 0.3)
parar()

#andar até cada vaga
if path == 1:
    andar_em_metros(frente, 3, 0.05)
elif path == 2:
    andar_em_metros(frente, 3, 0.475)
elif path == 3:
    andar_em_metros(frente, 3, 2*0.475)
elif path == 4:
    andar_em_metros(frente, 3, 3.35)
elif path == 5:
    andar_em_metros(frente, 3, 3.35+0.475)
elif path == 6: #podia ser um else
    andar_em_metros(frente, 3, 3.35+(2*0.475))

girar_90_180(antihorario, 90) #girar 90º para a esquerda

while le_distancia(SensorUsFrente) > 0.2: #andar até estar dentro da vaga
    andar_livre(frente, 3)
parar()


#################################################################################
	
# Pause simulation
clientID = glob.clientID
#sim.simxPauseSimulation(clientID,sim.simx_opmode_oneshot_wait)

# Now close the connection to V-REP:
#sim.simxAddStatusbarMessage(clientID, 'Programa pausado', sim.simx_opmode_blocking )
sim.simxFinish(clientID)
print ('Program ended')