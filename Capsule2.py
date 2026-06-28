# -*- coding: utf-8 -*-
"""
Created on Sun Jun 21 20:33:46 2026

@author: LENOVO
"""

#Capsule02

# #If Else

# comparing tuples
# tuple1 = (1,2,3)
# tuple2 = (3,2,1)

# if tuple1 == tuple2:
#     print("Tuple are equal")
# else:
#     print("Tuple are not equal")

# age = 20
# is_student = True
# has_job = True

# if age>18 and not is_student or has_job:
#     print("Eligible for some opportunities")
# # ==============================================
# one line

# score = 43
# result ="Pass" if score>=50 else ("Retake" if score>= 40 else "Fail")
# print(result)
# ==============================================
# multiplication table

# user_input = int(input("Enter a number :"))

# print(f'Total of {user_input} for odd multiples is as follows:')
# for i in range(1,11,2):
#     result = user_input * i
#     print(f'{user_input} x {i} = {result}')

# user_input = int(input("Enter a number :"))

# print(f'Total of {user_input} for odd multiples is as follows:')
# for i in range(1,11):
#     result = user_input * i
#     print(f'{user_input} x {i} = {result}')

# # ==============================================

# Print Multiplication table in reverse
# Get user input for the number

# user_input = int(input("Enter a number:"))

# print('f Reverse table of {user_input} is as follow')
# for i in range (10,0, -1):
#     result = user_input * i
#     print(f'{user_input} X {i} = {result}')

# # ==============================================

# calculate the sum number from 0 to 10

# a = 0
# for i in range (0,11):
#     a+=i
# print(a)
# ======================================

# a = 0
# prev_a = 0
# for i in range (0,6):
#     prev_a=a #store prev value of a
#     a+=i
#     print(f'current value of i: {i} and current value of a : {a} which is {prev_a}+ {i}')
#     print(f' Sum first 5 numbers is: {a}')

# ==============================================
#  the user enter a value and then calc the sum of numbers up to that value


# user_input = int(input("Enter a number:"))
# sum_result = 0

#  # cal the sum of numbers up to the user-entered value
 
# for i in range(0,user_input + 1):
#     sum_result +=  i
# print(f'Sum of numbers from 0 to {user_input} is: {sum_result}')

# ==============================================

# print every element of a list 

# my_list = {'Apple', 'Orange','Mango', 'Strawberry', 'Kiwi'}

# #using a for a loop to print each element
# for i in my_list:
#     print(i)

# # ==============================================

# print key-value pairs of dictionary

# student_marks = {'N' : 90, 'J': 98, 'K' : 80, 'A' : 90}
# for i in student_marks:
#     print("Student:", i, "Marks:", student_marks[i])

# # Access a specific key value pair
# A_marks = student_marks['A']
# print("A's marks:", A_marks)

# # ==============================================
# for i in range(-1,-6,-1):
#     print(i)
# ==============================================
# Len Function
# Used to find lenght of number or element

# my_string = "Hello"
# length_of_string = len(my_string)
# print(length_of_string)

# ==============================================
# Reserve a list
# my_list = ['Apple', 'Mango', 'Kiwi', 'Watermelon', 'Cherry']
# # Using a for loop to print the list in reverse order
# for i in range(len(my_list)-1,-1,-1):
#     print(my_list[i])

# ==============================================
# same with while loop
# my_list = ['Apple', 'Mango', 'Kiwi', 'Watermelon', 'Cherry']
# i = len(my_list)-1
# while i>= 0:
#     print(my_list[i])
# #     i -= 1

# # user to input a number which represents the count of fruits they want to print r
    
# my_list = ['Apple', 'Mango', 'Kiwi', 'Watermelon', 'Cherry']
# n = int(input("Enter the number of fruits to print the lists:"))
# i=0
# while i<=n-1:
#     print(my_list[i])
#     i += 1

# =====================================================

# a = {1,2,3,4}
# b = {1,2,3,4,4}
# c = {1,2,3,4,5}

# sum_a = sum(a)
# sum_b = sum(b)
# sum_c = sum(c)

# print(f"The sum of tuple a is: {sum_a}")
# print(f"The sum of tuple b is: {sum_b}")
# print(f"The sum of tuple c is: {sum_c}")

# =====================================================

# count 
# word_list = ["apple", "banana", "apple", "orange", "apple", "grape"]
# count_apple = word_list.count("apple")

# print(f"The count of 'apple' in the list is : {count_apple}")

# my_string = "Hello, World!"

# #count occurences of the letter 'o'
# count_o = my_string.count('o')

# print("The character 'o' appears", count_o, "times in the string")

# The Syntax is:
# split
# used to split a string into a list of substring based on a specified deliminator

# The syntax is

# date_input = input("Enter a date(dd-mm-yyyy)")

# day, month, year = date_input.split('-')

# print("Day:", day)
# print("Month:", month)
# print("Year:", year)

# sentence = "Python;is;a;versatile;programming;language"
# word_list = sentence.split(';', maxsplit=2)
# print("Original sentence:", sentence)
# print("Word list:", word_list)
# =====================================================

# startswith() and endwith()

# file_name = "document.txt"
# if file_name.startswith("document"):
#     print("This is a document file.")
# elif file_name.startswith("image"):
#     print("This is a image file.")
# else:
#     print("Unknown file type.")

# # endswith()

# email = input("Enter the email:")
# if email.endswith(".com"):
#     print("This is a valid email")
# else:
#     print("NOt valid")

# =====================================================

# define a tuple of valid prefixes

