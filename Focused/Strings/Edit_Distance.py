## Work in Progress..will remove this comment when finished
def edit_distance(word1, word2):
    lookup_word1 = {}
    lookup_word2 = {}
    word1_list = [''] * len(word1)
    word2_list = [''] * len(word2)
    word1_set = set()
    word2_set = set()

    
    for i, chr in enumerate(word1):
        word_lst = lookup_word1.get(chr, [])
        word_lst.append(i)
        lookup_word1[chr] = word_lst

    for i, chr in enumerate(word2):
        word_lst = lookup_word2.get(chr, [])
        word_lst.append(i)
        lookup_word2[chr] = word_lst
    '''
    match_count = 0
    last_word1_index = -1

    for word2_index, chr in enumerate(word2):
        word1_pos = lookup_word1.get(chr,[])
        
        word1_index = -1
        for pos in word1_pos:
            word1_index = pos
            if pos < last_word1_index:
                continue
            break
        if word1_index == -1:
            continue
        
        word1_list.insert(word1_index, chr)
        word2_list.insert(word2_index, chr)
    '''
    print(word1_list)
    print(word2_list)
    print(lookup_word1)
    print(lookup_word2)


    for chr in word2:
        print(f"{chr} : {lookup_word1.get(chr, [])} and {lookup_word2.get(chr, [])}")
        
    return lookup_word1


print("\n")
print(edit_distance("intention", "execution"))
print("\n")