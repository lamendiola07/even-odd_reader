# Mendiola, Logie A. | BSCPE 1-5 | Object-Oriented Programming | Assignment #4: P-1

# Write a Python program that reads a text file named numbers.txt that contains 20 integers. 
# The program will create two other text file;
# The first text file will be named 'even.txt' that will contains all even numbers extracted from the numbers.txt
# The second text file will be named 'odd.txt' that will contains all odd numbers extracted from the numbers.txt

# Extra codes for design
import pyfiglet
from simple_colors import *

print(blue("~ooOo~~ooOo~~ooOo~~ooOo~~ooOo~~ooOo~~ooOo~~ooOo~~ooOo~~ooOo~~ooOo~~ooOo~~ooOo~~ooOo~~ooOo~~ooOo~~ooOo~~ooOo~~ooOo~~ooOo~~ooOo~~ooOo~~ooOo~~ooOo~~ooOo~~ooOo~"))
print(blue(pyfiglet.figlet_format("Task # 4: P-1", font = "3x5" )))
print(blue("~ooOo~~ooOo~~ooOo~~ooOo~~ooOo~~ooOo~~ooOo~~ooOo~~ooOo~~ooOo~~ooOo~~ooOo~~ooOo~~ooOo~~ooOo~~ooOo~~ooOo~~ooOo~~ooOo~~ooOo~~ooOo~~ooOo~~ooOo~~ooOo~~ooOo~~ooOo~"))

print(yellow("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ HELLO USER! WELCOME BACK TO OUR SYSTEM ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"))
print(yellow("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ TODAY WE WILL CREATE A PROGRAM TO READ TEXT FILES CONTAINING 20 INTEGERS ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"))
print(yellow("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ AND EXTRACTING ALL EVEN AND ODD INTEGERS IN TWO SEPARATE TEXT FILES ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"))
print(green("\n\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ READY TO GO? ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"))
print(green("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ - - - INITIATING SEQUENCE - - - ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"))

def number_seperator():
    # create method to open text files: numbers.txt, even.txt , and odd.txt
    with open("numbers.txt") as integer_file, open("even.txt", "a") as even_integer_extraction, open("odd.txt", "a") as odd_integer_extraction:

    # read numbers.txt to determine integer placement
        for line in integer_file:
            line_placement = int(line)

            # if integer line placement is even,
            if line_placement % 2 == 0:
                even_integer = line_placement

                # overwrites to even.txt
                even_integer_extraction.write(str(even_integer) + '\n')
            
            # if integer line placement is odd,
            else:
                odd_integer = line_placement

                #overwrites to odd.txt
                odd_integer_extraction.write(str(odd_integer) + '\n')

number_seperator()

#extra code
print("\nThe 'numbers.txt' file contains the ff. integers:")
print("1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20")

print("\nThe Extracted Even Numbers from the 'numbers.txt' file are:")
print("2, 4, 6, 8, 10, 12, 14, 16, 18, 20")

print("\nThe Extracted Odd Numbers from the 'numbers.txt' file are:")
print("1, 3, 5, 7, 9, 11, 13, 15, 17, 19")