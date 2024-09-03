class Checkbook:
    def __init__(self):
        """
        Inicializa una instancia de la clase Checkbook con un saldo inicial de 0.0.
        """
        self.balance = 0.0

    def deposit(self, amount):
        """
        Deposita una cantidad en la cuenta.

        Args:
            amount (float): La cantidad de dinero a depositar. Debe ser positiva.
        """
        if amount <= 0:
            print("Amount must be greater than zero.")
            return
        self.balance += amount
        print("Deposited ${:.2f}".format(amount))
        print("Current Balance: ${:.2f}".format(self.balance))

    def withdraw(self, amount):
        """
        Retira una cantidad de la cuenta si hay suficientes fondos.

        Args:
            amount (float): La cantidad de dinero a retirar. Debe ser positiva.
        """
        if amount <= 0:
            print("Amount must be greater than zero.")
            return
        if amount > self.balance:
            print("Insufficient funds to complete the withdrawal.")
        else:
            self.balance -= amount
            print("Withdrew ${:.2f}".format(amount))
            print("Current Balance: ${:.2f}".format(self.balance))

    def get_balance(self):
        """
        Imprime el saldo actual de la cuenta.
        """
        print("Current Balance: ${:.2f}".format(self.balance))

def main():
    """
    Función principal que maneja la interacción con el usuario.
    Permite al usuario realizar depósitos, retiros y consultar el saldo.
    """
    cb = Checkbook()
    while True:
        action = input("What would you like to do? (deposit, withdraw, balance, exit): ").strip().lower()
        if action == 'exit':
            print("Exiting the program.")
            break
        elif action == 'deposit':
            try:
                amount = float(input("Enter the amount to deposit: $").strip())
                cb.deposit(amount)
            except ValueError:
                print("Invalid amount. Please enter a numeric value.")
        elif action == 'withdraw':
            try:
                amount = float(input("Enter the amount to withdraw: $").strip())
                cb.withdraw(amount)
            except ValueError:
                print("Invalid amount. Please enter a numeric value.")
        elif action == 'balance':
            cb.get_balance()
        else:
            print("Invalid command. Please try again.")

if __name__ == "__main__":
    main()