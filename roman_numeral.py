"""
Author: Kara Meyer
Date: 11-26-2019
Description: This program will simplify roman numerals given in a text file.
And print the number of characters saved. 

REQUIREMENTS:
+ Numerals must be arranged in descending order of size.
+ Only one I, X, and C can be used as the leading numeral in part of a
subtractive pair. I can only be placed before V and X. X can only be placed
before L and C. C can only be placed before D and M.
+ In the text file, each new roman numeral must be on a new line.

Guide to Roman Numerals:
I = 1     V = 5     X = 10    L = 50
C = 100   D = 500   M = 1000
IV = 4    IX = 9    XL = 40   XC = 90
CD = 400  CM = 900
"""


def roman_to_int(roman_numerals):
    """Convert the roman numeral to an int."""
    romans = roman_numerals
    int_numeral = 0
    for index, numeral in enumerate(romans):
        if numeral == "I":
            if index == len(romans) - 1:
                int_numeral += 1
            elif romans[index + 1] == "V" or romans[index + 1] == "X":
                int_numeral -= 1
            else:
                int_numeral += 1
        if numeral == "V":
            int_numeral += 5
        if numeral == "X":
            if index == len(romans) - 1:
                int_numeral += 10
            elif romans[index + 1] == "L" or romans[index + 1] == "C":
                int_numeral -= 10
            else:
                int_numeral += 10
        if numeral == "L":
            int_numeral += 50
        if numeral == "C":
            if index == len(romans) - 1:
                int_numeral += 100
            elif romans[index + 1] == "D" or romans[index + 1] == "M":
                int_numeral -= 100
            else:
                int_numeral += 100
        if numeral == "D":
            int_numeral += 500
        if numeral == "M":
            int_numeral += 1000
    return int_numeral


def int_to_roman(int_numeral):
    """Convert the int to simplified roman numerals."""
    simplify = ""
    while int_numeral >= 1000:
        simplify = simplify + "M"
        int_numeral -= 1000
    if int_numeral >= 900:
        simplify = simplify + "CM"
        int_numeral -= 900
    while int_numeral >= 500:
        simplify = simplify + "D"
        int_numeral -= 500
    if int_numeral >= 400:
        simplify = simplify + "CD"
        int_numeral -= 400
    while int_numeral >= 100:
        simplify = simplify + "C"
        int_numeral -= 100
    if int_numeral >= 90:
        simplify = simplify + "XC"
        int_numeral -= 90
    while int_numeral >= 50:
        simplify = simplify + "L"
        int_numeral -= 50
    if int_numeral >= 40:
        simplify = simplify + "XL"
        int_numeral -= 40
    while int_numeral >= 10:
        simplify = simplify + "X"
        int_numeral -= 10
    if int_numeral == 9:
        simplify = simplify + "IX"
        int_numeral -= 9
    while int_numeral >= 5:
        simplify = simplify + "V"
        int_numeral -= 5
    if int_numeral == 4:
        simplify = simplify + "IV"
        int_numeral -= 4
    while int_numeral >= 1:
        simplify = simplify + "I"
        int_numeral -= 1
    return simplify


# Remove whitespace from the raw lines and add them to an array.
romans_text = open("roman_numeral_text.txt", "r")
raw_lines = romans_text.readlines()
lines = []
for index in range(len(raw_lines)):
    this_line = raw_lines[index]
    remove_whitespace = this_line.rstrip()
    lines.append(remove_whitespace)

# Count the characters in original text and simplify the roman numerals.
count = 0
simplified_romans = []
for index in range(len(lines)):
    # Count characters
    count += len(lines[index])

    # Simplify numerals
    int_numeral = roman_to_int(lines[index])
    simplified_line = int_to_roman(int_numeral)
    simplified_romans.append(simplified_line)

# Calculate the characters in the simplified array.
new_count = (sum(len(i) for i in simplified_romans))

# Calculate the characters saved.
characters_saved = count - new_count
print(characters_saved)
