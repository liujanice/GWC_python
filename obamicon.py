from PIL import Image

# RGB values for recoloring.
"""
#Obamicon
darkBlue = (0, 51, 76)
red = (217, 26, 33)
lightBlue = (112, 150, 158)
yellow = (252, 227, 166)
"""
# Obamicon = [(0, 51, 76),(217, 26, 33), (112, 150, 158), (252, 227, 166)]
"""
NOT NECESSARY ANYMORE
#magenta_colors
darkmagenta =(139, 0, 139)
mediummagenta= (128, 0, 128)
magenta = (255, 0, 255)
lightmagenta = (255, 20, 147)

#pastel_colors
babyblue = (224, 255, 255)
mintyblue = (240, 255, 240)
mediumblue = (240, 248, 255)
iceblue = (245, 255, 250)
"""

def retry():
    print("Find an image you would like to put a filter on. Save it onto your computer and put it in the Documents Folder. Make sure the file is in .JPG form")
    user_image = raw_input("What image would you like to put the filter on? Enter in the image file name (example: flower.jpg) ")
    # to test
    # image_jpg = user_image + '.jpg'


    # Import image.
    my_image = Image.open(user_image)
    #my_image = Image.open(image_jpg)
    #change IMAGENAME to the path on your computer to the image you're using

    image_list = my_image.getdata() #each pixel is represented in the form (red value, green value, blue value, transparency). You don't need the fourth value.
    image_list = list(image_list) #Turns the sequence above into a list. The list can be iterated through in a loop.
    #image_list is the list of pixel colors for old image
    recolored = [] #an empty list that will hold the pixel data for the new image.

    print("What filter would you like to use?")
    choice_filter = raw_input("Enter in: 1 for Obamicon, 2 for magenta, 3 for pastel blues ")
    if choice_filter == "1":
        Obamicon = [(0, 51, 76),(217, 26, 33), (112, 150, 158), (252, 227, 166)]
        pixel_intensity = 0
        for pixel in image_list:
            R = pixel[0]
            G = pixel[1]
            B = pixel[2]
            pixel_intensity = R + G + B
            if pixel_intensity < 182:
                recolored.append(Obamicon[0])
            elif pixel_intensity >=182 and pixel_intensity <= 364:
                recolored.append(Obamicon[1])
            elif pixel_intensity >= 364 and pixel_intensity <= 546:
                recolored.append(Obamicon[2])
            elif pixel_intensity > 546:
                recolored.append(Obamicon[3])
    elif choice_filter == "2":
        magenta_colors = [(139, 0, 139), (128, 0 , 128),(255, 0, 255),(255, 20, 147)]
        pixel_intensity = 0
        for pixel in image_list:
            R = pixel[0]
            G = pixel[1]
            B = pixel[2]
            pixel_intensity = R + G + B
            if pixel_intensity < 182:
                recolored.append(magenta_colors[0])
            elif pixel_intensity >=182 and pixel_intensity <= 364:
                recolored.append(magenta_colors[1])
            elif pixel_intensity >= 364 and pixel_intensity <= 546:
                recolored.append(magenta_colors[2])
            elif pixel_intensity > 546:
                recolored.append(magenta_colors[3])
    elif choice_filter == "3":
        pastel_blues = [(224, 255, 255) , (240, 255, 240), (240, 248, 255), (245, 255, 250)]
        for pixel in image_list:
            R = pixel[0]
            G = pixel[1]
            B = pixel[2]
            pixel_intensity = R + G + B
            if pixel_intensity < 182:
                recolored.append(pastel_blues[0])
            elif pixel_intensity >=182 and pixel_intensity <= 364:
                recolored.append(pastel_blues[1])
            elif pixel_intensity >= 364 and pixel_intensity <= 546:
                recolored.append(pastel_blues[2])
            elif pixel_intensity > 546:
                recolored.append(pastel_blues[3])
    else:
        print("Oops! Try Again.")
        choice_filter = raw_input("Enter in: 1 for Obamicon, 2 for magenta, 3 for pastel blues ")

# Create a new image using the recolored list. Display and save the image.
    new_image = Image.new("RGB", my_image.size) #Creates a new image that will be the same size as the original image.
    new_image.putdata(recolored) #Adds the data from the recolored list to the image.
    new_image.show() #show the new image on the screen
    new_image.save("recolored.jpg", "jpeg") #save the new image as "recolored.jpg"
def retry_prompt():
    print("Would you like to play again?")
    user_retry = raw_input("Enter 'y' to continue or 'n' to end ")
    if user_retry == 'y':
        retry()
        retry_prompt()
    elif user_retry == 'n':
        i = 2
i = 0
while i < 1:
    retry()
    retry_prompt()
else:
    print("Thanks for playing!")



"""
# MY CODE to fulfill Minimum requirements for this to work
#User can input an image they want to recolor, or put a filter on
print("Find an image you would like to put a filter on. Save it onto your computer and put it in the Documents Folder. Make sure the file is in .JPG form")
user_image = raw_input("What image would you like to put the filter on? Enter in the image file name (example: imagename.jpg)  ")

# Import image.
my_image = Image.open(user_image) #change IMAGENAME to the path on your computer to the image you're using
image_list = my_image.getdata() #each pixel is represented in the form (red value, green value, blue value, transparency). You don't need the fourth value.
image_list = list(image_list) #Turns the sequence above into a list. The list can be iterated through in a loop.
#image_list is the list of pixel colors for old image
recolored = [] #an empty list that will hold the pixel data for the new image.

pixel_intensity = 0

#YOUR CODE to loop through the original list of pixels and build a new list based on intensity should go here.
for pixel in image_list:
    R = pixel[0]
    G = pixel[1]
    B = pixel[2]
    pixel_intensity = R + G + B
    if pixel_intensity < 182:
        recolored.append(darkBlue)
    elif pixel_intensity >=182 and pixel_intensity <= 364:
        recolored.append(red)
    elif pixel_intensity >= 364 and pixel_intensity <= 546:
        recolored.append(lightBlue)
    elif pixel_intensity > 546:
        recolored.append(yellow)

# Create a new image using the recolored list. Display and save the image.
new_image = Image.new("RGB", my_image.size) #Creates a new image that will be the same size as the original image.
new_image.putdata(recolored) #Adds the data from the recolored list to the image.
new_image.show() #show the new image on the screen
new_image.save("recolored.jpg", "jpeg") #save the new image as "recolored.jpg"
"""
