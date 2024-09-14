# this program generates a color scheme based on the base color the user inputs
# the user can choose the color scheme or
# have the program recommend a color scheme based on the type of style the user is aiming for
# a color scheme is generated using the traditional color wheel; however, 3 additional colors are included (pink, brown,
# and gray) due to their popularity
import sys

# the color wheel starts at yellow and ends at yellow-green; however, due to the use of indexing, the color wheel has
# duplicated in the list below
basic_color_wheel = ["yellow", "yellow-orange", "orange", "red-orange", "red", "purple-red", "purple", "purple-blue",
                     "blue", "blue-green", "green", "yellow-green", "yellow", "yellow-orange", "orange", "red-orange",
                     "red", "purple-red", "purple", "purple-blue", "blue", "blue-green", "green", "yellow-green"]

global user_base_color
global user_style
global generated_colors
global method

# set empty string for get_user_color_scheme function for when user decides to choose their own color scheme
empty_string = ""

# initialize method-restart for restarting program
method_restart = ""


def continue_or_quit_program():
    try_again = ""
    while try_again not in ["Y", "N"]:
        try_again = (input('Enter "Y" for yes or "N" for no: ')).strip(" ").replace('"', "").upper()
        if try_again == "N":
            sys.exit('This program has ended since "N" was chosen.')
        elif try_again == "Y":
            return try_again
        else:
            print("\nInvalid input.")


# provide list of color options to the user and ask user to input their desired base color
# and remove any whitespaces or parenthesis from user input and set user input to lowercase
# check that base color is a valid base color. if not ask the user if they would like to enter
# another base color or quit. if the base color is valid, set user color input to valid base color format to be used
# in program
def get_base_color():
    global user_base_color
    try_again = "Y"
    while try_again == "Y":
        user_base_color = (input("\nBase Color Options:\n"
                                 "1) Yellow\n"
                                 "2) Yellow-Orange\n"
                                 "3) Orange\n"
                                 "4) Red-Orange\n"
                                 "5) Red\n"
                                 "6) Purple-Red\n"
                                 "7) Purple\n"
                                 "8) Purple-Blue\n"
                                 "9) Blue\n"
                                 "10) Blue-Green\n"
                                 "11) Green\n"
                                 "12) Yellow-Green\n"
                                 "13) Brown\n"
                                 "14) Pink\n"
                                 "15) Gray\n\n"
                                 "Enter a base color: ")).strip(" ").replace(")", "").lower()
        if user_base_color in ["1", "1 yellow", "yellow"]:
            user_base_color = "yellow"
            try_again = "N"
        elif user_base_color in ["2", "2 yellow-orange", "yellow-orange", "yellow orange", "orange yellow",
                                 "orange-yellow"]:
            user_base_color = "yellow-orange"
            try_again = "N"
        elif user_base_color in ["3", "3 orange", "orange"]:
            user_base_color = "orange"
            try_again = "N"
        elif user_base_color in ["4", "4 red-orange", "red-orange", "red orange", "orange red", "orange-red"]:
            user_base_color = "red-orange"
            try_again = "N"
        elif user_base_color in ["5", "5 red", "red"]:
            user_base_color = "red"
            try_again = "N"
        elif user_base_color in ["6", "6 purple-red", "purple-red", "purple red", "red purple", "red-purple"]:
            user_base_color = "purple-red"
            try_again = "N"
        elif user_base_color in ["7", "7 purple", "purple"]:
            user_base_color = "purple"
            try_again = "N"
        elif user_base_color in ["8", "8 purple-blue", "purple-blue", "purple blue", "blue purple", "blue-purple"]:
            user_base_color = "purple-blue"
            try_again = "N"
        elif user_base_color in ["9", "9 blue", "blue"]:
            user_base_color = "blue"
            try_again = "N"
        elif user_base_color in ["10", "10 blue-green", "blue-green", "blue green", "green blue", "green-blue"]:
            user_base_color = "blue-green"
            try_again = "N"
        elif user_base_color in ["11", "11 green", "green"]:
            user_base_color = "green"
            try_again = "N"
        elif user_base_color in ["12", "12 yellow-green", "yellow-green", "yellow green", "green yellow",
                                 "green-yellow"]:
            user_base_color = "yellow-green"
            try_again = "N"
        elif user_base_color in ["13", "13 brown", "brown"]:
            user_base_color = "brown"
            try_again = "N"
        elif user_base_color in ["14", "14 pink", "pink"]:
            user_base_color = "pink"
            try_again = "N"
        elif user_base_color in ["15", "15 gray", "gray"]:
            user_base_color = "gray"
            try_again = "N"
        else:
            print("\nInvalid color. Would you like to enter another color?")
            try_again = continue_or_quit_program()
    return user_base_color


