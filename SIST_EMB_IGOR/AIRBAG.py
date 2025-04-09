import random
import time

def 
def sensor_de_impacto():
    return random.choice(["nenhum impacto detectado", "air bag acionado!"])

def acender_lampada():
    estado_sensor = sensor_de_impacto()
    print("-------------------------")
    if estado_sensor == "air bag acionado!":
        print(" Lâmpada : 💡 (acesa)")
    else:
        print(" Lâmpada : desligada")
    print(f" Sensor detectou: {estado_sensor}")
    print("-------------------------")

def interruptor():
    while True:
        acender_lampada()
        time.sleep(5)

interruptor()