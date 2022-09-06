from email.mime import image
import time
from reportlab.lib.enums import TA_JUSTIFY
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch

import letter_funcs as lf

doc = SimpleDocTemplate("letter.pdf",pagesize=letter,
                        rightMargin=72,leftMargin=72,
                        topMargin=72,bottomMargin=18)

def generate_letter():
    
    Story = []

    image_info = lf.obtain_image()
    news_list = lf.get_news()
    celestials = lf.get_celestial_events()

    if type(image_info) != int and type(news_list) != int and type(celestials) != int:
        
        # Adding paragraph styles

        styles = getSampleStyleSheet()
        styles.add(ParagraphStyle(name='Arial', alignment=TA_JUSTIFY))

        ptext = "<font face = 'times' color = 'red' size = 15> <b>" + "NASA Image Of The Day" + "</b></font>"
        
        Story.append(Paragraph(ptext, styles['Normal']))
        Story.append(Spacer(1,12))
        Story.append(Spacer(1,12))

        # Adding Daily Image of the Day
        im = Image('image.png', 3 * inch , 2 * inch)
        Story.append(im)

        Story.append(Spacer(1,12))
        
        #Adding Image Title
        ptext = "<b>Title : </b>" + image_info['title']
        Story.append(Paragraph(ptext, styles['Normal']))
        Story.append(Spacer(1,12))

        #Adding Image Explanation:
        ptext = "<b>Explanation : </b>" + image_info['explanation']
        Story.append(Paragraph(ptext, styles['Normal']))
        Story.append(Spacer(1,12))
        ptext = '<u><link href = "' + image_info['url'] + '"> <font color = "blue">' + 'Check it out here!' + '</font></link></u>'
        Story.append(Paragraph(ptext, styles['Normal']))

        Story.append(Spacer(1,12))
        Story.append(Spacer(1,12))

        #Adding Headlines

        #Adding headline title
        ptext = "<font face = 'times' color = 'red' size = 15> <b>" + "Today's Stories" + "</b></font>"
        Story.append(Paragraph(ptext, styles['Normal']))
        Story.append(Spacer(1,12))

        #Adding first headline
        ptext = "<u><b><font color = 'blue'>" + '<link href= "' + news_list[0][1] +'">' + news_list[0][0] + "</link></font></b></u>"
        Story.append(Paragraph(ptext, styles['Normal']))
        Story.append(Spacer(1,12))

        #Adding second headline
        ptext = "<u><b><font color = 'blue'>" + '<link href= "' + news_list[1][1] +'">' + news_list[1][0] + "</link></font></b></u>"
        Story.append(Paragraph(ptext, styles['Normal']))
        Story.append(Spacer(1,12))
        
        #Adding third headline
        ptext = "<u><b><font color = 'blue'>" + '<link href= "' + news_list[2][1] +'">' + news_list[2][0] + "</link></font></b></u>"
        Story.append(Paragraph(ptext, styles['Normal']))
        Story.append(Spacer(1,12))
        Story.append(Spacer(1,12))

        #Adding Celestial events stuff
        ptext = "<font face = 'times' color = 'red' size = 15> <b>" + "What to look out for tonight!" + "</b></font>"
        Story.append(Paragraph(ptext, styles['Normal']))
        Story.append(Spacer(1,12))
        ptext = "<u><b><font color = 'blue'>" + '<link href= "' + celestials[1] +'">' + celestials[0] + "</link></font></b></u>"
        Story.append(Paragraph(ptext, styles['Normal']))
        Story.append(Spacer(1,12))
        Story.append(Spacer(1,12))
        Story.append(Spacer(1,12))
        Story.append(Spacer(1,12))
        ptext = "<font face = 'Helvetica'> Hope to see you tomorrow! </font>"
        Story.append(Paragraph(ptext, styles['Normal']))


        doc.build(Story)

generate_letter()



