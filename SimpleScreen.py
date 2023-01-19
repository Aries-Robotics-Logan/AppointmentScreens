from datetime import date


def main_menu():
    menu = [
        'I have an appointment',
        'I would like to schedule an appointment',
        'Refilling a prescription',
        'Quit'
    ]
    show_menu(menu)
    return get_valid_input(range(len(menu)))


def show_menu(menu):
    for index, option in enumerate(menu):
        print(f'({index}) {option}')


def doctor_menu():
    dmenu = [
        "Dr. Bishop (Podiatry)",
        "Dr. Malak (Orthopaedics)",
        "Dr. Sanders (Oncology)",
        "Dr. Gray (Optometry)",
        "Dr. Kumar (Cardiology)",
    ]
    show_menu(dmenu)
    return get_valid_input(range(len(dmenu)))


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


##def day():
    ##    currentdate = []
    ##line = str(date.today())
    ##splice = line.split("-")
    ##while currentdate == []:
        ##    if splice[1] == 1:
        ##    currentdate.append("January")
        ##if splice[1] == 2:
        ####    currentdate.append("February")
        ##if splice[1] == 3:
    ##    currentdate.append("March")
    ##currentdate.append(splice[2])
    ##return currentdate


def main():
    while True:
        doc_list = ["Dr. Bishop", "Dr. Malak", "Dr. Sanders", "Dr. Gray", "Dr. Kumar"]
        print()
        ##usefullist = day()
        ##print(f"Today is {usefullist[0]} {usefullist[1]}")
        print(date.today())
        print("Welcome to Cascade Health Services!")
        name = input("Enter your full legal name: ")
        age = input("What is your current age: ")
        print("What are you visiting for? ")
        option = main_menu()
        if option == 0:
            if int(age) < 0 or int(age) > 100:
                break
            print("Who do you have your appointment with?")
            sec_option = doctor_menu()
            print(name, "--", age)
            print(f"Great, {doc_list[sec_option]} will see you now!")
            break
        if option == 1:
            print("Great, who would you want to meet with?")
            sec_option = doctor_menu()
            print(f"Okay, so {doc_list[sec_option]} is actually busy for a while. Can you do next month?")
            answer = input("(Y/y) for yes or (N/n) for no: ")
            if answer.upper() == "Y":
                print("Great! We will put you down for the 23rd of next month at 11:00 am")
                break
        if option == 2:
            print("Haha")
        if option == 3:
            break


if __name__ == '__main__':
    main()