# valid_prefixes = ("http://", "https://", "ftp://")

# #user input

# url = input("Enter a website url:")
# if url.startswith(valid_prefixes):
#     print("The URL is valid")
# else:
#     print("Not Valid")

# =====================================================

# strip()
# used in wiping the extra spaces

# word_with_spaces = " Python "
# cleaned_word = word_with_spaces.strip()

# print("Original world:", word_with_spaces)
# print("Cleaned:", cleaned_word)

# user_names =["John", "Alice", " Bob", "Charlie"]

# cleaned_names = [name.strip() for name in user_names]
# print(user_names)
# print(cleaned_names)

# # =====================================================
# insert()
# toy_cars = ["Red Car", "Blue Car", " Blue Car", "Green Car"]
# print("Original Toy Cars:", toy_cars)
# new_toy_car = "Yellow Car"

# toy_cars.insert(0, new_toy_car)

# print("Updated Toy Cars:", toy_cars)
# =====================================================
# numbers =[5,2,8,1,3]

# print("Original numbers:", numbers)

# numbers.reverse()

# print("Reverse Order:", numbers)
# =====================================================
# any()

# bool_values = [False, False, True, False]
# is_any_true = any(bool_values)

# if is_any_true:
#     print("Atleast one value is True.")
# else:
#     print("No value is true.")

# =====================================================
# color_palette = ("red", "blue", "green", "yellow", "purple")

# user_color_input = input("Enter the color you are looking for in the palette:"). lower()

# if user_color_input in color_palette:
#     print(f"Yes, the color {user_color_input}")
# =====================================================

# append() for list and add() for sets.add() is used for elements in det

# shopping_cart = {"apple", "banana", "orange"}

# item_to_add = input("Enter the item you want to add to your shopping cart:").lower()

# shopping_cart.add(item_to_add)

# print("Updated shopping cart:", shopping_cart)
# =====================================================

# remove() and discard()

# fruits = {"apple", "banana", "orange"}
# fruits.discard("orange")
# print(fruits)
# =====================================================
# intersection

# basket1 = {"apple", "banana", "orange"}
# basket2 = {"banana", "grape", "kiwi"}
# combined_basket= basket1.intersection(basket2)
# print(combined_basket)

# =====================================================
# union
# basket1 = {"apple", "banana", "orange"}
# basket2 = {"banana", "grape", "kiwi"}
# combined_basket = basket1.union(basket2)
# print(combined_basket)
# =====================================================



# year = int(input("Please enter a year:"))

# if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
#     print(f"{year} is a leap year.")
# else:
#     print(f"{year} is not a leap year.")

def count_vowels(word):
    vowels = "aeiouAEIOU"
    count = 0
    for char in word:
        if char in vowels:
            count += 1
    return count



# Prompt the user for input
word = input("Enter a word: ")

# Count and display the number of vowels
result = count_vowels(word)
print(f"The number of vowels in '{word}' is: {result}")



def print_a_names():
    names = []
    
    # Collect 6 names from the user
    print("Please enter 6 names:")
    for i in range(6):
        name = input(f"Enter name {i+1}: ").strip()
        names.append(name)
    
    print("\nNames that start with 'A' or 'a':")
    
    # Filter and print names starting with 'a' (case-insensitive)
    found_any = False
    for name in names:
        if name.lower().startswith('a'):
            print(name)
            found_any = True
            
    if not found_any:
        print("No names started with the letter 'A'.")

# Run the program
if __name__ == "__main__":
    print_a_names()
    
    

def process_numbers():
    numbers = []
    
    print("Please enter 10 integers:")
    for i in range(10):
        while True:
            try:
                num = int(input(f"Enter integer {i+1}"))
                numbers.append(num)
                break
            except ValueError:
                print("Invalid input. Please enter valid value.")
                
    print("\nProcessing Results:")
    
    for num in numbers:
        if num % 2 == 0:
            print(f"{num} is even -> Squared: {num ** 2} ")
        else:
            print(f"{num} is odd -> Cubed: {num ** 3} ")
            
if __name__ == "__main__":
    process_numbers()
    
    
def calculate_flower_order():
    print("--- Welcome to the Flower Delivery Service ---")
    
    # Constants
    ROSE_PRICE = 10
    
    # Input validation for count of roses
    while True:
        try:
            rose_count = int(input("Enter the number of roses you wish to order: "))
            if rose_count >= 0:
                break
            print("Please enter a valid positive number.")
        except ValueError:
            print("Invalid input. Please enter a whole number.")
            
    # Input validation for delivery distance
    while True:
        try:
            distance = float(input("Enter the delivery distance (in km): "))
            if distance >= 0:
                break
            print("Distance cannot be negative.")
        except ValueError:
            print("Invalid input. Please enter a valid number for distance.")

    # Calculate the base cost of roses
    rose_cost = rose_count * ROSE_PRICE
    
    # Determine delivery charges based on distance
    if distance <= 5:
        delivery_charge = 25
    elif distance <= 10:
        delivery_charge = 50
    else:
        delivery_charge = 75

    # Calculate total price
    total_price = rose_cost + delivery_charge

    # Display receipt
    print("\n--- Your Order Receipt ---")
    print(f"Roses Order Cost ({rose_count} x Rs. {ROSE_PRICE}): Rs. {rose_cost}")
    print(f"Delivery Charge ({distance:.1f} km): Rs. {delivery_charge}")
    print("-" * 26)
    print(f"Total Price to Pay: Rs. {total_price}")

# Run the program
if __name__ == "__main__":
    calculate_flower_order()