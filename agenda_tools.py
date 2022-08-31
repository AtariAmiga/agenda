from reportlab.pdfbase import pdfmetrics


def font_ascent(c):
    face = pdfmetrics.getFont(c._fontname).face
    return (face.ascent * c._fontsize) / 1000.0


def draw_vertical_separators(c, gs):
    c.setLineWidth(0.5)
    for i in range(1, 3):
        x = i * gs.col_width()
        c.line(x, gs.margin, x, gs.page_height - gs.margin)


def draw_header(canvas, x, y_top, date, gs):
    # https://docs.python.org/fr/3.6/library/datetime.html#strftime-strptime-behavior
    col_width = (gs.page_width - gs.inner_margin) / 3.0

    num_day = date.strftime('%#d') # '#' gets rid of the leading zero (Windows only)
    canvas.setFont(gs.font_name, 50)
    canvas.drawString(x + gs.margin, y_top - font_ascent(canvas) - gs.margin, num_day)

    day_name = date.strftime('%A').upper()
    canvas.setFont(gs.font_name, 20)
    a = font_ascent(canvas)
    canvas.drawRightString(x + gs.col_width() - gs.margin, y_top - gs.margin - a, day_name)

    month_and_year = date.strftime('%B %Y')
    canvas.setFont(gs.font_name, 12)
    canvas.drawRightString(x + col_width - gs.margin, y_top - gs.margin - 2 * a, month_and_year)


def draw_lines(canvas, x, y_top, y_bottom, gs):
    space = 4
    canvas.setLineWidth(0.1)

    j = 1
    while True:
        y = y_top - gs.line_height * j
        if y < y_bottom + gs.line_height/2: break
        canvas.line(x + gs.margin, y, x + gs.col_width() / gs.matter_ratio - space, y)
        canvas.line(x + gs.col_width() / gs.matter_ratio + space, y, x + gs.col_width() - gs.margin, y)
        j  += 1
