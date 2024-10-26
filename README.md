<h1 align="center">🏤 Savannah, GA Utility Bill Pay Automation 🤖 </h1>

<p align="center">A Selenium-based Python script that simplifies water utility bill payments for homeowners, landlords, & business owners in Savannah, GA USA.</p>

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

# Donations


If you appreciate my work and would like to show your support, there are two convenient ways to make a donation:

1. **GitHub Sponsors**
   - [Donate via GitHub Sponsors](https://github.com/sponsors/Prem-ium)
   - This is the preferred donation method as you can place donations with no transaction fees & possibily receive perks for your donation.
   - [![GitHub Sponsor](https://img.shields.io/badge/sponsor-30363D?style=for-the-badge&logo=GitHub-Sponsors&logoColor=#EA4AAA)](https://github.com/sponsors/Prem-ium)

2. **Buy Me A Coffee**
   - [Donate via Buy Me A Coffee](https://www.buymeacoffee.com/prem.ium)
   - [![Buy Me A Coffee](https://img.shields.io/badge/Buy%20Me%20a%20Coffee-ffdd00?style=for-the-badge&logo=buy-me-a-coffee&logoColor=black)](https://www.buymeacoffee.com/prem.ium)

Your generous donations will go a long way in helping me cover the expenses associated with developing new features and promoting the project to a wider audience. I extend my heartfelt gratitude to all those who have already contributed. Thank you for your support!
## FAQ

#### How can this repository help Savannah Georgia property owners pay utility bills?

This repository contains a Python script that automates the process of paying utility bills for Savannah properties using Selenium. It can save time and hassle for landlords and business owners who need to pay multiple bills every month.

#### What inspired you to create this script?

I created this script because I was frustrated with the Savannah GA GOV Utility Bill payment website. It was slow, cumbersome, and required me to enter the same information over and over again for each property. I wanted a faster and easier way to pay my utility bills online.

## License

This project operates under the [MIT](https://github.com/Prem-ium/Savannah-Utility-AutoPay/blob/main/LICENSE.MD) license.

## Disclaimer:
Please be careful when storing financial information such as card or bank details in this program. Storing this information in your `.env` is not always secure and could expose you to fraud or theft. We do not recommend storing permanently any sensitive financial information in this program. If you choose to do so, you are solely responsible for any financial loss that may happen. Use at your own risk. It is **highly recommended** you use Privacy to create virtual cards if you chose to leave your info permanently.
[Use Privacy.com to secure your payments. ](https://privacy.com/join/G25UX)

Privacy will allow you to pause and unpause your card at any time, allowing you to securely ensure your financial safety in the event of a breach.

## Example Output
```
--------------------------------------------------
Use "FULLY_AUTOMATED" at your own risk. Storing financial information in plain text is not recommended.
If you insist on using that feature, please consider using Privacy to protect yourself from theft.

Privacy is a service that allows you to create virtual cards that are locked to a specific merchant and can be closed at any time.
Sign up using the following link to help yourself stay safe & secure -- you will receive $5 after making a purchase:

https://privacy.com/join/G25UX
--------------------------------------------------
Multi-threading enabled. Running automation in parallel...
--------------------------------------------------
Account: 07XXX0 Barcode: 12XX00 Payment Method: bank


Account: 07XXX0 with barcode: 12XX00 found.

An outstanding balance exists... Continuing...

------------------------
Account:	07XXX0
Barcode:	12XX00
Amount due:	$125.21
------------------------

Done!
Thank you for using Prem-ium's Savannah, GA Water Bill Automation Script!
```
