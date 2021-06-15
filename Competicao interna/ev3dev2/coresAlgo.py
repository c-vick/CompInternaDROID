import ev3dev2.globalDefs as glob
import ev3dev2.sim as sim
from ev3dev2.motor import andar_em_metros, andar_livre, giro_livre, Stop as parar, TurnDirectionAng as girar_90_180, andar_frente_esquerda, andar_frente_direita
from ev3dev2.sensor import getColor as le_cor, getDistanceIR as le_distancia, getForce as le_forca
from ev3dev2.garraAlgo import abrir_garra, fechar_garra_total
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


def dancinha(): #perguntar se as fitas de cores vão ser que nem na atividade das vagas(entre as cores não tem espaço em branco). Porque na Figura 1 do edital tem espaço em branco entre as cores
    #le as cores
    i = 0
    cores = []
    cores.append(le_cor(CorEsquerda)) #já vai começar com o robo em cima da primeira cor
    while le_cor(CorEsquerda) != glob.BRANCO and le_cor(CorEsquerda) != glob.PRETO:
        while le_cor(CorEsquerda) == cores[i]:
            andar_livre(frente, 3)
        parar()
        if le_cor(CorEsquerda) != glob.BRANCO:
            cores.append(le_cor(CorEsquerda))
            i += 1
    print(cores) #teste

    #andar até a linha amarela e ficar dentro do quadrado
    while le_cor(CorEsquerda) != glob.AMARELO:
        andar_livre(frente, 3)
    time.sleep(0.2) #espera para parar, para que o robo esteja dentro do quadrado
    parar()

    #dancinha
    girou_horario = 0
    for cor in cores:
        if cor == glob.AZUL:
            girar_90_180(antihorario, 90)
            girou_horario -= 1
            print("fez azul")#teste
            time.sleep(1)#teste
        elif cor == glob.VERMELHO:
            girar_90_180(horario, 90)
            girou_horario += 1
            print("fez vermelho")#teste
            time.sleep(1)#teste
        elif cor == glob.VERDE:
            girar_90_180(horario, 90) #pode girar duas vezes 90º ou tentar girar 180º, mas não sei se a função de girar 180º ta funcionando
            girar_90_180(horario, 90)
            girou_horario += 2
            print("fez verde")#teste
            time.sleep(1)#teste
        elif cor == glob.AMARELO: #testar as funções de abrir e fechar a garra
            fechar_garra_total()
            abrir_garra()
            fechar_garra_total()
            abrir_garra()
            print("fez amarelo")#teste
            time.sleep(1)#teste

    #alinhar o robo para a frente, pois depois dos giros ele pode estar virado para o lado errado
    while girou_horario != 0:
        if girou_horario > 0:
            girar_90_180(antihorario, 90)
            girou_horario -= 1
            print("girou antihorario")#teste
        elif girou_horario < 0:
            girar_90_180(horario, 90)
            girou_horario += 1
            print("girou horario")#teste