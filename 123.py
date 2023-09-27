def some_func(c, b):
    return c + b

print(some_func(3, 4))


def drop_cap(words):
    split_words = words.split(" ")
    for word in split_words:
        if len(word) > 2:
            word.capitalize()
    print(split_words)


drop_cap("hhh hyt u ghjj gHHHJK Ujj")