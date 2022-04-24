README.md

#Setting API keys
You need to have set the API keys correctly.  Onyphe and etintel seems to require some payment. Greynoise has a 14 day trial that can be used
    etintel_api_key: str = 'your emerging threats intelligence api key'
    greynoise_api_key: str = 'your greynoise community api key'
    onyphe_api_key: str = 'apikey your onyphe api key'
    shodan_api_key: str = 'your shodan api key'
    virustotal_api_key: str = 'your virustotal api key'

#Usage

    main.py

#Sample Output

    Enter the IP:- 58.216.151.245
    58.216.151.245 found in GreyNoise
    58.216.151.245 found in Shodan
    58.216.151.245 found in VirusTotal - Historical Whois
    Results written to 58.216.151.245_20220424_140443.csv
