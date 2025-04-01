<h1 align="center">🏤 Savannah, GA Utility Bill Pay Automation 🤖</h1>

<p align="center">
   Automate water utility bill payments for Savannah, GA properties using this Python-based Selenium script. Designed to save time for homeowners, landlords, and businesses handling multiple accounts.
</p>

<p align="right"> 
   <img src="https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54"/>
   <img src="https://img.shields.io/badge/-selenium-%43B02A?style=for-the-badge&logo=selenium&logoColor=white"/>
   <a href="https://github.com/sponsors/Prem-ium" target="_blank">
      <img src="https://img.shields.io/badge/sponsor-30363D?style=for-the-badge&logo=GitHub-Sponsors&logoColor=#EA4AAA" alt="Github Sponsor"/>
   </a>
</p>

---


This project provides a **Python Selenium script** that automates the process of paying water utility bills for properties located in Savannah, GA. Designed to address frustrations with the slow, repetitive government website, this script streamlines bill payments, saving time and reducing errors for landlords, property managers, and business owners managing multiple properties.

---

## 🔧 Installation

1. **Clone this repository, navigate into the folder, and install dependencies**:
   ```sh
   git clone https://github.com/Prem-ium/Savannah-Utility-AutoPay.git
   cd Savannah-Utility-AutoPay
   pip install -r requirements.txt
   ```
2. **Set up your `.env` file** (refer to the example and variable descriptions below).
3. **Run the script**:
   ```sh
   python main.py
   ```

---

## ⚙️ Environment Variables

To configure the script, add the following variables to your `.env` file:

### Required Variables:

| Variable         | Description                             | Type   |
|------------------|-----------------------------------------|--------|
| `ACCOUNT_NUMBERS`| Comma-separated list of account numbers | String |
| `BARCODES`       | Comma-separated list of barcodes        | String |
| `PAYOR_INFO`     | JSON string with payor's information    | JSON   |

### Optional Variables:

| Variable         | Description                                          | Type    | Default |
|------------------|------------------------------------------------------|---------|---------|
| `HANDLE_PAYMENT` | Automates payment handling (true/false)              | Boolean | True    |
| `FULLY_AUTOMATED`| Enables full automation (true/false)                 | Boolean | False   |
| `MULTI_THREADING`| Runs multithreaded automation (true/false)           | Boolean | True    |
| `PAYMENT_METHOD` | Payment method: `bank`, `credit`, or `debit`         | String  | bank    |
| `BANK`           | JSON string with bank account details                | JSON    |         |
| `CREDIT_CARD`    | JSON string with credit card details                 | JSON    |         |
| `DEBIT_CARD`     | JSON string with debit card details                  | JSON    |         |

Replace placeholder values with real details before running the script.

---

## 🙋‍♂️ FAQ

### How does this repository help Savannah property owners?
This repository automates the repetitive task of paying water utility bills. By handling account logins, payment submissions, and confirmations, it significantly reduces the time spent on bill payments for individuals managing multiple accounts.

### What inspired this project?
The Savannah water bill payment website is slow and cumbersome, often requiring repetitive information entry for each property. This script simplifies the process, saving time and frustration.

---

## 💻 Example Output

```sh
--------------------------------------------------
Use "FULLY_AUTOMATED" at your own risk. Storing financial information in plain text is not recommended.
If you insist on using that feature, please consider using Privacy to protect yourself from theft.

Privacy allows you to create virtual cards locked to specific merchants. Sign up here for $5:
https://privacy.com/join/G25UX
--------------------------------------------------
Multi-threading enabled. Running automation in parallel...
--------------------------------------------------
Account: 07XXX0 Barcode: 12XX00 Payment Method: bank

Account: 07XXX0 with barcode: 12XX00 found.
An outstanding balance exists... Continuing...

------------------------
Account:    07XXX0
Barcode:    12XX00
Amount due: $125.21
------------------------
07XXX0:BANK Fully Automated variable is set to False. You must manually submit your payment. You have 5 minutes before the browser closes.

Done!
Thank you for using Prem-ium's Savannah, GA Water Bill Automation Script!
```
OR
```
--------------------------------------------------
Multi-threading enabled. Running automation in parallel...
--------------------------------------------------
Account: 07XXX0 Barcode: 12XX00 Payment Method: bank


Account: 07XXX0 with barcode: 12XX00 found.
--------------------------------------------------
No outstanding balance found for account 07XXX0 and 12XX00. Exiting...
--------------------------------------------------
```
---

## ❤️ Support My Work

If you find this project helpful, you can show your support in the following ways:

1. **GitHub Sponsors** 
   [![GitHub Sponsor](https://img.shields.io/badge/sponsor-30363D?style=for-the-badge&logo=GitHub-Sponsors&logoColor=#EA4AAA)](https://github.com/sponsors/Prem-ium)

2. **Buy Me A Coffee**  
   [![Buy Me A Coffee](https://img.shields.io/badge/Buy%20Me%20a%20Coffee-ffdd00?style=for-the-badge&logo=buy-me-a-coffee&logoColor=black)](https://www.buymeacoffee.com/prem.ium)

3. **Referral Links**  
   Use my curated [Referral Links](https://github.com/Prem-ium/Referral-Link-Me/blob/main/README.md) to earn rewards and support my project(s).

---

## ⚠️ Disclaimer

Please exercise caution when storing sensitive financial information such as bank or card details in this script. Saving this information in plain text files (e.g., `.env`) is not secure and could expose you to theft.  

We highly recommend using [Privacy.com](https://app.privacy.com/join/G25UX) to generate virtual cards for added security. By doing so, you can control, pause, or close your cards anytime.

---

## 📜 License

This project is licensed under the [MIT License](https://github.com/Prem-ium/Savannah-Utility-AutoPay/blob/main/LICENSE.MD).