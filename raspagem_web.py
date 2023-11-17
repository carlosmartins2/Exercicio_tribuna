from bs4 import BeautifulSoup
import requests

manchetes=[]

url = 'https://tribunademinas.com.br/noticias/cultura'
resp = requests.get(url)

if resp.status_code != 200:
    print('Erro ao conectar ao site, tente novamente mais tarde!')

else:
    html_content = resp.text
    
    soup = BeautifulSoup(html_content, 'html.parser')
    
    main = soup.find('main')

    row1 = main.find_all('div' ,class_="row")
    sm57 = row1[1].find('div' ,class_="col-sm-8")
    
    row2 = sm57.find_all('div' ,class_="row")
    
    for row in row2:
        h2 = row.find('h2')
        if h2:
            materia=[h2.text]
            p = row.find('p' ,class_="excerpt")
            materia.append(p.text)
            manchetes.append(materia)

    for manchete in manchetes:
        print(manchete)
