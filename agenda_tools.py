from reportlab.pdfbase import pdfmetrics

def font_ascent(c):
    face = pdfmetrics.getFont(c._fontname).face
    return (face.ascent * c._fontsize) / 1000.0

def draw_header(canvas, x, date, gs):
    # https://docs.python.org/fr/3.6/library/datetime.html#strftime-strptime-behavior
    col_width = (gs.width - gs.inner_margin) / 3.0

    num_day = date.strftime('%#d') # '#' gets rid of the leading zero (Windows only)
    canvas.setFont(gs.font_name, 60)
    canvas.drawString(x + gs.margin, gs.height - font_ascent(canvas) - gs.margin, num_day)

    day_name = date.strftime('%A').upper()
    canvas.setFont(gs.font_name, 20)
    a = font_ascent(canvas)
    canvas.drawRightString(x + gs.col_width() - gs.margin, gs.height - gs.margin - a, day_name)

    month_and_year = date.strftime('%B %Y')
    canvas.setFont(gs.font_name, 12)
    canvas.drawRightString(x + col_width - gs.margin, gs.height - gs.margin - 2 * a, month_and_year)


def draw_lines(canvas, x, gs):
    for j in range(1, gs.nbr_lines):
        canvas.setLineWidth(0.1)
        y = gs.line_height() * j
        canvas.line(x + gs.margin, y, x + gs.col_width() / gs.matter_ratio - 2, y)
        canvas.line(x + gs.col_width() / gs.matter_ratio + 2, y, x + gs.col_width() - gs.margin, y)
