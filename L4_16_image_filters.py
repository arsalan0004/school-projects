# Group number: L4 - 16 
# Current milestone: 3 
# Date of submission: Dec 1, 2019


from Cimpl import choose_file, load_image, copy, create_color, set_color,\
                  show, Image, get_color, get_height, get_width, show, save_as



def flip_vertical(original_image: Image) -> Image :
    """William Pontefract 101153592
    
    Takes in an image (image), creates a copy and then returns 
    the copy flipped on the vertical axis.
    
    >>>flip_vertical(image)
    flipped_image
    """
    flipped_image = copy(original_image) 
    
    #This section of the code gets the color of a given pixel and then assigns
        #that color to the pixel exactly opposite by subtracting from width.
    for pixel in original_image : 
        x, y, (r, g, b) = pixel
        
        new_color = create_color(r, g, b)
        set_color(flipped_image, (get_width(original_image)) - 1 - x, y, 
                  new_color)
    
    return flipped_image 


def flip_horizontal(image: Image) -> Image: #Flips an image upside down
    """Return a horizontally flipped copy of the original image along 
    the horizontal axis at the midpoint of the image.
    
    Author: Dulsan Nelumdeniyage
    
    >>> image = load_image(choose_file())
    >>> flip_horizontal(image)
    """    

    horizontally_flipped_image = copy(image)
    for x, y, (r, g, b) in image:
        color1 = create_color(r, g, b)
        set_color(horizontally_flipped_image, x, (get_height(image) - 1 - y),\
                  color1)
    
    return horizontally_flipped_image    



def grayscale(image: Image) -> Image: # Turns the color of each pixel to gray
                                      # Making a grey image of the original
    """
    author: Prof. of ECOR 1051, Donald Bailey
    Return a grayscale copy of image.
    
    >>> image = load_image(choose_file())
    >>> gray_image = grayscale(image)
    >>> show(gray_image)
    """
    new_image = copy(image)
    for x, y, (r, g, b) in image:

        # Use the pixel's brightness as the value of RGB components for the 
        # Shade of gray. These means that the pixel's original colour and the
        # Corresponding gray shade will have approximately the same brightness.
        
        brightness = (r + g + b) // 3
        
        # Or, brightness = (r + g + b) / 3
        # Create_color will convert an argument of type float to an int
        
        gray = create_color(brightness, brightness, brightness)
        set_color(new_image, x, y, gray)      
    return new_image


def sepia(image: Image) -> Image: 
    """ :return a sepia copy of the image
    
    Author: Dulsan Nelumdeniyage
    
    >>> image = load_image(choose_file())
    >>> sepia_image = sepia(image)
    >>> show(sepia_image)
    """
    original_image = copy(image)
    
    sepia_image = grayscale(original_image)
    
    for x, y, (r, g, b) in sepia_image:
        if g < 63:
            color1 = create_color(r * 1.1, g, b * 0.9)
            set_color(sepia_image, x, y, color1)
        elif 63 <= g <= 191:
            color2 = create_color(r * 1.15, g, b * 0.85)
            set_color(sepia_image, x, y, color2)
        else:
            color3 = create_color(r * 1.08, g, b * 0.93)
            set_color(sepia_image, x, y, color3)
    return(sepia_image)


def extreme_contrast(original_image: Image) -> Image:
    """
    William Pontefract 101153592
    
    Takes in  an image(original_image), returns a copy of the image where any 
    r,g,b, value in each individual pixel is 255 if it was > 127 or 0 if it 
    was <= 127.
    
    >>>extreme_contrast('p2-original.jpg')
    extreme_image
    >>>extreme_contrast('p3-original.jpg')
    extreme_image
    >>>extreme_contrast('p4-original.jpg')
    extreme_image
    """
    
    extreme_image = copy(original_image) #Creates an unlinked copy
    
    for pixel in original_image: 
        #Main body of the code, checks the r, g, and b components 
            #of each pixel and if they are below or equal to 127 it reduces it 
            #to 0, if it is greater than 127 it changes it to 255.
        x, y, (r, g, b)=pixel
        
        if r > 127:
            r = 255
        else:
            r = 0
        if g > 127:
            g = 255
        else:
            g = 0   
        if b > 127:
            b = 255
        else:
            b = 0             
        
        #This section of code creates the new color data for the pixel and sets 
            #the new value.
        newc=create_color(r,g,b) 
        set_color(extreme_image,x,y,newc) 
    
    return extreme_image 

    
