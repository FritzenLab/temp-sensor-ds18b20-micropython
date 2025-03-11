# Complete project details at https://RandomNerdTutorials.com/raspberry-pi-pico-ds18b20-micropython/

import machine, onewire, ds18x20, time

ds_pin = machine.Pin(15)
ds_sensor = ds18x20.DS18X20(onewire.OneWire(ds_pin))

roms = ds_sensor.scan()
print('Found DS devices: ', roms)
initialtime= time.ticks_ms() #https://docs.micropython.org/en/latest/library/time.html
timeds18b20= time.ticks_ms()
timeled= time.ticks_ms()

onboardled= machine.Pin(25, machine.Pin.OUT)

while True:
    #currenttime= time.ticks_ms() #Every time it passes here, gets the current time
    
    if time.ticks_diff(time.ticks_ms(), timeds18b20) > 200: # this IF will be true every 200 ms
            timeds18b20= time.ticks_ms() #update with the "current" time
            
            ds_sensor.convert_temp() #only 200ms conversion time is necessary when sensor is read in 10 bit
    
    if time.ticks_diff(time.ticks_ms(), initialtime) > 1000: # this IF will be true every 3000 ms
            initialtime= time.ticks_ms() #update with the "current" time
            
            for rom in roms:
                #print(rom) # "raw"
                ds_sensor.write_scratch(rom, b'\x00\x00\x3f') # set sensor resolution to 10 bit
                tempC = ds_sensor.read_temp(rom)
                #tempF = tempC * (9/5) +32
                print('temperature (ºC):', "{:.2f}".format(tempC))
                #print('temperature (ºF):', "{:.2f}".format(tempF))
                #print()
     
    # statement below just blinks an LED
    if time.ticks_diff(time.ticks_ms(), timeled) > 200: # this IF will be true every 200 ms
        timeled= time.ticks_ms() #update with the "current" time
        
        if onboardled.value() == 0:
            onboardled.value(1)
        else:
            onboardled.value(0)
  
