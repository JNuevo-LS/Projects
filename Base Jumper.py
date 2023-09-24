# Using given number, base, and wanted base, convert given number to wanted base.
alphabet = ['a','b','c','d','e','f','g']

def base_above(num, og_base, wan_base): #Divided problem into two functions, to be called by the main function.
    string_a = ''
    remainder = num / wan_base
    decimal_r = remainder % 1
    true_remainder = remainder - decimal_r
    to_be_added = decimal_r * wan_base
    if to_be_added >= og_base: #If the number is larger than the original
         to_be_added = round(to_be_added, 1)
         string_a += alphabet[int(to_be_added)-og_base]
    elif to_be_added <= og_base:
        to_be_added = round(to_be_added, 1)
        string_a += str(int(to_be_added))
    while true_remainder != 0:
        remainder = true_remainder / wan_base
        decimal_r = remainder % 1
        true_remainder = remainder - decimal_r
        to_be_added = decimal_r * wan_base
        if to_be_added > og_base:
            to_be_added = round(to_be_added, 1)
            string_a += alphabet[int(to_be_added)-og_base]
        else:
            to_be_added = round(to_be_added, 1)
            string_a += str(int(to_be_added))
    return string_a

def base_below(num, og_base, wan_base):
    string_a = ''
    to_be_added = num % wan_base # Remainder of num and base
    quotient = num // wan_base
    string_a += str(to_be_added) # Adds newly calculated value
    while quotient != 0: # Continues the conversion in the common case of a longer number
        to_be_added = quotient % wan_base
        quotient = quotient // wan_base
        string_a += str(to_be_added)     
        return string_a

def convert_to_b10(num, og_base):
    string_a = ''
    added_up = 0
    num_string = str(num) #Used to target each digit
    for number in enumerate(num_string):
        number_digit = int(number[1]) * pow(og_base, (len(num_string) - number[0] - 1))
        added_up += int(number_digit)
    string_a = str(added_up)
    return string_a

def convert_larger_base_to_b10(num, og_base):
     number_string = str(num)
     number_list = []
     for number in number_string:
         number_list.append(number)
     print(number_list)
     back_to_int = 0
     for index, digit in enumerate(number_list):
         if digit in alphabet: #To deal with converting values above base 10 back to base 10 then convert
             digit_value = alphabet.index(digit) + 10
             digit_value = digit_value * pow(og_base, (len(number_string) - index- 1))
             print(digit_value)
             back_to_int += int(digit_value)
         else:
             if number_string.index(digit) < (len(number_string) - 1):
                digit = int(digit) * pow(og_base, (len(number_string) - number_string.index(digit) - 1))
                back_to_int += int(digit)
             else:
                 back_to_int += int(digit)
     return back_to_int


def base_jumper(num, og_base, wan_base):
    string_a = '' # String to be filled with calculated values
    if og_base > 10:
        num = convert_larger_base_to_b10(num, og_base)
        if wan_base == 10:
            string_a = num
        elif wan_base > 10:
            num = base_above(num, 10, wan_base)
            string_a = num
        else: 
            num = base_below(num, 10, wan_base)
            string_a = num
    elif og_base < 10 and og_base < wan_base:
        num = convert_to_b10(num, og_base)
        num = int(num)
        string_a = base_above(num, 10, wan_base)
    elif og_base == wan_base:
        return 'Original and wanted base match each other.'
    elif og_base > wan_base:
        string_a = base_below(num, og_base, wan_base)
    else:
        string_a = base_above(num, og_base, wan_base)
    final_string = string_a[::-1] # Reverses the string to the correct form
    return final_string

print(base_jumper('a64a2', 12, 16))
