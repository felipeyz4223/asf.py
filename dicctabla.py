import pyb

# Configurar la velocidad de trabajo del microcontrolador a 100 MHz
pyb.freq(100000000)

# Configurar UART2 para recepción y transmisión a 38400 baudios
uart2 = pyb.UART(2, 38400)
uart2.init(baudrate=38400, bits=8, parity=None, stop=1, timeout=261, flow=0, timeout_char=261, read_buf_len=339)
def comparar_valores(ieee754_values):

        # Inicializar listas para almacenar los resultados
    msb_values = []
    lsb_values = []
    
    # Iterar sobre cada valor en la secuencia de arreglos
    for value in ieee754_values:
        combined_data = (ieee754_values[0] << 24) | (ieee754_values[1] << 16) | (ieee754_values[2] << 8) | ieee754_values[3]  # Combinar los cuatro valores en uno solo
            # Realizar la comparación con los rangos hexadecimales
        if combined_data <= 0x3FC00000:
            return 1, 0
        elif combined_data < 0x40200000:
            return 2, 0
        elif combined_data < 0x40600000:
            return 3, 0
        elif combined_data < 0x40900000:
            return 4, 0
        elif combined_data < 0x40B00000:
            return 5, 0
        elif combined_data < 0x40D00000:
            return 6, 0
        elif combined_data < 0x40F00000:
            return 7, 0
        elif combined_data < 0x41080000:
            return 8, 0
        elif combined_data < 0x41180000:
            return 9, 0
        elif combined_data < 0x41280000:
            return 10, 0
        elif combined_data < 0x41380000:
            return 11, 0
        elif combined_data < 0x41480000:
            return 12, 0
        elif combined_data < 0x41580000:
            return 13, 0
        elif combined_data < 0x41680000:
            return 14, 0
        elif combined_data < 0x41780000:
            return 15, 0
        elif combined_data < 0x41840000:
            return 16, 0
        elif combined_data < 0x418C0000:
            return 17, 0
        elif combined_data < 0x41940000:
            return 18, 0
        elif combined_data < 0x419C0000:
            return 19, 0
        elif combined_data < 0x41A40000:
            return 20, 0
        elif combined_data < 0x41AC0000:
            return 21, 0
        elif combined_data < 0x41B40000:
            return 22, 0
        elif combined_data < 0x41BC0000:
            return 23, 0
        elif combined_data < 0x41C40000:
            return 24, 0
        elif combined_data < 0x41CC0000:
            return 25, 0
        elif combined_data < 0x41D40000:
            return 26, 0
        elif combined_data < 0x41DC0000:
            return 27, 0
        elif combined_data < 0x41E40000:
            return 28, 0
        elif combined_data < 0x41EC0000:
            return 29, 0
        elif combined_data < 0x41F40000:
            return 30, 0
        elif combined_data < 0x41FC0000:
            return 31, 0
        elif combined_data < 0x42020000:
            return 32, 0
        elif combined_data < 0x42060000:
            return 33, 0
        elif combined_data < 0x420A0000:
            return 34, 0
        elif combined_data < 0x420E0000:
            return 35, 0
        elif combined_data < 0x42120000:
            return 36, 0
        elif combined_data < 0x42160000:
            return 37, 0
        elif combined_data < 0x421A0000:
            return 38, 0
        elif combined_data < 0x421E0000:
            return 39, 0
        elif combined_data < 0x42220000:
            return 40, 0
        elif combined_data < 0x42260000:
            return 41, 0
        elif combined_data < 0x422A0000:
            return 42, 0
        elif combined_data < 0x422E0000:
            return 43, 0
        elif combined_data < 0x42320000:
            return 44, 0
        elif combined_data < 0x42360000:
            return 45, 0
        elif combined_data < 0x423A0000:
            return 46, 0
        elif combined_data < 0x423E0000:
            return 47, 0
        elif combined_data < 0x42420000:
            return 48, 0
        elif combined_data < 0x42460000:
            return 49, 0
        elif combined_data < 0x424A0000:
            return 50, 0
        elif combined_data < 0x424E0000:
            return 51, 0
        elif combined_data < 0x42520000:
            return 52, 0
        elif combined_data < 0x42560000:
            return 53, 0
        elif combined_data < 0x425A0000:
            return 54, 0
        elif combined_data < 0x425E0000:
            return 55, 0
        elif combined_data < 0x424C0000:
            return 56, 0
        elif combined_data < 0x42660000:
            return 57, 0
        elif combined_data < 0x426A0000:
            return 58, 0
        elif combined_data < 0x426E0000:
            return 59, 0
        elif combined_data < 0x42720000:
            return 60, 0
        elif combined_data < 0x42760000:
            return 61, 0
        elif combined_data < 0x427A0000:
            return 62, 0
        elif combined_data < 0x427E0000:
            return 63, 0
        elif combined_data < 0x42810000:
            return 64, 0
        elif combined_data < 0x42830000:
            return 65, 0
        elif combined_data < 0x42850000:
            return 66, 0
        elif combined_data < 0x42870000:
            return 67, 0
        elif combined_data < 0x42890000:
            return 68, 0
        elif combined_data < 0x428B0000:
            return 69, 0
        elif combined_data < 0x428D0000:
            return 70, 0
        elif combined_data < 0x428F0000:
            return 71, 0
        elif combined_data < 0x42910000:
            return 72, 0
        elif combined_data < 0x42930000:
            return 73, 0
        elif combined_data < 0x42950000:
            return 74, 0
        elif combined_data < 0x42970000:
            return 75, 0
        elif combined_data < 0x42990000:
            return 76, 0
        elif combined_data < 0x429B0000:
            return 77, 0
        elif combined_data < 0x429D0000:
            return 78, 0
        elif combined_data < 0x429F0000:
            return 79, 0
        elif combined_data < 0x42A10000:
            return 80, 0
        elif combined_data < 0x42A30000:
            return 81, 0
        elif combined_data < 0x42A50000:
            return 82, 0
        elif combined_data < 0x42A70000:
            return 83, 0
        elif combined_data < 0x42A90000:
            return 84, 0
        elif combined_data < 0x42AB0000:
            return 85, 0
        elif combined_data < 0x42AD0000:
            return 86, 0
        elif combined_data < 0x42AF0000:
            return 87, 0
        elif combined_data < 0x42B10000:
            return 88, 0
        elif combined_data < 0x42B30000:
            return 89, 0
        elif combined_data < 0x42B50000:
            return 90, 0
        elif combined_data < 0x42B70000:
            return 91, 0
        elif combined_data < 0x42B90000:
            return 92, 0
        elif combined_data < 0x42BB0000:
            return 93, 0
        elif combined_data < 0x42BD0000:
            return 94, 0
        elif combined_data < 0x42BF0000:
            return 95, 0
        elif combined_data < 0x42C10000:
            return 96, 0
        elif combined_data < 0x42C30000:
            return 97, 0
        elif combined_data < 0x42C50000:
            return 98, 0
        elif combined_data < 0x42C70000:
            return 99, 0
        elif combined_data < 0x42C90000:
            return 0, 1
        elif combined_data < 0x42CB0000:
            return 1, 1
        elif combined_data < 0x42CD0000:
            return 2, 1
        elif combined_data < 0x42CF0000:
            return 3, 1
        elif combined_data < 0x42D10000:
            return 4, 1
        elif combined_data < 0x42D30000:
            return 5, 1
        elif combined_data < 0x42D50000:
            return 6, 1
        elif combined_data < 0x42D70000:
            return 7, 1
        elif combined_data < 0x42D90000:
            return 8, 1
        elif combined_data < 0x42DB0000:
            return 9, 1
        elif combined_data < 0x42DD0000:
            return 10, 1
        elif combined_data < 0x42DF0000:
            return 11, 1
        elif combined_data < 0x42E10000:
            return 12, 1
        elif combined_data < 0x42E30000:
            return 13, 1
        elif combined_data < 0x42E50000:
            return 14, 1
        elif combined_data < 0x42E70000:
            return 15, 1
        elif combined_data < 0x42E90000:
            return 16, 1
        elif combined_data < 0x42EB0000:
            return 17, 1
        elif combined_data < 0x42ED0000:
            return 18, 1
        elif combined_data < 0x42EF0000:
            return 19, 1
        elif combined_data < 0x42F10000:
            return 20, 1
        elif combined_data < 0x42F30000:
            return 21, 1
        elif combined_data < 0x42F50000:
            return 22, 1
        elif combined_data < 0x42F70000:
            return 23, 1
        elif combined_data < 0x42F90000:
            return 24, 1
        elif combined_data < 0x42FB0000:
            return 25, 1
        elif combined_data < 0x42FD0000:
            return 26, 1
        elif combined_data < 0x42FF0000:
            return 27, 1
        elif combined_data < 0x43008000:
            return 28, 1
        elif combined_data < 0x43018000:
            return 29, 1
        elif combined_data < 0x43028000:
            return 30, 1
        elif combined_data < 0x43038000:
            return 31, 1
        elif combined_data < 0x43048000:
            return 32, 1
        elif combined_data < 0x43058000:
            return 33, 1
        elif combined_data < 0x43068000:
            return 34, 1
        elif combined_data < 0x43078000:
            return 35, 1
        elif combined_data < 0x43088000:
            return 36, 1
        elif combined_data < 0x43098000:
            return 37, 1
        elif combined_data < 0x430A8000:
            return 38, 1
        elif combined_data < 0x430B8000:
            return 39, 1
        elif combined_data < 0x430C8000:
            return 40, 1
        elif combined_data < 0x430D8000:
            return 41, 1
        elif combined_data < 0x430E8000:
            return 42, 1
        elif combined_data < 0x430F8000:
            return 43, 1
        elif combined_data < 0x43108000:
            return 44, 1
        elif combined_data < 0x43118000:
            return 45, 1
        elif combined_data < 0x43128000:
            return 46, 1
        elif combined_data < 0x43138000:
            return 47, 1
        elif combined_data < 0x43148000:
            return 48, 1
        elif combined_data < 0x43158000:
            return 49, 1
        elif combined_data < 0x43168000:
            return 50, 1
        elif combined_data < 0x43178000:
            return 51, 1
        elif combined_data < 0x43188000:
            return 52, 1
        elif combined_data < 0x43198000:
            return 53, 1
        elif combined_data < 0x431A8000:
            return 54, 1
        elif combined_data < 0x431B8000:
            return 55, 1
        elif combined_data < 0x431C8000:
            return 56, 1
        elif combined_data < 0x431D8000:
            return 57, 1
        elif combined_data < 0x431E8000:
            return 58, 1
        elif combined_data < 0x431F8000:
            return 59, 1
        elif combined_data < 0x43208000:
            return 60, 1
        elif combined_data < 0x43218000:
            return 61, 1
        elif combined_data < 0x43228000:
            return 62, 1
        elif combined_data < 0x43238000:
            return 63, 1
        elif combined_data < 0x43248000:
            return 64, 1
        elif combined_data < 0x43258000:
            return 65, 1
        elif combined_data < 0x43268000:
            return 66, 1
        elif combined_data < 0x43278000:
            return 67, 1
        elif combined_data < 0x43288000:
            return 68, 1
        elif combined_data < 0x43298000:
            return 69, 1
        elif combined_data < 0x432A8000:
            return 70, 1
        elif combined_data < 0x432B8000:
            return 71, 1
        elif combined_data < 0x432C8000:
            return 72, 1
        elif combined_data < 0x432D8000:
            return 73, 1
        elif combined_data < 0x432E8000:
            return 74, 1
        elif combined_data < 0x432F8000:
            return 75, 1
        elif combined_data < 0x43308000:
            return 76, 1
        elif combined_data < 0x43318000:
            return 77, 1
        elif combined_data < 0x43328000:
            return 78, 1
        elif combined_data < 0x43338000:
            return 79, 1
        elif combined_data < 0x43348000:
            return 80, 1
        elif combined_data < 0x43358000:
            return 81, 1
        elif combined_data < 0x43368000:
            return 82, 1
        elif combined_data < 0x43378000:
            return 83, 1
        elif combined_data < 0x43388000:
            return 84, 1
        elif combined_data < 0x43398000:
            return 85, 1
        elif combined_data < 0x433A8000:
            return 86, 1
        elif combined_data < 0x433B8000:
            return 87, 1
        elif combined_data < 0x433C8000:
            return 88, 1
        elif combined_data < 0x433D8000:
            return 89, 1
        elif combined_data < 0x433E8000:
            return 90, 1
        elif combined_data < 0x433F8000:
            return 91, 1
        elif combined_data < 0x43408000:
            return 92, 1
        elif combined_data < 0x43418000:
            return 93, 1
        elif combined_data < 0x43428000:
            return 94, 1
        elif combined_data < 0x43438000:
            return 95, 1
        elif combined_data < 0x43448000:
            return 96, 1
        elif combined_data < 0x43458000:
            return 97, 1
        elif combined_data < 0x43468000:
            return 98, 1
        elif combined_data < 0x43478000:
            return 99, 1
        elif combined_data < 0x43488000:
            return 0, 2
        elif combined_data < 0x43498000:
            return 1, 2
        elif combined_data < 0x434A8000:
            return 2, 2
        elif combined_data < 0x434B8000:
            return 3, 2
        elif combined_data < 0x434C8000:
            return 4, 2
        elif combined_data < 0x434D8000:
            return 5, 2
        elif combined_data < 0x434E8000:
            return 6, 2
        elif combined_data < 0x434F8000:
            return 7, 2
        elif combined_data < 0x43508000:
            return 8, 2
        elif combined_data < 0x43518000:
            return 9, 2
        elif combined_data < 0x43528000:
            return 10, 2
        elif combined_data < 0x43538000:
            return 11, 2
        elif combined_data < 0x43548000:
            return 12, 2
        elif combined_data < 0x43558000:
            return 13, 2
        elif combined_data < 0x43568000:
            return 14, 2
        elif combined_data < 0x43578000:
            return 15, 2
        elif combined_data < 0x43588000:
            return 16, 2
        elif combined_data < 0x43598000:
            return 17, 2
        elif combined_data < 0x435A8000:
            return 18, 2
        elif combined_data < 0x435B8000:
            return 19, 2
        elif combined_data < 0x435C8000:
            return 20, 2
        elif combined_data < 0x435D8000:
            return 21, 2
        elif combined_data < 0x435E8000:
            return 22, 2
        elif combined_data < 0x435F8000:
            return 23, 2
        elif combined_data < 0x43608000:
            return 24, 2
        elif combined_data < 0x43618000:
            return 25, 2
        elif combined_data < 0x43628000:
            return 26, 2
        elif combined_data < 0x43638000:
            return 27, 2
        elif combined_data < 0x43648000:
            return 28, 2
        elif combined_data < 0x43658000:
            return 29, 2
        elif combined_data < 0x43668000:
            return 30, 2
        elif combined_data < 0x43678000:
            return 31, 2
        elif combined_data < 0x43688000:
            return 32, 2
        elif combined_data < 0x43698000:
            return 33, 2
        elif combined_data < 0x436A8000:
            return 34, 2
        elif combined_data < 0x436B8000:
            return 35, 2
        elif combined_data < 0x436C8000:
            return 36, 2
        elif combined_data < 0x436D8000:
            return 37, 2
        elif combined_data < 0x436E8000:
            return 38, 2
        elif combined_data < 0x436F8000:
            return 39, 2
        elif combined_data < 0x43708000:
            return 40, 2
        elif combined_data < 0x43718000:
            return 41, 2
        elif combined_data < 0x43728000:
            return 42, 2
        elif combined_data < 0x43738000:
            return 43, 2
        elif combined_data < 0x43748000:
            return 44, 2
        elif combined_data < 0x43758000:
            return 45, 2
        elif combined_data < 0x43768000:
            return 46, 2
        elif combined_data < 0x43778000:
            return 47, 2
        elif combined_data < 0x43788000:
            return 48, 2
        elif combined_data < 0x43798000:
            return 49, 2
        elif combined_data < 0x437A8000:
            return 50, 2
        elif combined_data < 0x437B8000:
            return 51, 2
        elif combined_data < 0x437C8000:
            return 52, 2        
        elif combined_data < 0x437D8000:
            return 53, 2
        elif combined_data < 0x437E8000:
            return 54, 2
        elif combined_data < 0x437F8000:
            return 55, 2
        elif combined_data < 0x43804000:
            return 56, 2
        elif combined_data < 0x4380C000:
            return 57, 2
        elif combined_data < 0x43814000:
            return 58, 2
        elif combined_data < 0x4381C000:
            return 59, 2
        elif combined_data < 0x43824000:
            return 60, 2
        elif combined_data < 0x4382C000:
            return 61, 2
        elif combined_data < 0x43834000:
            return 62, 2
        elif combined_data < 0x4383C000:
            return 63, 2
        elif combined_data < 0x43844000:
            return 64, 2
        elif combined_data < 0x4384C000:
            return 65, 2
        elif combined_data < 0x43854000:
            return 66, 2
        elif combined_data < 0x4385C000:
            return 67, 2
        elif combined_data < 0x43864000:
            return 68, 2
        elif combined_data < 0x4386C000:
            return 69, 2
        elif combined_data < 0x43874000:
            return 70, 2
        elif combined_data < 0x4387C000:
            return 71, 2
        elif combined_data < 0x43884000:
            return 72, 2
        elif combined_data < 0x4388C000:
            return 73, 2
        elif combined_data < 0x43894000:
            return 74, 2
        elif combined_data < 0x4389C000:
            return 75, 2
        elif combined_data < 0x438A4000:
            return 76, 2
        elif combined_data < 0x438AC000:
            return 77, 2
        elif combined_data < 0x438B4000:
            return 78, 2
        elif combined_data < 0x438BC000:
            return 79, 2
        elif combined_data < 0x438C4000:
            return 80, 2
        elif combined_data < 0x438CC000:
            return 81, 2
        elif combined_data < 0x438D4000:
            return 82, 2
        elif combined_data < 0x438DC000:
            return 83, 2
        elif combined_data < 0x438E4000:
            return 84, 2
        elif combined_data < 0x438EC000:
            return 85, 2
        elif combined_data < 0x438F4000:
            return 86, 2
        elif combined_data < 0x438FC000:
            return 87, 2
        elif combined_data < 0x43904000:
            return 88, 2
        elif combined_data < 0x4390C000:
            return 89, 2
        elif combined_data < 0x43914000:
            return 90, 2
        elif combined_data < 0x4391C000:
            return 91, 2
        elif combined_data < 0x43924000:
            return 92, 2
        elif combined_data < 0x4392C000:
            return 93, 2
        elif combined_data < 0x43934000:
            return 94, 2
        elif combined_data < 0x4393C000:
            return 95, 2
        elif combined_data < 0x43944000:
            return 96, 2
        elif combined_data < 0x4394C000:
            return 97, 2
        elif combined_data < 0x43954000:
            return 98, 2
        elif combined_data < 0x4395C000:
            return 99, 2
        elif combined_data < 0x43964000:
            return 0, 3
        elif combined_data < 0x4396C000:
            return 1, 3  
        elif combined_data < 0x43974000:
            return 2, 3
        elif combined_data < 0x4397C000:
            return 3, 3
        elif combined_data < 0x43984000:
            return 4, 3
        elif combined_data < 0x4398C000:
            return 5, 3
        elif combined_data < 0x43994000:
            return 6, 3
        elif combined_data < 0x4399C000:
            return 7, 3
        elif combined_data < 0x439A4000:
            return 8, 3
        elif combined_data < 0x439AC000:
            return 9, 3
        elif combined_data < 0x439B4000:
            return 10, 3
        elif combined_data < 0x439BC000:
            return 11, 3
        elif combined_data < 0x439C4000:
            return 12, 3
        elif combined_data < 0x439CC000:
            return 13, 3
        elif combined_data < 0x439D4000:
            return 14, 3
        elif combined_data < 0x439DC000:
            return 15, 3
        elif combined_data < 0x439E4000:
            return 16, 3
        elif combined_data < 0x439EC000:
            return 17, 3
        elif combined_data < 0x439F4000:
            return 18, 3
        elif combined_data < 0x439FC000:
            return 19, 3
        elif combined_data < 0x43A04000:
            return 20, 3
        elif combined_data < 0x43A0C000:
            return 21, 3
        elif combined_data < 0x43A14000:
            return 22, 3
        elif combined_data < 0x43A1C000:
            return 23, 3
        elif combined_data < 0x43A24000:
            return 24, 3
        elif combined_data < 0x43A2C000:
            return 25, 3
        elif combined_data < 0x43A34000:
            return 26, 3
        elif combined_data < 0x43A3C000:
            return 27, 3
        elif combined_data < 0x43A44000:
            return 28, 3
        elif combined_data < 0x43A4C000:
            return 29, 3
        elif combined_data < 0x43A54000:
            return 30, 3
        elif combined_data < 0x43A5C000:
            return 31, 3
        elif combined_data < 0x43A64000:
            return 32, 3
        elif combined_data < 0x43A6C000:
            return 33, 3
        elif combined_data < 0x43A74000:
            return 34, 3
        elif combined_data < 0x43A7C000:
            return 35, 3
        elif combined_data < 0x43A84000:
            return 36, 3
        elif combined_data < 0x43A8C000:
            return 37, 3
        elif combined_data < 0x43A94000:
            return 38, 3
        elif combined_data < 0x43A9C000:
            return 39, 3
        elif combined_data < 0x43AA4000:
            return 40, 3
        elif combined_data < 0x43AAC000:
            return 41, 3
        elif combined_data < 0x43AB4000:
            return 42, 3
        elif combined_data < 0x43ABC000:
            return 43, 3
        elif combined_data < 0x43AC4000:
            return 44, 3
        elif combined_data < 0x43ACC000:
            return 45, 3
        elif combined_data < 0x43AD4000:
            return 46, 3
        elif combined_data < 0x43ADC000:
            return 47, 3
        elif combined_data < 0x43AE4000:
            return 48, 3
        elif combined_data < 0x43AEC000:
            return 49, 3
        elif combined_data < 0x43AF4000:
            return 50, 3
        elif combined_data < 0x43AFC000:
            return 51, 3
        elif combined_data < 0x43B04000:
            return 52, 3
        elif combined_data < 0x43B0C000:
            return 53, 3
        elif combined_data < 0x43B14000:
            return 54, 3
        elif combined_data < 0x43B1C000:
            return 55, 3
        elif combined_data < 0x43B24000:
            return 56, 3
        elif combined_data < 0x43B2C000:
            return 57, 3
        elif combined_data < 0x43B34000:
            return 58, 3
        elif combined_data < 0x43B3C000:
            return 59, 3    
        else:
            return None, None  # Valor fuera del rango definido
        msb_value = value[:2]
        lsb_value = value[2:]
        
        # Agregar los valores a las listas correspondientes
        msb_values.append(msb_value)
        lsb_values.append(lsb_value)
    
    # Devolver las listas de valores MSB y LSB
    return msb_values, lsb_values
    

