from requests_html import HTMLSession

#Read from URL file later
session = HTMLSession()
url = 'https://snowtrace.io/token/0x136Acd46C134E8269052c62A67042D6bDeDde3C9?a=0xE840E73aE7087D2A582B8fE56caC95b624a71D82'

r = session.get(url)
container = r.html.find('div.col-md.u-ver-divider.u-ver-divider--left.u-ver-divider--none-md', first = True).text

#Remove unnecessary strings and cast as float
balance = container.replace("Balance\n", "")
balance = float(balance.replace(" MEMO", ""))

print(balance)