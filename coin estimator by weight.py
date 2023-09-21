#Weights of each coin in grams

penny_w = 2.5
nickel_w = 5
dime_w = 2.268
quarter_w = 5.67

#User directions:

print('We currently support the following types of coins: Pennies, Nickels, Dimes, and Quarters')
print('Call on the function estimator(weight of your coins here, type of coin here) to use the estimator service.')

#Supported coin types for ease of use / less code clutter

penny_names = ['penny', 'pennies', 'cent', 'cents', 'C', '$0.01', '0.01']
nickel_names = ['nickel', 'nickels', '0.05', '$0.05']
dime_names = ['dime', 'dimes', '$0.10', '$0.1', '0.1', '0.10']
quarter_names = ['quarter', 'quarters', '0.25', '$0.25']


def estimator(scale=input('Pounds or grams? '), weight=input('How much do your coins weigh? '), type=input('What coins do you need estimated? ')):
    if scale == 'lb' or scale == 'pounds':
        weight = int(weight) * 453.592
    else: pass
    if type in penny_names:
        coin_number = int(weight) / penny_w
    elif type in nickel_names:
        coin_number = int(weight) / nickel_w
    elif type in dime_names:
        coin_number = int(weight) / dime_w
    elif type in quarter_names:
        coin_number = int(weight) / quarter_w
    else: 
        print('Type of coin is not found.')    
    wrap_count = coin_number // 50
    extras = coin_number % 50
    return f'We have estimated a total of {coin_number} coins, to be fitted into {wrap_count} wrap(s), with a remaining number of {extras}.'