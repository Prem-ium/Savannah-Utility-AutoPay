# Use "FULLY_AUTOMATED" at your own risk. Storing financial information in plain text is not recommended. 
# If you insist on using that feature, please consider using Privacy to protect yourself from theft.
# Privacy is a service that allows you to create virtual cards that are locked to a specific merchant, and can be closed at any time.
# Sign up using (https://app.privacy.com/join/G25UX) link to help yourself stay safe & secure-- you will receive $5 after making a purchase. 

# MIT License
# Copyright (c) 2023 Prem-ium
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
#The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

import os, json, traceback, threading

from time                                       import sleep
from dotenv                                     import load_dotenv

from webdriver_manager.chrome                   import ChromeDriverManager
from selenium.webdriver.chrome.service          import Service
from selenium                                   import webdriver
from selenium.webdriver.common.by               import By
from selenium.webdriver.support.ui              import Select
from selenium.common.exceptions                 import (NoSuchElementException)

# Import .env variables
load_dotenv()

if not os.environ["ACCOUNT_NUMBERS"]:
    raise Exception("ACCOUNT_NUMBERS is not set in .env file. Please set it and try again.")
elif not os.environ["BARCODES"]:
    raise Exception("BARCODES is not set in .env file. Please set it and try again.")
else:
    ACCOUNTS = os.environ["ACCOUNT_NUMBERS"].split(',')
    BARCODES = os.environ.get('BARCODES').split(',')

if len(ACCOUNTS) != len(BARCODES):
    raise Exception("ACCOUNT_NUMBERS and BARCODES are not the same length. Please make sure they are and try again.")

if not os.environ["PAYOR_INFO"]:
    raise Exception("PAYOR_INFO is not set in .env file. Please set it and try again.")
else:
    PAYOR_INFO = os.environ.get('PAYOR_INFO')
    PAYOR_INFO = json.loads(PAYOR_INFO)
    
HANDLE_PAYMENT = True if os.environ.get('HANDLE_PAYMENT', 'False').lower() == 'true' else False
if HANDLE_PAYMENT:
    PAYMENT_METHOD = os.environ.get('PAYMENT_METHOD').split(',')
    if len(PAYMENT_METHOD) != len(ACCOUNTS):
        raise Exception("PAYMENT_METHOD and ACCOUNT_NUMBERS are not the same length. Please make sure they are and try again.")

# Methods
def get_driver():
    """
    Initialize and configure a Selenium Chrome WebDriver instance.

    This method sets up a Chrome WebDriver with specific options, such as:
    - Disabling automation detection (to avoid websites detecting Selenium usage).
    - Starting the browser in a minimized window.

    Returns:    selenium.webdriver.Chrome:  An instance of the configured Chrome WebDriver.
    
    Raises:     Exception:                  If there is an issue initializing the WebDriver."""

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    chrome_options.add_argument("--start-minimized")
    try:
        driver = webdriver.Chrome(
                service=Service(ChromeDriverManager().install()),
                options=chrome_options)
    except:
        driver = webdriver.Chrome()
    return driver

def update_payment(index):
    """
    Retrieve payment details from environment variables based on the payment method.

    Args:
        index (int): Index of the payment method in PAYMENT_METHOD.

    Returns:
        tuple: (payment_method (str), payment_info (dict)) containing:
            - payment_method: Type of payment ("bank", "credit", "debit").
            - payment_info: Payment details parsed from environment variables."""
    
    name = PAYMENT_METHOD[index].split(':')[1]
    if 'bank' in PAYMENT_METHOD[index]:
        bank_info = os.environ.get(name)
        bank_info = json.loads(bank_info)
        payment_method = "bank"
        return payment_method, bank_info
    elif 'credit' in PAYMENT_METHOD[index]:
        cc_info = os.environ.get(name)
        cc_info = json.loads(cc_info)
        payment_method = "credit"
        return payment_method, cc_info
    elif 'debit' in PAYMENT_METHOD[index]:
        db_info = os.environ.get(name)
        db_info = json.loads(db_info)
        payment_method = "debit"
        return payment_method, db_info

