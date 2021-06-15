# IMPORTANT: for each successful call to simxStart, there
# should be a corresponding call to simxFinish at the end!

import ev3dev2.sim as sim
import time
import numpy as np
from ev3dev2.sensor import getDistanceIR as le_distancia
import ev3dev2.globalDefs as glob
from ev3dev2.globalDefs import *

def Stop(clientID, _robotFrontRightMotor, _robotFrontLeftMotor, _robotBackRightMotor, _robotBackLeftMotor):
	sim.simxPauseCommunication(clientID, True)
	sim.simxSetJointTargetVelocity(clientID,_robotFrontRightMotor, 0, sim.simx_opmode_oneshot)
	sim.simxSetJointTargetVelocity(clientID,_robotFrontLeftMotor, 0, sim.simx_opmode_oneshot)
	sim.simxSetJointTargetVelocity(clientID,_robotBackRightMotor, 0, sim.simx_opmode_oneshot)
	sim.simxSetJointTargetVelocity(clientID,_robotBackLeftMotor, 0, sim.simx_opmode_oneshot)
	sim.simxPauseCommunication(clientID, False)
	time.sleep(0.1)

def Girar_X_graus(clientID, _robotRightMotor, _robotLeftMotor, _robo, d, graus):
	
	# d = 1 , anti horario, esquerda
	# d =-1 , horario, direita
	# v = velocidade
	
	v = 5
	g = graus
	erro,b_inicial=sim.simxGetObjectOrientation(clientID,_robo,-1,sim.simx_opmode_streaming)
	while(erro != 0):
		erro,b_inicial=sim.simxGetObjectOrientation(clientID,_robo,-1,sim.simx_opmode_streaming)


	gamma_inicial=b_inicial[2]*180/(np.pi)
	gamma_target=gamma_inicial-g*d
	if(abs(gamma_target) > 190):
		gamma_target = d*g
		
	sim.simxPauseCommunication(clientID, True)
	sim.simxSetJointTargetVelocity(clientID,_robotRightMotor,d*v, sim.simx_opmode_oneshot)
	sim.simxSetJointTargetVelocity(clientID,_robotLeftMotor,(-1)*d*v, sim.simx_opmode_oneshot)
	sim.simxPauseCommunication(clientID, False)

	while(True):
		erro,b=sim.simxGetObjectOrientation(clientID,_robo,-1,sim.simx_opmode_buffer)
		gamma=b[2]*180/(np.pi)
 
		#print(gamma)
		if(abs(abs(gamma)-abs(gamma_inicial))>=0.85*g):
			break
		
		#print(gamma_inicial,gamma)
	Stop(clientID, _robotRightMotor, _robotLeftMotor)
	erro,b_inicial=sim.simxGetObjectOrientation(clientID,_robo,-1,sim.simx_opmode_buffer)
	#gamma_inicial=b_inicial[2]*180/(np.pi)

	sim.simxPauseCommunication(clientID, True)
	sim.simxSetJointTargetVelocity(clientID,_robotRightMotor,d*0.5, sim.simx_opmode_oneshot)
	sim.simxSetJointTargetVelocity(clientID,_robotLeftMotor,(-1)*d*0.5, sim.simx_opmode_oneshot)
	sim.simxPauseCommunication(clientID, False)

	#print(gamma_inicial,gamma_target,gamma)
	while(True):
		sign = np.sign(gamma)
		erro,b=sim.simxGetObjectOrientation(clientID,_robo,-1,sim.simx_opmode_buffer)
		gamma=b[2]
		gamma=gamma*180/(np.pi)

		#print(gamma)
		if(d*(gamma-gamma_target) < 0 or np.sign(gamma) != sign):
			break
		
	#print(gamma_inicial,gamma)
	Stop(clientID, _robotRightMotor, _robotLeftMotor)

