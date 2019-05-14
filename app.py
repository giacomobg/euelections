from flask import Flask
from bs4 import BeautifulSoup
app = Flask(__name__)

@app.route('/')
def show_ui():
    print('hi')
    with open('main.html', 'rb') as html_file:
        html = html_file.read()
    soup = BeautifulSoup(html)
    # create table
    header_names = ['Region', 'Conservative', 'Labour', 'Liberal Democrats', 'Greens', 'Brexit Party', 'Change UK', 'SNP/Plaid Cymru', 'UKIP']
    table = soup.new_tag('table')
    header = [soup.new_tag('th').append(h) for h in header_names]
    header_tag = soup.new_tag('thead').append(soup.new_tag('tr').extend(header))
    table.append(header_tag)

    soup.body.p.append(table)
    return str(soup)

if __name__ == '__main__':
    pass