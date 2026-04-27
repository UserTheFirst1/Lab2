def main():
    display_main_menu()
    float_list = get_user_input()
    sort_temperature(float_list)
    calc_average(float_list)
    find_min_max(float_list)
    calc_median_temperature(float_list)

def display_main_menu():
    print("Enter some numbers separated by commas (eg. 5, 65, 34)")


def get_user_input():
    numlist = input("Enter numbers: ")
    splitlist = numlist.split(",")

    float_list = []
    for count in splitlist:
        float_list.append(float(count.strip()))  

    return float_list


def sort_temperature(float_list):
    float_list.sort()
    return float_list
    


def calc_average(float_list):
    if len(float_list) == 0:
        return 0

    average = sum(float_list) / len(float_list)
    print("The Average Is " + str(average))
    return average


def find_min_max(float_list):
    min_temp = min(float_list)
    max_temp = max(float_list)

    print("Min Temperature is " + str(min_temp))  
    print("Max Temperature is " + str(max_temp)) 

    return [min_temp, max_temp]


def calc_median_temperature(float_list):  
    sorted_list = sort_temperature(float_list)
    length = len(sorted_list)

    if length == 0:
        return 0

    if length % 2 == 0:
        mid1 = length // 2 - 1
        mid2 = length // 2
        median = (sorted_list[mid1] + sorted_list[mid2]) / 2
    else:
        mid = length // 2
        median = sorted_list[mid]

    return median

main()