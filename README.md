
# Savannah GA Utility Bill AutoPay

A Selenium Python script to automate utility bill payments for propety owners of Savannah, GA.

## Installation

1. Clone this repository, cd into it, and install dependancies:
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


## FAQ

#### Who is this repository applicable for?

This repository is applicable to any person(s) within the Savannah, Georgia area who is responsible for paying utility bills. Ideally, landlords and business owners can rapidly pay for different locations.


#### Why did you create this script?

I loathed the Savannah GA GOV Utility Bill payment website. Manually having to type the same information multiple times for three seperate propety utility bills became exhausting, so I decided to automate it using a script.

#### WARNING:
Storing sensitive financial information such as debit/credit card or bank credentials is highly discouraged. If you must store financial information, it is recommended that you use caution and proceed at your own risk. The developer(s) of this program are not responsible for any financial loss incurred that may occur as a result of storing financial information in this program. Use at your own risk. 
[Use Privacy.com to get Virtual Cards to protect yourself and ensure you aren't overcharged.](https://privacy.com/join/G25UX)