def _adjust_component(color_value: int)->int :
    """William Pontefract 101153592
    Takes in the value of r/g/b from a pixel and puts into one of 4 values based
    on which of the 4 divisions it was in originally.
    
    Condition:Only for internal use by posterize
    """
    
    #This code uses greater than less than to bring the color_value into
        #one of four ranges then returns the midpoint of that range as new color
        #value.
    if color_value > 191 : 
        return 223
    elif color_value > 127 :
        return 159
    elif color_value > 63 :
        return 95
    else :
        return 31


def posterize(original_image: Image)->Image:
    """William Pontefract 101153592
    
    Takes in an imagereturns a copy of the image where each color channel per 
    pixel is divided so there are only four values per color channel.
    
    >>>posterize(Image)
    posterimage
    """
    posterized_image = copy(original_image)#Creates an unlinked copy of the 
                                               #original image.
    
    #For every pixel uses adjust component to create new color data for the 
        #pixel, then sets that new color.
    for pixel in posterized_image : 
        x, y, (r, g, b) = pixel
        
        new_color = create_color(_adjust_component(r), _adjust_component(g),
                                 _adjust_component(b))
        set_color(posterized_image, x, y, new_color) 
    
    return posterized_image


def detect_edges(image: Image, threshold: int) -> Image:
    """
    Made my Arsalan Syed, student#: 101169528
    
    Colors the edges of a photo black. Everything else is colored white.  
    
    ex. 
    >>>detect_edges(image, 0.3)
    image
    >>>detect_edges(image, 0.5)
    image
    >>>detect_edges(image, 0.1)
    image

    """
    original_image = image

    image_height = get_height(original_image)
    image_width = get_width(original_image) 
    
    
    
    for i in range(image_height): 
        for j in range(image_width):
            
            if ( i != image_height - 1):
                
                pixel_on_target = get_color(original_image, j, i)  
                average_brightness_target = (pixel_on_target[0] +
                                             pixel_on_target[1] +
                                             pixel_on_target[2])/3
                
                pixel_one_below = get_color(original_image, j, i + 1)
                average_brightness_one_below = (pixel_one_below[0] +
                                                pixel_one_below[1] + 
                                                pixel_one_below[2])/3
                
                if(abs(average_brightness_target -
                       average_brightness_one_below) >= threshold):
                    black = create_color(0, 0, 0)
                    set_color(original_image, j, i, black)
                else:
                    white = create_color(255, 255, 255)
                    set_color(original_image, j, i, white)                    
    
    return(original_image)


def detect_edges_better(original_image: Image, threshold: int) -> Image: 
    """
    Made my Arsalan Syed, student#: 101169528
    
    Colors the edges of a photo black. Everything else is colored white.  
    
    >>>detect_edges_better(image, 0.5)
    image
    >>>detect_edges_better(image,0.1)
    image 
    >>>detect_edges_better(image,0.05)
    image

    """

    image_height = get_height(original_image)
    image_width = get_width(original_image) 
    
    
    
    for i in range(image_height): 
        for j in range(image_width):
            
            if ( i != image_height - 1):
                if ( j != image_width - 1):
                
                    pixel_on_target = get_color(original_image, j, i)  
                    average_brightness_target = (pixel_on_target[0] +
                                                 pixel_on_target[1] +
                                                 pixel_on_target[2])/3
                    
                    pixel_one_below = get_color(original_image, j, i + 1)
                    average_brightness_one_below = (pixel_one_below[0] +
                                                    pixel_one_below[1] +
                                                    pixel_one_below[2])/3
                    
                    pixel_on_right = get_color(original_image, j + 1, i)
                    average_brightness_on_right = (pixel_on_right[0] +
                                                   pixel_on_right[1] +
                                                   pixel_on_right[2])/3
                    
                    if((abs(average_brightness_target -
                            average_brightness_one_below) >=  threshold) or 
                       (abs(average_brightness_target -
                            average_brightness_on_right) >= threshold) ):
                        black = create_color(0, 0, 0)
                        set_color(original_image, j, i, black)
                    else:
                        white = create_color(255, 255, 255)
                        set_color(original_image, j, i, white)                    
     
    return(original_image)


