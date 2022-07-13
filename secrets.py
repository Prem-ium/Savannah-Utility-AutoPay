handlePayment = True
fullyAutomated = False
payment_method = 'credit'

# Examples:
#payment_method = 'bank'
#payment_method = 'credit'
#payment_method = 'debit'

ACCOUNT_NUMBERS = "youraccountnumberhere, yourotheraccountnumberhere_ifyouhavemorethanone"
BARCODES = "yourbarcodehere, yourotherbarcodehere_ifyouhavemorethanone"

PayerInfo = {
    'FirstName': 'Fake',
    'LastName': 'Name',
    'HouseNumber': '220',
    'Street': 'Fake Address',
    'City': 'Atlanta',
    'State': 'Georgia',
    'Zip': '30301',
    'Email': 'fake_email@gmail.com',
    'Phone': '9087653849',
}

bank = {
    'Type': 'Checking',
    'Routing': '041215663',
    'Account': '75478206529',
    'Banker': 'FAKEBANK',
    'Holder': 'FAKE NAME',
}

# Luhn algorithm
cc_card = {
    'number': '4111111111111111',
    'expirationMonth': '02',
    'expirationYear': '2023',
    'ccv': '123',
    'cardholder': 'Dumb Dumb',
}

db_card = {
    'number': '4111111111111111',
    'expirationMonth': '11',
    'expirationYear': '2023',
    'ccv': '123',
    'cardholder': 'Dumb Dumb',
}