def process_user_method():
    global color_scheme
    global choose_method
    global method
    # get color scheme from the user if the user chooses to pick their own scheme
    if method == "1" or method_restart == "2":
        color_scheme = get_user_color_scheme(empty_string)
        print(f"\nYour color scheme is {color_scheme}.")
        choose_method = generate_color_scheme()
    # get style from user and match style to a color scheme if the user wants a color scheme recommendation
    elif method == "2" or method_restart == "3":
        style = get_user_style()
        color_scheme = get_user_color_scheme(style)
        print(f"\nYour recommended color scheme is {color_scheme}.")
        choose_method = generate_color_scheme()
    elif method_restart == "1":
        choose_method = generate_color_scheme()
    else:
        print("\nInvalid method chosen. Would you like to try again?")
        choose_method = continue_or_quit_program()
    return choose_method


# provide a list of color schemes that the user can choose from if the user chooses to pick their own color scheme and
# return chosen color scheme
# check if the color scheme chosen by the user is valid. if it is not, ask the user if they would like to enter
# another color scheme or quit
def get_user_color_scheme(x):
    global color_scheme
    style = x
    try_again = "Y"
    while try_again == "Y":
        user_color_scheme = ""
        if method == "1" or method_restart == "2":
            user_color_scheme = (input("\nColor Scheme Options:\n"
                                       "1) Analogous\n"
                                       "2) Complementary\n"
                                       "3) Triadic\n"
                                       "4) Split Complementary\n"
                                       "5) Tetradic or Rectangular\n"
                                       "6) Monochromatic\n"
                                       "7) Square\n\n"
                                       "Enter a color scheme: ")).strip(" ").replace(")", "").lower()
        if user_color_scheme in ["1", "1 analogous", "analogous"] or style == "1":
            color_scheme = "analogous"
            try_again = "N"
        elif user_color_scheme in ["2", "2 complementary", "complementary"] or style == "2":
            color_scheme = "complementary"
            try_again = "N"
        elif user_color_scheme in ["3", "3 triadic", "triadic"] or style == "3":
            color_scheme = "triadic"
            try_again = "N"
        elif (user_color_scheme in ["4", "4 split complementary", "split complementary", "split-complementary"]
              or style == "4"):
            color_scheme = "split complementary"
            try_again = "N"
        elif user_color_scheme in ["5", "5 tetradic or rectangular", "tetradic or rectangular", "tetradic",
                                   "rectangular"] or style == "5":
            color_scheme = "tetradic or rectangular"
            try_again = "N"
        elif user_color_scheme in ["6", "6 monochromatic", "monochromatic"] or style == "6":
            color_scheme = "monochromatic"
            try_again = "N"
        elif user_color_scheme in ["7", "7 square", "square"] or style == "7":
            color_scheme = "square"
            try_again = "N"
        else:
            print("\nInvalid color scheme. Would you like to enter another color scheme?")
            try_again = continue_or_quit_program()
    return color_scheme


# provide a list of styles that they user can choose from if the user chooses to receive a color scheme recommendation
def get_user_style():
    global user_style
    try_again = "Y"
    while try_again == "Y":
        # list style in same numbered order as color scheme options from get color scheme function so that the set user
        # color scheme input function can be reused to get a color scheme
        user_style = (input("\nWhat style are you looking for?\n"
                            "Style Options:\n"
                            "1) Soft, cohesive, natural, and harmonious\n"
                            "2) Energizing and vivid\n"
                            "3) Playful, vibrant, and eye pleasing\n"
                            "4) Bold, contrasting, and busy\n"
                            "5) Unique, loud, and fun\n"
                            "6) Simple, eye-catching, sophisticated, and cohesive\n"
                            "7) Visually interesting and unique\n\n"
                            "Enter the number of your chosen style option: ")).strip(" ").replace(")", "")
        # check if the style chosen by the user is valid. if it is not, ask the user if they would like to choose
        # another style or quit
        if user_style in ["1", "2", "3", "4", "5", "6", "7"]:
            try_again = "N"
        else:
            print("\nInvalid style input. Would you like to enter another style?")
            try_again = continue_or_quit_program()
    return user_style


