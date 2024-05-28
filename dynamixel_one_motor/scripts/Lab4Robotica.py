from cmath import pi
import numpy as np
import rospy
import time
import os
from std_msgs.msg import String
from sensor_msgs.msg import JointState
from dynamixel_workbench_msgs.srv import DynamixelCommand

# Autor: Felipe Chaves Delgadillo, Marco Antonio Quimbay

# Definición de torques máximos para cada motor
torques = [500, 500, 500, 500, 500]

# Posiciones de referencia para cada caso
posiciones_deg = [[0, 0, 0, 0, 0],
                  [25, 25, 20, -20, 0],
                  [-35, 35, -30, 30, 0],
                  [85, -20, 55, 25, 0],
                  [80, -35, 55, -45, 0]]

# Valores análogos de las posiciones home y los casos obtenidos desde dynamixel_wizard

posiciones_analog = [[514,510,818,512,512],
                     [597,597,888,444,512],
                     [393,630,716,616,512],
                     [802,445,1000,599,512],
                     [786,395,1000,360,512]]

#ir actualizando el caso para poder desplazarse entre casos sin tener que volver al home
global caso_actual
caso_actual = 0


# Función para enviar comandos a los motores Dynamixel
def Enviar_Comando_Articulacion(comando, id_motor, dir_nombre, valor, delay):
    rospy.wait_for_service('dynamixel_workbench/dynamixel_command')
    try:
        comando_dynamixel = rospy.ServiceProxy('/dynamixel_workbench/dynamixel_command', DynamixelCommand)
        resultado = comando_dynamixel(comando, id_motor, dir_nombre, valor)
        rospy.sleep(delay)
        return resultado.comm_result
    except rospy.ServiceException as error:
        print(str(error))

# Función de callback para manejar los estados de las articulaciones
def callback(data):
    global posiciones_actuales
    posiciones_actuales = np.multiply(data.position, 180 / pi)
    posiciones_actuales[2] -= 90
    #imprimir_posiciones(posiciones_actuales,posiciones_deg[caso_actual])

# Función para imprimir las posiciones actuales de las articulaciones
def imprimir_posiciones(real, teorico):
    print('\nPosición motores:\n')
    for i, posicion in enumerate(real):
        print(f'{i + 1}: {posicion:.2f}°\t', end=' ')
    error = np.sqrt(np.mean(np.subtract(teorico, real) ** 2))
    print(f'\n\nError RMS posición: {error:.2f}°\n')

# Función para mover gradualmente las articulaciones hacia una posición objetivo
def mover(indice_articulacion, posicion_objetivo, posicion_actual):
    delta = (posicion_objetivo - posicion_actual)
    Enviar_Comando_Articulacion('', indice_articulacion + 1, 'Goal_Position', posicion_objetivo, 0.5)

# Función principal
if __name__ == '__main__':
    try:
        # Inicializar el nodo de ROS
        rospy.init_node('joint_listener', anonymous=True)
        rospy.Subscriber("/dynamixel_workbench/joint_states", JointState, callback)

        # Configurar los límites de torque de los motores
        for i, torque in enumerate(torques):
            Enviar_Comando_Articulacion('', i + 1, 'Torque_Limit', torque, 0)

        os.system('clear')

        # Ir a la posición de home
        print('Ir a la posición de home\n')
        for i, pos in enumerate(posiciones_analog[0]):
            Enviar_Comando_Articulacion('', i + 1, 'Goal_Position', pos, 1)
            print(f'Movimiento del eslabón {i + 1}\n')
            time.sleep(0.5)
        print('En la posición de home\n')

        # Imprimir las posiciones reales respecto a la posición de home
        imprimir_posiciones(posiciones_actuales, posiciones_deg[0])

        while not rospy.is_shutdown():

            time.sleep(10)
            os.system('clear')

            # Realizar la rutina de movimiento para el caso seleccionado
            caso_actual = int(input('1. [25, 25, 20, -20, 0]\n2. [-35, 35, -30, 30, 0]\n3. [85, -20, 55, 25, 0]\n4. [80, -35, 55, -45, 0]\n0. Posición de HOME\n\nSeleccione el caso a ejecutar: '))
            print(f'Iniciando movimiento para el caso {caso_actual}\n')
            for i, pos in enumerate(posiciones_analog[caso_actual]):
                print(f'Movimiento del eslabón {i + 1}')
                mover(i, pos, posiciones_analog[caso_actual][i])
            print('Movimiento finalizado.')

            # Imprimir las posiciones actuales y teóricas
            imprimir_posiciones(posiciones_actuales, posiciones_deg[caso_actual])
            
    except rospy.ROSInterruptException:
        pass

