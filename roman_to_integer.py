## PROBLEM SOURCE: https://leetcode.com/problems/roman-to-integer/

## PROBLEM DESCRIPTION: Given a roman numeral, convert it to an integer.

dct_roman = {"I":1,
            "II": 2,
            "III": 3,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000}

#print(dict_roman)

input_test = "XXI"

#def roman_converter(roman_number):
roman_number = input_test
lst = []
lst[:0]=roman_number

previous_is_block = False
i = 0
result = 0
for e in lst:
    #print(result,previous_is_block)
    if roman_number in dct_roman:
        ## CHECK IF STRING IS A NUMBER ITSELF, CAN STOP HERE
        result = dct_roman[roman_number]
    else:
        current = lst[i]
        if i > 0:
            ## CHECK IF THERE IS A PREVIOUS NUMBER
            previous = lst[i-1]
            print(f"{i} iteration. Previous: {previous} Current: {current} Result={result}")
            if dct_roman[current] > dct_roman[previous] and previous_is_block == False:
                ## CHECK IF PREVIOUS IS SMALLER THAN CURRENT THAN THIS IS A BLOCK
                #### If that is the case, we need to 1) disregard previous
                #### and 2) add current - previous (e.g IX = 9 or X(10)-I(1))
                print("Block detected")
                result = result - dct_roman[previous] + (dct_roman[current] - dct_roman[previous])
                print(f"{i} iteration. Previous: {previous} Current: {current} Result={result}")
                previous_is_block = True
            else:
                ## IF NOT A BLOCK, JUST ADD IT
                result = result + dct_roman[current]
                print(f"{i} iteration. Previous: {previous} Current: {current} Result={result}")
                previous_is_block = False
        else:
            ## IF IT IS THE FIRST, JUST ADD IT TO THE RESULT
            result = result + dct_roman[current]
            print(f"{i} iteration. Current: {current} Result={result}")
            previous_is_block = False
    
    i += 1
print(f"The result is: {result}")