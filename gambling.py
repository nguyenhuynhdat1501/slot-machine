import random as rd
ROWS = 3
COLS = 3
MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

symbol_count = {
    "A":2,
    "B":4,
    "C":8,
    "D":6
}
def check_winnings(columns,lines,bet,values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol]*bet
            winning_lines.append(line+1)
    return winnings, winning_lines
def deposit():
    while True:
        amount = input("what would you like to deposit? $$")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("amount must be greater than 0")
        else:
            print("amount must be a number")
    return amount
def get_num_of_lines():
    while True:
        lines = input("how many lines would you like to bet on (1 - "+str(MAX_LINES)+")?")
        if lines.isdigit():
            lines = int(lines)
            if lines >= 1 and lines <= 3:
                break
            else:
                print("enter a number from 1 to 3")
        else:
            print("enter a number from 1 to 3")
    return lines
def get_bet():
    while True:
        bet = input("How much do you wanna bet?")
        if bet.isdigit():
            bet = int(bet)
            if 1 <= bet <= 100:
                break
            else:
                print(f"Bet must be between ${MIN_BET} and ${MAX_BET}")
        else:
            print("please enter a number")
    return bet
def get_slot_machine_spin(rows,cols,syms):
    all_sym = []
    for sym,count in symbol_count.items():
        for _ in  range(count):
            all_sym.append(sym)
    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_sym[:]
        for _ in range(rows):
            value = rd.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)
    return columns
def print_slot_machine(columns):
    for row in range(len(columns[0])):
         for i,column in enumerate(columns):
             if i != len(columns) - 1:
                 print(column[row],end=" | ")
             else:
                 print(column[row],end="")
         print()
def game(balance):
    lines = get_num_of_lines()
    while True:
        bet = get_bet()
        total_bet = lines*bet
        if (total_bet <= balance):
            break
        else:
            print("your deposit is not enough, please consider the amount you wanna bet")
    print(f"you are betting ${balance} on %{lines} - Total bet is equal to: ${total_bet}")
    slots = get_slot_machine_spin(ROWS,COLS,symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots,lines,bet,symbol_count)
    print(f"You won ${winnings}.")
    print(f"You won on lines:", *winning_lines)
    return winnings - total_bet
def main():
    balance = deposit()
    while True:
        print(f"Current balance is ${balance}")
        spin = input("please enter to play (q to quit)")
        if spin == "q":
            break
        balance += game(balance)
    print(f"You left with ${balance}")
main()