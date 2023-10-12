from gpiozero import LED
from time import sleep
print("Hola")
# Configuración de pines GPIO
led_azul = LED(17)  # Define un objeto LED para el pin GPIO 17
led_rojo = LED(18)  # Define un objeto LED para el pin GPIO 18
led_verde = LED(27)  # Define un objeto LED para el pin GPIO 27

def apagar_todos():
    # Apaga todos los LEDs
    led_azul.off()
    led_rojo.off()
    led_verde.off()

def encender_led(color):
    apagar_todos()  # Asegura que todos los LEDs estén apagados antes de encender uno
    
    # Enciende el LED correspondiente al color seleccionado
    if color == 'azul':
        led_azul.on()
    elif color == 'rojo':
        led_rojo.on()
    elif color == 'verde':
        led_verde.on()

try:
    color_elegido = input("Ingresa el color (azul, rojo o verde): ").lower()  # Pide al usuario que ingrese un color
    encender_led(color_elegido)  # Enciende el LED correspondiente al color elegido
    sleep(5)  # El LED permanecerá encendido durante 5 segundos
    apagar_todos()  # Apaga todos los LEDs
except KeyboardInterrupt:
    pass
finally:
    apagar_todos()  # En caso de que se interrumpa el programa, asegura que todos los LEDs estén apagados
