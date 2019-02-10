import variation_and_pronunciation as vp

my_dict = {
    "name": "[Catherine # Kea se rin]",
    "nickname": "Straight-A",
    "age": "18",
    "greeting": "How are you?",
    "school": "the Extremely Excellent University",
}


class Node:
    def __init__(self, name, options, fn=None):
        self.name = name
        self.options = options

        if fn:
            self.fn = fn
        else:
            self.fn = identity


class State:
    def __init__(self, current_node, flag, fn, running):
        self.current_node = current_node
        self.flag = flag
        self.fn = fn
        self.running = running


def print_hi(state):
    string = "Hi, {greeting} What do you want to know about me?"
    print(vp.interpret_display(vp.expand(string, my_dict)))
    return state


def introduce_name(state):
    string = "My name is {name}."
    print(vp.interpret_pronunciation(vp.expand(string, my_dict)))
    if state.flag:
        introduce_name_1()
        state.current_node = Name_1
    return state


def introduce_name_1():
    string = "You can also call me {nickname}."
    print(vp.interpret_display(vp.expand(string, my_dict)))


def introduce_age(state):
    string = "I am {age} years old."
    print(vp.interpret_display(vp.expand(string, my_dict)))
    state.user_age = input("How old are you?\n")
    """
    if int(state.user_age) > my_age:
        state.flag = True
    else:
        state.flag = False
    """
    return state


def introduce_school(state):
    string = "I'm now studying at {school}."
    print(vp.interpret_display(vp.expand(string, my_dict)))
    return state


def bye(state):
    print("See you!")
    state.running = False
    return state


def identity():
    pass


def run_state(state):
    return state.current_node.fn(state)


def next_state(state):
    while(state.running):
        for i in range(len(state.current_node.options)):
            print(str(i + 1) + '. ' + state.current_node.options[i])

        user_answer = input("What next? Please choose a number.\n")
        is_valid = False
        while not is_valid:
            try:
                user_answer = int(user_answer)
                if user_answer in range(1, len(state.current_node.options) + 1):
                    is_valid = True
            except ValueError:
                print("Please give a valid number")

        for item in nodes:
            if state.current_node.options[user_answer - 1] == item.name:
                state.current_node = item
                return state
    return state


MENU = Node('MENU', ['Name', 'Age', 'School', 'Exit'], print_hi)
Name = Node('Name', ['MENU', 'Exit'], introduce_name)
Age = Node('Age', ['MENU', 'Exit'], introduce_age)
School = Node('School', ['MENU', 'Exit'], introduce_school)
Name_1 = Node('Name_1', ['MENU', 'Exit'])
Exit = Node('Exit',[], bye)

state = State(MENU, True, next_state, True)

Running = True

nodes = [MENU, Name, Age, School, Name_1, Exit]


while (state.running):
    # runnning current state
    state = run_state(state)
    # checking for next state
    state = state.fn(state)
