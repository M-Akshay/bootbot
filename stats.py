def get_num_words(file):
     with open(file) as f:
        num_words = 0
        file_contents = f.read()
        file_string = file_contents.split()
        for word in file_string:
            num_words += 1
        return num_words

def get_count_characters(file):
    with open(file) as f:
        file_contents = f.read()
        unique = {}
        for char in file_contents:
            words = char.lower()
            if words not in unique:
                unique[words]=1
            else:
                unique[words]+=1
        return unique

def chars_to_sorted_list(char_dict):
    # Create a list to hold dictionaries
    char_list = []
    # For each character and count in the dictionary
    for char, count in char_dict.items():
        # Add a dictionary to the list
        char_list.append({"char": char, "num": count})
    
    # Now sort the list
    # How would you sort the list by the "num" key in descending order?
    def sort_on(dict_item):
        return dict_item["num"]
    char_list.sort(reverse=True,key=sort_on)
    
    return char_list