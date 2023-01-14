
# Savannah GA Utility Bill AutoPay

A selenium python script to automate the utility bill payment for residents of Savannah GA.


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

- `ACCOUNT_NUMBERS`: A comma-separated string of account numbers. These are used to identify the accounts that the application will interact with.

- `BARCODES`: A comma-separated string of barcodes. These are used to identify the barcodes that the application will interact with.

- `PAYOR_INFO`: A JSON string containing the payor's information, including first and last name, address, email, and phone number.

#### Optional Enviornmental Variables: 

- `HANDLE_PAYMENT`: A boolean value indicating whether the application should handle payments or not.

- `FULLY_AUTOMATED`: A boolean value indicating whether the application should run in fully automated mode or not.

- `PAYMENT_METHOD`: A string indicating the payment method to be used. It can take values `bank`, `credit`, `debit`.

- `BANK`: A JSON string containing the bank information, including bank type, routing number, account number, bank name, and account holder name.

- `CREDIT_CARD`: A JSON string containing the credit card information, including the card number, expiration date, CCV, and cardholder name.

- `DEBIT_CARD`: A JSON string containing the debit card information, including the card number, expiration date, CCV, and cardholder name.

It is important to note that these variables should be replaced with real values before the application is run in order for it to function properly.


## FAQ

#### Who is this repository applicable for?

Any person(s) within the Savannah, Georgia area which is responsible for paying utility bills. Ideally, landlords and business owners can rapidly pay for different location(s).

#### Why did you create this script?

I despise Savannah GA GOV Utility Bill process. Manually having to type the same information multiple times for three seperate bills became exhausting, so I decided to automate it.

#### WARNING:
Storing sensitive financial information such as debit/credit card or bank credentials is highly discouraged. If you must store financial information, it is recommended that you use caution and proceed at your own risk. The developer(s) of this program are not responsible for any financial loss incurred that may occur as a result of storing financial information in this program. Use at your own risk. 
[Use Privacy.com to get Virtual Cards to protect yourself.](https://privacy.com/join/G25UX)
