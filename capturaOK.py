import machine
from machine import UART

# Configurar UART para la comunicación serial en la puerta de entrada 2 (UART 2)
uart_in = machine.UART(2, baudrate=38400)  # Ajusta los pines según tu configuración

# Configurar UART para la comunicación serial en la puerta de salida 2 (UART 2)
uart_out = machine.UART(2, baudrate=38400)  # Ajusta los pines según tu configuración

# Buffer para almacenar el mensaje completo
message_buffer = bytearray()

# Función para recibir y procesar un mensaje completo
def receive_and_process():
    global message_buffer
    
    while uart_in.any():
        received_byte = uart_in.read(1)
        message_buffer.append(received_byte[0])
        if len(message_buffer) >= 339:
            process_message()

# Función para procesar el mensaje completo y extraer los elementos 16 y 20
def process_message():
    global message_buffer
    
    # Extraer los elementos 16 y 20 del mensaje
    data_16 = message_buffer[15]
    data_20 = message_buffer[19]
    
    # Retransmitir los datos capturados
    uart_out.write(bytearray([data_16, data_20]))
    print("Datos transmitidos:", data_16, data_20)
    
    # Limpiar el buffer para el próximo mensaje
    message_buffer.clear()

# Bucle principal
while True:
    receive_and_process()
