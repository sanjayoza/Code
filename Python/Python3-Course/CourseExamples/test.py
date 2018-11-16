def func(word, letter):
    word = word.lower()
    letter = letter.lower()
    count = 0
    for l in word:
       if l == letter:
          count += 1
    return count

val = func("hello", "L")
print(val)
