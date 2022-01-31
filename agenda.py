# pip install reportlab
import datetime
import locale

from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4

A4_landscape = tuple(reversed(A4))
c = canvas.Canvas("hello.pdf", pagesize=A4_landscape)

width = A4_landscape[0]
height = A4_landscape[1]

locale.setlocale(locale.LC_ALL, 'fr_FR.utf8')
now = datetime.datetime.today()

col_width = width / 3.0
for i in range(1, 3):
    x = i * col_width
    c.line(x, 0, x, height)

nbr_lines = 20
top = 50
line_height = (height - top) / nbr_lines
for i in range(0, 3):
    x = i * col_width
    date = (now + datetime.timedelta(days=i)).strftime('%A %d %B %Y') # https://docs.python.org/fr/3.6/library/datetime.html#strftime-strptime-behavior
    c.drawCentredString(x + col_width/2, height - top, date)
    for j in range(0, nbr_lines):
        y = line_height * j
        c.line(x + 5, y, x + col_width/4 - 2, y)
        c.line(x + col_width/4 + 2, y, x + col_width - 5, y)


c.showPage()
c.save()