# Credit/Debit Card Functions
"""
    CC_CARD/DB_CARD (dict): A dictionary containing card details:
        - 'number' (str): Credit card number.
        - 'ccv' (str): Credit card CVV.
        - 'expirationMonth' (str): Card expiration month (MM).
        - 'expirationYear' (str): Card expiration year (YYYY).
        - 'cardholder' (str): Cardholder's full name.
"""
def pay_with_credit(driver, CC_CARD):
    """
        Fill in credit card payment details on the payment page using the provided WebDriver.
    """
    driver.find_element(By.XPATH, value ='//*[@id="category-CC"]/div[1]/div/label/span').click()
    sleep(2)
    driver.find_element(By.XPATH, value ='//*[@id="ccAccountNumber"]').send_keys(CC_CARD['number'])
    driver.find_element(By.XPATH, value ='//*[@id="ccCvv"]').send_keys(CC_CARD['ccv'])
    Select(driver.find_element(By.ID, value='ccExpiryDateMonth')).select_by_value(CC_CARD['expirationMonth'])
    Select(driver.find_element(By.ID, value='ccExpiryDateYear')).select_by_value(CC_CARD['expirationYear'])
    driver.find_element(By.XPATH, value ='//*[@id="ccCardHolderName"]').send_keys(CC_CARD['cardholder'])

def pay_with_debit(driver, DB_CARD):
    """
        Fill in debit card payment details on the payment page using the provided WebDriver.
    """
    driver.find_element(By.XPATH, value ='//*[@id="category-DC"]/div[1]/div/label/span').click()
    sleep(2)
    driver.find_element(By.ID, value ='dcAccountNumber').send_keys(DB_CARD['number'])
    driver.find_element(By.ID, value ='dcCvv').send_keys(DB_CARD['ccv'])
    Select(driver.find_element(By.ID, value='dcExpiryDateMonth')).select_by_value(DB_CARD['expirationMonth'])
    Select(driver.find_element(By.ID, value='dcExpiryDateYear')).select_by_value(DB_CARD['expirationYear'])
    driver.find_element(By.ID, value ='dcCardHolderName').send_keys(DB_CARD['cardholder'])

def pay_with_bank(driver, BANK):
    """
        Fill in bank account details on the payment page using the provided WebDriver.
    """
    try:
        driver.find_element(By.XPATH, value ='/html/body/div[6]/div[1]/form/div[2]/div[2]/div[6]/fieldset/div[3]/div[1]/div/label/span').click()
    except:
        driver.find_element(By.XPATH, value ='//*[@id="category-DD"]/div[1]/div/label/span').click()
    sleep(2)
    # Retrieve Checking or Saving Account Attribute
    try:
        driver.find_element(By.XPATH, value = f"//button[contains(.,'{BANK['Type']}')]").click()
    except NoSuchElementException:
        if (BANK['Type'] == 'Checking'):
            driver.find_element(By.XPATH, value ='//*[@id="hide-radio-pm-dd-1"]/div/div[2]/div/fieldset/div/label/span').click()
        elif (BANK['Type'] == 'Savings'):
            driver.find_element(By.XPATH, value ='//*[@id="hide-radio-pm-dd-1"]/div/div[2]/div/fieldset/div[2]/label/span').click()
    # Enter Account Information
    driver.find_element(By.XPATH, value ='//*[@id="ddBankName"]').send_keys(BANK['Banker'])
    driver.find_element(By.XPATH, value ='//*[@id="ddAccountHolderName"]').send_keys(BANK['Holder'])

    try:
        driver.find_element(By.XPATH, value ='/html/body/div[6]/div[1]/form/div[2]/div[1]/div[5]/fieldset/div[3]/div[2]/div/div[3]/div[1]/input').send_keys(BANK['Routing'])
    except:
        sleep(5)
        driver.find_element(By.XPATH, value = '//*[@id="ddRoutingNumber"]').send_keys(BANK['Routing'])

    driver.find_element(By.XPATH, value='//*[@id="ddAccountNumber"]').send_keys(BANK['Account'])
    driver.find_element(By.XPATH, value='//*[@id="ddAccountNumber2"]').send_keys(BANK['Account'])

