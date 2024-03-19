# Configurar UART para la comunicación serial en la puerta de entrada 2 (UART 2)
uart_in = machine.UART(2, baudrate=38400)  # Ajusta los pines según tu configuración

# Configurar UART para la comunicación serial en la puerta de salida 2 (UART 2)
uart_out = machine.UART(2, baudrate=38400)  # Ajusta los pines según tu configuración

# Buffer para almacenar la primera parte del mensaje
first_part_buffer = bytearray()

# Buffer para almacenar la segunda parte del mensaje
second_part_buffer = bytearray()

# Ristra inimem para comparación
inimem = bytearray([0x5A, 0x5A, 0x01, 0x4C])

# Función para recibir, procesar y retransmitir un mensaje completo
def receive_process_transmit():
    global first_part_buffer
    global second_part_buffer
    
    while uart_in.any():
        received_byte = uart_in.read(1)
        if len(first_part_buffer) < 4:
            first_part_buffer.append(received_byte[0])
        elif len(second_part_buffer) < 339:
            second_part_buffer.append(received_byte[0])
        
    if len(first_part_buffer) == 4 and first_part_buffer == inimem:
        transmit_selected_bytes()
        received_byte = bytearray()  # Limpiar el buffer para el próximo mensaje

# Función para transmitir los bytes seleccionados de la segunda parte del mensaje
def transmit_selected_bytes():
    global second_part_buffer
    
    if len(second_part_buffer) >= 339:
        selected_bytes = [
            second_part_buffer[11],
            second_part_buffer[15],
            second_part_buffer[28],
            second_part_buffer[29],
            second_part_buffer[30],
            second_part_buffer[31]
        ]
        uart_out.write(bytearray(selected_bytes))
        print("Bytes seleccionados transmitidos:", selected_bytes)
        second_part_buffer.clear()  # Limpiar el buffer para el próximo mensaje
        first_part_buffer.clear()   # Limpiar el buffer de la primera parte del mensaje


# Bucle principal
while True:
    receive_process_transmit()
