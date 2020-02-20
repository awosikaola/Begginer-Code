def reverse(rev):
    case = ''
    index = len(rev)
    while index > 0:
        case += rev[index -1]
        index = index-1
    return case

print (reverse('asdfisagoat'))
