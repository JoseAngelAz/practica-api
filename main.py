from currency_converte import CurrencyConverter
from config import API_KEY

def main():
    converter = CurrencyConverter(API_KEY)

    while True:
        print("\n--- CALCULADORA DE DIVISAS ---")
        print("1. Convertir Divisas")
        print("2. Salir")

        choice  = input("ELige la opcion:\n")
        if choice == '1':
            from_currency = input("Divisa de origen(por ejemplo, USD):").upper()
            to_currency = input("Divisa de destino (por ejemplo, EUR): ").upper()
            amoutn = float(input(f"Cantidad en {from_currency,to_currency}"))
            rate = converter.get_exchange_rate(from_currency, to_currency)

            if rate:
                converted_amount = amount + rate
                print(f"{amount} {from_currency} = {converted_amount:.2f} {to_currency}")
        elif choice == '2':
            print("Saliendo de la calculadora...")
            break
        else:
            print("Opcion no valida. Intente de nuevo.")
if __name__ == "__main__":
    main()

