README.md

# Setting API keys <br>
You need to have set the API keys correctly.  Onyphe and etintel seems to require some payment. Greynoise has a 14 day trial that can be used
    <br>etintel_api_key: str = 'your emerging threats intelligence api key'
    <br>greynoise_api_key: str = 'your greynoise community api key'
    <br>onyphe_api_key: str = 'apikey your onyphe api key'
    <br>shodan_api_key: str = 'your shodan api key'
    <br>virustotal_api_key: str = 'your virustotal api key'

# Usage
Run main.py. It will request for IP to scraped.<br>
    main.py

# Sample Output
A csv file will be created with the scrap data.
    <br>Enter the IP:- 58.216.151.245
    <br>58.216.151.245 found in GreyNoise
    <br>58.216.151.245 found in Shodan
    <br>58.216.151.245 found in VirusTotal - Historical Whois
    <br>Results written to 58.216.151.245_20220424_140443.csv
