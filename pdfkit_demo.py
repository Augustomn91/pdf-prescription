import pdfkit

try:
    options_value = {
        'page-size': 'A4',
        'orientation': 'landscape',
        'margin-top': '0.45in',
        'margin-right': '0.45in',
        'margin-left': '0.45in',
        'margin-bottom': '0.45in',
    }

    pdf_file = pdfkit.from_file('pdf_scheme.html', 'out.pdf', options=options_value)


except OSError:
    pass

