import random

MaxLines = 3
MaxBet = 100
MinBet = 1

ROWS = 3
COLS = 3

SymbolCount = {"A": 2, "B": 4, "C": 6, "D": 8}

SymbolValue = {"A": 5, "B": 4, "C": 3, "D": 2}


def check_winnings(columns, lines, bet, values):
    winnings = 0
    WinningLines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            WinningLines.append(line + 1)

    return winnings, WinningLines


def get_slot_machine_spin(rows, cols, symbols):
    allSymbols = []
    for symbol, SymbolCount in symbols.items():
        for _ in range(SymbolCount):
            allSymbols.append(symbol)

    columns = []
    for _ in range(cols):
        column = []
        CurrentSymbol = allSymbols[:]
        for _ in range(rows):
            value = random.choice(CurrentSymbol)
            CurrentSymbol.remove(value)
            column.append(value)

        columns.append(column)

    return columns


def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="\n")


def deposit():
    while True:
        amount = input("What would you like to deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please enter a number.")

    return amount


def get_number_of_lines():
    while True:
        lines = input("Enter the number of lines to bet on (1-" + str(MaxLines) + ")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MaxLines:
                break
            else:
                print("Enter a valid number of lines.")
        else:
            print("Please enter a number.")

    return lines


def get_bet():
    while True:
        amount = input("What would you like to bet on each line? $")
        if amount.isdigit():
            amount = int(amount)
            if MinBet <= amount <= MaxBet:
                break
            else:
                print(f"Amount must be between ${MinBet} - ${MaxBet}.")
        else:
            print("Please enter a number.")

    return amount


def spin(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(
                f"You do not have enough to bet that amount, your current balance is: ${balance}"
            )
        else:
            break

    print(
        f"You are betting ${bet} on {lines} lines. Total bet is equal to: ${total_bet}"
    )

    Spin = get_slot_machine_spin(ROWS, COLS, SymbolCount)
    print_slot_machine(Spin)
    winnings, WinningLines = check_winnings(Spin, lines, bet, SymbolValue)
    print(f"You won ${winnings}.")
    print(f"You won on lines:", *WinningLines)
    return winnings - total_bet


def main():
    balance = deposit()
    while True:
        print(f"Current balance is ${balance}")
        answer = input("Press enter to play (q to quit).")
        if answer == "q":
            break
        balance += spin(balance)

    print(f"You left with ${balance}")


main()
