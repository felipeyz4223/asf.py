import machine
from machine import UART

# Configurar UART para la comunicación serial en la puerta de entrada 2 (UART 2)
uart_in = machine.UART(2, baudrate=38400)  # Ajusta los pines según tu configuración

# Configurar UART para la comunicación serial en la puerta de salida 2 (UART 2)
uart_out = machine.UART(2, baudrate=38400)  # Ajusta los pines según tu configuración

# Función para recibir y retransmitir un mensaje completo
def receive_and_transmit():
    received_message = uart_in.readline()  # Leer el mensaje completo

    if received_message:  # Verificar si se recibió algún mensaje
        print("Mensaje recibido:", received_message)
        uart_out.write(received_message)  # Retransmitir el mensaje


# Bucle principal
while True:
    receive_and_transmit()
