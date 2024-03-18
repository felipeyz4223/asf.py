import machine
from machine import UART
# Configurar UART para la comunicación serial en la puerta de entrada 2 (UART 2)
uart_in = machine.UART(2, baudrate=38400) # Ajusta los pines según tu configuración

# Configurar UART para la comunicación serial en la puerta de salida 2 (UART 2)
uart_out = machine.UART(2, baudrate=38400) # Ajusta los pines según tu configuración

# Función para detectar la secuencia de inicio y retransmitir el dato indicador de cabeza junto con el dato de la ristra
def detect_and_retransmit():
    start_sequence = bytearray([0x01, 0x4C])
    data = bytearray()

    # Almacena los datos capturados en un arreglo
    captured_data = []

    # Buffer de recepción específico para los datos de la ristra
    track_data_buffer = bytearray()

    # Índice para recorrer la zona de tracks
    track_index = 0

    # Bandera para indicar que hemos capturado el indicador de cabeza
    head_indicator_captured = False

    # Esperar a que se detecte la secuencia de inicio
    while True:
        received_data = uart_in.read(1)
        if received_data is not None:
            data.append(received_data[0])

            # Verificar si hemos capturado la secuencia de inicio y el indicador de cabeza
            if not head_indicator_captured and len(data) >= 12:
                head_indicator = data[11]  # Capturar el indicador de cabeza
                head_indicator_captured = True

            if head_indicator_captured:
                # Capturar los datos de la ristra
                track_data_buffer.append(received_data[0])

                # Cuando tengamos suficientes datos en el buffer de la ristra, procesarlos
                if len(track_data_buffer) >= 20:
                    track_data = track_data_buffer[:20]  # Extraer los datos de la ristra
                    track_value = track_data[3]  # Capturar el valor del dato de la ristra

                    # Verificar si el valor está entre 1 y 16
                    if track_value in range(1, 17):
                        captured_data.append((head_indicator, track_value))  # Almacenar el par (indicador de cabeza, valor de la ristra)

                    # Reiniciar el buffer de datos de la ristra
                    track_data_buffer = bytearray()

                    # Incrementar el índice de la ristra
                    track_index += 1

            
            # Si hemos capturado suficientes datos de la ristra, transmitirlos
            if track_index >= 16:
                if captured_data:  # Verificar si la lista no está vacía
                    print("Captured Data:", captured_data)  # Imprimir los datos capturados
                    uart_out.write(bytearray([head_indicator, captured_data[0][1]]))  # Retransmitir el primer dato capturado de la ristra
                    print("Transmitted Data:", [head_indicator, captured_data[0][1]])  # Imprimir los datos transmitidos
                break
# Loop principal
while True:
    detect_and_retransmit()

