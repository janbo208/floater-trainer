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


TILE_LIST1 = ["147", "144", "14", "146", "145", "124", "1224", "157", "156",
              "1", "134", "1123", "1567", "1456", "14556", "15", "1346",
              "2", "13468", "1345"]
TILE_LIST9 = ["369", "669", "69", "469", "569", "689", "6889", "359", "459",
              "9", "679", "7899", "3459", "4569", "45569", "59", "4679",
              "8", "24679", "5679"]

TILE_LIST2 = ["245", "257", "2457", "255", "258", "25", "268", "2579", "267",
              "2", "24579", "2678", "2567", "25667", "2456", "2234", "26", "3"]
TILE_LIST8 = ["568", "358", "3568", "558", "258", "58", "248", "1358", "348",
              "8", "13568", "2348", "3458", "34458", "4568", "6788", "48", "7"]

TILE_LIST3 = ["23578", "2", "356", "368", "336", "114", "36", "377", "379", "378",
              "3", "1233", "3678", "36778", "1234", "37", "2344", "3567", "3345",
              "3445", "2345", "3456", "334566", "1234567", "2345678"]
TILE_LIST7 = ["23578", "8", "457", "247", "477", "699", "47", "337", "137", "237",
              "7", "7789", "2347", "23347", "6789", "37", "6678", "3457", "5677",
              "5667", "5678", "4567", "445677", "3456789", "2345678"]


@dataclass
class TilePair:

    label: str
    first: int
    second: int
    order: int


TILEPAIR19 = TilePair("19", 1, 9, 0)
TILEPAIR28 = TilePair("28", 2, 8, 1)
TILEPAIR37 = TilePair("37", 3, 7, 2)


def get_tile_list(type):
    match type:
        case TILEPAIR19.first:
            return TILE_LIST1
        case TILEPAIR19.second:
            return TILE_LIST9
        case TILEPAIR28.first:
            return TILE_LIST2
        case TILEPAIR28.second:
            return TILE_LIST8
        case TILEPAIR37.first:
            return TILE_LIST3
        case TILEPAIR37.second:
            return TILE_LIST7
