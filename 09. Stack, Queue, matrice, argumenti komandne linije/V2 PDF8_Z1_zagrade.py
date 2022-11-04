# Unosi se aritmeticki izraz kao string, npr: 2+3*(5-2)
# Napisati program koji proverava da li su zagrade pravilno uparene.

def da_li_su_dobre_zagrade(izraz):
    br_zatvorenih = 0
    br_otvorenih = 0
    for znak in izraz:
        if znak == "(":
            br_otvorenih += 1
        elif znak == ")":
            br_zatvorenih += 1
            if br_zatvorenih > br_otvorenih:
                return False

    #print(br_otvorenih,br_zatvorenih)
    #if br_otvorenih == br_zatvorenih:
    #    return True
    #else:
    #    return False
    return br_otvorenih == br_zatvorenih

test_pravilan = "(2+3)* ( 5 - 2 ) "
test_puno_otvorenih = "(2+3)* ( 5 - 2 )( "
test_puno_zatvorenih = "(2+3)* )( 5 - 2 ) "
print(da_li_su_dobre_zagrade(test_pravilan))
print(da_li_su_dobre_zagrade(test_puno_otvorenih))
print(da_li_su_dobre_zagrade(test_puno_zatvorenih))