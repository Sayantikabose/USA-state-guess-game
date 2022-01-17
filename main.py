import turtle
import pandas
screen = turtle.Screen()
screen.title("US STATE NAMES") 
image="blank_states_img.gif"
screen.addshape(image) 
turtle.shape(image) 

data = pandas.read_csv("50_states.csv")
all_states= data["state"].to_list()
guess_state=[]
while(len(guess_state)<50):
    answer = screen.textinput(title=f"{len(guess_state)}/50 staes correct", prompt="Guess the name of a US state").title()
    if (answer == "Exit"):
        missing=[] 
        #for states in all_states:
            #if (states not in guess_state):
                #missing.append(states)

        missing =[states for states in all_states if states not in guess_state ] 
        df = pandas.DataFrame(missing)
        df.to_csv("missingstate.csv") 
        break
    if answer in all_states: 
       guess_state.append(answer) 
       t= turtle.Turtle()
       t.hideturtle()
       t.penup()
       state_data=data[data["state"]== answer]
       t.goto(int(state_data["x"]),int( state_data["y"]))
       t.write(answer)



    

