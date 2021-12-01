# Wonderland Scraper

### Goal
To create a web scraper that tracks and evaluates different, wanted values of investment status.

### Usage
Copy your MetaMask public key for the wallet that contains the `AVAX` and `MEMO` tokens and paste it in the `pubkeys.txt` text file. There may be one public key on each line of the text file. You may place as many keys as you want to keep track of. Leave no whitespace at the end of the file or in-between the public keys.

From the directory containing all source files, run the scraper file using the following command:

```python Scraper.py```

The program will run in the terminal and update the output spreadsheets every 8 hours.
To exit the program, either press `Ctrl + C` in the terminal window or close the terminal window.

### Results
The program will output `n` output files, where n is the number of public keys listed in the text file `pubkeys.txt`. Each output file will have a number associated with it. This number refers to which line the public key is on in the `pubkeys.txt` text file.
