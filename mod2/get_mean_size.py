import sys

def get_mean_size(lines):
    file_count = len(lines)
    if file_count == 0:
        exit('Нет файлов')
    size_sum = sum([int(x.split()[4]) for x in lines])
    return size_sum/file_count

if __name__ == '__main__':
    print(get_mean_size(sys.stdin.readlines()[1:]))