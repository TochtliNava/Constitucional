# Bienvenida

¿Qué es un raspberry pi? Es una pequeña computadora que cabe en la palma de tu mano y que te permite hacer maravillas con la electrónica y la programación. Con un Raspberry Pi puedes crear desde una consola de videojuegos retro hasta un robot que te sirva el café (con un poco de esfuerzo). ¿No te parece emocionante? ¡En este manual aprenderás los conceptos básicos para empezar a realizar proyectos con tu Raspberry Pi! 

Te divertirás, experimentarás y descubrirás todo lo que puedes lograr con esta increíble herramienta. ¡Prepárate para entrar en el mundo del Raspberry Pi!

<div style="page-break-after: always;"></div>

# Conociendo el Raspberry Pi
![Modelo B del Raspberry Pi 4 de 2018](https://th.bing.com/th/id/R.edbd95223c0953caf3094b4ef1bb63d2?rik=ZKDxcraRY7v8NA&pid=ImgRaw&r=0=30px)

El Raspberry Pi es un ordenador pequeño y de bajo coste, del tamaño de una tarjeta de crédito, que se puede utilizar para diversos fines educativos, creativos y experimentales. El Raspberry Pi tiene varias características que lo hacen atractivo para los aficionados a la informática, la electrónica y la programación. Algunas de estas características son:

- Un procesador ARM de 64 bits y cuatro núcleos, que varía según el modelo, desde el Cortex-A72 a 1,5 GHz del Raspberry Pi 4 hasta el Cortex-A76 a 2,4 GHz del Raspberry Pi 5 (aún no lanzado oficialmente).
- Una memoria RAM de 1 GB, 2 GB o 4 GB, según el modelo y la versión.
- Una GPU integrada que permite la salida de vídeo por HDMI, con soporte para resoluciones 4K y formatos como HEVC y OpenGL.
<div style="page-break-after: always;"></div>

- Una ranura para tarjetas microSD, donde se almacena el sistema operativo y los archivos del usuario.
- Varios puertos USB, que permiten conectar periféricos como teclados, ratones, cámaras o discos duros.
- Un puerto GPIO de 40 pines, que permite conectar sensores, motores, luces y otros componentes electrónicos para crear proyectos interactivos.
- Una conexión inalámbrica WiFi y Bluetooth, que facilita la comunicación con otros dispositivos y redes.

El Raspberry Pi se puede utilizar para aprender a programar en diferentes lenguajes, como Python, Scratch o C++, así como para crear aplicaciones web, juegos, robots, sistemas de domótica o multimedia. El Raspberry Pi también se puede utilizar como un ordenador personal para navegar por internet, ver vídeos o editar documentos. El Raspberry Pi es compatible con varios sistemas operativos basados en Linux, como Raspbian, Ubuntu o Kali Linux.

El Raspberry Pi se puede adquirir por un precio muy asequible, desde los 35 dólares del modelo más básico hasta los 75 dólares del modelo más avanzado. El Raspberry Pi se puede comprar en la página web oficial de la fundación Raspberry Pi o en otras tiendas online especializadas. Además del Raspberry Pi, se necesita un cable de alimentación USB-C (Regularmente viene integrado en el kit), una tarjeta microSD (Dependiendo del modelo podemos usar desde SD 512MB hasta SDXC 2TB en formato exFAT) con el sistema operativo instalado y un monitor con cable HDMI. También se recomienda tener un teclado y un ratón USB, así como una carcasa protectora para el Raspberry Pi.

<div style="page-break-after: always;"></div>

![Raspberry Pi 3 Model B+ 2017](https://i0.wp.com/www.circuituncle.com/wp-content/uploads/2019/10/Rpi3b-1.png?fit=720,480&ssl=1)

En este manual, vamos a trabajar con el Raspberry Pi 3 B+ 2017, una pequeña computadora que se puede usar para diversos fines. El Raspberry Pi 3 B+ 2017 tiene un procesador de cuatro núcleos, una memoria RAM de 1 GB, una conexión WiFi y Bluetooth integradas, y cuatro puertos USB. Con el Raspberry Pi 3 B+ 2017, podemos aprender a programar, crear juegos, controlar dispositivos electrónicos, y mucho más. Es una herramienta muy versátil y divertida para explorar el mundo de la tecnología.

<div style="page-break-after: always;"></div>

## Puertos

Los puertos del raspberry son las interfaces físicas que permiten conectar diferentes dispositivos y componentes al ordenador. Es importante conocer los puertos del raspberry para saber cómo aprovechar sus capacidades y funcionalidades. Algunos de los puertos más comunes para el modelo B+ son:

<div style="display: flex; justify-content: center;">
<img src="https://www.arcadexpress.com/blog/wp-content/uploads/2020/01/raspb_detalle3.jpg" alt="drawing" width="500"/>
</div>

-   4 puertos USB 2.0
-   1 puerto de RED
-   1 puerto HDMI
-   1 puerto mini-Jack
-   1 Puerto micro-USB (carga)
-   1 Lector tarjetas microSD
-   Bluetooth

<div style="page-break-after: always;"></div>

-   Wifi
-   CPU + GPU Broadcom BCM2837B0, Cortex-A53 (ARMv8) 64-bit SoC @ 1.4GHz
-   1 Gb de RAM
-   40 pines GPIO (de Entrada/Salida)

### Puertos GPIO

En cuanto a lo que es directamente la placa Raspberry Pi, sabemos que está preparada para trabajar con programación física de componentes electrónicos mediante sus pines GPIO (general-purpose input/output). Estos pines de propósito general de entrada/salida son algunos de los que se pueden ver en dos filas de 20 pines. En la siguiente imagen podemos ver más claramente a que corresponde cada pin.

![Raspberry y sus puertos GPIO](https://solectroshop.com/img/cms/Curso%20Raspberry%20Pi%20desde%200/5/Imagen36.png)

Cualquiera de los pines GPIO puede designarse (en el software) como un pin de entrada o salida y utilizarse para una amplia gama de propósitos, como conectar un LED o un sensor.

![Un acercamiento a los pines](https://solectroshop.com/img/cms/Curso%20Raspberry%20Pi%20desde%200/5/Imagen37.png)

> **Nota: la numeración de los pines GPIO no está en orden numérico; Los pines GPIO 0 y 1 están presentes en la placa (pines físicos 27 y 28) pero están reservados para uso avanzado (ver más abajo).**

**Voltajes**

Dos pines de 5V y dos pines de 3V3 (3,3V) están presentes en la placa, así como varios pines de tierra (GND: 0V), que no son configurables. Los pines restantes son todos pines 3V3 de uso general, lo que significa que las salidas están configuradas en 3V3 y las entradas son tolerantes a 3V3.

**Salidas**

Un pin GPIO designado como pin de salida se puede configurar en estado alto (3V3) o bajo (0V).

**Entradas**

Un pin GPIO designado como pin de entrada se puede leer como alto (3V3) o bajo (0V). Esto se hace más fácil con el uso de resistencias internas pull-up o pull-down. Los pines GPIO2 y GPIO3 tienen resistencias pull-up fijas, pero para otros pines esto se puede configurar en el software.

**Más**

Además de los dispositivos de entrada y salida simples, los pines GPIO se pueden usar con una variedad de funciones alternativas, algunas están disponibles en todos los pines, otras en pines específicos.

- PWM: Pines que admiten la Modulación de ancho de pulso, usada para transmitir información a través de un canal de comunicaciones o para controlar la cantidad de energía que se envía a una carga.

  * Software PWM disponible en todos los pines

  * Hardware PWM disponible en GPIO12, GPIO13, GPIO18, GPIO19

- SPI: El Bus SPI (del inglés Serial Peripheral Interface) es un estándar de comunicaciones, usado principalmente para la transferencia de información entre circuitos integrados en equipos electrónicos.

  * SPI0: MOSI (GPIO10); MISO (GPIO9); SCLK (GPIO11); CE0 (GPIO8), CE1 (GPIO7)

  * SPI1: MOSI (GPIO20); MISO (GPIO19); SCLK (GPIO21); CE0 (GPIO18); CE1 (GPIO17); CE2 (GPIO16)

- I2C: Circuito Integrado Interno (I²C, del inglés Inter-Integrated Circuit), se usa internamente para la comunicación entre diferentes partes de un circuito, por ejemplo, entre un controlador y circuitos periféricos integrados.

  * Datos: (GPIO2); Reloj (GPIO3)

  * Datos EEPROM: (GPIO0); Reloj EEPROM (GPIO1)

- Serie: Puertos para comunicación UART, en inglés de Universal Asynchronous Receiver-Transmitter, mediante pin de transmisión TX y pin de recepción RX.

  * TX (GPIO14); RX (GPIO15)

Existen 2 formas de numerar los pines de la Raspberry Pi, en modo GPIO o en modo BCM. Esto es importante a la hora de programar. La diferencia entre estas notaciones generalmente lo notamos cuando estamos controlando los GPIO con python u otro lenguaje y tenemos que ingresar en qué modo usaremos los gpio en GPIO.BOARD o GPIO.BCM.

La opción GPIO.BOARD especifica que se está refiriendo a los pines por su número, es decir los números impresos en nuestra Raspberry Pi (por ejemplo P1), en la imagen siguiente te mostramos el pin 1 y el pin 2, para seguir numerando seria de izquierda a derecha, siendo el que está debajo del pin 1 el pin 3, toda esa fila serían los pines impares y la opuesta los pines pares.

La opción GPIO.BCM se refiere a los pines por su número de "Broadcom SOC channel", estos no son correlativos como en el modo BOARD, en la imagen siguiente se muestran tanto los pines en BOARD como en BCM de las distintas versiones de Raspberry Pi, siendo los BCM los que su nombre comienza con GPIO y los centrales los pines BOARD. Los BCM serían por así decirlo como la numeración del procesador y los BOARD del conector.

![Numeracion BCM](https://solectroshop.com/img/cms/Curso%20Raspberry%20Pi%20desde%200/5/Imagen38.png)

Para controlar GPIO con Python, primero debes importar una librería de código escrito previamente. El más común y difundido es el RPi.GPIO, utilizado para crear miles de proyectos desde los primeros días de la RPi.
