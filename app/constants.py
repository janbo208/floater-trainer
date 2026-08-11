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

        reversed_shapes = []
        for shape in self.shapes:
            reversed_shape = reverse(shape)
            reversed_shapes.append(reversed_shape)
        reversed_type = -self.type

        return ShapeList(reversed_type, reversed_shapes, self.order)


FLOATER_LIST1 = ShapeList(1, ["147", "144", "14", "146", "145", "124", "1224", "157", "156",
                              "1", "134", "1123", "1567", "1456", "14556", "15", "1346",
                              "2", "13468", "1345"], 0)
FLOATER_LIST9 = FLOATER_LIST1.reversed()

FLOATER_LIST2 = ShapeList(2, ["245", "257", "2457", "255", "258", "25", "268", "2579", "267",
                              "2", "24579", "2678", "2567", "25667", "2456", "2234", "26", "3"], 1)
FLOATER_LIST8 = FLOATER_LIST2.reversed()

FLOATER_LIST3 = ShapeList(3, ["23578", "2", "356", "368", "336", "114", "36", "377", "379", "378",
                              "3", "1233", "3678", "36778", "1234", "37", "2344", "3567", "3345",
                              "3445", "2345", "3456", "334566", "1234567", "2345678"], 2)
FLOATER_LIST7 = FLOATER_LIST3.reversed()

PENCHAN_LIST1 = ShapeList(4, ["1224", "1246", "1244", "1245", "3", "1255", "1256", "1266", "1267",
                              "12", "12567", "12456", "11223"], 3)
PENCHAN_LIST9 = PENCHAN_LIST1.reversed()

KANCHAN_OUTER_LIST1 = ShapeList(5, ["1346", "1344", "1124", "1335", "1334", "1356", "1366", "1367",
                                    "13", "13678", "1355", "11233", "13345", "12234", "22344",
                                    "13567", "13456"], 4)
KANCHAN_OUTER_LIST9 = KANCHAN_OUTER_LIST1.reversed()

KANCHAN_INNER_LIST1 = ShapeList(6, ["3566", "3557", "3556", "3578", "35", "12346", "23446", "2235",
                                    "33455", "35678"], 5)
KANCHAN_INNER_LIST9 = KANCHAN_INNER_LIST1.reversed()

COMBINED_LIST = [FLOATER_LIST1,
                 FLOATER_LIST2,
                 FLOATER_LIST3,
                 PENCHAN_LIST1,
                 KANCHAN_OUTER_LIST1,
                 KANCHAN_INNER_LIST1,
                 ]

COMBINED_LIST_REVERSED = [FLOATER_LIST9,
                          FLOATER_LIST8,
                          FLOATER_LIST7,
                          PENCHAN_LIST9,
                          KANCHAN_OUTER_LIST9,
                          KANCHAN_INNER_LIST9,
                          ]


def get_list_type_at(index, reversed=False):
    if not reversed:
        return COMBINED_LIST[index].type
    else:
        return COMBINED_LIST_REVERSED[index].type


def get_shape_list(type):
    if type > 0:
        return COMBINED_LIST[type-1].shapes
    else:
        return COMBINED_LIST_REVERSED[-type-1].shapes


@dataclass
class TypeLabels:

    floater19 = "19"
    floater28 = "28"
    floater37 = "37"
    penchan = "penchan"
    kanchan_outer = "outer kanchan"
    kanchan_inner = "inner kanchan"


TYPELABELS_LIST = [TypeLabels.floater19, TypeLabels.floater28, TypeLabels.floater37,
                   TypeLabels.penchan, TypeLabels.kanchan_inner, TypeLabels.kanchan_outer]
