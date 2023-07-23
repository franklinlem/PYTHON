from urllib.request import urlopen

def codigofonte(url):
    pagina = urlopen(url)
    html = pagina.read()
    return html.decode()

html = codigofonte('http://www.delegaciaeletronica.policiacivil.sp.gov.br')
print(html)
