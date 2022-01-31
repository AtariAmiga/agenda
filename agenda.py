# pip install reportlab
import datetime
import locale

from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics

A4_landscape = tuple(reversed(A4))
c = canvas.Canvas("hello.pdf", pagesize=A4_landscape)

width = A4_landscape[0]
height = A4_landscape[1]

x = c.getAvailableFonts()
# ['Courier', 'Courier-Bold', 'Courier-BoldOblique', 'Courier-Oblique',
# 'Helvetica', 'Helvetica-Bold', 'Helvetica-BoldOblique', 'Helvetica-Oblique',
# 'Symbol', 'Times-Bold', 'Times-BoldItalic', 'Times-Italic', 'Times-Roman', 'ZapfDingbats']
# =>
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

font_name = 'Garamond'
font_file = 'GARA.TTF'
pdfmetrics.registerFont(TTFont(font_name, font_file))

locale.setlocale(locale.LC_ALL, 'fr_FR.utf8')
now = datetime.datetime.today()

inner_margin = 30
right_page = False
if right_page:
    c.translate(inner_margin, 0)
col_width = (width - inner_margin) / 3.0
margin = 5
for i in range(1, 3):
    x = i * col_width
    c.line(x, margin, x, height - margin)

nbr_lines = 30
top = 50
line_height = (height - top) / nbr_lines
matter_ratio = 5

def font_ascent(c):
    face = pdfmetrics.getFont(c._fontname).face
    return (face.ascent * c._fontsize) / 1000.0

c.setLineWidth(0.1)
for i in range(0, 3):
    x = i * col_width
    date = now + datetime.timedelta(days=i)
    num_day = date.strftime('%d') # https://docs.python.org/fr/3.6/library/datetime.html#strftime-strptime-behavior
    day = date.strftime('%A').upper() # https://docs.python.org/fr/3.6/library/datetime.html#strftime-strptime-behavior

    c.setFont(font_name, 40)
    c.drawString(x + margin, height - font_ascent(c) - margin, num_day)
    c.setFont(font_name, 25)
    c.drawRightString(x + col_width - margin, height - font_ascent(c) - margin, day)

    for j in range(1, nbr_lines):
        y = line_height * j
        c.line(x + margin, y, x + col_width / matter_ratio - 2, y)
        c.line(x + col_width / matter_ratio + 2, y, x + col_width - margin, y)


c.showPage()
c.save()