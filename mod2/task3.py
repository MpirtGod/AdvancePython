import sys


def decode(code):
    index = code.find('.')
    if index == -1:
        return code
    else:
        if index+1==len(code):
            new_code = code[:-1]
        elif code[index+1] != '.':
            new_code = code[:index - 1] + code[index:]
        else:
            new_code = code[:index-2] + code[index+1:]
        code = decode(new_code)
    return code

if __name__ == '__main__':
    # print(decode(sys.stdin.readline()))
    print(decode(input()))