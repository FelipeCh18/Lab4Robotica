 Laboratorio 4 - Cinemática Directa - Phantom X - ROS

***INTEGRANTES***

* Marco Antonio Quimbay Dueñas
* Felipe Chaves Delgadillo

Para llevar a cabo la práctica, el primer paso consistió en hacer la Cinemática Directa del Robot en la posición de Home y así obtener los parámetros de DH. En la figura pueden observarse las distintas distancias que existen entre los eslabones del robot, y sus respectivas magnitudes, adquiridas mediante el uso de un calibrador.

<p align="center">
    <img src=images/modelo_directo.jpg alt="Cinemática Directa " width="450">
</p>

Obteniendo la siguiente DH:

<p align="center">
    <img src=images/DHstd.jpg alt="DH en la posición de Home " width="450">
</p>

Posteriormente, mediante el uso del toolbox de matlab se grafican las distintas poses  del robot y sus respectivas DH solicitadas en la guía de laboratorio, obteniendo:

* 0, 0, 0, 0, 0.

<p align="center">
    <img src="images/pose Home.PNG" alt="Pose Home" width="450">
</p>

* 25, 25, 20,-20, 0.
 
<p align="center">
    <img src="images/pose 1.PNG" alt="Pose 1" width="450">
</p>

* -35,35,-30, 30, 0.
 
<p align="center">
    <img src="images/pose 2.PNG" alt="Pose 2" width="450">
</p>

* 85,-20, 55, 25, 0.

<p align="center">
    <img src="images/pose 3.PNG" alt="Pose 3" width="450">
</p>

 * 80,-35, 55,-45, 0.

<p align="center">
    <img src="images/pose 4.PNG" alt="Pose 4" width="450">
</p>

Finalmente, mediante el método trchain(), se obtiene la orientación y posición del NOA para una configuración específica de las articulaciones q1, q2, q3, q4 y q5. Este proceso incluye una serie de rotaciones y traslaciones puras que permiten determinar la pose del NOA.

La fórmula resultante es:

MTH = 'Rz(q1) Tz(4) Rx(-90) Rz(q2+pi/2) Tx(-10.5) Rz(q3+pi/2) Tx(-10.5) Rz(q4+pi/2) Rx(-90) Rz(q5) Tz(6.5)'

Y la MTH resultante es igual a:

![image](https://github.com/FelipeCh18/Lab4Robotica/assets/72814340/ef923b05-39c1-4774-bd83-96020a9133b3)



## Implementación en ROS

Después de sacar el modelo geométrico directo, se procedió a implementar la solución en ROS teniendo en cuenta las recomendaciones de la guía, por lo que para realizar dichos puntos, se hizo un solo programa en la cual se integra todos los puntos, primero importamos las librerias necesarias para el funcionamiento del programa:

![image](https://github.com/FelipeCh18/Lab4Robotica/assets/95656388/9df3d0a2-2985-4838-ae31-4384a7656c1f)


Después programamos los arreglos con los torques de cada motor, los ángulos de cada una de las poses del robot y su equivalente análogo el cual facilitará el movimiento y declaramos una variable global sobre la pose en la que esté el robot con el fin de poder estimar de mejor manera los movimientos y los errores RMS de cada motor:

![image](https://github.com/FelipeCh18/Lab4Robotica/assets/95656388/b59ee55d-2ba0-4ca2-85ca-b9131ed675fc)


Ahora debemos programar el servicio de Dynamizel, el cual se mantiene en constante contacto con el nodo activo y el roscore, agilizando la comunicación entre ROS y el robot:

![image](https://github.com/FelipeCh18/Lab4Robotica/assets/95656388/3eeb3bd4-1251-4b34-b0ed-1458f34628c7)


Sabiendo que necesitamos del suscriptor para saber las posiciones de los motores, debemos preparar un callback el cual se programó de la siguiente manera:

![image](https://github.com/FelipeCh18/Lab4Robotica/assets/95656388/8f98aab3-a710-4e72-ab5e-3589aec8a99e)


Lo siguiente es para imprimir las posiciones de los motores con la última posición dada por la función de callback, el cuál tiene en cuenta el error RMS de posición de los motores: 

![image](https://github.com/FelipeCh18/Lab4Robotica/assets/95656388/8406d07f-8a79-4f9f-b332-90cbebecaf36)


Ahora debemos programar el movimiento de las articulaciones simplemente llamando al sistema de envío de comandos de Dynamixel dándole la posición objetivo: 

![image](https://github.com/FelipeCh18/Lab4Robotica/assets/95656388/2048c0a0-60df-406d-be4e-94b677527c9d)


Finalmente, tenemos el código principal en el cual se incluye el movimiento hacia el home y el bucle para ir de una posición a otra sin tener que reejecutar el programa, también se da una espera de 10 segundos para que el usuario pueda leer los estados de los motores en la posición actual y limpia la información para dar una interfaz más amigable: 

![image](https://github.com/FelipeCh18/Lab4Robotica/assets/95656388/a7685e66-f6a9-4560-ba62-a94d2c753c99)
![image](https://github.com/FelipeCh18/Lab4Robotica/assets/95656388/65dbad6d-f8bb-4a48-9ab4-d82d6dd3311f)



Cabe aclarar que la interfaz HMI se programó para la consola de linux.






