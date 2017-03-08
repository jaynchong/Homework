import simplegui

num = 0 

def create_timer(time):
	global num
	num = num + 1

def draw_handler(canvas): 
	global num
	canvas.draw_text(str(num),(40,40), 20,"Red")

def button_stop(): 
	timer.stop()

def button_start(): 
	timer.start()

def button_reset():
	timer.reset()

def format(t):
	t = int


frame = simplegui.create_frame("Stopwatch",100,100)
button1 = frame.add_button("Stop", button_stop, 100)
button2 = frame.add_button("Start", button_start, 100)
button3 = frame.add_button("Reset", button_reset, 100)
timer=simplegui.create_timer(100,create_timer)
frame.set_draw_handler(draw_handler)
frame.start()

