# Complete project details at https://RandomNerdTutorials.com/raspberry-pi-pico-ds18b20-micropython/

import machine, onewire, ds18x20, time

ds_pin = machine.Pin(15)
ds_sensor = ds18x20.DS18X20(onewire.OneWire(ds_pin))

roms = ds_sensor.scan()
print('Found DS devices: ', roms)
initialtime= time.ticks_ms() #https://docs.micropython.org/en/latest/library/time.html


while True:
    currenttime= time.ticks_ms() #Every time it passes here, gets the current time
    if time.ticks_diff(time.ticks_ms(), initialtime) > 2000: # this IF will be true every 3000 ms
            initialtime= time.ticks_ms() #update with the "current" time
            
            ds_sensor.convert_temp()
            time.sleep_ms(750)
            for rom in roms:
                #print(rom) # "raw"
                tempC = ds_sensor.read_temp(rom)
                #tempF = tempC * (9/5) +32
                print('temperature (ºC):', "{:.2f}".format(tempC))
                #print('temperature (ºF):', "{:.2f}".format(tempF))
                #print()
  
