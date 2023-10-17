#%%
from gpiozero import LED
import psutil

G_LED = 18
Y_LED = 24
R_LED = 23


# Inicializa los LEDs
g_led = LED(G_LED)
y_led = LED(Y_LED)
r_led = LED(R_LED)


     
    while True:
       
        cpu_por = psutil.cpu_percent(interval=1) 
    
    
        if  cpu_por < 10:
            g_led.on()
            y_led.off()
            r_led.off()
            print(cpu_por)

        elif 10 <= cpu_por <= 20:
            g_led.off()
            y_led.blink()
            r_led.off()
            print(cpu_por)

        else:
            g_led.off()
            y_led.off()
            r_led.blink() 
            print(cpu_por)


# %%
