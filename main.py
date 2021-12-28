"""
IP Address Lookup
Programmed by: Paramon Yevstigneyev
Programmed in: Python 3.8.3 (64-Bit)
Description:
This is a program that will allow a user,
to look up an IPv4 or IPv6 address.
It will display the country that
it's reserved for.

ex.
2.17.12.1 an IPv4 address range reserved for Russian Federation.
2001:FE80:CAFE::1 is an IPv6 address range reserved for Switzerland.
"""
import lookup

def LookingUpIP(bol):

    looking_upIP = bol
    while looking_upIP:
        
        if bol:
            lookup.ip_info()

        elif not bol:
            break
try:
    print("IP Address Lookup\n")
    LookingUpIP(True)

# If the user presses a
# keyboard shortcut such as
# ctrl + c. It will prevent
# the progam from pulling up an error.
except KeyboardInterrupt:
    print()
    LookingUpIP(False)

    

# If the user enters an invalid
# IPv4 or IPv6 address. It will
# tell the user they entered an
# invalid IPv4/v6 address.
except KeyError:
    print("Invalid IP Address\n")
    LookingUpIP(True)

except:
    LookingUpIP(True)