def Girar_90_graus_v3(clientID, _robotFrontRightMotor, _robotFrontLeftMotor, _robotBackRightMotor, _robotBackLeftMotor, _robo, d):
	# d = 1 , anti horario, esquerda
	# d =-1 , horario, direita
	# v = velocidade

	v = 1

	erro,b_inicial=sim.simxGetObjectOrientation(clientID, _robo, -1, sim.simx_opmode_streaming)
	while(erro != 0):
		erro,b_inicial=sim.simxGetObjectOrientation(clientID, _robo, -1, sim.simx_opmode_streaming)

	print("Início: ", b_inicial) #teste

	sim.simxPauseCommunication(clientID, True)
	sim.simxSetJointTargetVelocity(clientID,_robotFrontRightMotor,(-1)*d*v, sim.simx_opmode_oneshot)
	sim.simxSetJointTargetVelocity(clientID,_robotFrontLeftMotor,d*v, sim.simx_opmode_oneshot)
	sim.simxSetJointTargetVelocity(clientID,_robotBackRightMotor,(-1)*d*v, sim.simx_opmode_oneshot)
	sim.simxSetJointTargetVelocity(clientID,_robotBackLeftMotor,d*v, sim.simx_opmode_oneshot)
	sim.simxPauseCommunication(clientID, False)

	while True:
		erro,b=sim.simxGetObjectOrientation(clientID, _robo, -1, sim.simx_opmode_buffer)
		print("Durante o while: ", b)
		# if ((abs(b[1]) - abs(b_inicial[1])) > 1.419):
		if (abs(abs(b[1]*180/(np.pi)) - abs(b_inicial[1]*180/(np.pi))) > 88):
			print((abs(b[1]) - abs(b_inicial[1])))
			break
	Stop(clientID, _robotFrontRightMotor, _robotFrontLeftMotor, _robotBackRightMotor, _robotBackLeftMotor)


def Girar_90_graus_v2(clientID, _robotFrontRightMotor, _robotFrontLeftMotor, _robotBackRightMotor, _robotBackLeftMotor, _robo, d):

	# d = 1 , anti horario, esquerda
	# d =-1 , horario, direita
	# v = velocidade
	
	v = 3
	g = 90
	erro,b_inicial=sim.simxGetObjectOrientation(clientID,_robo,-1,sim.simx_opmode_streaming)
	while(erro != 0):
		erro,b_inicial=sim.simxGetObjectOrientation(clientID,_robo,-1,sim.simx_opmode_streaming)


	gamma_inicial=b_inicial[1]*180/(np.pi)
	gamma_target=gamma_inicial-g*d
	maxgamma = 0
	if(abs(gamma_target) > 90):
		gamma_target = d*g
		
	sim.simxPauseCommunication(clientID, True)
	sim.simxSetJointTargetVelocity(clientID,_robotFrontRightMotor,(-1)*d*v, sim.simx_opmode_oneshot)
	sim.simxSetJointTargetVelocity(clientID,_robotFrontLeftMotor,d*v, sim.simx_opmode_oneshot)
	sim.simxSetJointTargetVelocity(clientID,_robotBackRightMotor,(-1)*d*v, sim.simx_opmode_oneshot)
	sim.simxSetJointTargetVelocity(clientID,_robotBackLeftMotor,d*v, sim.simx_opmode_oneshot)
	sim.simxPauseCommunication(clientID, False)

	while(True):
		erro,b=sim.simxGetObjectOrientation(clientID,_robo,-1,sim.simx_opmode_buffer)
		gamma=b[1]*180/(np.pi)
		
		# print("b: ", b) #TESTE
		# print("gamma no while: ", gamma) #TESTE
		# print("gamma_inicial em graus: ", gamma_inicial) #TESTE
		# print("if: ", abs(abs(gamma)-abs(gamma_inicial))) #TESTE

		#print(gamma_inicial, gamma, gamma_target)
		if(abs(abs(gamma)-abs(gamma_inicial))>=0.80*g):
			break
		


		#time.sleep(0.01)
		
		#print(gamma_inicial,gamma)
	Stop(clientID, _robotFrontRightMotor, _robotFrontLeftMotor, _robotBackRightMotor, _robotBackLeftMotor)
	erro,b_inicial=sim.simxGetObjectOrientation(clientID,_robo,-1,sim.simx_opmode_buffer)
	#gamma_inicial=b_inicial[2]*180/(np.pi)

	sim.simxPauseCommunication(clientID, True)
	sim.simxSetJointTargetVelocity(clientID,_robotFrontRightMotor,(-1)*d*0.5, sim.simx_opmode_oneshot)
	sim.simxSetJointTargetVelocity(clientID,_robotFrontLeftMotor,d*0.5, sim.simx_opmode_oneshot)
	sim.simxSetJointTargetVelocity(clientID,_robotBackRightMotor,(-1)*d*0.5, sim.simx_opmode_oneshot)
	sim.simxSetJointTargetVelocity(clientID,_robotBackLeftMotor,d*0.5, sim.simx_opmode_oneshot)
	sim.simxPauseCommunication(clientID, False)

	#print(gamma_inicial,gamma_target,gamma)
	while(True):
		sign = np.sign(gamma)
		erro,b=sim.simxGetObjectOrientation(clientID,_robo,-1,sim.simx_opmode_buffer)
		gamma=b[1]
		gamma=gamma*180/(np.pi)

		#print(gamma, gamma_target)
		#print(abs(abs(gamma)-abs(gamma_target)))
		if(abs(abs(abs(gamma)-abs(gamma_target))) < 2 or np.sign(gamma) != sign):
			break
		
	#print(gamma_inicial,gamma)
	Stop(clientID, _robotFrontRightMotor, _robotFrontLeftMotor, _robotBackRightMotor, _robotBackLeftMotor)


