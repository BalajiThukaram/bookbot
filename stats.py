def get_number_of_words(fileContents):
    return len(fileContents)

def get_char_list(fileContents):
    char_list = {}
    for content in fileContents:
        words = content.split()
        for word in words:
            for char in word:
                lower_char = char.lower()
                if(lower_char not in char_list):
                    char_list[lower_char] = 1
                else:
                    char_list[lower_char] +=1
    return char_list

def sort_on(items):
    return items['num']
def sort_dict(char_list):
    sorted_list = []
    for char in char_list:
        temp = {}
        val = char_list[char]
        temp['char'] = char
        temp['num'] = val
        sorted_list.append(temp)
    sorted_list.sort(reverse=True,key=sort_on)
    proper_list = []
    for lista in sorted_list:
        temp1 = {}
        temp1[lista["char"]] = lista["num"]
        proper_list.append(temp1)
    return proper_list
