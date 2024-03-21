import pyb

from comparar_valores import *
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
def parseRows(cabezalId, last_section):
    #0 .. 15
    all_tracks = {}
    for i in range(16):
        track_num = ""
        trackDict = {}
        track_num , trackDict = parseRowTrack( last_section[i*20 : (i+1)*20] )
        all_tracks[ (cabezalId , track_num) ] = trackDict

    if(last_section[16*20 + 1:] == b'\xA5\xA5' ):
        print("message_ends")

    return all_tracks

def prepareTxArr(all_tracks_arr):
    msgArr = []
    for trackNum in all_tracks_arr.keys():
        print("Número de pista:", trackNum)  # Imprimir el número de pista
        
        msgArr.append( str(trackNum[0]) )
        msgArr.append( str(trackNum[1]) )# Convertir el número de pista a una cadena

        bcd_value = all_tracks_arr[trackNum]["ieee754_value"]
        print("Valor IEEE754 encontrado:", bcd_value)  # Imprimir el valor IEEE754
        msb_values, lsb_values = comparar_valores( all_tracks_arr[trackNum]["ieee754_value"] )
        msgArr.append(str(msb_values) + str(lsb_values))
        #msgArr.append(str(bcd_value))

        # Vaciar las variables locales
        trackNum_str = None
        bcd_value = None
        msb_values = None
        lsb_values = None
    return msgArr

def prepareTxMsg( all_tracks_dict ):
    msgArr = []
    for trackId in sorted(all_tracks_dict.keys()):
        trackId_str = str(trackId)  # Convertir el número de pista a una cadena
        print("Número de pista:", trackId_str)  # Imprimir el número de pista

        msgArr.append(trackId_str)

        msb_values, lsb_values = comparar_valores( all_tracks_dict[trackId]["ieee754_value"] )
        msgArr.append(str(msb_values) + str(lsb_values))

        # Vaciar las variables locales
        trackId_str = None
        msb_values = None
        lsb_values = None
    msgStr = ",".join(msgArr)
    return msgStr

def prepareArrForTxMsg(all_tracks_arr):
    msgStr = ",".join(all_tracks_arr)
    return msgStr

# Función para transmitir un mensaje por UART2
def transmit_message(message):
    uart2.write(message)

# Bucle principal
while True:
    # Leer mensaje de UART2
    received_message = uart2.readline()

    all_tracks = {}  # dict is cleared.  
    #No longer using a list, since all_tracks.keys() are (cabezal_id,tracknum) ordinal pairs

    # Verificar si se recibió algún dato
    if received_message:
        # Imprimir el mensaje recibido en la consola
        print("Mensaje recibido:", received_message)

        # Si quedan datos en el mensaje, procesarlos
        remaining_data = received_message[:]
        while remaining_data:
            # Separar los primeros 339 datos del mensaje restante
            first_339_data = remaining_data[:339]

            # Dividir la palabra en cuatro secciones
            section1 = first_339_data[:4]
            section2 = first_339_data[4:16]
            section3 = first_339_data[16:336]
            section4 = first_339_data[336:]

            # cabezal ID == 0,1,2,3,4,5,6,7
            # • BDT CAS	        (00)
            # • BDT CAS ABF     (01)
            # • LDT CAS         (02)
            # • DEMON CAS       (03)
            # • BDT FAS         (04)
            # • BDT FAS ABF     (05)
            # • LDT FAS         (06)
            # • DEMON FAS       (07)
            cabezal_id = section2[11]

            # Procesar las secciones del mensaje restante
            if section1 == b'\x5A\x5A\x01\x4C':
                # Transmitir solo la sección 3
                all_tracks = parseRows(cabezal_id, section3)
            else:
                # Transmitir toda la palabra recibida
                transmit_message(received_message)

            # Actualizar los datos restantes
            remaining_data = remaining_data[339:]
            # prevent while loop from infinite loops
            if( len(remaining_data) < 339 ):
                break

        # Transmitir los datos procesados (si es necesario)
        if all_tracks:
            # Realizar la transmisión de los datos procesados
            msgTx = "$" + prepareTxMsg(all_tracks) + "*"
            print("mensaje para TX ::::  ",  msgTx )
            transmit_message(msgTx)
