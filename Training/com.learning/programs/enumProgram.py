__author__ = 'aganiger'

from enum import Enum
import enum


class Country(Enum):
    Afghanistan = 93
    Albania = 355
    Algeria = 213
    Andorra = 376
    Angola = 244
    Antarctica = 672

for data in Country:
    print(data.name + ":" + str(data.value))


class CountryCode(enum.IntEnum):
    Afghanistan = 93
    Albania = 355
    Algeria = 213
    Andorra = 376
    Angola = 244
    Antarctica = 672


for data in sorted(CountryCode):
    print(data.name + ":" + str(data.value))

CountryCodeList = list(map(int, CountryCode))
print(CountryCodeList)


class Country(enum.Enum):
    Afghanistan = 93
    Albania = 355
    Algeria = 213
    Andorra = 376
    India = 244
    Antarctica = 672
    Angola = 244


for country in Country:
    print("%s %d" % (country.name, country.value))