def two_tone(image: Image, firstColor: str, secColor: str) -> Image:
    
    """
    written by Arsalan Syed, student# 101169528
    returns a picture in two color tones, depending on what colors are selected
    
    ex.
    >>>two_tone(exampleimage.jpg, "black", "white")
    image
    two_tone(exampleimage.jpg, "black", "red")
    image
    two_tone(exampleimage.jpg, "black", "lime")
    image
    
    """
    
    if(secColor == "white"):
        selection2 = create_color(0,0,0)
    elif(secColor == "black"):
        selection2 = create_color(255,255,255)
    elif(secColor == "red"):
        selection2 = create_color(255,0,0)
    elif(secColor == "lime"):
        selection2 = create_color(0,255,0)
    elif(secColor == "blue"):
        selection2 = create_color(0,0,255)
    elif(secColor == "yellow"):
        selection2 = create_color(255,255,0)
    elif(secColor == "cyan"):
        selection2 = create_color(0,255,255)
    elif(secColor == "magenta"):
        selection2 = create_color(255,0,255)  
    elif(secColor == "grey"):
        selection2 = create_color(128,128,128)       
    
    if(firstColor == "white"):
        selection1 = create_color(0,0,0)
    elif(firstColor == "black"):
        selection1 = create_color(255,255,255)
    elif(firstColor == "red"):
        selection1 = create_color(255,0,0)
    elif(firstColor == "lime"):
        selection1 = create_color(0,255,0)
    elif(firstColor == "blue"):
        selection1 = create_color(0,0,255)
    elif(firstColor == "yellow"):
        selection1 = create_color(255,255,0)
    elif(firstColor == "cyan"):
        selection1 = create_color(0,255,255)
    elif(firstColor == "magenta"):
        selection1 = create_color(255,0,255)  
    elif(firstColor == "grey"):
        selection1 = create_color(128,128,128)    
    
    
    for x, y, (r, g, b) in image:
        if((r <= 170) or (g <= 170 ) or ( b <= 170)):     
            set_color(image, x, y, selection1)
        else:
            set_color(image, x, y, selection2)
  
    return(image)


def three_tone(image: Image,
               firstColor: str,
               secColor: str,
               thirdColor: str) -> Image:
    
    """
    written by Arsalan Syed, student# 101169528
    returns a picture in three colors, depending on what colors the user selects
    
    ex.
    >>>two_tone(exampleimage.jpg, "black", "white", "blue")
    image
    two_tone(exampleimage.jpg, "black", "red", "lime")
    image
    two_tone(exampleimage.jpg, "black", "lime", "white")
    image
    
    """
    
    if(thirdColor == "white"):
        selection3 = create_color(0,0,0)
    elif(thirdColor == "black"):
        selection3 = create_color(255,255,255)
    elif(thirdColor == "red"):
        selection3 = create_color(255,0,0)
    elif(thirdColor == "lime"):
        selection3 = create_color(0,255,0)
    elif(thirdColor == "blue"):
        selection3 = create_color(0,0,255)
    elif(thirdColor == "yellow"):
        selection3 = create_color(255,255,0)
    elif(thirdColor == "cyan"):
        selection3 = create_color(0,255,255)
    elif(thirdColor == "magenta"):
        selection3 = create_color(255,0,255)  
    elif(thirdColor == "grey"):
        selection3 = create_color(128,128,128)       
    
    if(secColor == "white"):
        selection2 = create_color(0,0,0)
    elif(secColor == "black"):
        selection2 = create_color(255,255,255)
    elif(secColor == "red"):
        selection2 = create_color(255,0,0)
    elif(secColor == "lime"):
        selection2 = create_color(0,255,0)
    elif(secColor == "blue"):
        selection2 = create_color(0,0,255)
    elif(secColor == "yellow"):
        selection2 = create_color(255,255,0)
    elif(secColor == "cyan"):
        selection2 = create_color(0,255,255)
    elif(secColor == "magenta"):
        selection2 = create_color(255,0,255)  
    elif(secColor == "grey"):
        selection2 = create_color(128,128,128)       
    
    if(firstColor == "white"):
        selection1 = create_color(0,0,0)
    elif(firstColor == "black"):
        selection1 = create_color(255,255,255)
    elif(firstColor == "red"):
        selection1 = create_color(255,0,0)
    elif(firstColor == "lime"):
        selection1 = create_color(0,255,0)
    elif(firstColor == "blue"):
        selection1 = create_color(0,0,255)
    elif(firstColor == "yellow"):
        selection1 = create_color(255,255,0)
    elif(firstColor == "cyan"):
        selection1 = create_color(0,255,255)
    elif(firstColor == "magenta"):
        selection1 = create_color(255,0,255)  
    elif(firstColor == "grey"):
        selection1 = create_color(128,128,128)      
    
    
    
    for x, y, (r, g, b) in image:
        if((r <= 84) or (g <= 84) or ( b <= 84)):     
            set_color(image, x, y, selection1)
        elif((84 < r <= 170) or (84 < g <= 170) or ( 84 < b <= 170)):
            set_color(image, x, y, selection2)
        elif((r > 170) or (g > 170) or ( b > 170)): 
            set_color(image, x, y, selection3)
              
    return(image)

