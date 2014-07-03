#!/usr/bin/python
from pptx import Presentation
import sys
import random

from pptx.enum.shapes import MSO_SHAPE
prs = Presentation()

def title_slide(presentation,title,subtitle = ""):
	slide = prs.slides.add_slide(prs.slide_layouts[0])
	slide.shapes.title.text = title
	slide.placeholders[1].text = subtitle

def add_bullet_slide(presentation,title,bullets_text):
	slide = prs.slides.add_slide(prs.slide_layouts[1])
	slide.shapes.title.text = title
	tf = slide.shapes.placeholders[1].textframe
	paragraph = tf
	for i in bullets_text:
		paragraph.text = i
		paragraph = tf.add_paragraph()
#	tf.text = 'Find the bullet slide layout'

source = open(sys.argv[1],"r")

lines = source.readlines()
title_slide(prs,lines[0],lines[1])
lines = lines[2:len(lines)]
for i in range(len(lines)):
	lines[i] = lines[i].replace("\n","")
	print lines[i]
print lines
questions = []
for l in range(len(lines)/5):
	questions.append((lines[l*5],lines[l*5+1:l*5+5]))
#	print " >>>> " +  lines[l*5]
#	for i in lines[l*5+1:l*5+5]:
#		print i
random.shuffle(questions)
for q in questions:
	right = q[1][0]
	random.shuffle(q[1])
	for i in range(len(q[1])):
		if q[1][i] == right:
			print right + " is at " + str(i+1)
#	print q[1]
	add_bullet_slide(prs,q[0],q[1])

prs.save('test.pptx')
