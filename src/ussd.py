import sys

user = {
    'phone_number': '+261340000808',
    'balance': 50000,
    'pin': '1234',
    'data_balance': 500,
    'credit_expiry': '30/06/2023'
}

def display_main_menu():
    print("\nBienvenue sur Yas Telma !")
    print("1. Consulter mon numéro")
    print("2. Vérifier mon solde")
    print("3. Transférer du crédit")
    print("4. Changer mon code PIN")
    print("5. Forfaits et Internet")
    print("6. Appels et SMS")
    print("7. Services bancaires")
    print("8. Services Yas")
    print("9. Quitter")
    return input("Choisissez une option (1-9) : ")

def check_phone_number():
    print(f"\nVotre numéro Yas Telma est : {user['phone_number']}")
    input("\nAppuyez sur Entrée pour revenir au menu principal...")

def check_balance():
    print(f"\nVotre solde actuel est : {user['balance']} Ar")
    print(f"Votre solde data : {user['data_balance']} Mo")
    print(f"Validité du crédit jusqu'au : {user['credit_expiry']}")
    input("\nAppuyez sur Entrée pour revenir au menu principal...")

def transfer_credit():
    print("\n--- Transfert de crédit ---")
    amount = input("Entrez le montant à transférer (Ar) : ")
    recipient = input("Entrez le numéro du destinataire (+261...) : ")
    pin = input("Entrez votre code PIN : ")

    if pin != user['pin']:
        print("\nCode PIN incorrect !")
    elif not amount.isdigit() or int(amount) <= 0:
        print("\nMontant invalide !")
    elif int(amount) > user['balance']:
        print("\nSolde insuffisant !")
    else:
        user['balance'] -= int(amount)
        print(f"\nTransfert de {amount} Ar vers {recipient} effectué avec succès !")
        print(f"Nouveau solde : {user['balance']} Ar")

    input("\nAppuyez sur Entrée pour revenir au menu principal...")

def change_pin():
    print("\n--- Changement de code PIN ---")
    current_pin = input("Entrez votre code PIN actuel : ")

    if current_pin != user['pin']:
        print("\nCode PIN incorrect !")
    else:
        new_pin = input("Entrez votre nouveau code PIN (4 chiffres) : ")
        if len(new_pin) != 4 or not new_pin.isdigit():
            print("\nLe nouveau PIN doit être composé de 4 chiffres !")
        else:
            user['pin'] = new_pin
            print("\nCode PIN changé avec succès !")

    input("\nAppuyez sur Entrée pour revenir au menu principal...")

def internet_menu():
    print("\n--- Forfaits et Internet ---")
    print("1. Forfaits Internet")
    print("2. Forfaits appels + Internet")
    print("3. Achat bundle Internet")
    print("4. Retour au menu principal")
    choice = input("Choisissez une option (1-4) : ")

    if choice == '1':
        print("\nForfaits Internet disponibles:")
        print("1. 100 Mo - 1 000 Ar")
        print("2. 500 Mo - 5 000 Ar")
        print("3. 1 Go - 10 000 Ar")
        print("4. 5 Go - 25 000 Ar")
        input("\nAppuyez sur Entrée pour revenir...")
    elif choice == '2':
        print("\nForfaits appels + Internet:")
        print("1. 30 min + 100 Mo - 2 000 Ar")
        print("2. 60 min + 500 Mo - 5 000 Ar")
        print("3. 120 min + 1 Go - 10 000 Ar")
        input("\nAppuyez sur Entrée pour revenir...")
    elif choice == '3':
        print("\nBundle Internet:")
        print("1. 10 Mo - 100 Ar")
        print("2. 50 Mo - 500 Ar")
        print("3. 100 Mo - 1 000 Ar")
        input("\nAppuyez sur Entrée pour revenir...")

def calls_sms_menu():
    print("\n--- Appels et SMS ---")
    print("1. Forfaits appels")
    print("2. Forfaits SMS")
    print("3. Forfaits appels internationaux")
    print("4. Retour au menu principal")
    choice = input("Choisissez une option (1-4) : ")

    if choice == '1':
        print("\nForfaits appels:")
        print("1. 30 min - 1 000 Ar")
        print("2. 60 min - 2 000 Ar")
        print("3. 120 min - 4 000 Ar")
        input("\nAppuyez sur Entrée pour revenir...")
    elif choice == '2':
        print("\nForfaits SMS:")
        print("1. 50 SMS - 500 Ar")
        print("2. 100 SMS - 1 000 Ar")
        print("3. 200 SMS - 2 000 Ar")
        input("\nAppuyez sur Entrée pour revenir...")
    elif choice == '3':
        print("\nForfaits appels internationaux:")
        print("1. 10 min vers l'international - 5 000 Ar")
        print("2. 30 min vers l'international - 15 000 Ar")
        input("\nAppuyez sur Entrée pour revenir...")

def banking_menu():
    print("\n--- Services bancaires ---")
    print("1. Paiement de factures")
    print("2. Transfert d'argent")
    print("3. Rechargement compte bancaire")
    print("4. Retour au menu principal")
    choice = input("Choisissez une option (1-4) : ")

    if choice == '1':
        print("\nPaiement de factures:")
        print("1. Eau - JIRAMA")
        print("2. Electricité - JIRAMA")
        print("3. TV - ORANGE")
        input("\nAppuyez sur Entrée pour revenir...")
    elif choice == '2':
        print("\nTransfert d'argent:")
        print("1. Vers compte bancaire")
        print("2. Vers mobile money")
        input("\nAppuyez sur Entrée pour revenir...")
    elif choice == '3':
        print("\nRechargement compte bancaire:")
        amount = input("Entrez le montant à recharger : ")
        print(f"Rechargement de {amount} Ar effectué avec succès !")
        input("\nAppuyez sur Entrée pour revenir...")

def yas_services_menu():
    print("\n--- Services Yas ---")
    print("1. Yas Play (Musique)")
    print("2. Yas News (Actualités)")
    print("3. Yas Games (Jeux)")
    print("4. Retour au menu principal")
    choice = input("Choisissez une option (1-4) : ")

    if choice == '1':
        print("\nYas Play - Écoutez de la musique:")
        print("1. Top 100")
        print("2. Musique malgache")
        print("3. Musique internationale")
        input("\nAppuyez sur Entrée pour revenir...")
    elif choice == '2':
        print("\nYas News - Restez informé:")
        print("1. Actualités nationales")
        print("2. Actualités internationales")
        print("3. Sports")
        input("\nAppuyez sur Entrée pour revenir...")
    elif choice == '3':
        print("\nYas Games - Jeux mobiles:")
        print("1. Jeux d'action")
        print("2. Jeux de puzzle")
        print("3. Jeux de sport")
        input("\nAppuyez sur Entrée pour revenir...")

def run_ussd_service():
    while True:
        choice = display_main_menu()

        if choice == '1':
            check_phone_number()
        elif choice == '2':
            check_balance()
        elif choice == '3':
            transfer_credit()
        elif choice == '4':
            change_pin()
        elif choice == '5':
            internet_menu()
        elif choice == '6':
            calls_sms_menu()
        elif choice == '7':
            banking_menu()
        elif choice == '8':
            yas_services_menu()
        elif choice == '9':
            print("\nMerci d'avoir utilisé Yas Telma. Au revoir !")
            sys.exit()
        else:
            print("\nOption invalide. Veuillez choisir une option valide.")
            input("\nAppuyez sur Entrée pour continuer...")

if __name__ == "__main__":
    run_ussd_service()

