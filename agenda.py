# pip install reportlab
import datetime
import locale

from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4

from agenda_tools import draw_header, draw_lines, draw_vertical_separators

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

class GlobalSettings():
    def __init__(self, page_setting):
        self.inner_margin = 40

        self.margin = 15
        self.page_width = page_setting[0]
        self.page_height = page_setting[1]
        self.font_name = 'Garamond'
        self.font_file = 'GARA.TTF'
        self.matter_ratio = 4.5
        self.nbr_lines = 30
        self.top_margin = 60

    def col_width(self):
        return (self.page_width - self.inner_margin) / 3.0

    def line_height(self):
        return (self.page_height - self.top_margin) / self.nbr_lines

gs = GlobalSettings(A4_landscape)
pdfmetrics.registerFont(TTFont(gs.font_name, gs.font_file))

c.showPage()  # First page, empty, but we should print "Année 2021-2022"
for week_num in range(1, 53):
    monday = datetime.date.fromisocalendar(2022, week_num, 1)

    for week_part in [0, 1]:
        c.translate(week_part*gs.inner_margin, 0)
        draw_vertical_separators(c, gs)
        for day in [0, 1, 2]:
            x = day * gs.col_width()
            # if week_part == 1 and day == 2: continue
            date = monday + datetime.timedelta(days=day + week_part * 3)

            draw_header(c, x, date, gs)
            draw_lines(c, x, gs)
        c.showPage()
c.save()