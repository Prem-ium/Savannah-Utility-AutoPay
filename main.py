# Sazn (Prem) 
# Python Automation Application

# USE handlePayment AND fullyAutomated AT YOUR OWN RISK.
# If you are insitent on using either, I HIGHLY RECOMMEND YOU USE A VIRTUAL DEBIT CARD OR A PRIVACY.COM TEMPORARY CARD.

from lib2to3.pgen2 import driver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException, UnexpectedAlertPresentException

import time
import secrets

ACCOUNTS = secrets.ACCOUNT_NUMBERS.split(',')
BARCODES = secrets.BARCODES.split(',')

# Payment Method Functions
def payWithCreditCard(driver):
    driver.find_element(By.XPATH, value ='//*[@id="category-CC"]/div[1]/div/label/span').click()
    time.sleep(2)
    driver.find_element(By.XPATH, value ='//*[@id="ccAccountNumber"]').send_keys(secrets.cc_card['number'])
    driver.find_element(By.XPATH, value ='//*[@id="ccCvv"]').send_keys(secrets.cc_card['ccv'])
    Select(driver.find_element(By.ID, value='ccExpiryDateMonth')).select_by_value(secrets.cc_card['expirationMonth'])
    Select(driver.find_element(By.ID, value='ccExpiryDateYear')).select_by_value(secrets.cc_card['expirationYear'])
    driver.find_element(By.XPATH, value ='//*[@id="ccCardHolderName"]').send_keys(secrets.cc_card['cardholder'])

def payWithDebitCard(driver):
    driver.find_element(By.XPATH, value ='//*[@id="category-DC"]/div[1]/div/label/span').click()
    time.sleep(2)
    driver.find_element(By.ID, value ='dcAccountNumber').send_keys(secrets.db_card['number'])
    driver.find_element(By.ID, value ='dcCvv').send_keys(secrets.db_card['ccv'])
    Select(driver.find_element(By.ID, value='dcExpiryDateMonth')).select_by_value(secrets.db_card['expirationMonth'])
    Select(driver.find_element(By.ID, value='dcExpiryDateYear')).select_by_value(secrets.db_card['expirationYear'])
    driver.find_element(By.ID, value ='dcCardHolderName').send_keys(secrets.db_card['cardholder'])

def payWithBank(driver):
    # Bank Account 
    driver.find_element(By.XPATH, value ='//*[@id="category-DD"]/div[1]/div/label/span').click()
    time.sleep(2)

    if (secrets.bank['Type'] == 'Checking'):
        driver.find_element(By.XPATH, value ='//*[@id="hide-radio-pm-dd-1"]/div/div[2]/div/fieldset/div/label/span').click()
    elif (secrets.bank['Type'] == 'Savings'):
        driver.find_element(By.XPATH, value ='//*[@id="hide-radio-pm-dd-1"]/div/div[2]/div/fieldset/div[2]/label/span').click()
    
    driver.find_element(By.XPATH, value ='//*[@id="ddBankName"]').send_keys(secrets.bank['Banker'])
    driver.find_element(By.XPATH, value ='//*[@id="ddAccountHolderName"]').send_keys(secrets.bank['Holder'])
    driver.find_element(By.XPATH, value ='/html/body/div[6]/div[1]/form/div[2]/div[1]/div[5]/fieldset/div[3]/div[2]/div/div[3]/div[1]/input').send_keys(secrets.bank['Routing'])
    driver.find_element(By.XPATH, value='//*[@id="ddAccountNumber"]').send_keys(secrets.bank['Account'])
    driver.find_element(By.XPATH, value='//*[@id="ddAccountNumber2"]').send_keys(secrets.bank['Account'])

