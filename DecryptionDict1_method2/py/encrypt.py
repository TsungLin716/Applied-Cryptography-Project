import random
import decrypt


def char_to_index(c: chr) -> int:
    if c == ' ':
        return 0
    else:
        return ord(c) - ord('a') + 1


def gen_random_char() -> chr:
    random_num = random.randint(0, 26)  # end is inclusive
    if random_num == 0:
        return ' '
    else:
        return chr(ord('a') + random_num - 1)


def gen_random_number(seed):
    random.seed(seed)
    return random.uniform(0, 1)


def encrypt(plain_text: str, prob_of_random_ciphertext: float, key: list) -> str:
    l = len(plain_text)
    random_len = 0

    plain_index = 0
    cipher_text = ""

    # Just for check.
    r_bits = ""

    while len(cipher_text) < l + random_len:
        coin_value = gen_random_number(l ^ len(cipher_text))
        if coin_value > prob_of_random_ciphertext:
            pc = plain_text[plain_index]
            j = char_to_index(pc)
            cipher_text = cipher_text + key[j]
            plain_index += 1
        else:
            r = gen_random_char()
            cipher_text = cipher_text + r
            random_len += 1
            r_bits += r

    print("# of random bits added: ", random_len)
    print("total added random bits: ", r_bits)
    print("added random bit freq: ", decrypt.count_char_freq(r_bits))

    return cipher_text


def main():
    plain_text = "he is a dumb ass"
    key = " abcdefghijklmnopqrstuvwxyz"
    prob_of_random_ciphertext = 0.2
    print(encrypt(plain_text, prob_of_random_ciphertext, key))


if __name__ == '__main__':
    main()
