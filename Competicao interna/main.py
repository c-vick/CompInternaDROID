from ev3dev2.motor import andar_em_metros, andar_livre, giro_livre, Stop as parar, TurnDirectionAng as girar_90_180
from ev3dev2.sensor import getColor as le_cor, getDistanceIR as le_distancia, getForce as le_forca
import ev3dev2.globalDefs as glob
import ev3dev2.sim as sim
import time
from ev3dev2.garraAlgo import fechar_garra, abrir_garra, fechar_garra_cubo, abrir_garra_cubo
from ev3dev2.obstaculosAlgo import segue_linha, desvia_obst_parado, desvia_obst_mexe
from ev3dev2.coresAlgo import dancinha
import numpy as np

CorEsquerda = glob.color_sensor_Left
CorDireita = glob.color_sensor_Right
SensorUsFrente = glob.us_front
SensorUsEsquerda = glob.us_left
SensorForcaEsq = glob.sens_force_esq
SensorForcaDir = glob.sens_force_dir
frente = glob.frente
tras = glob.tras
horario = glob.horario
antihorario = glob.antihorario
cubo = glob.cubo

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

# fechar_garra()
# fechar_garra_cubo(cubo)
# time.sleep(1)
# andar_em_metros(frente, 1, 0.3)
# abrir_garra_cubo(cubo)

# girar_90_180(horario, 90)
# time.sleep(1)
# girar_90_180(horario, 90)
# time.sleep(1)
# girar_90_180(horario, 90)
# time.sleep(1)
# girar_90_180(horario, 90)

erro,b_inicial=sim.simxGetObjectQuaternion (glob.clientID, glob.robo, -1, sim.simx_opmode_streaming)
while(erro != 0):
    erro,b_inicial=sim.simxGetObjectQuaternion (glob.clientID, glob.robo, -1, sim.simx_opmode_streaming)
print(b_inicial)
print(b_inicial[1]*180/(np.pi))

# segue_linha()
# desvia_obst_parado()
# dancinha()















# cores = []
# cores.append(6)

# for i in range (4): #le as cores e salva em uma lista
#     while le_cor(CorEsquerda) == cores[i] and le_cor(CorDireita) == cores[i]: #verifica os dois sensores, talvez possa verificar só um
#         andar_livre(frente, 3)
#     parar()
#     cores.append(le_cor(CorEsquerda))
# print(cores) #teste

# if cores[1] == glob.VERDE and cores[2] == glob.VERMELHO and cores[3] == glob.AZUL:
#     path = 1
# elif cores[1] == glob.VERMELHO and cores[2] == glob.AMARELO and cores[3] == glob.VERDE:
#     path = 2
# elif cores[1] == glob.AZUL and cores[2] == glob.VERDE and cores[3] == glob.AMARELO:
#     path = 3
# elif cores[1] == glob.VERMELHO and cores[2] == glob.AZUL and cores[3] == glob.AMARELO:
#     path = 4
# elif cores[1] == glob.AMARELO and cores[2] == glob.VERDE and cores[3] == glob.AZUL:
#     path = 5
# elif cores[1] == glob.AZUL and cores[2] == glob.VERMELHO and cores[3] == glob.VERDE: #podia ser um else
#     path = 6
# print(path) #teste

# while le_distancia(SensorUsEsquerda) != 1: #andar até o vão na parede
#     andar_livre(frente, 3)
# time.sleep(0.2) #esperar um pouco para não bater o lado esquerdo quando for passar pelo vão
# parar()

# # giro_livre(antihorario, 0.5) #girar para passar pelo vão
# # time.sleep(1.32)
# # parar()
# girar_90_180(antihorario, 90) #girar para passar pelo vão

# andar_em_metros(frente, 3, 0.6) #passar pelo vão

# if path == 1 or path == 2 or path == 3:
#     # giro_livre(antihorario, 0.5) #girar aproximadamente 90º para a esquerda
#     # time.sleep(1.2)
#     # parar()
#     girar_90_180(antihorario, 90)  #girar aproximadamente 90º para a esquerda
#     andar_em_metros(frente, 3, 1.4)
#     if path == 1:
#         andar_em_metros(frente, 3, 0.9)
#     elif path == 2:
#         andar_em_metros(frente, 3, 0.425)
#     # giro_livre(horario, 0.5) #girar aproximadamente 90º para a direita
#     # time.sleep(1.2)
#     # parar()
#     girar_90_180(horario, 90) #girar aproximadamente 90º para a direita
#     while le_distancia(SensorUsFrente) > 0.3: #andar até a parede
#         andar_livre(frente, 3)
#     parar()

# if path == 4 or path == 5 or path == 6:
#     # giro_livre(horario, 0.5) #girar aproximadamente 90º para a direita
#     # time.sleep(1.2)
#     # parar()
#     girar_90_180(horario, 90) #girar aproximadamente 90º para a direita
#     andar_em_metros(frente, 3, 0.8)
#     if path == 5:
#         andar_em_metros(frente, 3, 0.425)
#     elif path == 6:
#         andar_em_metros(frente, 3, 0.9)
#     # giro_livre(antihorario, 0.5) #girar aproximadamente 90º para a esquerda
#     # time.sleep(1.2)
#     # parar()
#     girar_90_180(antihorario, 90)  #girar aproximadamente 90º para a esquerda
#     while le_distancia(SensorUsFrente) > 0.3: #andar até a parede
#         andar_livre(frente, 3)
#     parar()

#################################################################################
	
# Pause simulation
clientID = glob.clientID
#sim.simxPauseSimulation(clientID,sim.simx_opmode_oneshot_wait)

# Now close the connection to V-REP:
#sim.simxAddStatusbarMessage(clientID, 'Programa pausado', sim.simx_opmode_blocking )
sim.simxFinish(clientID)
print ('Program ended')