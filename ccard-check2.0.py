from datetime import datetime

def check_credit_card(card_number, expiration_date):
    card_info = {
        "American Express": {"prefixes": ["34", "37"], "bank": "American Express"},
        "Visa": {"prefixes": ["4"], "bank": "Visa"},
        "MasterCard": {"prefixes": ["51", "52", "53", "54", "55"], "bank": "MasterCard"},
        "Discover": {"prefixes": ["6011"], "bank": "Discover"}
    }

    bank_names = {
        "011": "Bancomer",
        "012": "Banamex",
        "014": "HSBC",
        "019": "Santander",
        "022": "Scotiabank",
        "044": "Inbursa"
    }

    countries = {
        "United States": ["4"],
        "Canada": ["4"],
        "Mexico": ["4"],
        "United Kingdom": ["51", "52", "53", "54", "55"],
        "Australia": ["51", "52", "53", "54", "55"]
    }

    card_number = card_number.replace(" ", "").replace("-", "")
    
    if len(card_number) != 16 or not card_number.isdigit():
        return False, None, None, None, None, None, None

    card_type = "Desconocido"
    bank = "Desconocido"
    country = "Desconocido"
    bank_brand = "Desconocido"
    expiration_valid = False

    for key, value in card_info.items():
        for prefix in value["prefixes"]:
            if card_number.startswith(prefix):
                card_type = key
                bank = value["bank"]
                break
    
    if card_number[:3] in bank_names:
        bank_brand = bank_names[card_number[:3]]
    
    current_date = datetime.now()
    expiration_month, expiration_year = expiration_date.split()
    expiration_date = datetime(int("20" + expiration_year), int(expiration_month), 1)
    if current_date < expiration_date:
        expiration_valid = True
    
    for country_name, country_bins in countries.items():
        for bin in country_bins:
            if card_number.startswith(bin):
                country = country_name
                break

    return True, card_type, bank, country, bank_brand, expiration_valid

card_number = input("Ingresa el número de la tarjeta de crédito: ")
expiration_date = input("Ingresa la fecha de vencimiento (mes año ej. 12 23): ")

valid, card_type, bank, country, bank_brand, expiration_valid = check_credit_card(card_number, expiration_date)

if valid:
    print("La tarjeta de crédito es válida.")
    print("Tipo de Tarjeta:", card_type)
    print("Banco:", bank)
    print("País:", country)
    print("Marca de Banco:", bank_brand)
    
    if expiration_valid:
        print("La tarjeta está activa.")
    else:
        print("La tarjeta ha expirado.")
else:
    print("La tarjeta de crédito es inválida.")