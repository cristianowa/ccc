#!/usr/bin/python
from pptx import Presentation

prs = Presentation()

def title_slide(presentation,title,subtitle = ""):
	slide = prs.slides.add_slide(prs.slide_layouts[0])
	slide.shapes.title.text = title
	slide.placeholders[1].text = subtitle

def add_bullet_slide(presentation,bullets_text):
	slide = prs.slides.add_slide(prs.slide_layouts[1])
	slide.shapes.title.text = 'Adding a Bullet Slide'
	tf = slide.shapes.placeholders[1].textframe
	paragraph = tf
	for i in bullets_text:
		paragraph.text = i
		paragraph = tf.add_paragraph()
#	tf.text = 'Find the bullet slide layout'

title_slide(prs,"teste","so um testezinho")
add_bullet_slide(prs,["um","dois","tres"])
add_bullet_slide(prs,["1","2","3"])

prs.save('test.pptx')
