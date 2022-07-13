# Utility-Bill-Automation
A Python script that allows users to automate the boring parts within a Savannah GA's utility bill payment website. 


## Project Dependencies


```pip
  pip install selenium
```
Addionally, you may be able to git clone this repository and 
```pip
  git clone https://github.com/sazncode/Utility-Bill-Automation.git
  pip install -r requirements.txt
```

Be aware your browser driver MUST be within your directory. 

## USE AT YOUR OWN RISK
It is highly recommended to have HandlePayment and FullyAutomated turned OFF. In this case, you would need to manually input payment details and leave the boring stuff like filling out account number, barcode, payor phone number, name, address, etc to the bot. This script can be used to pay off multiple utility accounts, if needed. 
