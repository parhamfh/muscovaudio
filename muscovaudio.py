#!/usr/local/bin/python

import sys

import pygame
from pygame import Surface
from pygame.font import Font
from pygame.locals import KEYDOWN, K_ESCAPE

class Colour(object):
	BLACK = (0, 0, 0)
	WHITE = (255, 255, 255)
	BLUE = (0, 0, 255)
	AQUAMARINE = (127 ,255, 212)
	CHOCOLATE = (255, 127, 36)
	TURQUOISE = (0, 245, 255)
	
class Muscovaudio(object):
	def __init__(self):
		print "running"
		self.canvas_width =630
		self.canvas_height = 470
		self.run()
	
	def draw(self):
		
		self.canvas.draw_content()
		self.window.blit(self.canvas, (5,5))
	
	def run(self):
		# Initialize pygame
		pygame.init()
			
		# Pygame.display stuff
		pygame.display.set_caption('MUSCOVAUDIO')
		
		# Create canvas
		self.canvas = Canvas(self.canvas_width, self.canvas_height, Colour.BLACK)
		
		# Create & init application Window 
		self.window = Window()
		self.window.init_window()
		
		# Init MouseHandler against our canvas
		mh = MouseHandler(self.canvas)
		
		# Update the pygame display
		self.draw()
		pygame.display.update()		
		
		while True:
				# Check events
				events = pygame.event.get()
				for e in events:
					mh.handle_event(e)
					
					if e.type == KEYDOWN:
						# Check if user has aborted
						if e.key == K_ESCAPE:
							pygame.quit()
							sys.exit(0)
							
				# Update the pygame display
				self.draw()
				pygame.display.update()
				
class Canvas(Surface):
	
	def __init__(self, width, height, color):
		super(Canvas, self).__init__((width, height))
		
		# Canvas for temporary lines
		self.work_canvas = Surface((width, height)) 
		self.color = color
		self.work_canvas.set_colorkey(color)
		
		# Canvas for drawn lines 
		self.line_canvas = Surface((width, height))

		# List of lines
		self.lines = []
		
		# Mouse info text position
		self.mouse_info_x = 0
		self.mouse_info_y = 0
		self.mouse_canvas = Surface ((200,100))
		
		# Mouse canvas
		self.mouse_canvas.set_colorkey(color)
		
	def draw_measuring_line(self,start,end):
		# Erase old measuring line
		self.work_canvas.fill(self.color)
		# Draw new measuring line
		pygame.draw.line(self.work_canvas, Colour.AQUAMARINE, start, end)
	
	def draw_line(self,start,end):
		# Draw an actual, permanent line and erase measuring line
		self.work_canvas.fill(self.color)
		pygame.draw.line(self.line_canvas, Colour.TURQUOISE, start, end,5)
	
	def draw_mouse_info(self, message, dragging=False):
		# Empty mouse canvas
		self.mouse_canvas.fill(self.color)
		# Create font and blit onto canvas
		font = Font(None, 22)
		mouse_info = font.render(message, 1, Colour.WHITE, Colour.BLUE)
		self.mouse_canvas.blit(mouse_info, (self.mouse_info_x, self.mouse_info_y))
		
		# If Mouse is dragging, notify
		if dragging:
			ti = Font(None, 30).render("DRAGGING",1,Colour.CHOCOLATE, Colour.WHITE)
			self.mouse_canvas.blit(ti, (self.mouse_info_x, self.mouse_info_y+20))
	
	def draw_content(self):
		# Draw the stuff on the canvas 
		self.blit(self.line_canvas,(0,0))
		self.blit(self.work_canvas,(0,0))
		self.blit(self.mouse_canvas,(self.get_width()-240,self.get_height()-80))
	
class Window(object):
	
	def __init__(self, width=640, height=480, bkg_color=Colour.WHITE):
		self.width = width
		self.height = height
		self.background_color = bkg_color
		self.window = None
		self.init_window()
		
	def init_window(self):
		self.window = pygame.display.set_mode((self.width,self.height))
		self.window.fill(self.background_color)
		
	def change_background_color(self, r_g_b):
		self.window.fill(r_g_b)
	
	def blit(self, canvas, pos):
		self.window.blit(canvas, pos)

class MouseHandler(object):
	
	BUTTONS = {1:"Left Button", 3:"Right Button"}

	def __init__(self, canvas):
		
		self.canvas = canvas
		
		# Mouse states
		self.mouse_down = False
		self.mouse_button = 0
		
		# Mouse action 
		self.dragging = False
		self.drag_start_x = 0
		self.drag_start_y = 0
		self.drag_end_x = 0
		self.drag_end_y = 0
		
	def handle_event(self, event):
		# Get mouse position
		(self.x, self.y) = pygame.mouse.get_pos()
		
		# Check if the event is mouse-related
		if event.type == pygame.MOUSEBUTTONDOWN:
			self.mouse_down = True
			self.mouse_button = self.BUTTONS[event.button]  
				
		elif event.type == pygame.MOUSEBUTTONUP:
			self.mouse_down = False
			self.mouse_button = self.BUTTONS[event.button]
		
		self.measure_line()
		# Write out mouse info
		self.write_mouse_info()
	
	@property
	def left_button_pressed(self):
#		print self.mouse_button == "Left Button"
		return self.mouse_button == "Left Button"
	
	def measure_line(self):
		if not self.dragging and self.mouse_down and self.left_button_pressed:
			self.drag_start_x = self.x
			self.drag_start_y = self.y
			self.drag_end_x = self.x
			self.drag_end_y = self.y
			self.dragging = True
			
		elif self.dragging and self.mouse_down and self.left_button_pressed:
			self.drag_end_x = self.x
			self.drag_end_y = self.y 
			self.canvas.draw_measuring_line((self.drag_start_x,self.drag_start_y),(self.drag_end_x, self.drag_end_y))
		
		elif self.dragging and not self.mouse_down and self.left_button_pressed:
			self.dragging = False
			self.canvas.draw_line((self.drag_start_x,self.drag_start_y),(self.drag_end_x, self.drag_end_y))
			
	def write_mouse_info(self):
		
		# Build string
		message = "x = %s "\
				  "y = %s"%(self.x, self.y)
		
		# If key pressed add that info
		if self.mouse_down:
			message = message + " %s"%self.mouse_button

		# Draw Mouse info on canvas
		self.canvas.draw_mouse_info(message,self.dragging)		

class Ball(object):

	def __init__(self, x_init, y_init, r, vel=0):
		self.x = x_init
		self.y = y_init
		self.radius = r
		self.velocity = vel


if __name__ == "__main__":
	muscovaudio = Muscovaudio()
	