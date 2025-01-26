from dataclasses import dataclass


@dataclass
class Suit:

    lower: str
    short: str
    order: int


SUIT_MAN = Suit("man", "m", 0)
SUIT_PIN = Suit("pin", "p", 1)
SUIT_SOU = Suit("sou", "s", 2)


@dataclass
class Suits:

    man = SUIT_MAN
    pin = SUIT_PIN
    sou = SUIT_SOU
    short = [SUIT_MAN.short, SUIT_PIN.short, SUIT_SOU.short]


@dataclass
class ShapeList:

    def __init__(self, type, shapes, order=0):
        self.type = type
        self.shapes = shapes
        self.order = order

    def reversed(self):
        def reverse(shape):
            reversed_shape = [10 - int(c) for c in shape]
            reversed_shape = sorted(reversed_shape)
            reversed_shape = ''.join(str(value) for value in reversed_shape)
            return reversed_shape

        reversed_list = []
        for shape in self.shapes:
            reversed_shape = reverse(shape)
            reversed_list.append(reversed_shape)
        return reversed_list


FLOATER_LIST1 = ShapeList(1, ["147", "144", "14", "146", "145", "124", "1224", "157", "156",
                              "1", "134", "1123", "1567", "1456", "14556", "15", "1346",
                              "2", "13468", "1345"], 0)
FLOATER_LIST9 = ShapeList(9, FLOATER_LIST1.reversed(), 0)

FLOATER_LIST2 = ShapeList(2, ["245", "257", "2457", "255", "258", "25", "268", "2579", "267",
                              "2", "24579", "2678", "2567", "25667", "2456", "2234", "26", "3"], 1)
FLOATER_LIST8 = ShapeList(8, FLOATER_LIST2.reversed(), 1)

FLOATER_LIST3 = ShapeList(3, ["23578", "2", "356", "368", "336", "114", "36", "377", "379", "378",
                              "3", "1233", "3678", "36778", "1234", "37", "2344", "3567", "3345",
                              "3445", "2345", "3456", "334566", "1234567", "2345678"], 2)
FLOATER_LIST7 = ShapeList(7, FLOATER_LIST3.reversed(), 2)


@dataclass
class FloaterType:

    label: str
    first: int
    second: int
    order: int


FLOATER_TYPE19 = FloaterType("19", 1, 9, 0)
FLOATER_TYPE28 = FloaterType("28", 2, 8, 1)
FLOATER_TYPE37 = FloaterType("37", 3, 7, 2)


def get_floater_list(type):
    match type:
        case FLOATER_LIST1.type:
            return FLOATER_LIST1.shapes
        case FLOATER_LIST9.type:
            return FLOATER_LIST9.shapes
        case FLOATER_LIST2.type:
            return FLOATER_LIST2.shapes
        case FLOATER_LIST8.type:
            return FLOATER_LIST8.shapes
        case FLOATER_LIST3.type:
            return FLOATER_LIST3.shapes
        case FLOATER_LIST7.type:
            return FLOATER_LIST7.shapes
