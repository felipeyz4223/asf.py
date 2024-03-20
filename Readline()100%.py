import pyb

# Configurar la velocidad de trabajo del microcontrolador a 100 MHz
pyb.freq(100000000)

# Configurar UART2 para recepción y transmisión a 38400 baudios
uart2 = pyb.UART(2, 38400)
uart2.init(baudrate=38400, bits=8, parity=None, stop=1, timeout=261, flow=0, timeout_char=261, read_buf_len=339)

# Función para transmitir un mensaje por UART2
def transmit_message(message):
    uart2.write(message)

# Bucle principal
while True:
    # Leer mensaje de UART2
    received_data = uart2.readline()
    
    # Verificar si se recibió algún dato
    if received_data:
        # Imprimir el mensaje recibido en la consola
        print("Mensaje recibido:", received_data)
        
        # Dividir la palabra en tres secciones
        section1 = received_data[:4]
        section2 = received_data[4:16]
        section3 = received_data[16:]
        
        # Verificar el valor del primer arreglo
        if section1 == b'\x5A\x5A\x01\x4C':
            # Transmitir solo la sección 2
            transmit_message(section2)
        else:
            # Transmitir toda la palabra recibida
            transmit_message(received_data)
