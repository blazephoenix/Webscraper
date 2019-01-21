from flask import Flask, render_template
from bs4 import BeautifulSoup
import requests

source = requests.get('https://medium.com/@naik.tanmay283').text

soup = BeautifulSoup(source, 'lxml')

""" profile = soup.div.h1.text
desc = soup.div.p.text
img_src = soup.find('img')['src']
img_id = img_src.split('/')[7]
img_link = f'https://miro.medium.com/fit/c/240/240/{img_id}'
 """

app = Flask(__name__)
@app.route('/')
def index():
    profile = soup.div.h1.text
    desc = soup.div.p.text
    img_src = soup.find('img')['src']
    img_id = img_src.split('/')[7]
    img_link = f'https://miro.medium.com/fit/c/240/240/{img_id}'

    return render_template('index.html', **locals())

app.run(debug=True)
