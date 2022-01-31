# pip install reportlab
import datetime
import locale

from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4

from agenda_tools import draw_header, draw_lines

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

locale.setlocale(locale.LC_ALL, 'fr_FR.utf8')
now = datetime.datetime.today()

class GlobalSettings():
    def __init__(self, page_setting):
        self.inner_margin = 40

        self.margin = 10
        self.width = page_setting[0]
        self.height = page_setting[1]
        self.font_name = 'Garamond'
        self.font_file = 'GARA.TTF'
        self.matter_ratio = 5
        self.nbr_lines = 30
        self.top = 50

    def col_width(self):
        return (self.width - self.inner_margin) / 3.0

    def line_height(self):
        return (self.height - self.top) / self.nbr_lines

gs = GlobalSettings(A4_landscape)

pdfmetrics.registerFont(TTFont(gs.font_name, gs.font_file))

right_page = False
if right_page:
    c.translate(gs.inner_margin, 0)

c.setLineWidth(0.5)
for i in range(1, 3):
    x = i * gs.col_width()
    c.line(x, gs.margin, x, gs.height - gs.margin)

for i in range(0, 3):
    x = i * gs.col_width()
    date = now + datetime.timedelta(days=i)

    draw_header(c, x, date, gs)
    draw_lines(c, x, gs)

c.showPage()
c.save()