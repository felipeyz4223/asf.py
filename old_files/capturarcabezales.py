# Bucle principal
while True:
    # Lista para almacenar los datos de los mensajes recibidos
    received_messages = []
    received_messages = uart2.readline()
    # Verificar si se recibió algún dato
    if received_messages:
        # Imprimir el mensaje recibido en la consola
        print("Mensaje recibido:", received_messages)

        # Iterar sobre los mensajes recibidos
        for message in received_messages:
            # Separar los primeros 339 datos del mensaje
            first_339_data = message[:339]
            

            section1 = first_339_data[:4]
            section2 = first_339_data[4:16]
            section3 = first_339_data[16:336]
            section4 = first_339_data[336:]
            
            # Verificar el valor del primer arreglo
            if section1 == b'\x5A\x5A\x01\x4C':
                # Transmitir solo la sección 2
                
                all_tracks = parseRows(section3)

            else:
                # Transmitir toda la palabra recibida
                transmit_message(received_messages)
            
            # Si quedan datos en el mensaje, procesarlos
            remaining_data = message[339:]
            if remaining_data:
                # Separar los primeros 339 datos del mensaje restante
                first_339_data = remaining_data[:339]
                
                # Dividir la palabra en cuatro secciones
                section1 = first_339_data[:4]
                section2 = first_339_data[4:16]
                section3 = first_339_data[16:336]
                section4 = first_339_data[336:]
                
                if section1 == b'\x5A\x5A\x01\x4C':
                    # Transmitir solo la sección 2
                    
                    all_tracks = parseRows(section3)
                
                # Actualizar los datos restantes
                remaining_data = remaining_data[339:]
            else:
                print(all_tracks)
                #transmit_message(section2)
                msgTx = "$" +  prepareTxMsg(all_tracks) + "*"
                print("mensaje para TX ::::  ",  msgTx )
                transmit_message( msgTx )
