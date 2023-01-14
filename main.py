# Sazn (Prem) 
# Python Automation Application

# USE handlePayment AND fullyAutomated AT YOUR OWN RISK.
# If you are insistent on using either, I HIGHLY RECOMMEND YOU USE A VIRTUAL DEBIT CARD OR A PRIVACY.COM (https://privacy.com/join/G25UX) TEMPORARY CARD.
import os
import json
from time import sleep
from dotenv import load_dotenv
from lib2to3.pgen2 import driver

from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import (
    NoSuchElementException,
    UnexpectedAlertPresentException
)

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
    PAYMENT_METHOD = os.environ.get('PAYMENT_METHOD').lower()
    if PAYMENT_METHOD == 'bank':
        BANK = os.environ.get('BANK')
        BANK = json.loads(BANK)
    elif PAYMENT_METHOD == 'credit':
        CC_CARD = os.environ.get('CREDIT_CARD')
        CC_CARD = json.loads(CC_CARD)
    elif PAYMENT_METHOD == 'debit':
        DB_CARD = os.environ.get('DEBIT_CARD')
        DB_CARD = json.loads(DB_CARD)

FULLY_AUTOMATED = True if os.environ.get('FULLY_AUTOMATED', 'False').lower() == 'true' else False

def getDriver():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    chrome_options.add_argument("--start-minimized")
    try:
        driver = webdriver.Chrome(
                service=Service(ChromeDriverManager(cache_valid_range=30).install()),
                options=chrome_options)
    except:
        driver = webdriver.Chrome()
    return driver

# Payment Method Functions
def payWithCreditCard(driver):
    driver.find_element(By.XPATH, value ='//*[@id="category-CC"]/div[1]/div/label/span').click()
    sleep(2)
    driver.find_element(By.XPATH, value ='//*[@id="ccAccountNumber"]').send_keys(CC_CARD['number'])
    driver.find_element(By.XPATH, value ='//*[@id="ccCvv"]').send_keys(CC_CARD['ccv'])
    Select(driver.find_element(By.ID, value='ccExpiryDateMonth')).select_by_value(CC_CARD['expirationMonth'])
    Select(driver.find_element(By.ID, value='ccExpiryDateYear')).select_by_value(CC_CARD['expirationYear'])
    driver.find_element(By.XPATH, value ='//*[@id="ccCardHolderName"]').send_keys(CC_CARD['cardholder'])

def payWithDebitCard(driver):
    driver.find_element(By.XPATH, value ='//*[@id="category-DC"]/div[1]/div/label/span').click()
    sleep(2)
    driver.find_element(By.ID, value ='dcAccountNumber').send_keys(DB_CARD['number'])
    driver.find_element(By.ID, value ='dcCvv').send_keys(DB_CARD['ccv'])
    Select(driver.find_element(By.ID, value='dcExpiryDateMonth')).select_by_value(DB_CARD['expirationMonth'])
    Select(driver.find_element(By.ID, value='dcExpiryDateYear')).select_by_value(DB_CARD['expirationYear'])
    driver.find_element(By.ID, value ='dcCardHolderName').send_keys(DB_CARD['cardholder'])

def payWithBank(driver):
    # Bank Account 
    driver.find_element(By.XPATH, value ='//*[@id="category-DD"]/div[1]/div/label/span').click()
    sleep(2)
    try:
        if (BANK['Type'] == 'Checking'):
            driver.find_element(By.XPATH, value ='//*[@id="hide-radio-pm-dd-1"]/div/div[2]/div/fieldset/div/label/span').click()
        elif (BANK['Type'] == 'Savings'):
            driver.find_element(By.XPATH, value ='//*[@id="hide-radio-pm-dd-1"]/div/div[2]/div/fieldset/div[2]/label/span').click()
    except:
        try:
            if (BANK['Type'] == 'Checking'):
                driver.find_element(By.XPATH, value = "//button[contains(.,'Checking')]").click()
            elif (BANK['Type'] == 'Savings'):
                driver.find_element(By.XPATH, value = "//button[contains(.,'Savings')]").click()
        except:
            pass
    driver.find_element(By.XPATH, value ='//*[@id="ddBankName"]').send_keys(BANK['Banker'])
    driver.find_element(By.XPATH, value ='//*[@id="ddAccountHolderName"]').send_keys(BANK['Holder'])
    try:
        driver.find_element(By.XPATH, value ='/html/body/div[6]/div[1]/form/div[2]/div[1]/div[5]/fieldset/div[3]/div[2]/div/div[3]/div[1]/input').send_keys(BANK['Routing'])
    except:
        try:
            sleep(5)
            driver.find_element(By.XPATH, value = '//*[@id="ddRoutingNumber"]').send_keys(BANK['Routing'])
        except:
            pass
    driver.find_element(By.XPATH, value='//*[@id="ddAccountNumber"]').send_keys(BANK['Account'])
    driver.find_element(By.XPATH, value='//*[@id="ddAccountNumber2"]').send_keys(BANK['Account'])