def automate(account, barcode):
    # URL of the bill website to be scraped
    url = 'https://revenue.savannahga.gov/revwebpayub/default.aspx'

    driver = webdriver.Chrome()
    driver.get(url)

    # Barcode/Account Number Page
    driver.find_element(By.ID, value ='objWP_epayment_ESearchManager1_Web_CO_SearchPanel1_txt_GFD0').send_keys(account)
    driver.find_element(By.ID, value ='objWP_epayment_ESearchManager1_Web_CO_SearchPanel1_txt_GFD1').send_keys(barcode)
    driver.find_element(By.XPATH, value ='//*[@id="objWP_epayment_ESearchManager1_Web_CO_SearchPanel1_btnGo"]').click()
 
    # check if element exists
    if (driver.find_elements(By.XPATH, value ='//*[@id="objWP_epayment_ESearchManager1_vdsSummary"]/ul/li')):
        driver.execute_script('alert(\'Barcode is incorrect. Exiting...\');')
        print('Incorrect barcode provided. Exiting...')
        time.sleep(10)
        return
    elif (driver.find_elements(By.XPATH, value ='//*[@id="objWP_epayment_ESearchManager1_Web_CO_SearchPanel1_lblNoResult"]')):
        driver.execute_script('alert(\'No results found, please check account number and barcode are correct & run again upon account number/barcode correction. Exiting...\');')
        print('No results found, please check account number and barcode are correct. Exiting...')
        time.sleep(15)
        return
    print('Account number and barcode are correct.')
    driver.find_element(By.XPATH, value ='/html/body/form/table/tbody/tr[2]/td[2]/table[2]/tbody/tr[2]/td/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[3]/td/table/tbody/tr[5]/td/input[2]').click()
    try:
        if (driver.find_element(By.XPATH, value ='//*[@id="ctl02_grdAmount_ctl01_lblEmptyGrid"]').get_attribute('innerHTML') == 'No Outstanding Balance Found.'):
            driver.execute_script('alert(\'No outstanding balance found. Exiting...\');')
            print('No outstanding balance found. Exiting...')
            time.sleep(10)
            return
    except NoSuchElementException:
        print('An outstanding balance exists... Continuing...')
    
    # Next Step Page
    driver.find_element(By.XPATH, value='//*[@id="ctl02_hlinkNextStep"]').click()
    driver.find_element(By.XPATH, value='//*[@id="ctl02_hlinkNextStep"]').click()
    # NEW PAYER INFO PAGE
    driver.find_element(By.XPATH, value ='//*[@id="ctl02_txtFirstName"]').send_keys(secrets.PayerInfo['FirstName'])
    driver.find_element(By.XPATH, value ='//*[@id="ctl02_txtLastName"]').send_keys(secrets.PayerInfo['LastName'])
    driver.find_element(By.XPATH, value ='//*[@id="ctl02_txtCivic"]').send_keys(secrets.PayerInfo['HouseNumber'])
    driver.find_element(By.XPATH, value ='//*[@id="ctl02_txtEmail"]').send_keys(secrets.PayerInfo['Email'])
    driver.find_element(By.XPATH, value ='//*[@id="ctl02_txtStreet"]').send_keys(secrets.PayerInfo['Street'])
    driver.find_element(By.XPATH, value ='//*[@id="ctl02_txtCity"]').send_keys(secrets.PayerInfo['City'])
    Select(driver.find_element(By.ID, value='ctl02_ddlState')).select_by_visible_text(secrets.PayerInfo['State'])
    driver.find_element(By.XPATH, value ='//*[@id="ctl02_txtZipCode"]').send_keys(secrets.PayerInfo['Zip'])
    driver.find_element(By.XPATH, value ='//*[@id="ctl02_hlinkNextStep"]').click()
    driver.find_element(By.XPATH, value ='//*[@id="main-container"]/form/div/div[2]/div/input').click()

    #Payment Page
    driver.find_element(By.XPATH, value ='//*[@id="customer.dayPhone.formattedText"]').send_keys(secrets.PayerInfo['Phone'])
    if secrets.handlePayment == True:
        if(secrets.payment_method == 'bank'):
            payWithBank(driver)
        elif (secrets.payment_method == 'credit'):
            payWithCreditCard(driver)
        elif (secrets.payment_method == 'debit'):
            payWithDebitCard(driver)
    else:
        driver.execute_script("alert('Payment must be manually entered from this point. Handle Payment variable is False. Browser closes in 10 minutes.');")
        time.sleep(600)
        return
    time.sleep(2)
    # Submit 
    driver.find_element(By.XPATH, value ='//*[@id="main-container"]/form/div[2]/div[2]/div/input[1]').click()

    if secrets.fullyAutomated:
        time.sleep(6)
        # TERMS AND CONDITIONS AGREEMENT!!
        driver.find_element(By.XPATH, value ='//*[@id="main-container"]/form/div/div/div[6]/div/div/label/span').click()
        # FINAL SUBMIT BUTTON!!!
        driver.find_element(By.XPATH, value ='//*[@id="make-payment-btn"]').click()
    else:
        driver.execute_script("alert('Fully Automated variable is set to False. You must manually submit your payment. You have 5 minutes before the browser closes.');")
        time.sleep(300)

# Main Program
def main():
    try:
        i = 0
        for account in ACCOUNTS:
            print(f'Now running for account: {account} and barcode: {BARCODES[i]}')
            automate(account, BARCODES[i])
            time.sleep(2)
            i+=1
            print()
    except Exception as e:
        print(e)
        driver.execute_script("alert('Error occurred. Browser closes in 5 minutes.');")
        time.sleep(300)
        return

if __name__ == '__main__':
    main()
    time.sleep(3)
