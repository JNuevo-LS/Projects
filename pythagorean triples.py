def check_pythagorean_triple(list):
    sorted_list = sorted(list)
    try: 
        if len(sorted_list) != 3:
            return sorted_list[0] + sorted_list[1] == sorted_list[2]
    except:
            print("Please only include integers.")

given_list = [40, 40, 'b']

print(check_pythagorean_triple(given_list))