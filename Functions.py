def show_menu(menu):
    for index, option in enumerate(menu):
        print(f'({index}) {option}')


def get_valid_input(valid_inputs):
    while True:
        response = input('Option: ').strip()
        if not response.isdigit():
            print(f'Invalid option: {response}')
            continue
        response = int(response)
        if response not in valid_inputs:
            print(f'Invalid option: {response}')
            continue

        return response


def datify(number):
    if number == 1 or number == 21:
        return str(number) + "st"
    if number == 2 or number == 22:
        return str(number) + "nd"
    if number == 3 or number == 23:
        return str(number) + "rd"
    if (number >= 4 and number <= 20) or number >= 24:
        return str(number) + "th"


def prepareforapp(name, age, doctor, date, time):
    print()
    print(f"Appointment Info:")
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"Doctor: {doctor}")
    print(f"Appointment: {date} @ {time} am")