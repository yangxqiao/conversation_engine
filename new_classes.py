class State:

    def __init__(self, name, options):
        self.name = name
        self.options = options


menu = State('menu', ['s1', 's2',])
s1 = State('s1', ['menu', 's3'])
s2 = State('s2', ['menu', 's2'])
s3 = State('s3', ['menu'])

states = [menu, s1, s2, s3]

current_state = menu

Running = True

while(Running):
    print "\nNow we are at state: %s." % current_state.name
    for i in range(len(current_state.options)):
        print str(i+1) + '. ' + current_state.options[i]

    user_answer = int(raw_input("What next? Please choose a number.\n"))

    for item in states:
        if current_state.options[user_answer - 1] == item.name:
            current_state = item
            break