def automate_bill(account, barcode, index):
    """
    Automates bill retrieval and payment for a given account.

    Args:
        account (str): Account number to identify the bill.
        barcode (str): Barcode associated with the account.
        index (int): Index of the selected payment method.

    Workflow:
        - Navigates to the payment portal.
        - Inputs account and barcode to retrieve billing information.
        - Verifies outstanding balance and handles payment using bank, credit, or debit info.
        - Supports full or partial automation based on configuration.
    """

    if HANDLE_PAYMENT:
        payment_info = update_payment(index)
        if (payment_info[0] == 'bank'):
            bank_info = payment_info[1]
        elif (payment_info[0] == 'credit'):
            cc_info = payment_info[1]
        elif (payment_info[0] == 'debit'):
            db_info = payment_info[1]

        print(f'Account: {account} Barcode: {barcode} Payment Method: {payment_info[0]}\n\n')
    driver = get_driver()
    try:
        driver.get('https://revenue.savannahga.gov/revwebpayub/default.aspx')

        # Enter Account Number and Barcode
        driver.find_element(By.ID, value ='objWP_epayment_ESearchManager1_Web_CO_SearchPanel1_txt_GFD0').send_keys(account)
        driver.find_element(By.ID, value ='objWP_epayment_ESearchManager1_Web_CO_SearchPanel1_txt_GFD1').send_keys(barcode)
        driver.find_element(By.XPATH, value ='//*[@id="objWP_epayment_ESearchManager1_Web_CO_SearchPanel1_btnGo"]').click()
    
        # Check for invalid numbers
        if (driver.find_elements(By.XPATH, value ='//*[@id="objWP_epayment_ESearchManager1_vdsSummary"]/ul/li')):
            driver.execute_script('alert(\'Barcode is incorrect. Exiting...\');')
            print('Incorrect barcode provided. Exiting...')
            sleep(10)
            driver.quit()
            return
        elif (driver.find_elements(By.XPATH, value ='//*[@id="objWP_epayment_ESearchManager1_Web_CO_SearchPanel1_lblNoResult"]')):
            driver.execute_script('alert("No results found.\\nCheck account number and barcode are correct & run again upon account number/barcode correction.\\nExiting...");')
            print('No results found, please check account number and barcode are correct. Exiting...')
            sleep(15)
            driver.quit*()
            return
        
        # Continue, if correct values provided
        print(f'Account: {account} with barcode: {barcode} found.\n')
        sleep(4)
        driver.find_element(By.XPATH, value ='/html/body/form/table/tbody/tr[2]/td[2]/table[2]/tbody/tr[2]/td/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[3]/td/table/tbody/tr[5]/td/input[2]').click()

        # Check for outstanding balance, return if none
        try:
            if (driver.find_element(By.XPATH, value ='//*[@id="ctl02_grdAmount_ctl01_lblEmptyGrid"]').get_attribute('innerHTML') == 'No Outstanding Balance Found.'):
                driver.execute_script(f'alert("No outstanding balance found for:\\nAccount:\\t{account}\\nBarcode:\\t{barcode}\\nExiting browser...");')
                print(f'{"-"*45}\nNo outstanding balance found for account {account} and {barcode}. Exiting...\n{"-"*45}')
                sleep(10)
                driver.quit()
                return
        except NoSuchElementException:
            print('An outstanding balance exists... Continuing...')
        sleep(3)

        try:
            amount = driver.find_element(By.XPATH, value ='/html/body/form/table/tbody/tr[2]/td[2]/table[2]/tbody/tr[2]/td/table/tbody/tr/td/table/tbody/tr[4]/td[2]/div/table/tbody/tr[2]/td[2]/div/table/tbody/tr[3]/td[2]/table/tbody/tr/td/span').text
            print(f'\n{"-"*45}\nAccount:\t{account}\nBarcode:\t{barcode}\nAmount due:\t{amount}\n{"-"*45}\n')
        except: pass

        # Next Step Page
        driver.find_element(By.XPATH, value='//*[@id="ctl02_hlinkNextStep"]').click()
        driver.find_element(By.XPATH, value='//*[@id="ctl02_hlinkNextStep"]').click()
        sleep(3)

        # Billing Address/Information Page
        driver.find_element(By.XPATH, value ='//*[@id="ctl02_txtFirstName"]').send_keys(PAYOR_INFO['FirstName'])
        driver.find_element(By.XPATH, value ='//*[@id="ctl02_txtLastName"]').send_keys(PAYOR_INFO['LastName'])
        driver.find_element(By.XPATH, value ='//*[@id="ctl02_txtCivic"]').send_keys(PAYOR_INFO['HouseNumber'])
        driver.find_element(By.XPATH, value ='//*[@id="ctl02_txtEmail"]').send_keys(PAYOR_INFO['Email'])
        driver.find_element(By.XPATH, value ='//*[@id="ctl02_txtStreet"]').send_keys(PAYOR_INFO['Street'])
        driver.find_element(By.XPATH, value ='//*[@id="ctl02_txtCity"]').send_keys(PAYOR_INFO['City'])
        Select(driver.find_element(By.ID, value='ctl02_ddlState')).select_by_visible_text(PAYOR_INFO['State'])
        driver.find_element(By.XPATH, value ='//*[@id="ctl02_txtZipCode"]').send_keys(PAYOR_INFO['Zip'])
        driver.find_element(By.XPATH, value ='//*[@id="ctl02_hlinkNextStep"]').click()
        sleep(3)
        driver.find_element(By.XPATH, value ='//*[@id="main-container"]/form/div/div[2]/div/input').click()
        sleep(5)

        # Payment Page
        driver.find_element(By.XPATH, value ='//*[@id="customer.dayPhone.formattedText"]').send_keys(PAYOR_INFO['Phone'])
        if HANDLE_PAYMENT == True:
            if (payment_info[0] == 'bank'):
                pay_with_bank(driver, bank_info)
            elif (payment_info[0] == 'credit'):
                pay_with_credit(driver, cc_info)
            elif (payment_info[0] == 'debit'):
                pay_with_debit(driver, db_info)
            sleep(3)
        else:
            driver.execute_script("alert('Payment information must be manually entered from this point.\\nHandle Payment variable was assigned to False.\\n Browser will close in 10 minutes.');")
            sleep(600)
            driver.quit()
            return
        
        # Submit Button
        driver.find_element(By.XPATH, value ='//*[@id="main-container"]/form/div[2]/div[2]/div/input[1]').click()
        fully_automate = True if os.environ.get('FULLY_AUTOMATED', 'False').lower() == 'true' else False
        if fully_automate:
            # Agree to terms and conditions & submit payment, if fully automated
            sleep(5)
            driver.find_element(By.XPATH, value ='//*[@id="main-container"]/form/div/div/div[6]/div/div/label/span').click()
            driver.find_element(By.XPATH, value ='//*[@id="make-payment-btn"]').click()
            sleep(10)
            print(f'Payment submitted for account {account} and barcode {barcode}. Exiting...')
        else:
            driver.execute_script(f"alert('{account}:{PAYMENT_METHOD[index].split(':')[1]} Fully Automated variable is set to False. You must manually submit your payment. You have 5 minutes before the browser closes.');")
            print(f"{account}:{PAYMENT_METHOD[index].split(':')[1]} Fully Automated variable is set to False. You must manually submit your payment. You have 5 minutes before the browser closes.")
            sleep(300)
    except:
        print(f'An unexpected error occurred.\nBrowser will close in 1 minute.\n\n{traceback.format_exc()}')
        sleep(60)
    driver.quit()

