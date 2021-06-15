# coding=utf-8
# Insert in a script in Coppelia
 
import ev3dev2.sim as sim
import ev3dev2.globalDefs as glob
from ev3dev2.globalDefs import *
from ev3dev2.giroAlgo import Girar_180_graus_v2, Girar_90_graus_v2, Girar_90_graus_v3
import time

import numpy as np
import ev3dev2.sensor as sense

## FUNÇÕES DE LOCOMOÇAO ######################################

def Stop():
	sim.simxPauseCommunication(glob.clientID, True)
	sim.simxSetJointTargetVelocity(glob.clientID,glob.robotFrontRightMotor, 0, sim.simx_opmode_oneshot)
	sim.simxSetJointTargetVelocity(glob.clientID,glob.robotFrontLeftMotor, 0, sim.simx_opmode_oneshot)
	sim.simxSetJointTargetVelocity(glob.clientID,glob.robotBackRightMotor, 0, sim.simx_opmode_oneshot)
	sim.simxSetJointTargetVelocity(glob.clientID,glob.robotBackLeftMotor, 0, sim.simx_opmode_oneshot)
	sim.simxPauseCommunication(glob.clientID, False)
	time.sleep(0.1)

def MoveForward(v):
	sim.simxPauseCommunication(glob.clientID, True)
	sim.simxSetJointTargetVelocity(glob.clientID,glob.robotRightMotor, v, sim.simx_opmode_oneshot)
	sim.simxSetJointTargetVelocity(glob.clientID,glob.robotLeftMotor, v, sim.simx_opmode_oneshot)
	sim.simxPauseCommunication(glob.clientID, False)

def MoveBack(v):
	sim.simxPauseCommunication(glob.clientID, True)
	sim.simxSetJointTargetVelocity(glob.clientID,glob.robotRightMotor, -v, sim.simx_opmode_oneshot)
	sim.simxSetJointTargetVelocity(glob.clientID,glob.robotLeftMotor, -v, sim.simx_opmode_oneshot)
	sim.simxPauseCommunication(glob.clientID, False)

def MoveDirectionPosition(direcao, dist):   #Andar reto para frente ou para trás
	andar_em_metros(direcao, 5, dist)

def andar_livre(d,v):
	
	# d = 1 , andar para frente
	# d =-1 , andar para trás
	# v = velocidade
	sim.simxPauseCommunication(glob.clientID, True)
	sim.simxSetJointTargetVelocity(glob.clientID, glob.robotFrontRightMotor,d*v*(-1), sim.simx_opmode_oneshot)
	sim.simxSetJointTargetVelocity(glob.clientID, glob.robotFrontLeftMotor,d*v*(-1), sim.simx_opmode_oneshot)
	sim.simxSetJointTargetVelocity(glob.clientID, glob.robotBackRightMotor,d*v*(-1), sim.simx_opmode_oneshot)
	sim.simxSetJointTargetVelocity(glob.clientID, glob.robotBackLeftMotor,d*v*(-1), sim.simx_opmode_oneshot)
	sim.simxPauseCommunication(glob.clientID, False)

def giro_livre(d,v):
	
	# d = 1 , anti horario, esquerda
	# d =-1 , horario, direita
	# v = velocidade

	sim.simxPauseCommunication(glob.clientID, True)
	sim.simxSetJointTargetVelocity(glob.clientID,glob.robotFrontRightMotor,(-1)*d*v, sim.simx_opmode_oneshot)
	sim.simxSetJointTargetVelocity(glob.clientID,glob.robotFrontLeftMotor,d*v, sim.simx_opmode_oneshot)
	sim.simxSetJointTargetVelocity(glob.clientID,glob.robotBackRightMotor,(-1)*d*v, sim.simx_opmode_oneshot)
	sim.simxSetJointTargetVelocity(glob.clientID,glob.robotBackLeftMotor,d*v, sim.simx_opmode_oneshot)
	sim.simxPauseCommunication(glob.clientID, False)


def andar_frente_direita(d,v):
    sim.simxPauseCommunication(glob.clientID, True)
    sim.simxSetJointTargetVelocity(glob.clientID, glob.robotFrontRightMotor,d*v*(-1), sim.simx_opmode_oneshot)
    sim.simxSetJointTargetVelocity(glob.clientID, glob.robotFrontLeftMotor,0, sim.simx_opmode_oneshot)
    sim.simxSetJointTargetVelocity(glob.clientID, glob.robotBackRightMotor,d*v*(-1), sim.simx_opmode_oneshot)
    sim.simxSetJointTargetVelocity(glob.clientID, glob.robotBackLeftMotor,0, sim.simx_opmode_oneshot)
    sim.simxPauseCommunication(glob.clientID, False)

def andar_frente_esquerda(d,v):
    sim.simxPauseCommunication(glob.clientID, True)
    sim.simxSetJointTargetVelocity(glob.clientID, glob.robotFrontRightMotor,0, sim.simx_opmode_oneshot)
    sim.simxSetJointTargetVelocity(glob.clientID, glob.robotFrontLeftMotor,d*v*(-1), sim.simx_opmode_oneshot)
    sim.simxSetJointTargetVelocity(glob.clientID, glob.robotBackRightMotor,0, sim.simx_opmode_oneshot)
    sim.simxSetJointTargetVelocity(glob.clientID, glob.robotBackLeftMotor,d*v*(-1), sim.simx_opmode_oneshot)
    sim.simxPauseCommunication(glob.clientID, False)

