import machine
from machine import UART

# Configurar UART para la comunicación serial en la puerta de entrada 2 (UART 2)
uart_in = machine.UART(2, baudrate=38400)  # Ajusta los pines según tu configuración

# Configurar UART para la comunicación serial en la puerta de salida 2 (UART 2)
uart_out = machine.UART(2, baudrate=38400)  # Ajusta los pines según tu configuración

# Función para recibir, procesar y retransmitir un mensaje completo
def process_and_transmit():
    received_message = uart_in.readline()  # Leer el mensaje completo

    if received_message:  # Verificar si se recibió algún mensaje
        print("Mensaje recibido:", received_message)
        
        # Dividir el mensaje en partes utilizando el espacio como separador
        message_parts = received_message.split()
        
        # Verificar si hay suficientes partes en el mensaje
        if len(message_parts) >= 20:
            # Capturar los datos importantes de las posiciones 15 y 19
            data_15 = message_parts[15]
            data_19 = message_parts[19]
            
            # Crear un arreglo de retransmisión con los datos capturados
            transmission_data = [data_15, data_19]
            
            # Transmitir los datos capturados
            uart_out.write(' '.join(transmission_data))
            print("Datos transmitidos:", transmission_data)

# Bucle principal
while True:
    process_and_transmit()
