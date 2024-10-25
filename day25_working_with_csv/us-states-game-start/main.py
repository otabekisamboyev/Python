import turtle
import pandas

image = "blank_states_img.gif"
screen = turtle.Screen()
screen.addshape(image)
screen.title("U.S. States Game")
screen.setup(width=725, height=491)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
state_list = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="What's another state's "
                                                                                             "name?").title()
    if answer_state == "Exit":
        missing_states = []
        for state in state_list:
            if state not in guessed_states:
                missing_states.append(state)
        print(missing_states)

        new_data = pandas.DataFrame(guessed_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_state in state_list:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        x, y = int(state_data.x.iloc[0]), int(state_data.y.iloc[0])
        t.goto(x, y)
        t.write(answer_state)
