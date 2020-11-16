name_of_the_book=['the','great','expidition','of','the','great','alexander']
word_counter={}
for word in name_of_the_book:
    if word not in word_counter:
        word_counter[word]=1
    else:
        word_counter[word] += 1
    print(word_counter)