# take user's base color and generate color scheme based on base color's position in the basic color wheel list
def analogous(color_one):
    if color_one == "brown":
        print("\nYour first color combination option is: brown and orange\n"
              "Your second color combination option is: brown and green")
    elif color_one == "pink":
        print("\nYour color combination option is: pink, purple, red")
    elif color_one == "gray":
        print("\nYour first color combination option is: gray and black"
              "\nYour second color combination option is: gray and white")
    else:
        base_color_index = basic_color_wheel.index(color_one)
        color_two = basic_color_wheel[base_color_index - 2]
        color_three = basic_color_wheel[base_color_index - 1]
        color_four = basic_color_wheel[base_color_index + 1]
        color_five = basic_color_wheel[base_color_index + 2]
        combo1 = [color_two, color_three, color_one]
        combo2 = [color_three, color_one, color_four]
        combo3 = [color_one, color_four, color_five]
        separator = ", "
        print(f"\nYour first color combination option is: {separator.join(combo1)}",
              f"\nYour second color combination option is: {separator.join(combo2)}",
              f"\nYour third color combination option is: {separator.join(combo3)}")


# take user's base color and generate color scheme based on base color's position in the basic color wheel list
def complementary(color_one):
    if color_one == "brown":
        print("\nYour color combination is: brown and blue-purple")
    elif color_one == "pink":
        print("\nYour color combination is: pink and green")
    elif color_one == "gray":
        print("\nNo option available.")
    else:
        base_color_index = basic_color_wheel.index(color_one)
        color_two = basic_color_wheel[base_color_index + 6]
        print(f"\nYour color combination option is: {color_one} and {color_two}")


# take user's base color and generate color scheme based on base color's position in the basic color wheel list
def triadic(color_one):
    if color_one == "brown":
        print("\nYour color combination is: brown, green, blue-purple")
    elif color_one == "pink":
        print("\nYour color combination is: pink, blue, green")
    elif color_one == "gray":
        print("\nNo option available.")
    else:
        base_color_index = basic_color_wheel.index(color_one)
        color_two = basic_color_wheel[base_color_index + 4]
        color_three = basic_color_wheel[base_color_index - 4]
        print(f"\nYour color combination option is: {color_one}, {color_two}, and {color_three}")


# take user's base color and generate color scheme based on base color's position in the basic color wheel list
def split_complementary(color_one):
    if color_one == "brown":
        print("\nYour color combination is: brown, blue, blue-green")
    elif color_one == "pink":
        print("\nYour color combination is: pink, light-blue, light-green")
    elif color_one == "gray":
        print("\nNo option available.")
    else:
        base_color_index = basic_color_wheel.index(color_one)
        color_two = basic_color_wheel[base_color_index + 5]
        color_three = basic_color_wheel[base_color_index + 7]
        print(f"\nYour color combination option is: {color_one}, {color_two}, and {color_three}")


# take user's base color and generate color scheme based on base color's position in the basic color wheel list
def tetradic(color_one):
    if color_one == "brown":
        print("\nYour color combination option is: brown, blue-green, blue, red-orange")
    elif color_one == "pink":
        print("\nYour color combination option is: pink, green, blue, orange")
    elif color_one == "gray":
        print("\nNo option available.")
    else:
        base_color_index = basic_color_wheel.index(color_one)
        color_two = basic_color_wheel[base_color_index + 2]
        color_three = basic_color_wheel[base_color_index + 6]
        color_four = basic_color_wheel[base_color_index + 8]
        color_five = basic_color_wheel[base_color_index - 2]
        color_six = basic_color_wheel[base_color_index - 6]
        color_seven = basic_color_wheel[base_color_index - 8]
        combo1 = [color_one, color_two, color_three, color_four]
        combo2 = [color_one, color_five, color_six, color_seven]
        separator = ", "
        print(f"\nYour first color combination option is: {separator.join(combo1)}",
              f"\nYour second color combination option is: {separator.join(combo2)}")


# take user's base color and generate color scheme using a separate monochromatic color scheme list
def monochromatic(color_one):
    print(f"\nYou can pair {color_one} with any two colors listed below:")
    print(f"1) a darker variation of {color_one}\n2) another darker variation of {color_one}\n"
          f"3) a lighter variation of {color_one}\n4) another lighter variation of {color_one}\n"
          f"5) black\n6) white")
    if color_one != "gray":
        print(f"7) a variation of {color_one}-gray\n8) another variation of {color_one}-gray")


