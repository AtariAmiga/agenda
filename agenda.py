# pip install reportlab

from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4

A4_landscape = tuple(reversed(A4))
c = canvas.Canvas("hello.pdf", pagesize=A4_landscape)

width = A4_landscape[0]
height = A4_landscape[1]

col_width = width / 3.0
for i in range(1, 3):
    x = i * col_width
    c.line(x, 0, x, height)

for i in range(0, 3):
    x = i * col_width
    c.drawCentredString(x + col_width/2, height - 50, "Hello World")

c.showPage()
c.save()