import pyb

# Configurar la velocidad de trabajo del microcontrolador a 100 MHz
pyb.freq(100000000)

# Configurar UART2 para recepción y transmisión a 38400 baudios
uart2 = pyb.UART(2, 38400)
uart2.init(baudrate=38400, bits=8, parity=None, stop=1, timeout=261, flow=0, timeout_char=261)

#from a single row, cut out the important info, return num & dict
def parseRowTrack(row_track):
    trackDict = {}
    track_num = row_track[3]
    track_valido = row_track[16:19]
    ieee754_value = row_track[16:19]  # might not work, so maybe  row_track[17:20]
    trackDict["track_valido"] = track_valido 
    trackDict["ieee754_value"] = ieee754_value
    print(track_num , " :: ", trackDict )
    return track_num , trackDict

#parse all rows, return Dictionary of each track as key
def parseRows(last_section):
    #0 .. 15
    all_tracks = {}
    for i in range(16):
        track_num = ""
        trackDict = {}
        track_num , trackDict = parseRowTrack( last_section[i*20 : (i+1)*20] )
        all_tracks[track_num] = trackDict
        
    if(last_section[16*20 + 1:] == b'\xA5\xA5' ):
        print("message_ends")
    
    return all_tracks

def prepareTxArr(all_tracks):
    msgArr = []
    for trackNum in all_tracks.keys():
        trackNum_str = str(trackNum)  # Convertir el número de pista a una cadena
        print("Número de pista:", trackNum_str)  # Imprimir el número de pista
        msgArr.append(trackNum_str)

        bcd_value = all_tracks[trackNum]["ieee754_value"]
        print("Valor IEEE754 encontrado:", bcd_value)  # Imprimir el valor IEEE754
        msgArr.append(str(bcd_value))

        # Vaciar las variables locales
        trackNum_str = None
        bcd_value = None
    return msgArr

def prepareTxMsg(all_tracks):
    msgArr = []
    for trackNum in sorted(all_tracks.keys()):
        trackNum_str = str(trackNum)  # Convertir el número de pista a una cadena
        print("Número de pista:", trackNum_str)  # Imprimir el número de pista
        msgArr.append(trackNum_str)

        bcd_value = all_tracks[trackNum]["ieee754_value"]
        print("Valor IEEE754 encontrado:", bcd_value)  # Imprimir el valor IEEE754
        msgArr.append(str(bcd_value))

        # Vaciar las variables locales
        trackNum_str = None
        bcd_value = None

    msgStr = ",".join(msgArr)
    return msgStr

# Función para transmitir un mensaje por UART2
def transmit_message(message):
    uart2.write(message)

# Bucle principal
while True:
    # Leer mensaje de UART2
    received_message = uart2.readline()
    all_tracks = []
    # Verificar si se recibió algún dato
    if received_message:
        # Imprimir el mensaje recibido en la consola
        print("Mensaje recibido:", received_message)

        # Separar los primeros 339 datos del mensaje
        first_339_data = received_message[:339]
        
        # Dividir la palabra en cuatro secciones
        section1 = first_339_data[:4]
        section2 = first_339_data[4:16]
        section3 = first_339_data[16:336]
        section4 = first_339_data[336:]
        
        # Procesar las secciones del primer mensaje
        # Verificar el valor del primer arreglo
        if section1 == b'\x5A\x5A\x01\x4C':
            # Transmitir solo la sección 2
            all_tracks = all_tracks + prepareTxArr(parseRows(section3))
        else:
            # Transmitir toda la palabra recibida
            transmit_message(received_message)
        
        # Si quedan datos en el mensaje, procesarlos
        remaining_data = received_message[339:]
        while remaining_data:
            # Separar los primeros 339 datos del mensaje restante
            first_339_data = remaining_data[:339]
            
            # Dividir la palabra en cuatro secciones
            section1 = first_339_data[:4]
            section2 = first_339_data[4:16]
            section3 = first_339_data[16:336]
            section4 = first_339_data[336:]
            
            # Procesar las secciones del mensaje restante
            if section1 == b'\x5A\x5A\x01\x4C':
                # Transmitir solo la sección 2
                all_tracks = all_tracks + prepareTxArr(parseRows(section3))
            else:
                # Transmitir toda la palabra recibida
                transmit_message(received_message)
            
            # Actualizar los datos restantes
            remaining_data = remaining_data[339:]
        
        # Transmitir los datos procesados (si es necesario)
        if all_tracks:
            # Realizar la transmisión de los datos procesados
            msgTx = "$" + prepareTxMsg(all_tracks) + "*"
            print("mensaje para TX ::::  ",  msgTx )
            transmit_message(msgTx)
