from apscheduler.schedulers.blocking import BlockingScheduler
from requests_html import HTMLSession
import time
import csv

def outputToFile(fileNum, pubKey):
    url = "https://snowtrace.io/token/0x136acd46c134e8269052c62a67042d6bdedde3c9?a=" + pubKey
    session = HTMLSession()
    
    url = url.replace("\n", "");

    #Open the webpage and search for the right place to find balance
    r = session.get(url)
    container = r.html.find('#ContentPlaceHolder1_divFilteredHolderBalance.col-md.u-ver-divider.u-ver-divider--left.u-ver-divider--none-md', first = True).text

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

    outputFile = "output" + str(fileNum) + ".csv"

    try:
        with open(outputFile, 'r') as file:
            #If the fle does exist, read the inital investment value on row 2
            reader = csv.reader(file, delimiter = ",")
            next(reader)
            #Gets the initial investment from the first non-header row and formats it as float
            initialInvestment = (next(reader)[3].replace("$", ""))
            initialInvestment = (float) (initialInvestment.replace(",", ""))
            file.close()

    except FileNotFoundError:
        #If the file doesn't exist, create it and set up header rows
        with open(outputFile, 'w', newline = '') as file:
            writer = csv.writer(file, delimiter = ",")
            writer.writerow(["Timestamp","TIME Price","Amount of TIME","Value of TIME","ROI"])
            #set the intial investment equal to the current value
            initialInvestment = round(currPrice*balance, 2)
            file.close()


    #Append the new row of data to the file
    with open(outputFile, 'a', newline = '') as file:
        writer = csv.writer(file, delimiter = ",")
        writer.writerow([time.ctime(time.time()),str(priceString),str(round(balance, 5)),"$" + str(round(currPrice*balance, 2)),str(round((((currPrice*balance)-initialInvestment)/initialInvestment) * 100, 2)) + "%"])
        file.close()

def main():
    print(time.ctime())

    #Read the public key from the first line of the pubkey file
    file = open("pubkey.txt", "r")
    count = 0

    #Output info of each key to output file
    while 1:
        count += 1
        key = file.readline()
        if not key:
            break
        outputToFile(count, key)

    file.close()

main()

#Scheduler for running main every 8 hours
scheduler = BlockingScheduler()

scheduler.add_job(main, 'interval', hours = 8)

try:
        scheduler.start()
except (KeyboardInterrupt, SystemExit):
    pass
