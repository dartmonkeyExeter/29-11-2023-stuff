def get_num(message, minimum, maximum):
    valid = False
    while not valid:
        number = input(f"{message}\n")
        if(number.isnumeric() and int(number) > minimum and int(number) <= maximum):
            number = int(number)
            valid = True
        else:
            print(f"please enter a number between {minimum} and {maximum}")
    return number

def show_age():
    day = get_num("what day of the month were you born on?", 0, 31)
    month = get_num("what month were you born on?", 0, 12)
    year = get_num("what year were you born?", 1900, 2100)
    return f'{day}/{month}/{year}'

if __name__ == "__main__":
    print(show_age())
