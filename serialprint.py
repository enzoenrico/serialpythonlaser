import serial
import time


def startup():
    comport = input("[+]Insira uma posta Serial para uso: \n")
    try:
        global ser
        ser = serial.Serial(comport, 9600)

    except:
        print('[-]Erro na porta serial')

    if "COM" not in comport:
        print('[-]Insira uma porta válida!')
        exit()

    # iniciar a porta serial

    try:
        print(f"[~]Programa lendo/escrevendo: {ser.name}\n")

    except:
        print('[-]Algo deu errado, por favor reinicie o programa e tente novamente \n')


def write_coords(coord):
    # #imprimir linha do monitor serial
    # serial_line = ser.readline()
    # print(filter(["/n", "/r", "'"], serial_line))

    # mlk como caralhos eu traduzo utf-8 pra byte e pra utf-8 dnv
    # tem q coloca isso no codigo final
    # ser_line = ser.write(coord.encode('utf-8'))
    print(coord.encode('utf-8'))
    time.sleep(0.1)