#from a single row, cut out the important info, return num & dict
def parseRowTrack(row_track):
    trackDict = {}
    track_num = row_track[3]
    track_valido = row_track[17:20]   # la demcarcacion esta entre los bytes 17:20
    ieee754_value = row_track[17:20]  # might not work, so maybe  row_track[17:20]
    trackDict["track_valido"] = track_valido 
    trackDict["ieee754_value"] = ieee754_value
    print(track_num , " :: ", trackDict )
    return track_num , trackDict

#parse all rows, return Dictionary of each track as key
def parseRows( last_section):
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
def prepareTxMsg(all_tracks):
    msgArr = []
    for trackNum in sorted(all_tracks.keys()):
        # Convertir la clave de bytearray a str
        trackNum_str = bytes([trackNum]).decode('ascii', 'ignore')
        
        if trackNum_str == '\x00':
            continue
        

        trackNum= bytearray()
    
        #TODO:
        ## necesitas hacer un conversor de ieee754 --> BCD
        valorconvertidomsb,valorconvertidolsb  = comparar_valores( all_tracks[trackNum]["ieee754_value"] )
        #print("track encontrado", bcd_value)
        
        msgArr.append( valorconvertidomsb )
        msgArr.append( valorconvertidolsb )
        msgArr.append(trackNum_str)

    
    msgStr = ",".join(msgArr)
    return msgStr



def parseSensorNumber(sensorByteArr):

    sensorNumber = sensorByteArr[3]
    
    # Convertir la cadena limpia en un número entero
    sensorNumber = bytearray()
    
    return sensorNumber

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
        
        # Dividir la palabra en cuatro secciones
        section1 = received_data[:4]
        section2 = received_data[4:16]
        section3 = received_data[16:336]
        section4 = received_data[336:]
        
        # Verificar el valor del primer arreglo
        if section1 == b'\x5A\x5A\x01\x4C':
            # Transmitir solo la sección 2
            all_tracks = {}
            all_tracks = parseRows(section3)
            print(all_tracks)
            sensorNumber = parseSensorNumber(section2)
            msgTx = "$" +  prepareTxMsg(all_tracks) + "," + sensorNumber + "*"
            print("mensaje para TX ::::  ",  msgTx )
            transmit_message( msgTx )
        else:
            # Transmitir toda la palabra recibida
            transmit_message(received_data)