def TurnDirectionAng(direcao, ang):   #Girar para a direita ou para a esquerda pelo angulo que você escolher
	if (ang == 180):
		Girar_180_graus_v2(glob.clientID, glob.robotFrontRightMotor, glob.robotFrontLeftMotor, glob.robotBackRightMotor, glob.robotBackLeftMotor, glob.robo)
	else:
		# Girar_90_graus_v2(glob.clientID, glob.robotFrontRightMotor, glob.robotFrontLeftMotor, glob.robotBackRightMotor, glob.robotBackLeftMotor, glob.robo, direcao)
		Girar_90_graus_v3(glob.clientID, glob.robotFrontRightMotor, glob.robotFrontLeftMotor, glob.robotBackRightMotor, glob.robotBackLeftMotor, glob.robo, direcao)


def andar_em_metros(d,v,m):
	# d = 1 , andar para frente
	# d =-1 , andar para trás
	# v = velocidade
	# m = valor em metros
	d = d*-1

	
	erro,a_inicial=sim.simxGetObjectPosition(glob.clientID,glob.robot,-1,sim.simx_opmode_blocking)
	x_inicial=a_inicial[0]
	y_inicial=a_inicial[1]
	sim.simxPauseCommunication(glob.clientID, True)
	sim.simxSetJointTargetVelocity(glob.clientID, glob.robotFrontRightMotor,d*v, sim.simx_opmode_oneshot)
	sim.simxSetJointTargetVelocity(glob.clientID, glob.robotFrontLeftMotor,d*v, sim.simx_opmode_oneshot)
	sim.simxSetJointTargetVelocity(glob.clientID, glob.robotBackRightMotor,d*v, sim.simx_opmode_oneshot)
	sim.simxSetJointTargetVelocity(glob.clientID, glob.robotBackLeftMotor,d*v, sim.simx_opmode_oneshot)
	sim.simxPauseCommunication(glob.clientID, False)
	while(True):
		erro,a=sim.simxGetObjectPosition(glob.clientID,glob.robot,-1,sim.simx_opmode_blocking)
		x=a[0]
		y=a[1]
		#print(x,y)
		if(abs(x-x_inicial)>=m or abs(y-y_inicial)>=m): 
			break 
	Stop()
	time.sleep(0.2)


def MoveForwardPosition(dist):
	MoveDirectionPosition(frente, dist)



def gira_livre_uma_roda(roda, d, v):
		 
			# roda: escolher com qual roda girar
			# d = 1 , anti horario
			# d = -1 , horario
			# v = velocidade  
	if (roda == direita):		
		sim.simxPauseCommunication(glob.clientID, True)
		sim.simxSetJointTargetVelocity(glob.clientID, glob.robotLeftMotor, d*v, sim.simx_opmode_oneshot)
		sim.simxSetJointTargetVelocity(glob.clientID,glob.robotRightMotor, 0, sim.simx_opmode_oneshot)
		sim.simxPauseCommunication(glob.clientID, False)	   
	elif(roda == esquerda):	  
		sim.simxPauseCommunication(glob.clientID, True)
		sim.simxSetJointTargetVelocity(glob.clientID, glob.robotLeftMotor, 0, sim.simx_opmode_oneshot)
		sim.simxSetJointTargetVelocity(glob.clientID, glob.robotRightMotor, -d*v, sim.simx_opmode_oneshot)
		sim.simxPauseCommunication(glob.clientID, False)

def MoveSquareForward():
	andar_em_metros(frente, 8, 0.18)
	align.Align()


def TurnInSquare(angle): #gira no centro do quadrado e vai para ponta
	print(angle)
	if(sense.getColor(glob.color_sensor_Left) == PRETO or sense.getColor(glob.color_sensor_Right) == PRETO):
	#align.Align()
		MoveDirectionPosition(tras, 0.065)
	if(angle > 0):
		TurnDirectionAng(esquerda, abs(angle))
	if(angle < 0):
		TurnDirectionAng(direita, abs(angle))
	#MoveDirectionPosition(frente, 0.025)
	align.Align()

def inicio_virar_SUL(): # para a função COM VISÃO
	
	d=0

	while(True):
		
		erro,b=sim.simxGetObjectOrientation(glob.clientID,glob.robo,-1,sim.simx_opmode_blocking)
		gamma=(b[2]*180)/(np.pi)

		if(gamma>=-3 and gamma<=3):
			Stop()
			break

		if(d==0):
			if(gamma>0 and gamma<179.99):
				d = 1
			else:
				d = -1

		v=4
		sim.simxPauseCommunication(glob.clientID, True)
		sim.simxSetJointTargetVelocity(glob.clientID,glob.robotRightMotor,d*v, sim.simx_opmode_oneshot)
		sim.simxSetJointTargetVelocity(glob.clientID,glob.robotLeftMotor,(-1)*d*v, sim.simx_opmode_oneshot)
		sim.simxPauseCommunication(glob.clientID, False)

	align.Align()
	andar_em_metros(tras, 5, 0.065)
	return

def inicio_virar_NORTE(): # para a função SEM VISÃO; lembrar de adicionar no if(nao viu prataleira) virar 180.

	d=0

	while(True):
		
		erro,b=sim.simxGetObjectOrientation(glob.clientID,glob.robo,-1,sim.simx_opmode_blocking)
		gamma=(b[2]*180)/(np.pi)

		if(gamma>=177 or gamma<=-177):
			Stop()
			break

		if(d==0):
			if(gamma>0 and gamma<179.99):
				d = 1
			else:
				d =-1
		
		v=4
		sim.simxPauseCommunication(glob.clientID, True)
		sim.simxSetJointTargetVelocity(glob.clientID,glob.robotRightMotor,d*v, sim.simx_opmode_oneshot)
		sim.simxSetJointTargetVelocity(glob.clientID,glob.robotLeftMotor,(-1)*d*v, sim.simx_opmode_oneshot)
		sim.simxPauseCommunication(glob.clientID, False)

	align.Align()
	return