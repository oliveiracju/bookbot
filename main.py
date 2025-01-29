path_to_file = './books/frankenstein.txt'

def main():
    with open(path_to_file) as f:
        file_contents = f.read()
        count_result = count_specific_word(file_contents)

        for key in count_result:
            print(f"The '{key}' character was found {count_result[key]} times")


def count_specific_word(words):
    result = {}

    for i in range(len(words)):
        letter = words[i].lower()
        
        if letter.isalpha() == False:
            continue

        if letter in result:
            result[letter] += 1
        else:
            result[letter] = 1
    
    return result
    

main()