# Runs on the https://missions.astro-pi.org/mz/code_submissions/new
# Also runs on https://www.esa.int/Education/AstroPI/Astro_PI_Sense_HAT_emulator

# Import the libraries
from sense_hat import SenseHat
from time import sleep

from itertools import cycle, islice

# Add colour variables and image

# Color's are stored as RGB tuples
c = (0,0,0)
k = (0,0,0)
b = (0,98,225)
g = (0,225,0)
w = (225,225,225)


# An 16x8 multidimensional list
# pixel art map of 'earth'

#When working outside of Colab make sure to use real rgb values
earth_pixels = [
 [w, b, w, b, w, b, w, g, w, b, g, w, g, w, b, w],
 [b, b, g, b, b, g, b, b, g, b, b, g, g, b, b, g],
 [b, b, g, g, g, g, b, g, g, g, g, g, g, b, b, b],
 [b, b, b, g, g, b, b, b, b, g, g, g, g, b, b, b],
 [b, b, b, g, b, g, b, g, g, g, b, g, g, b, b, b],
 [g, b, b, b, g, b, b, g, g, b, b, g, b, b, g, g],
 [g, b, b, b, g, b, b, g, g, b, b, b, b, b, g, g],
 [b, w, b, w, b, w, b, w, g, w, b, w, b, w, g, w],
]

# A 8x8 multidimensional list pixel art map of circle
mask_pixels = [
 [k, k, w, w, w, w, k, k],
 [k, w, w, w, w, w, w, k],
 [w, w, w, w, w, w, w, w],
 [w, w, w, w, w, w, w, w],
 [w, w, w, w, w, w, w, w],
 [w, w, w, w, w, w, w, w],
 [k, w, w, w, w, w, w, k],
 [k, k, w, w, w, w, k, k],
]



# Set up the Sense HAT
sense = SenseHat()
sense.set_rotation(270, False)

# Set up the colour sensor
sense.color.gain = 60 # Set the sensitivity of the sensor
sense.color.integration_cycles = 64 # The interval at which the reading will be taken

for i in range(28*15):
    sc = sense.color
    c = (sc.red,sc.green,sc.blue)
    # Display the image
    # The image is stored as a list
    frog = [c,c,c,c,c,c,c,c,
             c,c,g,c,c,g,c,c,
             c,g,k,g,g,k,g,c,
             c,g,g,g,g,g,g,c,
             c,g,k,k,k,k,g,c, 
             c,g,g,g,g,g,g,c,
             c,g,g,g,g,g,g,c,
             c,c,g,c,c,g,c,c,]
    
    world = [k,k,k,k,k,k,k,k,
             k,k,b,w,w,b,k,k,
             k,c,b,b,b,b,b,k,
             k,c,c,c,b,c,c,k,
             k,b,c,b,b,b,c,k, 
             k,b,b,b,b,b,b,k,
             k,k,b,w,w,b,k,k,
             k,k,k,k,k,k,k,k,]
    
    # Display the image
    sense.set_pixels(world)
    sleep(1/15)
sense.clear()