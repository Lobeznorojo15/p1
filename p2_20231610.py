#%%
from gpiozero import LED
import psutil

G_LED = 18
Y_LED = 24
R_LED = 23


g_led = LED(G_LED)
y_led = LED(Y_LED)
r_led = LED(R_LED)


try:
    while True:
        cpu_por = psutil.cpu_percent(interval=1) 
    
        if  cpu_por < 10:
            g_led.on()
            y_led.off()
            r_led.off()
            print(cpu_por)

        elif cpu_por >= 10.0 and cpu_por < 20.0:
            g_led.off()
            y_led.blink()
            r_led.off()
            print(cpu_por)

        else:
            g_led.off()
            y_led.off()
            r_led.blink() 
            print(cpu_por)


except KeyboardInterrupt:
    pass

finally:
    g_led.off()
    y_led.off()
    r_led.off()
# %%