def Girar_180_graus_v2(clientID, _robotFrontRightMotor, _robotFrontLeftMotor, _robotBackRightMotor, _robotBackLeftMotor, _robo): 

	v = 3
	g = 90
	d = 0
	offset = 10

	erro,b_inicial=sim.simxGetObjectOrientation(clientID,_robo,-1,sim.simx_opmode_streaming)
	while(erro != 0):
		erro,b_inicial=sim.simxGetObjectOrientation(clientID,_robo,-1,sim.simx_opmode_streaming)


	gamma_inicial=b_inicial[1]*180/(np.pi)
	gamma_target=-gamma_inicial
	sign = np.sign(gamma_inicial)
	#if(np.sign(gamma_target+offset*sign) == sign):
	#	d = 1

		
	sim.simxPauseCommunication(clientID, True)
	sim.simxSetJointTargetVelocity(clientID,_robotFrontRightMotor,v, sim.simx_opmode_oneshot)
	sim.simxSetJointTargetVelocity(clientID,_robotFrontLeftMotor,(-1)*v, sim.simx_opmode_oneshot)
	sim.simxSetJointTargetVelocity(clientID,_robotBackRightMotor,v, sim.simx_opmode_oneshot)
	sim.simxSetJointTargetVelocity(clientID,_robotBackLeftMotor,(-1)*v, sim.simx_opmode_oneshot)
	sim.simxPauseCommunication(clientID, False)

	time.sleep(1.1)


	while(True):
		erro,b=sim.simxGetObjectOrientation(clientID,_robo,-1,sim.simx_opmode_buffer)
		gamma=b[1]*180/(np.pi)
		print(gamma_inicial,gamma)
		
 
		if(np.sign(gamma) != sign and abs(gamma_inicial) < 12):
			sign = -sign
		print(gamma_target+offset*sign, offset, sign)
		#print(gamma >= gamma_target+offset, not sign)

		if(gamma <= gamma_target+offset*sign and sign > 0):
			break
		elif(gamma >= gamma_target+offset*sign and sign < 0):
			break

		time.sleep(0.01)
		
	Stop(clientID, _robotFrontRightMotor, _robotFrontLeftMotor, _robotBackRightMotor, _robotBackLeftMotor)
	erro,b_inicial=sim.simxGetObjectOrientation(clientID,_robo,-1,sim.simx_opmode_buffer)
	#gamma_inicial=b_inicial[2]*180/(np.pi)

	sim.simxPauseCommunication(clientID, True)
	sim.simxSetJointTargetVelocity(clientID,_robotFrontRightMotor,0.5, sim.simx_opmode_oneshot)
	sim.simxSetJointTargetVelocity(clientID,_robotFrontLeftMotor,(-1)*0.5, sim.simx_opmode_oneshot)
	sim.simxSetJointTargetVelocity(clientID,_robotBackRightMotor,0.5, sim.simx_opmode_oneshot)
	sim.simxSetJointTargetVelocity(clientID,_robotBackLeftMotor,(-1)*0.5, sim.simx_opmode_oneshot)
	sim.simxPauseCommunication(clientID, False)

	#print(gamma_inicial,gamma_target,gamma)
	while(True):
		sign = np.sign(gamma)
		erro,b=sim.simxGetObjectOrientation(clientID,_robo,-1,sim.simx_opmode_buffer)
		gamma=b[1]
		gamma=gamma*180/(np.pi)

		#print(gamma)
		if(abs(gamma-gamma_target) < 2 or np.sign(gamma) != sign):
			break
		
	#print(gamma_inicial,gamma)
	Stop(clientID, _robotFrontRightMotor, _robotFrontLeftMotor, _robotBackRightMotor, _robotBackLeftMotor)