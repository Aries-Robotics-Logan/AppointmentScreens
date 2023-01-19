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