import random
import time
 
def sensor_de_presenca():
    return random.choice(["presença", "nenhuma presença"])

def lampada():
    estado_sensor = sensor_de_presenca()
    print("-------------------------")
    print(f" Sensor detectou: {estado_sensor}") 
    if estado_sensor == "presença":
        print(" Lâmpada : 💡 (acesa)")
    else:
        print(" Lâmpada : desligada")
    print("-------------------------")

def interruptor():
    while True:
        lampada()
        time.sleep(5)

interruptor()
