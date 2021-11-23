from requests_html import HTMLSession

#Read from URL file later
session = HTMLSession()
url = 'https://snowtrace.io/token/0xfe8eb55d570e679b02b56e81ea9cba2847d75324?a=0x689f45d3ff4f72f49248b7b0188c3b39e182d0c7'

r = session.get(url)
container = r.html.find('div.col-md.u-ver-divider.u-ver-divider--left.u-ver-divider--none-md', first = True).text

#Remove unnecessary strings and cast as float
balance = container.replace("Balance\n", "")
balance = balance.replace(",", "")
balance = (float) (balance.replace(" MEMO", ""))

print(balance)