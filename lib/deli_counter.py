katz_deli = []

def line(katz_deli):
    message = "The line is currently:"
    if len(katz_deli) > 0:
        for i in range(len(katz_deli)):
            message += f" {i + 1}. {katz_deli[i]}"
        print(message)
    else:
        print('The line is currently empty.')

def take_a_number(katz_deli, next_person):
    katz_deli.append(next_person)
    print(f"Welcome, {next_person}. You are number {len(katz_deli)} in line.")

def now_serving(katz_deli):
    if not katz_deli:
        print("There is nobody waiting to be served!")
    else:
        print(f"Currently serving {katz_deli[0]}.")
        del(katz_deli[0])