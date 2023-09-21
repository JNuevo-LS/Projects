def bottles_of_beer_lyrics(bottle_number = 99):
    count = bottle_number 
    while count > 0:
        if count >= 1:
            if count > 1:
                bottle = 'bottles'
            print(f'{count} {bottle} of beer on the wall, {count} {bottle} of beer.')
            count -= 1
            if count == 1:
                bottle = 'bottle'
            print(f'Take one down and pass it around, {count} {bottle} of beer on the wall.')
        if count == 0:
            count = 99
            print(f"""No more bottles of beer on the wall, no more bottles of beer.
            Go to the store and buy some more. {count} bottles of beer on the wall.""")
            break

print(bottles_of_beer_lyrics())