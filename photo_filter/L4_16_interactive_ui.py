# Group number: L4 - 16 
# Current milestone: 3 
# Date of submission: Dec 1, 2019

from Cimpl import load_image, show, save_as, choose_file, Image

from L4_16_image_filters import detect_edges, detect_edges_better, \
                                extreme_contrast, flip_horizontal, \
                                flip_vertical, grayscale, posterize,\
                                sepia, three_tone, two_tone, _adjust_component



filtered_image = None

valid_list=["2", "3", "T", "S", "L", "P", "X", "E", "I", "V", "H", "Q"]

command_list=[("T",sepia), ("P",posterize), 
              ("X",extreme_contrast), ("V",flip_vertical), 
              ("H",flip_horizontal)]

def sorter(user_input, valid_list, filtered_image) -> Image:
    """
    created by Arsalan Syed, student # 101169528
    
    checks if the user has inputted a valid input. If so, then the user_input
    is routed to the function_call function. If not, user is presented with
    an error message.
    
    ex. 
    
    >>>sorter("Q", [("T",sepia), ("P",posterize), 
              ("X",extreme_contrast), ("V",flip_vertical), 
              ("H",flip_horizontal)], image)
    image 
    >>>sorter("L", [("T",sepia), ("P",posterize), 
              ("X",extreme_contrast), ("V",flip_vertical), 
              ("H",flip_horizontal)], image)
    image 
    >>>sorter("L", [("T",sepia), ("P",posterize), 
              ("X",extreme_contrast), ("V",flip_vertical), 
              ("H",flip_horizontal)], image)
    image 
    >>>sorter("Ll", [("T",sepia), ("P",posterize), 
              ("X",extreme_contrast), ("V",flip_vertical), 
              ("H",flip_horizontal)], image)
    Error: no such command 
    image
    
    """
    

    if user_input not in valid_list :
        print("Error: No such command")
        return filtered_image
            
    else:
        return function_call(user_input, filtered_image)


def function_call(user_input, filtered_image) -> Image:
    """
    created by William Pontefract 101153592
    
    determines which filter function the user wants to apply to their picture
    and routes their picture to that function. If the image is not loaded, 
    then the user will be presented with an error message 
    
    ex. 
    >>>function_call("X", image)
    image 
    >>>function_call("X", None)
    error: No Image Loaded
    No image loaded
    None
    >>>function_call("2", image)
    image
     >>>function_call("2", None)
    error: No Image Loaded
    No image loaded
    None
    
    
    """
    
    if ((filtered_image == None) and user_input != "L"):
        print("error: No image loaded")
        return None
    
    #else:
    for elem in command_list :
            #loops through the valid commands. If elem is found in command_list
            #then the corresponding function in that list is applied to 
            #the the photo the user has loaded 
        if user_input == elem[0] :
                filtered_image = elem[1](filtered_image)
                
        if user_input == "E" :
            filtered_image = detect_edges(filtered_image, 
                float(input("Threshold: ")))
            
        elif user_input == "I" :
            filtered_image = detect_edges_better(filtered_image, 
                                                 float(input("Threshold: ")))
        elif user_input == "2" :
            filtered_image = two_tone(filtered_image, "yellow", "cyan")
                                                  
        elif user_input == "3" :
            filtered_image = three_tone(filtered_image, "yellow", "magenta", 
                                        "cyan")
                                                
        elif user_input == "L":
            filtered_image = load_image(choose_file())
            
        elif user_input == "S":
            save_as(filtered_image)
        
        return filtered_image
    
        
while quit!=True:
    
    """ Author: Dulsan Nelumdeniyage student ID: 101165023
    
    User inputs the letter for what he/she wants to do and the corresponding
    function is called and returns an image.
    
    >>>L)oad image S)ave-as
       2)-tone 3)-tone X)treme contrast T)int sepia P)osterize
       E)dge detect I)mproved egde detect V)ertical flip H)orizontal flip
       Q)uit
       
       : L
    image
    
    """
    
    valid=True
    
    print("L)oad image S)ave-as")
    print("2)-tone 3)-tone X)treme contrast T)int sepia P)osterize")
    print("E)dge detect I)mproved egde detect V)ertical flip H)orizontal flip")
    print("Q)uit")
    print(" ")
    
    user_input = str.upper(str(input(": ")))
    
    if(user_input == "Q"): #Ends the loop and outputs print statement
        print("good bye")
        quit = True
        filtered_image = None
    else:
        filtered_image = sorter(user_input, valid_list, filtered_image)
    if(filtered_image != None and (user_input in valid_list)):
        show(filtered_image)
    
  


