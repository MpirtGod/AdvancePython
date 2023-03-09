import sys


def decode(code):
    result = []
    for ch in code:
        result.append(ch)

        if len(result) > 2 and result[-1] == '.' and result[-2] == '.':
            result.pop()
            result.pop()
            if result:
                result.pop()

    return ''.join(ch for ch in result if ch !='.')


if __name__ == '__main__':
    print(decode(sys.stdin.readline()))
