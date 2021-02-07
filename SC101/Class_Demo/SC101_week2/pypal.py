
WITHDRAW_LIMIT = 1000
INITIAL_MONEY = 0


class Pypal:
    def __init__(self, username, money=INITIAL_MONEY, withdraw_limit=WITHDRAW_LIMIT):
        self.__n = username
        self.__m = money
        self.__w_l = withdraw_limit

    def withdraw(self, amount):
        if amount > self.__w_l:
            print('Exceed Limit')
        elif self.__m - amount < 0:
            print('Illegal')
        else:
            self.__m -= amount
            print(f'{self.__n}: {self.__m}')

    # Getter
    def get_money(self):
        return self.__m

    # Setter
    def set_name(self, new_name):
        self.__n = new_name
        print('Successfully updated!')


def bank():
    jerry_a = Pypal('YH', money=1000, withdraw_limit=700)
    jerry_a.withdraw(1000)
    jerry_a.withdraw(700)
    jerry_a.set_name('YHL')
    jerry_a.withdraw(300)
    print("")

    bob_a = Pypal('Robert', money=10000, withdraw_limit=5000)
    bob_a.withdraw(3000)
    bob_money = bob_a.get_money()
    print('Bob has', bob_money)

if __name__ == '__main__':
    bank()