def automate(account, barcode):
    # URL of the bill website to be scraped
    url = 'https://revenue.savannahga.gov/revwebpayub/default.aspx'

    driver = getDriver()
    driver.get(url)

    # Barcode/Account Number Page
    driver.find_element(By.ID, value ='objWP_epayment_ESearchManager1_Web_CO_SearchPanel1_txt_GFD0').send_keys(account)
    driver.find_element(By.ID, value ='objWP_epayment_ESearchManager1_Web_CO_SearchPanel1_txt_GFD1').send_keys(barcode)
    driver.find_element(By.XPATH, value ='//*[@id="objWP_epayment_ESearchManager1_Web_CO_SearchPanel1_btnGo"]').click()
 
    # check if element exists
    if (driver.find_elements(By.XPATH, value ='//*[@id="objWP_epayment_ESearchManager1_vdsSummary"]/ul/li')):
        driver.execute_script('alert(\'Barcode is incorrect. Exiting...\');')
        print('Incorrect barcode provided. Exiting...')
        sleep(10)
        return
    elif (driver.find_elements(By.XPATH, value ='//*[@id="objWP_epayment_ESearchManager1_Web_CO_SearchPanel1_lblNoResult"]')):
        driver.execute_script('alert(\'No results found, please check account number and barcode are correct & run again upon account number/barcode correction. Exiting...\');')
        print('No results found, please check account number and barcode are correct. Exiting...')
        sleep(15)
        return
    print('Account number and barcode are correct.')
    sleep(4)
    driver.find_element(By.XPATH, value ='/html/body/form/table/tbody/tr[2]/td[2]/table[2]/tbody/tr[2]/td/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[3]/td/table/tbody/tr[5]/td/input[2]').click()
    try:
        if (driver.find_element(By.XPATH, value ='//*[@id="ctl02_grdAmount_ctl01_lblEmptyGrid"]').get_attribute('innerHTML') == 'No Outstanding Balance Found.'):
            driver.execute_script('alert(\'No outstanding balance found. Exiting...\');')
            print('No outstanding balance found. Exiting...')
            sleep(10)
            return
    except NoSuchElementException:
        print('An outstanding balance exists... Continuing...')
    sleep(3)
    # Next Step Page
    driver.find_element(By.XPATH, value='//*[@id="ctl02_hlinkNextStep"]').click()
    driver.find_element(By.XPATH, value='//*[@id="ctl02_hlinkNextStep"]').click()
    sleep(3)

    # NEW PAYER INFO PAGE
    driver.find_element(By.XPATH, value ='//*[@id="ctl02_txtFirstName"]').send_keys(PAYOR_INFO['FirstName'])
    driver.find_element(By.XPATH, value ='//*[@id="ctl02_txtLastName"]').send_keys(PAYOR_INFO['LastName'])
    driver.find_element(By.XPATH, value ='//*[@id="ctl02_txtCivic"]').send_keys(PAYOR_INFO['HouseNumber'])
    driver.find_element(By.XPATH, value ='//*[@id="ctl02_txtEmail"]').send_keys(PAYOR_INFO['Email'])
    driver.find_element(By.XPATH, value ='//*[@id="ctl02_txtStreet"]').send_keys(PAYOR_INFO['Street'])
    driver.find_element(By.XPATH, value ='//*[@id="ctl02_txtCity"]').send_keys(PAYOR_INFO['City'])
    Select(driver.find_element(By.ID, value='ctl02_ddlState')).select_by_visible_text(PAYOR_INFO['State'])
    driver.find_element(By.XPATH, value ='//*[@id="ctl02_txtZipCode"]').send_keys(PAYOR_INFO['Zip'])
    driver.find_element(By.XPATH, value ='//*[@id="ctl02_hlinkNextStep"]').click()
    driver.find_element(By.XPATH, value ='//*[@id="main-container"]/form/div/div[2]/div/input').click()
    sleep(5)
    #Payment Page
    driver.find_element(By.XPATH, value ='//*[@id="customer.dayPhone.formattedText"]').send_keys(PAYOR_INFO['Phone'])
    if HANDLE_PAYMENT == True:
        if(PAYMENT_METHOD == 'bank'):
            payWithBank(driver)
        elif (PAYMENT_METHOD == 'credit'):
            payWithCreditCard(driver)
        elif (PAYMENT_METHOD == 'debit'):
            payWithDebitCard(driver)
    else:
        driver.execute_script("alert('Payment must be manually entered from this point. Handle Payment variable is False. Browser closes in 10 minutes.');")
        sleep(600)
        return
    sleep(2)
    # Submit 
    driver.find_element(By.XPATH, value ='//*[@id="main-container"]/form/div[2]/div[2]/div/input[1]').click()

    if FULLY_AUTOMATED:
        sleep(6)
        # TERMS AND CONDITIONS AGREEMENT!!
        driver.find_element(By.XPATH, value ='//*[@id="main-container"]/form/div/div/div[6]/div/div/label/span').click()
        # FINAL SUBMIT BUTTON!!!
        driver.find_element(By.XPATH, value ='//*[@id="make-payment-btn"]').click()
    else:
        driver.execute_script("alert('Fully Automated variable is set to False. You must manually submit your payment. You have 5 minutes before the browser closes.');")
        sleep(300)

# Main Program
def main():
    try:
        i = 0
        for account in ACCOUNTS:
            print(f'Starting:\n\tAccount: {account}\n\tBarcode: {BARCODES[i]}\n\tPayment Method: {PAYMENT_METHOD}\n\n')
            automate(account, BARCODES[i])
            sleep(2)
            i+=1
            print()
    except Exception as e:
        print(e)
        driver.execute_script("alert('Error occurred. Browser closes in 5 minutes.');")
        sleep(300)
        return

if __name__ == '__main__':
    main()
    sleep(3)
    