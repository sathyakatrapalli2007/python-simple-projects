unique_words=[]
with open ("blank_space.txt","r") as f:
    list_of_all_words=f.readlines()
    for line in list_of_all_words:
        words=line.split()
        for word in words:
            if word not in unique_words:
                unique_words.append(word)
print(unique_words)