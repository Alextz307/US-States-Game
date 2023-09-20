import turtle
import pandas


screen = turtle.Screen()
screen.title('U.S. States Game')
screen.setup(width=725, height=485)

image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)

turtle_writer = turtle.Turtle()
turtle_writer.hideturtle()
turtle_writer.penup()
turtle_writer.color('black')

data = pandas.read_csv('50_states.csv')
remaining_states = set(data.state)

STATES = 50
guesses = 0

while guesses < STATES:
    answer_state = screen.textinput(title=f'{guesses}/{STATES} states correct', prompt="What's another state's name?")
    titled_state = answer_state.title()

    if titled_state == 'Exit':
        break

    if titled_state in remaining_states:
        guesses += 1
        remaining_states.remove(titled_state)

        row = data[data.state == titled_state]

        state_x, state_y = int(row.x.iloc[0]), int(row.y.iloc[0])

        turtle_writer.setposition(state_x, state_y)
        turtle_writer.write(arg=titled_state, align='center', font=('Arial', 8, 'normal'))

data_dict = {
    "State": list(remaining_states)
}

data_frame = pandas.DataFrame(data_dict)
data_frame.to_csv('states_to_learn.csv')
