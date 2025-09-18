#words = input().lower().split()
words = "a aa abC aa ac abc bcd a".lower().split()
print(f"{words = !s}")

# Création d'un dictionnaire, clé: mot (unique), valeur: nombre d'occurences

frequency_dictionary = {}
for w in words:
    if w not in frequency_dictionary:
        frequency_dictionary[w] = 1
    else:
        frequency_dictionary[w] += 1
#print(f"{frequency_dictionary = !s}")

for w, c in frequency_dictionary.items():
    print(f"{w} {c}")

#words_copy = []
#last_words = []

# for w in words:
#     c = 0
#     for ww in words:
#         if w == ww:
#             c += 1
#             if w not in last_words:
#                 last_words.append(w)
#     print(f"{w} {c}")

        # if w == ww:
        #     c += 1
        #     last_word = w
        #     if w != last_word:
        #         words_copy.append(w)
        #         last_word = w
            #print(f"{w} == {ww} : count: {c} : {words_copy = !s} : {last_word = !s}")


# for i in range(len(w)):
#     c = 0
#     last_word = ""
#     print(f"{w = !s}\n{w_copy = !s}\n{c = !s}\n__________")
#     for word in w:
#         if w[i] == word:
#             c += 1
#             print(f"true: {w[i] = !s} : {word = !s} : {w_copy = !s}")
#             if w[i] != last_word:
#                 w_copy.append(word)
#                 last_word = word
#         else:
#             print(f"false: {w[i] = !s} : {word = !s} : {w_copy = !s}")
#         #print(f"{w[i] = !s} : {word = !s}: True" if w[i] == word else f"{w[i] = !s} : {word = !s}: False")
#     #print(f"word: {w[i]} c: {c}")
#     print(":__________:")



# for word in w:
#     print(word)
#     print("_________")
#     #if w[i] == word:
#         #c += 1
#         #print(f"{w[i] = !s} : {word = !s}")
#     for i in range(0,len(w),1):
#         print(i)
#         print(w[i])
#         if w[i] == word:
#             print(f"{w[i] = !s} : {word = !s}")