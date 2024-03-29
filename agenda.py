# pip install reportlab
import datetime
import locale

from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4

from agenda_tools import draw_header, draw_lines, draw_vertical_separators, font_ascent

vertical = False

page_format = A4 if vertical else tuple(reversed(A4))
c = canvas.Canvas("agenda filles " + ('vertical' if vertical else 'horizontal') + ".pdf", pagesize=page_format)

width = page_format[0]
height = page_format[1]

# x = c.getAvailableFonts()
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
        self.line_height = 18
        self.top_margin = 60

    def col_width(self):
        return (self.page_width - self.inner_margin) / 3.0

gs = GlobalSettings(page_format)
pdfmetrics.registerFont(TTFont(gs.font_name, gs.font_file))

start = datetime.datetime(2022, 8, 29)
end = datetime.datetime(2023, 7, 9)

# First page
c.setFont(gs.font_name, 80)
a = font_ascent(c)
c.drawCentredString(gs.page_width/2, gs.page_height/2 - a/2, str(start.year) + ' - ' + str(end.year))
c.drawImage('logo.jpg', x=10, y=-60, width=200, preserveAspectRatio=True)  # todo: pourquoi y=-60 pour que ce soit en bas?!
c.showPage()


def tutu(year, week_num):
    monday = datetime.date.fromisocalendar(year, week_num, 1)
    for week_part in [0, 1]:
        c.translate(week_part * gs.inner_margin, 0)
        draw_vertical_separators(c, gs)
        for day in range(0, 3 + week_part):
            x = min(day, 2) * gs.col_width()
            # if week_part == 1 and day == 2: continue
            date = monday + datetime.timedelta(days=day + week_part * 3)

            y_top = gs.page_height / (1 if day < 3 else 2)
            y_bottom = gs.page_height / 2 if week_part == 1 and day == 2 else 0

            draw_header(c, x, y_top, date, gs)

            draw_lines(c, x, y_top - 60, y_bottom, gs)
        c.showPage()


for week_num in range(start.isocalendar().week, 53): # todo: faire mieux que cette astuce / wee
    tutu(start.year, week_num)
for week_num in range(1, end.isocalendar().week + 1):
    tutu(end.year, week_num)

c.save()