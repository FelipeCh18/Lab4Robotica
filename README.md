![image](https://github.com/FelipeCh18/Lab4Robotica/assets/72814340/9e4d79d3-77ea-40e8-af13-8efc43e8f434)# Laboratorio 4 - Cinemática Directa - Phantom X - ROS

***INTEGRANTES***

* Marco Antonio Quimbay Dueñas
* Felipe Chaves Delgadillo

Para llevar a cabo la práctica, el primer paso consistió en hacer la Cinemática Directa del Robot en la posición de Home y así obtener los parámetros de DH. En la figura pueden observarse las distintas distancias que existen entre los eslabones del robot, y sus respectivas magnitudes, adquiridas mediante el uso de un calibrador.

<p align="center">
    <img src=![image](https://github.com/FelipeCh18/Lab4Robotica/assets/72814340/9e4d79d3-77ea-40e8-af13-8efc43e8f434) alt="Cinemática Directa " width="450">
</p>

Obteniendo la siguiente DH:

<p align="center">
    <img src=images/paletizado_externo.png alt="DH en la posición de Home " width="450">
</p>

Posteriormente, mediante el uso del toolbox de matlab se grafican las distintas poses  del robot y sus respectivas DH solicitadas en la guía de laboratorio, obteniendo:

* 0, 0, 0, 0, 0.

<p align="center">
    <img src=images/DiagramaDeFlujoGeneral.png alt="Pose Home" width="250">
</p>

* 25, 25, 20,-20, 0.
 
<p align="center">
    <img src=images/DiagramaDeFlujoGeneral.png alt="Pose 1" width="250">
</p>

* -35,35,-30, 30, 0.
 
<p align="center">
    <img src=images/DiagramaDeFlujoGeneral.png alt="Pose 2" width="250">
</p>

* 85,-20, 55, 25, 0.

<p align="center">
    <img src=images/DiagramaDeFlujoGeneral.png alt="Pose 3" width="250">
</p>

 * 80,-35, 55,-45, 0.

<p align="center">
    <img src=images/DiagramaDeFlujoGeneral.png alt="Pose 3" width="250">
</p>

## Trayectorias 
Paletizado en z
<p align="center">
    <img src=images/paletizado_externo.png alt="Paletizado z " width="450">
</p>

Paletizado en S
<p align="center">
    <img src=images/paletizado_s.png alt="Paletizado en S " width="450">
</p>

Paletizado Externo
<p align="center">
    <img src=images/Paletizado_z.png alt="Paletizado Externo " width="450">
</p>

## Videos Demostrativos
A continuación se añaden los vídeos de los resultados obtenidos del laboratorio:

Vídeo de la ejecución en EPSON RC+ 7.0:

[VÍDEO DE LA EJECUCIÓN EN EPSON RC+ 7.0](https://drive.google.com/drive/folders/16ONF3JqlUhxU9FzaknRo4nXTZ7jvJ7LK?usp=sharing)

Vídeo de la demostración en vivo del funcionamiento:

[VÍDEO DE LA EJECUCIÓN](https://drive.google.com/drive/folders/1lr2AhREz9yGd2liMuURUi9P7plOJVTkf?usp=sharing)
