favorites = []
more_items = True

while more_items:
    user_input = input("Enter one of your favorite foods: ")
    if user_input == '':
        more_items = False
    else:
        favorites.append(user_input)

def pretty_print_unordered(to_print):
    for item in to_print:
        print("* " + str(item))

def pretty_print_ordered(to_print):
    i = 1
    for item in to_print:
        print(str(i) + ". " + str(item))
        i=i+1
    for i in range(len(to_print)):
        print(str(i+1) + ". " + str(to_print[i]))

print("You entered: ")
pretty_print_unordered(favorites)
pretty_print_ordered(favorites)
