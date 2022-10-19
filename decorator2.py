

def display(msg):
    print(msg)

def contact(ph):
    print(ph)

#instance = display
#instance("welcome to the decorator world")
def main(func):
    var = func("welcome to the decorator world")

main(display)
main(contact)