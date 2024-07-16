def main():
    with open("./books/frankenstein.txt") as f:
        dict_of_dicts = []
        file_contents=f.read()
        words = word_count(file_contents)
        print(f"---Begin report of {f.name[1:]} ---")
        print(f"{words} words found in the document")
        letter_dict = character_count(file_contents)
        for i in letter_dict:
            dict_of_dicts.append({'letter': i, "num" : letter_dict[i]})
        dict_of_dicts.sort(reverse = True, key=sort_on)
        for item in dict_of_dicts:
            print(f"The '{item['letter']}' character was found {item['num']} times")
    print('--- End report ---')
def word_count(total_words):
    words = total_words.split()
    return len(words)
def character_count(text):
    letter_dict = {}
    lower_text = text.lower()
    for i in lower_text:
        if i.isalpha():
            if i in letter_dict:
                letter_dict[i] += 1
            else:
                letter_dict[i] = 1
    return letter_dict
def sort_on(dict):
   return dict["num"]

main()
