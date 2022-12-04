class Card:
    __slots__ = ['__name', '__description', '__value']


    def __init__(self, name, description, value):
        self.__name = name
        self.__description = description
        self.__value = value

    def __hash__(self):
        return hash(self.__name) + hash(self.__description) + hash(self.__value)

    def __eq__(self, __o: object) -> bool:
        if type(self) == type(__o):
            return self.__name == __o.__name and self.__description == __o.__description and self.__value == __o.__value
        return False

    def __str__(self):
        return f"{self.__name} does {self.__description} and is worth {self.__value}"

    def get_name(self):
        return self.__name

    def get_value(self):
        return self.__value

class CardCollection:
    __slots__ = ['__cards']

    def __init__(self):
        self.__cards = set()


    def add_card(self, card:Card):
        self.__cards.add(card)

    def search(self, name):
        for card in self.__cards:
            if card.get_name() == name:
                print(card)
        print("Card not found")

    def total_value(self):
        sum = 0
        for card in self.__cards:
            sum += card.get_value()
        return sum

    def __str__(self) -> str:
        result = ""
        for card in self.__cards:
            result += str(card) + '\n'
        return result

    def __lt__(self, other):
        if len(self.__cards) == len(other.__cards):
            return self.total_value() < other.total_value()
        return len(self.__cards) < len(other.__cards)


def main():
    c1 = Card('card 1', 'card 1', 1)
    c2 = Card('card 2', 'card 2', 2)
    c3 = Card('card 1', 'card 1', 1)

    cc = CardCollection()
    cc.add_card(c1)
    cc.add_card(c2)
    cc.add_card(c3)
    print(cc)



main()