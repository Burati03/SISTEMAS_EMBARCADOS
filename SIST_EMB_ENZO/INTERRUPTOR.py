import random
import time

def sensor_de_presenca():
    return random.choice(["presença", "nenhuma presença"])

def acender_lampada():
    estado_sensor = sensor_de_presenca()
    print("-------------------------")
    print(" Lâmpada : 💡 (acesa)")
    if estado_sensor == "presença":

    else:
        print(" Lâmpada : desligada")
    print(f" Sensor detectou: {estado_sensor}")
    print("-------------------------")

def interruptor():
    while True:
        acender_lampada()
        time.sleep(5)

interruptor()