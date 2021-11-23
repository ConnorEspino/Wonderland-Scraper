from requests_html import HTMLSession
import csv
import time

def __init__():
    #TODO: Error handling for improper URL/Public keys
    #TODO: Allow option to output to google docs? If possible
    file = open("pubkey.txt", "r")

    #Read the public key from the first line of the pubkey file
    url = 'https://snowtrace.io/token/0x136acd46c134e8269052c62a67042d6bdedde3c9?a=' + file.readline()
    file.close()

    session = HTMLSession()

    #Open the webpage and search for the right place to find balance
    r = session.get(url)
    container = r.html.find('div.col-md.u-ver-divider.u-ver-divider--left.u-ver-divider--none-md', first = True).text

    #Remove unnecessary strings and cast as float
    balance = container.replace("Balance\n", "")
    balance = balance.replace(",", "")
    balance = (float) (balance.replace(" MEMO", ""))

    #Get current price of TIME
    r = session.get('https://coinmarketcap.com/currencies/wonderland/')
    priceString = r.html.find('div.priceValue')[0].text

    #Create a float representation of current price
    currPrice = priceString.replace("$", "")
    currPrice = (float) (currPrice.replace(",", ""))

    try:
        with open('output.csv', 'r') as file:
            #If the fle does exist, read the inital investment value on row 2
            reader = csv.reader(file, delimiter = ",")
            next(reader)
            initialInvestment = next(reader)[3]
            print(initialInvestment)
            file.close()

    except FileNotFoundError:
        #If the file doesn't exist, create it and set up header rows
        with open('output.csv', 'w', newline = '') as file:
            writer = csv.writer(file, delimiter = ",")
            writer.writerow(["Timestamp","TIME Price","Amount of TIME","Value of TIME","ROI"])
            #set the intial investment equal to the current value
            initialInvestment = round(currPrice*balance, 2)
            file.close()


    #Append the new row of data to the file
    with open('output.csv', 'a', newline = '') as file:
        writer = csv.writer(file, delimiter = ",")
        writer.writerow([time.ctime(time.time()),str(priceString),str(round(balance, 5)),"$" + str(round(currPrice*balance, 2)),str(round(((currPrice*balance)-initialInvestment)/initialInvestment, 2)) + "%"])
        file.close()
__init__()