import sys


def decode(code):
    mass = list(code)
    i=1
    while i<len(mass):
        if mass[i-1] == '.':
            if mass[i] == '.':
                for x in range(3):
                    if mass: mass.pop(i-2)
                if i!=1: i-=1
            else: mass.pop(i-1)
        else: i += 1
    if '.' in mass:
        mass.remove('.')
    return ''.join(mass)

if __name__ == '__main__':
    print(decode(sys.stdin.readline()))
