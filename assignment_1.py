with open('input_1.txt') as file_object:
    lines = file_object.readlines()
    text = ''.join(lines)
    
import re
words = re.findall(r"[a-zA-Z]+", text.lower())
print   (words)

def count_words(words):
    return len(words)

def count_unique_words(words):
    return len(set(words))

def count_characters_with_spaces(text):
    return len(text)

def count_characters_no_spaces(text):
    return len(re.sub(r"\s", "", text))

def average_word_length(words):
    total_letters = sum(len(word) for word in words)
    return round(total_letters / len(words), 1) if words else 0.0

from collections import Counter
def most_common_words(words):
    freq = Counter(words)
    max_count = max(freq.values())
    common = [word for word, count in freq.items() if count == max_count]
    return ", ".join(sorted(common)), max_count

word_count = count_words(words)
unique_words = count_unique_words(words)
char_with_spaces = count_characters_with_spaces(text)
char_no_spaces = count_characters_no_spaces(text)
avg_length = average_word_length(words)
common_words, common_freq = most_common_words(words)

lines = [
    f"Word count: {word_count}",
    f"Unique words: {unique_words}",
    f"Characters (with spaces): {char_with_spaces}",
    f"Characters (no spaces): {char_no_spaces}",
    f"Average word length: {avg_length:.1f}",
    f"Most common word(s): {common_words} ({common_freq})"
]

for line in lines:
    print(line)

with open("output_1_.txt") as file:
    for line in lines:
        file.write(line + "\n")




with open('input_2.txt') as file_object:
    lines = file_object.readlines()
    text = ''.join(lines)


import re
words = re.findall(r"[a-zA-Z]+", text.lower())


def count_words(words):
    return len(words)

def count_unique_words(words):
    return len(set(words))

def count_characters_with_spaces(text):
    return len(text)

def count_characters_no_spaces(text):
    return len(re.sub(r"\s", "", text))

def average_word_length(words):
    total_letters = sum(len(word) for word in words)
    return round(total_letters / len(words), 1) if words else 0.0

from collections import Counter
def most_common_words(words):
    freq = Counter(words)
    max_count = max(freq.values())
    common = [word for word, count in freq.items() if count == max_count]
    return ", ".join(sorted(common)), max_count


word_count = count_words(words)
unique_words = count_unique_words(words)
char_with_spaces = count_characters_with_spaces(text)
char_no_spaces = count_characters_no_spaces(text)
avg_length = average_word_length(words)
common_words, common_freq = most_common_words(words)


lines = [
    f"Word count: {word_count}",
    f"Unique words: {unique_words}",
    f"Characters (with spaces): {char_with_spaces}",
    f"Characters (no spaces): {char_no_spaces}",
    f"Average word length: {avg_length:.1f}",
    f"Most common word(s): {common_words} ({common_freq})"
]

for line in lines:
    print(line)

for line in lines:
    print(line)

with open("output_2_.txt", "w") as file:
    for line in lines:
        file.write(line + "\n")


with open('input_3.txt') as file_object:
    lines = file_object.readlines()
    text = ''.join(lines)
import re
words = re.findall(r"[a-zA-Z]+", text.lower())
def count_words(words):
    return len(words)

def count_unique_words(words):
    return len(set(words))

def count_characters_with_spaces(text):
    return len(text)

def count_characters_no_spaces(text):
    return len(re.sub(r"\s", "", text))

def average_word_length(words):
    total_letters = sum(len(word) for word in words)
    return round(total_letters / len(words), 1) if words else 0.0

from collections import Counter
def most_common_words(words):
    freq = Counter(words)
    max_count = max(freq.values())
    common = [word for word, count in freq.items() if count == max_count]
    return ", ".join(sorted(common)), max_count

word_count = count_words(words)
unique_words = count_unique_words(words)
char_with_spaces = count_characters_with_spaces(text)
char_no_spaces = count_characters_no_spaces(text)
avg_length = average_word_length(words)
common_words, common_freq = most_common_words(words)


lines = [
    f"Word count: {word_count}",
    f"Unique words: {unique_words}",
    f"Characters (with spaces): {char_with_spaces}",
    f"Characters (no spaces): {char_no_spaces}",
    f"Average word length: {avg_length:.1f}",
    f"Most common word(s): {common_words} ({common_freq})"
]

for line in lines:
    print(line)

with open("output_3_.txt", "w", encoding="utf-8") as file:
    for line in lines:
        file.write(line + "\n")