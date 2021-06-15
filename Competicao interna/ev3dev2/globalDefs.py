# coding=utf-8

import ev3dev2.sim as sim
import time

PRETO = 0
VERMELHO = 1
AMARELO = 2
VERDE = 3
AZUL = 5
BRANCO = 6
frente = 1
tras = -1
horario = -1
antihorario = 1

## Setters
def init(_clientID, robotname):
	global robot, robo, robotFrontLeftMotor, robotFrontRightMotor, robotBackRightMotor, robotBackLeftMotor
	global clientID
	global paEsquerda, paDireita, garraDir, garraEsq
	global elevador, irRight, irLeft, us_front, us_left
	global color_sensor_Left, color_sensor_Right
	global positionrobot, angLeft, angRight, orientationrobot
	global sens_force_esq, sens_force_dir
	global cubo

	clientID = _clientID

	sim.simxStartSimulation(clientID, sim.simx_opmode_oneshot_wait)
	print ('Connected to remote API server')
	sim.simxAddStatusbarMessage(clientID,'Funcionando...',sim.simx_opmode_oneshot_wait)
	time.sleep(0.02)

	# Coletar handles
	#Robô
	erro, robot = sim.simxGetObjectHandle(clientID, robotname, sim.simx_opmode_blocking) 
	erro, robo = sim.simxGetObjectHandle(clientID, 'Corpo', sim.simx_opmode_blocking)
	#Motores
	[erro, robotFrontLeftMotor] = sim.simxGetObjectHandle(clientID, 'Revolute_joint1', sim.simx_opmode_blocking)
	[erro, robotBackLeftMotor] = sim.simxGetObjectHandle(clientID, 'Revolute_joint2', sim.simx_opmode_blocking)
	[erro, robotFrontRightMotor] = sim.simxGetObjectHandle(clientID, 'Revolute_joint3', sim.simx_opmode_blocking)
	[erro, robotBackRightMotor] = sim.simxGetObjectHandle(clientID, 'Revolute_joint4', sim.simx_opmode_blocking)
	#Garra
	erro,paEsquerda=sim.simxGetObjectHandle(clientID,'joint_pa_esquerda_garra',sim.simx_opmode_blocking)
	erro,paDireita=sim.simxGetObjectHandle(clientID,'joint_pa_direita_garra',sim.simx_opmode_blocking)
	erro,elevador=sim.simxGetObjectHandle(clientID,'joint_acoplador_garra',sim.simx_opmode_blocking)
	erro,garraDir=sim.simxGetObjectHandle(clientID,'garra_dir',sim.simx_opmode_blocking)
	erro,garraEsq=sim.simxGetObjectHandle(clientID,'garra_esq',sim.simx_opmode_blocking)
	#Sensores
	erro, irRight = sim.simxGetObjectHandle(clientID, 'Sensor_IR_direito', sim.simx_opmode_blocking)
	erro, irLeft = sim.simxGetObjectHandle(clientID, 'Sensor_IR_esquerdo', sim.simx_opmode_blocking)
	erro, us_front = sim.simxGetObjectHandle(clientID, 'Sensor_us_frente', sim.simx_opmode_blocking)
	erro, us_left = sim.simxGetObjectHandle(clientID, 'Sensor_us_esq', sim.simx_opmode_blocking)
	erro , color_sensor_Left = sim.simxGetObjectHandle(clientID, 'Sensor_cor_esq', sim.simx_opmode_blocking)
	erro , color_sensor_Right = sim.simxGetObjectHandle(clientID, 'Sensor_cor_dir', sim.simx_opmode_blocking)
	erro, sens_force_esq = sim.simxGetObjectHandle(clientID, 'ForceSensor_esq', sim.simx_opmode_blocking)
	erro, sens_force_dir = sim.simxGetObjectHandle(clientID, 'ForceSensor_dir', sim.simx_opmode_blocking)
	#Cubo
	erro, cubo = sim.simxGetObjectHandle(clientID, 'Cubo_teste', sim.simx_opmode_blocking)

	

	# Criar stream de dados
	[erro, positionrobot] = sim.simxGetObjectPosition(clientID, robot, -1, sim.simx_opmode_streaming)

	erro, angLeft = sim.simxGetJointPosition(clientID, robotFrontLeftMotor, sim.simx_opmode_streaming)
	erro, angRight = sim.simxGetJointPosition(clientID, robotFrontRightMotor, sim.simx_opmode_streaming)
	[erro, orientationrobot] = sim.simxGetObjectOrientation(clientID,robot,-1,sim.simx_opmode_streaming)

	sim.simxReadProximitySensor(clientID, irRight, sim.simx_opmode_streaming)
	sim.simxReadProximitySensor(clientID, irLeft, sim.simx_opmode_streaming)
	sim.simxGetVisionSensorImage(clientID, color_sensor_Left, 0, sim.simx_opmode_streaming)
	sim.simxGetVisionSensorImage(clientID, color_sensor_Right, 0, sim.simx_opmode_streaming)
	sim.simxReadForceSensor(clientID, sens_force_esq, sim.simx_opmode_streaming)
	sim.simxReadForceSensor(clientID, sens_force_dir, sim.simx_opmode_streaming)
