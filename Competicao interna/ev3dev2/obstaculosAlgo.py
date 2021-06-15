import ev3dev2.globalDefs as glob
import ev3dev2.sim as sim
from ev3dev2.motor import andar_em_metros, andar_livre, giro_livre, Stop as parar, TurnDirectionAng as girar_90_180, andar_frente_esquerda, andar_frente_direita
from ev3dev2.sensor import getColor as le_cor, getDistanceIR as le_distancia, getForce as le_forca
import time

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



def segue_linha():
    while (le_distancia(SensorUsFrente) > 0.2) and (le_cor(CorDireita) == glob.BRANCO or le_cor(CorDireita) == glob.PRETO): #talvez botar aqui outra condição para caso ele veja as cores ou chegue na torre de hanoi
        andar_livre(1, 2)
        while le_cor(CorDireita) == 0:
            andar_frente_esquerda(1, 1)
        while le_cor(CorEsquerda) == 0:
            andar_frente_direita(1, 1)
    parar()

def desvia_obst_parado():
    girar_90_180(horario, 90)
    while le_distancia(SensorUsEsquerda) != 1:
        andar_livre(1, 3)
    time.sleep(0.1) #ver o tempo aqui, tem que esperar para o robo passar um pouco do bloco, para que quando ele gire ele não bata no bloco
    parar()

    girar_90_180(antihorario, 90)
    andar_em_metros(frente, 3, 0.3) #anda 30cm para a frente, pois ele para a 20cm do cubo e o cubo tem no mínimo 15cm, ai 30cm fica uma distância boa pra ele andar
    while le_distancia(SensorUsEsquerda) != 1:
        andar_livre(1, 3)
    time.sleep(0.2) #ver o tempo aqui, tem que esperar para o robo passar um pouco do bloco, para que quando ele gire ele não bata no bloco
    parar()

    girar_90_180(antihorario, 90)
    while le_cor(CorEsquerda) == glob.BRANCO:
        andar_livre(1, 3)
    time.sleep(1) #ver o tempo aqui, tem que esperar para parar, para que o robo fique centralizado com a linha
    parar()

    girar_90_180(horario, 90)

def desvia_obst_mexe():
    print('a')
