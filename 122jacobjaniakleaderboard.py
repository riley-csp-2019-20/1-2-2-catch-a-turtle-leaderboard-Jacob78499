# a121_catch_a_turtle.py
#-----import statements-----
import turtle as trtl
import random
import turtle as score_writer
import turtle as counter
import leaderboard as lb
#-----game configuration----
shape = "arrow"
size = 5
color = "red"
font_setup = ("Arial", 20, "normal")
timer = 10
counter_interval = 1000   #1000 represents 1 second
timer_up = False

#leaderboard variables
leaderboard_file_name = "a122_leaderboard.txt"
leader_names_list = []
leader_scores_list = []
player_name = input("please enter your name")


#-----initialize turtle-----
background_t = trtl.Turtle()
background_t.ht()
background_t.speed(0)
background_t.color("green")
background_t.pensize(10000)
background_t.circle(1)

Randy = trtl.Turtle(shape =shape)
Randy.color(color)
Randy.shapesize(size)
score = 0
score_writer = trtl.Turtle()
score_writer.penup()
score_writer.ht()
score_writer.speed(0)
score_writer.goto(-410, 370)
font = ("Arial", 20, "bold")
score_writer.write(score, font=font)

counter =  trtl.Turtle()
counter.ht()
counter.speed(0)
counter.penup()
counter.goto(360,370)


#-----game functions--------
def turtle_clicked(x,y):
  change_position()
  score_counter()


def countdown():
  global timer, timer_up
  counter.clear()
  if timer <= 0:
    counter.write("Time's Up", font=font_setup)
    timer_up = True
    manage_leaderboard()
  else:
    counter.write("Timer: " + str(timer), font=font_setup)
    timer -= 1
    counter.getscreen().ontimer(countdown, counter_interval) 

def change_position():
    Randy.penup()
    Randy.speed(0)
    Randy.ht()
    new_xpos = random.randint(-400,400)
    new_ypos = random.randint(-300,300)
    Randy.goto(new_xpos, new_ypos)
    Randy.st()

def score_counter():
    global score
    score += 1
    score_writer.clear()
    score_writer.write(score, font=font_setup)

# manages the leaderboard for top 5 scorers
def manage_leaderboard():
  
  global leader_scores_list
  global leader_names_list
  global score
  global Randy

  # load all the leaderboard records into the lists
  lb.load_leaderboard(leaderboard_file_name, leader_names_list, leader_scores_list)

  # TODO
  if (len(leader_scores_list) < 5 or score > leader_scores_list[4]):
    lb.update_leaderboard(leaderboard_file_name, leader_names_list, leader_scores_list, player_name, score)
    lb.draw_leaderboard(leader_names_list, leader_scores_list, True, Randy, score)

  else:
    lb.draw_leaderboard(leader_names_list, leader_scores_list, False, Randy, score)

  

#-----events----------------
Randy.onclick(turtle_clicked)
wn = trtl.Screen()
wn.ontimer(countdown, counter_interval) 
wn.mainloop()