def multithread():
    """
    Executes bill automation in parallel using multi-threading.
    """
    print(f'Multi-threading enabled. Running automation in parallel...\n{"-"*50}')
    
    threads = [
        threading.Thread(target=automate_bill, args=(account, barcode, i) if HANDLE_PAYMENT else (account, barcode))
        for i, (account, barcode) in enumerate(zip(ACCOUNTS, BARCODES))
    ]
    
    for thread in threads:
        thread.start()
        
    for thread in threads:
        thread.join()

# Main Method
def main():
    use_multithreading = True if os.environ.get('MULTI_THREADING', 'False').lower() == 'true' else False
    if use_multithreading:
        multithread()
    else:
        for i, (account, barcode) in enumerate(zip(ACCOUNTS, BARCODES)):
            print(f'\n{"-"*40}\nAccount #{i}:\t{account}\tBarcode #{i}:\t{barcode}\n{"-"*40}\n')
            automate_bill(account, barcode, i)

if __name__ == '__main__':
    message = """
Use "FULLY_AUTOMATED" at your own risk. Storing financial information in plain text is not recommended.
If you insist on using that feature, please consider using Privacy to protect yourself from theft.

Privacy is a service that allows you to create virtual cards that are locked to a specific merchant and can be closed at any time.
Sign up using the following link to help yourself stay safe & secure -- you will receive $5 after making a purchase:

https://app.privacy.com/join/G25UX
    """
    print(f"{'-'*50}\n{message}\n{'-'*50}")

    main()
    print(f"Done!\nThank you for using Prem-ium's Savannah, GA Water Bill Automation Script!\nIf you liked this project, please consider donating/sponsoring to support more projects like it:\t https://github.com/sponsors/Prem-ium")
