
#----imports----
import turtle as trtl
import random as rand
import time


#----initialize turtles----
player = trtl.Turtle() 
wn = trtl.Screen()
point = trtl.Turtle()
writer = trtl.Turtle()
player.setheading(90)
player.penup()

#sets point shape and color
point.shape("square")
point.color("yellow")
#identifies shapes
sprite_1 = "sprite_1.gif" 
sprite_2 = "sprite_2.gif" 
sprite_3 = "sprite_3.gif" 
sprite_4 = "sprite_4.gif" 
bullet = "bullet.gif"

#adds shapes to turtle list
wn.addshape(sprite_1) 
wn.addshape(sprite_2) 
wn.addshape(sprite_3) 
wn.addshape(sprite_4) 
wn.addshape(bullet)

point.speed(0)
point.penup()




#----variables----
score = 0
min_bullets = 0
max_bullets = 0
font_setup = ("Arial", 20, "normal")
bullet_list = []
speed = 0
color_list = ["red", "blue", "purple", "green", "orange"]



#----functions----

#gives the player a random character.
def random_char():
	player_shapes = ["sprite_1.gif", "sprite_2.gif", "sprite_3.gif", "sprite_4.gif"]
	chosen_sprite = str(player_shapes[rand.randint(0,3)])
	print (chosen_sprite)
	player.shape(chosen_sprite)

#asks the player for what difficulty they want, difficulty scales with speed.
def pick_difficulty():
	global min_bullets
	global max_bullets
	global speed

	difficulty = input("Hard | Medium | Easy: ")
	difficulty.lower()

	if difficulty == "easy":
		print("You chose easy.")
		min_bullets = 1
		max_bullets = 2
		speed = .25
		
	elif difficulty == "medium":
		print("You chose medium!")
		min_bullets = 2
		max_bullets = 3
		speed = .05

	elif difficulty == "hard":
		print("YOU CHOSE HARD!")
		min_bullets = 3
		max_bullets = 4
		speed = .01
	elif difficulty == "NIGHTMARE":
		print("Good luck.")
		min_bullets = 5
		max_bullets = 6
		speed = 0
	else:
		pick_difficulty()

#moves bullet, and kills player.
def move_bullet(bullet):
	global speed
	global wave
	if bullet.xcor() != -300:
		bullet.backward(100)
		time.sleep(speed)
		bxcor = bullet.xcor()
		bycor = bullet.ycor()
		pxcor = player.xcor()
		pycor = player.ycor()
		if (pxcor == bxcor and pycor == bycor) or (pxcor == bxcor+100 and pycor == bycor) or (pxcor == bxcor-100 and pycor == bycor):
			print("DEAD")
			player.hideturtle()
			game_over()
		move_bullet(bullet)
	else:
		bullet.hideturtle()
		bullet_list.remove(bullet)
	if len(bullet_list) == 0:
		get_bullets()

	
	

	
	
	
	

#moves player forward and checks for point collision
def move_forward():
	global score
	player.forward(100)
	cur_xcor = player.xcor()
	cur_ycor = player.ycor()
#border, returns player back to spawn
	if cur_xcor == 300 or cur_xcor == -300:
		player.setposition(0,0)
	if cur_ycor == 300 or cur_ycor == -300:
		player.setposition(0,0)
	
	pointxcor = point.xcor()
	pointycor = point.ycor()
#checks if position of player and point and/DIY collision then gains point and start point anim and respawns point.
	if cur_xcor == pointxcor and cur_ycor == pointycor:
		print("Gained a point!")
		score = score + 1
		point_anim()
		spawn_point()

#moves player backward and checks for point collision
def move_backward():
	global score
	player.backward(100)
	cur_xcor = player.xcor()
	cur_ycor = player.ycor()
#border, returns player back to spawn
	if cur_xcor == 300 or cur_xcor == -300:
		player.setposition(0,0)
	if cur_ycor == 300 or cur_ycor == -300:
		player.setposition(0,0)

	pointxcor = point.xcor()
	pointycor = point.ycor()
#checks if position of player and point and/DIY collision then gains point and start point anim and respawns point.
	if cur_xcor == pointxcor and cur_ycor == pointycor:
		print("Gained a point!")
		score = score + 1
		point_anim()
		spawn_point()
		

#moves player left and checks for point collision
def move_left():
	global score
	cur_xcor = player.xcor()
	cur_ycor = player.ycor()
	player.setposition(cur_xcor-100,cur_ycor)
	ncur_xcor = player.xcor()
	ncur_ycor = player.ycor()
#border, returns player back to spawn
	if ncur_xcor == 300 or ncur_xcor == -300:
		player.setposition(0,0)
	if ncur_ycor == 300 or ncur_ycor == -300:
		player.setposition(0,0)

	pointxcor = point.xcor()
	pointycor = point.ycor()
