<h1 align="center">🏤 Savannah, GA Utility Bill Pay Automation 🤖 </h1>

<p align="center">A Selenium-based Python script that simplifies utility bill payments for homeowners, landlords, & business owners in Savannah.</p>

<p align="right"> 
        <img src="https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54"/><img src="https://img.shields.io/badge/-selenium-%43B02A?style=for-the-badge&logo=selenium&logoColor=white"/><a href="https://github.com/sponsors/Prem-ium" target="_blank">
        <img src="https://img.shields.io/badge/sponsor-30363D?style=for-the-badge&logo=GitHub-Sponsors&logoColor=#EA4AA" alt="Github Sponsor"/></a>
</p>

## Installation

1. Clone this repository, CD into the folder, and install dependancies:
   ```sh
      git clone https://github.com/Prem-ium/Savannah-Utility-AutoPay.git
      cd Savannah-Utility-AutoPay
      pip install -r requirements.txt
   ```
2. Configure your `.env` file (See below and example for options)
3. Run the script:
   ```sh
      python main.py
   ```

## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

#### Required Enviornmental Variables: 

| Variable         | Description                                                       | Type    |
|------------------|-------------------------------------------------------------------|---------|
| `ACCOUNT_NUMBERS`| Comma-separated string of account numbers                          | String  |
| `BARCODES`       | Comma-separated string of barcodes                                 | String  |
| `PAYOR_INFO`     | JSON string containing payor's information                        | JSON    |


#### Optional Enviornmental Variables: 

| Variable         | Description                                                        | Type    | Default |
|------------------|--------------------------------------------------------------------|---------|---------|
| `HANDLE_PAYMENT` | A boolean value indicating whether the application handles payments | Boolean | True    |
| `FULLY_AUTOMATED`| A boolean value indicating fully automated mode                    | Boolean | False   |
| `MULTI_THREADING`| A boolean value indicating multithreading usage                     | Boolean | True    |
| `PAYMENT_METHOD` | String indicating payment method (bank, credit, debit)              | String  | bank    |
| `BANK`           | JSON string containing bank information                             | JSON    |         |
| `CREDIT_CARD`    | JSON string containing credit card information                     | JSON    |         |
| `DEBIT_CARD`     | JSON string containing debit card information                      | JSON    |         |


It is important to note that these variables should be replaced with real values before the application is run in order for it to function properly.

## Donations

I've been working on this project for a few months now, and I'm really happy with how it's turned out. 
If you would like to show your appreciation for my work, I have set up two methods of sending in a donation: 

<a href="https://github.com/sponsors/Prem-ium">Github Sponsors</a>, the ideal donation method, to make donations with no fees!
<a href="https://github.com/sponsors/Prem-ium" target="_blank">
        <img src="https://img.shields.io/badge/sponsor-30363D?style=for-the-badge&logo=GitHub-Sponsors&logoColor=#EA4AAA" alt="GitHub Sponsor" img width="25%">
</a>

Otherwise, <a href="https://www.buymeacoffee.com/prem.ium">Buy-Me-Coffee</a> can be used to place donations as well. 
<a href="https://www.buymeacoffee.com/prem.ium" target="_blank">
        <img src="https://raw.githubusercontent.com/Prem-ium/youtube-analytics-bot/main/output-examples/media/coffee-logo.png" alt="Buy Me A Coffee" img width="25%">
</a>

I extend my heartfelt gratitude to all those who have already contributed. 
Thank you for your support!

## FAQ

#### How can this repository help Savannah Georgia property owners pay utility bills?

This repository contains a Python script that automates the process of paying utility bills for Savannah properties using Selenium. It can save time and hassle for landlords and business owners who need to pay multiple bills every month.

#### What inspired you to create this script?

I created this script because I was frustrated with the Savannah GA GOV Utility Bill payment website. It was slow, cumbersome, and required me to enter the same information over and over again for each property. I wanted a faster and easier way to pay my utility bills online.

## License

This project operates under the [MT](https://choosealicense.com/licenses/mit/) license.

## Disclaimer:
Please be careful when storing financial information such as card or bank details in this program. Storing this information in your `.env` is not always secure and could expose you to fraud or theft. We do not recommend storing permanently any sensitive financial information in this program. If you choose to do so, you are solely responsible for any financial loss that may happen. Use at your own risk. It is **highly recommended** you use Privacy to create virtual cards if you chose to leave your info permanently.
[Use Privacy.com to secure your payments. ](https://privacy.com/join/G25UX)

Privacy will allow you to pause and unpause your card at any time, allowing you to securely ensure your financial safety in the event of a breach.
