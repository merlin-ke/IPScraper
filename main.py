from IPScraper import IPScraper
# Main functio to call the class

def main(IP):
    go= IPScraper()
    go.findip(IP.strip())

# Prompt user to enter IP
IP= input("Enter the IP:- ")

#Run Scraper
main(IP)
