def ubahString(word:str, appearance:int, changed_char:list, substitute:str):
    seen = list()
    list_letter = list(word)

    for letter in word.lower():
        if not letter in seen and letter != ' ':
            seen.append(letter)                       
            letter_position = [pos for pos, char in enumerate(word.lower()) if char == letter]

            if letter in changed_char and len(letter_position) >= appearance:
                list_letter[letter_position[appearance-1]] = substitute        

    output = ''.join(list_letter)

    return output

if __name__ == '__main__':
    print(ubahString('Mantap', 1, ['a', 'p'], '*'))