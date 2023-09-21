#Program to calculate how many coins of each type should be used to return change as a cashier

#Function to perform the operation

def change_calculator(payment, price):
    change1 = payment - price
    quarters = change1 // 0.25
    if quarters > 1 or quarters == 0:
        quarter_or_quarters = 'quarters'
    else: quarter_or_quarters = 'quarter'
    if change1 % 0.25 != 0:
        dimes = (change1 % 0.25) // 0.1
        if dimes > 1 or dimes == 0:
            dime_or_dimes = 'dimes'
        else: dime_or_dimes = 'dime'
        if (change1 % 0.25) % 0.1 != 0:
            nickels = ((change1 % 0.25) % 0.1) // 0.05
            if nickels > 1 or nickels == 0:
                nickel_or_nickels = 'nickels'
            else: nickel_or_nickels = 'nickel'
            if ((change1 % 0.25) % 0.1) % 0.05 != 0:
                pennies = (((change1 % 0.25) % 0.1) % 0.05) // 0.01
                if pennies > 1 or pennies == 0:
                    penny_or_pennies = 'pennies'
                else: penny_or_pennies = 'penny'
    else: pass
    print(f'Return {quarters} {quarter_or_quarters}, {dimes} {dime_or_dimes}, {nickels} {nickel_or_nickels}, and {pennies} {penny_or_pennies} to the customer.')

print(change_calculator(19.6, 19))

