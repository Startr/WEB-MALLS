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
ww =(12,12,12)

# An 16x8 multidimensional list
# pixel art map of 'earth'

#When working outside of Colab make sure to use real rgb values
earth_pixels = [
 [b, b, b, b, b, b, b, c, b, b, c, b, c, b, b, b],
 [b, b, c, b, b, c, b, b, c, b, b, c, c, b, b, c],
 [b, b, c, c, c, c, b, c, c, c, c, c, c, b, b, b],
 [b, b, b, c, c, b, b, b, b, c, c, c, c, b, b, b],
 [b, b, b, c, b, c, b, c, c, c, b, c, c, b, b, b],
 [c, b, b, b, c, b, b, c, c, b, b, c, b, b, c, c],
 [c, b, b, b, c, b, b, c, c, b, b, b, b, b, c, c],
 [b, b, b, b, b, b, b, b, c, b, b, b, b, b, c, w],
]

# A 8x8 multidimensional list pixel art map of circle
mask_pixels = [
 [k, k, ww, w, w, ww, k, k],
 [k, ww, ww, ww, ww, ww, ww, k],
 [ww, ww, ww, ww, ww, ww, ww, ww],
 [ww, ww, ww, ww, ww, ww, ww, ww],
 [ww, ww, ww, ww, ww, ww, ww, ww],
 [ww, ww, ww, ww, ww, ww, ww, ww],
 [k, ww, ww, ww, ww, ww, ww, k],
 [k, k, ww, w, w, ww, k, k],
]



# Set up the Sense HAT
sense = SenseHat()
sense.set_rotation(270, False)

# Set up the colour sensor
sense.color.gain = 60 # Set the sensitivity of the sensor
sense.color.integration_cycles = 64 # The interval at which the reading will be taken


#Our old image a static images
for i in range(1*15):
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


#New animation of spining globe
for i in range(32):

    sc = sense.color
    c = (sc.red,sc.green,sc.blue)

    earth_pixels = [
         [b, b, b, b, b, b, b, c, b, b, c, b, c, b, b, b],
         [b, b, c, b, b, c, b, b, c, b, b, c, c, b, b, c],
         [b, b, c, c, c, c, b, c, c, c, c, c, c, b, b, b],
         [b, b, b, c, c, b, b, b, b, c, c, c, c, b, b, b],
         [b, b, b, c, b, c, b, c, c, c, b, c, c, b, b, b],
         [c, b, b, b, c, b, b, c, c, b, b, c, b, b, c, c],
         [c, b, b, b, c, b, b, c, c, b, b, b, b, b, c, c],
         [b, b, b, b, b, b, b, b, c, b, b, b, b, b, c, w],
        ]
    
    view = ([list(islice(cycle(row), i, i+8)) for row in earth_pixels])
    # test if there is a white pixel in world_pixels if so
    # keep the pixel from view otherwise replace view's pixel
    # with the black from world_pixels
    view = [
        [
            view_pixel if mask_pixel == ww else mask_pixel
            for view_pixel, mask_pixel in zip(view_row, mask_row)
        ]
        for view_row, mask_row in zip(view, mask_pixels)
    ]
    # Initialize an empty list to hold the concatenated items
    concatenated_view_items = []
    
    # Iterate over each row in the 'view' matrix (assuming 'view' is a list of lists)
    for row in view:
        # Iterate over each item in the current row
        for item in row:
            # Append the current item to the list of concatenated items
            concatenated_view_items.append(item)
    
    # Reverse the order of items in the concatenated list to get a reversed view
    concatenated_view_items
        
    sense.set_pixels(concatenated_view_items)
    sleep(0.4)

    

#sense.clear()