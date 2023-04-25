# Mendiola, Logie A. | BSCPE 1-5 | Object-Oriented Programming | Assignment #4: P-1

# Write a Python program that reads a text file named numbers.txt that contains 20 integers. 
# The program will create two other text file;
# The first text file will be named 'even.txt' that will contains all even numbers extracted from the numbers.txt
# The second text file will be named 'odd.txt' that will contains all odd numbers extracted from the numbers.txt

# create method to open text files: numbers.txt, even.txt , and odd.txt
with open("numbers.txt") as integer_file, open("even.txt", "a") as even_integer_extraction, open("odd.txt", "a") as odd_integer_extraction: