from datetime import date
from random import randint
from Functions import show_menu, ager, get_valid_input, datify, prepareforapp


def main_menu():
    menu = [
        'I have an appointment',
        'I would like to schedule an appointment',
        'Refilling a prescription',
        'Quit'
    ]
    show_menu(menu)
    return get_valid_input(range(len(menu)))


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
    dict = {}
    while True:
        doc_list = ["Dr. Bishop", "Dr. Malak", "Dr. Sanders", "Dr. Gray", "Dr. Kumar"]
        print()
        ##usefullist = day()
        ##print(f"Today is {usefullist[0]} {usefullist[1]}")
        print(date.today())
        print("Welcome to Cascade Health Services!")
        name = input("Enter your full (first, middle, last) legal name: ")
        age = input("What is your current age: ")
        if ager(age):
            print("What are you visiting for? ")
            option = main_menu()
            if option == 0:
                if int(age) < 0 or int(age) > 100:
                    break
                print("Who do you have your appointment with?")
                sec_option = doctor_menu()
                print(name, "-- appointment for", date.today())
                print(f"Great, {doc_list[sec_option]} will see you now!")
                break
            if option == 1:
                test = 0
                print("Great, who would you want to meet with?")
                sec_option = doctor_menu()
                print(f"Okay, so {doc_list[sec_option]} is actually busy for a while.")
                while test != 1:
                    number = randint(1, 28)
                    time = randint(7, 11)
                    print(f"Can you do the {datify(number)} of next month at {time} am?")
                    answer = input("(Y/y) for yes or (N/n) for no: ")
                    if answer.upper() == "Y":
                        print(f"Great! We will put you down for the {datify(number)} of next month at {time} am")
                        prepareforapp(name, age, doc_list[sec_option], datify(number), time)
                        test = 1
                        break
                    elif answer.upper() == "N":
                        continue
                break
            if option == 2:
                if name not in dict:
                    prescription = input("What medication are you hoping to refill? ")
                    dict[name] = {}
                    amount = input("What is the dosage (mg per day) that you have been taking it at? ")
                    if prescription not in dict[name]:
                        dict[name] = f"{prescription} at {amount} milligrams per day"
                else:
                    ret = input(f"The last medication you got from us was {dict[name]}. Is that what you are looking to refill today? (Y/y) (N/n)")
                    if ret.upper() == "Y":
                        print("Fantastic, here you go!")
                    else:
                        prescription = input("What medication are you hoping to refill? ")
                        amount = input("What is the dosage that you have been taking it at? ")
                        dict[name] = f"{prescription} at {amount}"
                        print(f"We will get {dict[name]} for you right away!")
                print(dict[name])
            if option == 3:
                break
        else:
            print("I'm sorry, we need to have you with an adult. Please return with one. ")
            break

if __name__ == '__main__':
    main()