# take user's base color and generate color scheme based on base color's position in the basic color wheel list
def square(color_one):
    if color_one == "brown":
        print("\nYour color combination option is: brown, blue, green, purple")
    elif color_one == "pink":
        print("\nYour color combination option is: pink, blue-green, yellow-green, blue-purple")
    elif color_one == "gray":
        print("\nNo option available.")
    else:
        base_color_index = basic_color_wheel.index(color_one)
        color_two = basic_color_wheel[base_color_index + 3]
        color_three = basic_color_wheel[base_color_index + 6]
        color_four = basic_color_wheel[base_color_index + 9]
        print(f"\nYour color combination option is: {color_one}, {color_two}, {color_three}, and {color_four}")


# generate chosen color scheme (either chosen by user or by recommendation) using user's base color
def generate_color_scheme():
    if color_scheme == "analogous":
        analogous(base_color)
    elif color_scheme == "complementary":
        complementary(base_color)
    elif color_scheme == "triadic":
        triadic(base_color)
    elif color_scheme == "split complementary":
        split_complementary(base_color)
    elif color_scheme == "tetradic or rectangular":
        tetradic(base_color)
    elif color_scheme == "monochromatic":
        monochromatic(base_color)
    else:
        square(base_color)
    continue_generator = "N"
    return continue_generator


print("Welcome! This is a Color Scheme Generator.\n")

print("Please note that colors produced from this generator, with the exception of colors provided for the "
      "monochromatic color scheme, are based on the traditional color wheel.\n")

print("Also, please note that only two color schemes (analogous and monochromatic) can be offered for the "
      "color gray.\n")

print("Now, please choose a base color.")

# set base color from user input to variable useColorInput for user input checking
base_color = get_base_color()
print(f"\nYour base color is {user_base_color}.")

# check for valid choice provided by the user (should either be 1 for choosing their own color scheme or 2 for choosing
# to receive a recommendation)
choose_method = "Y"
while choose_method == "Y":
    # ask the user if they would like to choose their own color scheme or if they would like a recommendation instead
    print("\nWould you like to choose your own color scheme or would you like a recommendation?")
    method = (input('\nEnter the number "1" to choose your own color scheme, or enter the number "2" to receive '
                    'a recommendation: ')).strip(" ").replace('"', "")
    process_user_method()

# ask the user if they would like to start over, choose a different color scheme, receive a recommendation and choose
# a different style, or quit
start_over = "Y"
while start_over == "Y":
    # null out method after restarting the program so that correct if-statement is chosen after program restart
    method = ""
    print("\nWould you like to choose different base color, choose a different color scheme, choose a different style,"
          " or quit?")
    choice = (input('\nEnter the number "1" to choose a different base color;\nEnter the number "2" to choose a '
                    'different color scheme;\nEnter the number "3" to receive and recommendation and choose a '
                    'different style; or\nEnter the number "4" to quit: ')).strip(" ").replace('"', "")
    # get color scheme from the user if the user chooses to pick their own scheme
    if choice == "1":
        base_color = get_base_color()
        print(f"\nYour base color is {user_base_color}.")
        # ask the user if they would like to choose their own color scheme or if they would like a
        # recommendation instead
        print("\nWould you like to keep the same color scheme, choose a new color scheme, or receive a recommendation?")
        method_restart = (input('\nEnter the number "1" to keep the same color scheme;\nEnter the number "2" to choose '
                                'a new color scheme; or\nEnter enter the number "3" to receive '
                                'a recommendation: ')).strip(" ").replace('"', "")
        process_user_method()
        start_over = "Y"
    # get color scheme from the user if the user chooses to pick their own scheme
    elif choice == "2":
        # set method_restart to 2 to get a new color scheme since method variable is now null
        method_restart = "2"
        color_scheme = get_user_color_scheme(empty_string)
        print(f"\nYour color scheme is {color_scheme}.")
        generate_color_scheme()
        start_over = "Y"
    # get style from user and match style to a color scheme if the user wants a color scheme recommendation
    elif choice == "3":
        # set method_restart to null if it was set in a previous choice
        # (needed so color scheme function will work properly)
        method_restart = ""
        user_style = get_user_style()
        color_scheme = get_user_color_scheme(user_style)
        print(f"\nYour recommended color scheme is {color_scheme}.")
        generate_color_scheme()
        start_over = "Y"
    elif choice == "4":
        sys.exit('This program has ended since choice "4" was chosen.')
    else:
        print("\nInvalid option chosen. Would you like to try again?")
        start_over = continue_or_quit_program()
