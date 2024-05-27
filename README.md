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
    <img src="images/pose Home.PNG" alt="Pose Home" width="250">
</p>

* 25, 25, 20,-20, 0.
 
<p align="center">
    <img src=images/pose 1.PNG alt="Pose 1" width="250">
</p>

* -35,35,-30, 30, 0.
 
<p align="center">
    <img src=images/pose 2.PNG alt="Pose 2" width="250">
</p>

* 85,-20, 55, 25, 0.

<p align="center">
    <img src=images/pose 3.PNG alt="Pose 3" width="250">
</p>

 * 80,-35, 55,-45, 0.

<p align="center">
    <img src=images/pose 4.PNG alt="Pose 4" width="250">
</p>

Finalmente, mediante el método trchain(), se obtiene la orientación y posición del NOA para una configuración específica de las articulaciones q1, q2, q3, q4 y q5. Este proceso incluye una serie de rotaciones y traslaciones puras que permiten determinar la pose del NOA.

La fórmula resultante es:

MTH = 'Rz(q1) Tz(4) Rx(-90) Rz(q2+pi/2) Tx(-10.5) Rz(q3+pi/2) Tx(-10.5) Rz(q4+pi/2) Rx(-90) Rz(q5) Tz(6.5)'

Y la MTH resultante es igual a:

![image](https://github.com/FelipeCh18/Lab4Robotica/assets/72814340/ef923b05-39c1-4774-bd83-96020a9133b3)



## Implementación en ROS

Después de sacar el modelo geométrico directo, se procedió a implementar la solución en ROS teniendo en cuenta las recomendaciones de la guía, por lo que para realizar dichos puntos, se hizo un solo programa en la cual se integra todos los puntos, primero importamos las librerias necesarias para el funcionamiento del programa:

![image](https://github.com/FelipeCh18/Lab4Robotica/assets/95656388/eb250911-1135-4a1c-9661-e2197c475a3d)

Después programamos los arreglos con los ángulos de cada una de las poses del robot y su equivalente análogo el cual facilitará el movimiento:

![image](https://github.com/FelipeCh18/Lab4Robotica/assets/95656388/1140d247-c893-47f7-b835-2c1fd3ff38b3)

Ahora debemos programar el servicio de Dynamizel, el cual se mantiene en constante contacto con el nodo activo y el roscore, agilizando la comunicación entre ROS y el robot:

![image](https://github.com/FelipeCh18/Lab4Robotica/assets/95656388/22b8065e-ab02-470b-a343-77f054c078b8)

Sabiendo que necesitamos del suscriptor para saber las posiciones de los motores, debemos preparar un callback el cual se programó de la siguiente manera:

![image](https://github.com/FelipeCh18/Lab4Robotica/assets/95656388/ac1627ce-bb26-4a65-86ed-30d67b222845)

Lo siguiente es para imprimir posiciones, el cuál se tiene en cuenta con la precisión dada por los motores: 

![image](https://github.com/FelipeCh18/Lab4Robotica/assets/95656388/80c2c03e-2828-4353-b7fb-0ab48126d3a1)

Ahora debemos programar el movimiento de las articulaciones simplemente llamando al sistema de envío de comandos de Dynamixel: 

![image](https://github.com/FelipeCh18/Lab4Robotica/assets/95656388/26a71515-738d-41c4-ad45-7c1aae8e4598)

Finalmente, tenemos el código principal en el cual se incluye el movimiento hacia el home y el bucle para ir de una posición a otra sin tener que reejecutar el programa: 

![image](https://github.com/FelipeCh18/Lab4Robotica/assets/95656388/a71592ea-5b17-4329-8f60-d80835d1a646)

Cabe aclarar que la interfaz HMI se programó para la consola.