#checks if position of player and point and/DIY collision then gains point and start point anim and respawns point.
	if ncur_xcor == pointxcor and ncur_ycor == pointycor:
		print("Gained a point!")
		score = score + 1
		point_anim()
		spawn_point()

#moves player right and checks for point collision
def move_right():
	global score
	cur_xcor = player.xcor()
	cur_ycor = player.ycor() 
	player.setposition(cur_xcor+100,cur_ycor)
	ncur_xcor = player.xcor()
	ncur_ycor = player.ycor()
#border, returns player back to spawn
	if ncur_xcor == 300 or ncur_xcor == -300:
		player.setposition(0,0)
	if ncur_ycor == 300 or ncur_ycor == -300:
		player.setposition(0,0)

	pointxcor = point.xcor()
	pointycor = point.ycor()
#checks if position of player and point and/DIY collision then gains point and start point anim and respawns point.
	if ncur_xcor == pointxcor and ncur_ycor == pointycor:
		print("Gained a point!")
		score = score + 1
		point_anim()
		spawn_point()

# spawns the bullets in a random position on the right hand side of the border.
def spawn_bullet(bullet):
	
	spawn_pos = rand.randint(1,5)
	if spawn_pos == 1:
		bullet.hideturtle()
		bullet.setposition(300,0)
		bullet.showturtle()
		move_bullet(bullet)
		
	if spawn_pos == 2:
		bullet.hideturtle()
		bullet.setposition(300,200)
		bullet.showturtle()
		move_bullet(bullet)
	
	if spawn_pos == 3:
		bullet.hideturtle()
		bullet.setposition(300,100)
		bullet.showturtle()
		move_bullet(bullet)
	
	if spawn_pos == 4:
		bullet.hideturtle()
		bullet.setposition(300,-100)
		bullet.showturtle()
		move_bullet(bullet)
	
	if spawn_pos == 5:
		bullet.hideturtle()
		bullet.setposition(300,-200)
		bullet.showturtle()
		move_bullet(bullet)

#spawns a random amount of bullets according to the difficulty.

def get_bullets():

	num_of_bullets = rand.randint(min_bullets, max_bullets)
	for i in range(num_of_bullets):
		bullet = trtl.Turtle()
		bullet_list.append(bullet)
		bullet.penup()
		bullet.shape("bullet.gif")
		spawn_bullet(bullet)

#spawns the point in a somewhat random position
def spawn_point():

	random_pos = rand.randint(1,4)
	if random_pos == 1:
		point.setposition(-200,200)
	if random_pos == 2:
		point.setposition(200,-200)
	if random_pos == 3:
		point.setposition(200,200)
	if random_pos == 4:
		point.setposition(-200,-200)
	
	

# makes a red border telling you the boundaries of movement.
def make_border():
	writer.speed(0)
	writer.pencolor("Red")
	writer.penup()
	writer.setposition(300,-300)
	writer.pendown()
	for x in range(2):
		writer.left(90)
		writer.forward(600)
		writer.left(90)
		writer.forward(600)
	writer.hideturtle()
	writer.penup()

# writes the total points the player has gained/GAME OVER screen.
def game_over():
	writer.clear()
	player.speed(0)
	player.setposition(10000,10000)
	writer.setposition(-150,0)
	writer.write("GAME OVER! YOU LOSE!", font=("Arial", 25, "bold"))
	time.sleep(5)
	writer.clear()
	writer.write("You earned: "+str(score)+ " points!", font=("Arial", 25, "bold"))

#makes the point grow and change color.
def point_anim():
	global color_list
	if len(color_list) != 0:
		chosen_color_index = rand.randint(0,len(color_list))
		point.turtlesize(2)
		color = color_list[chosen_color_index]
		point.color(color)
		time.sleep(.1)
		point.turtlesize(1.5)
		point.color("yellow")
		time.sleep(.1)
		point.color(color)
		point.turtlesize(1)
		time.sleep(.1)
		point.color("Yellow")
	elif len(color_list) == 0:
		color_list.append("red")
		color_list.append("blue")
		color_list.append("purple")
		color_list.append("green")
		color_list.append("orange")
		point_anim()
		
	
#----event/calls----

#listens for movement then activates the move functions accordingly.

make_border()
writer.setposition(0,350)
wn.setup(750,750)

wn.onkey(move_forward, 'w')
wn.onkey (move_backward, 's')
wn.onkey(move_left, 'a')
wn.onkey(move_right, 'd')
wn.listen()

random_char()
pick_difficulty()
time.sleep(5)
spawn_point()
get_bullets()




wn.mainloop()
