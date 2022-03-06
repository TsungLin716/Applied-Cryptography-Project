import random


def gen_random_key() -> list:
    index_ls = [a for a in range(27)]
    random.shuffle(index_ls)
    key = list()
    for index in index_ls:
        if index == 0:
            key.append(' ')
        else:
            key.append(chr(ord('a') + index - 1))
    return list(key)


def main():
    print(gen_random_key())


if __name__ == '__main__':
    main()
