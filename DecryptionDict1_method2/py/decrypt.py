import random
import numpy as np


def count_char_freq(sentence: str) -> dict:
    d = {}
    for c in sentence:
        d[c] = d.get(c, 0) + 1
    return d


def get_sorted_char_count(sentence: str) -> list:
    dic = count_char_freq(sentence)
    count = []
    for c in dic.values():
        count.append(c)

    while len(count) < 27:
        count.append(0)

    count.sort(reverse=True)
    return count


def get_euclidean_dist(count1: list, count2: list) -> float:
    arr1 = np.asarray(count1)
    arr2 = np.asarray(count2)
    dist = np.linalg.norm(arr1-arr2)
    return dist


def decrypt(plain_candidates: list, cipher_text: str) -> str:
    plain_counts_ls = []
    for p in plain_candidates:
        plain_counts_ls.append(get_sorted_char_count(p))
        print("plain_count_sorted: ", get_sorted_char_count(p))
    cipher_counts = get_sorted_char_count(cipher_text)
    print("cipher_count_sorted: ", cipher_counts)

    dist_ls = []
    for pc in plain_counts_ls:
        dist_ls.append(get_euclidean_dist(pc, cipher_counts))

    print("dist list: ", dist_ls)

    return plain_candidates[np.argmin(dist_ls)]


def main():
    print(get_euclidean_dist([4,3,2], [4,3,2]))


if __name__ == '__main__':
    main()

