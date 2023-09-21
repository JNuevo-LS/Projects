# Using given number, base, and wanted base, convert given number to wanted base.
alphabet = ['a','b','c','d','e','f','g']
def base_jumper(num, og_base, wan_base):
    string_a = '' # String to be filled with calculated values
    if og_base > wan_base:
       to_be_added = num % wan_base # Remainder of num and base
       quotient = num // wan_base
       string_a += str(to_be_added) # Adds newly calculated value
       while quotient != 0: # Continues the conversion in the common case of a longer number
           to_be_added = quotient % wan_base
           quotient = quotient // wan_base
           string_a += str(to_be_added) 
    elif og_base < wan_base:
        remainder = num / wan_base
        decimal_r = remainder % 1
        true_remainder = remainder - decimal_r
        to_be_added = decimal_r * wan_base
        if to_be_added > og_base:
            string_a += alphabet[int(to_be_added)-og_base]
        elif to_be_added <= og_base
            string_a += str(to_be_added)
        while true_remainder != 0:
            remainder = num / wan_base
            decimal_r = remainder % 1
            true_remainder = remainder - decimal_r
            to_be_added = decimal_r * wan_base
            if to_be_added > og_base:
                string_a += alphabet[int(to_be_added)-og_base]
            else:
                string_a += str(to_be_added) 

    final_string = string_a[::-1] # Reverses the string to the correct form
    return final_string

print(base_jumper(17, 10, 16))


