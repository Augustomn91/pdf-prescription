import pdfkit

try:
    options_value = {
        'page-size': 'A4',
        'margin-top': '0.45in',
        'margin-right': '0.45in',
        'margin-left': '0.45in',
        'margin-bottom': '0.45in',
    }

    pdf_file = pdfkit.from_file('pdf_evolucao.html', 'evo.pdf', options=options_value)


except OSError:
    pass