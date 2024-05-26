def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        
    words = file_contents.split()

    letter_dict = count_letters(file_contents)

    print(letter_dict)

    print_report(letter_dict)



def count_letters(text):
    letter_count = {}

    for letter in text:
        letter = letter.lower()
        if letter == " ":
            continue
        else:
            if letter in letter_count:
                letter_count[letter] += 1
            else:
                letter_count[letter] = 1

    return letter_count

def print_report(letter_dict):
    my_keys = list(letter_dict.keys())
    my_keys.sort()
    sorted_dict = {i: letter_dict[i] for i in my_keys}

    for key in sorted_dict:
         print(f'The {key} was found {sorted_dict[key]} times')
       


if __name__ == "__main__":
    main()
    
