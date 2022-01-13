#spent_letters = []
#required_letters = []
#c0 = None
#c1 = None
#c2 = None
#c3 = None
#c4 = None

spent_letters = []
required_letters = []
c0 = None
c1 = None
c2 = None
c3 = None
c4 = None

with open("/Users/jim.odonnell/Downloads/words.txt", 'r') as file:
    for word in file:
        word = word.strip().lower()
        word_letters = set(word)
        invalid_word = False

        if len(word) != 5:
            invalid_word = True
        if None != c0 and word[0] != c0:
            invalid_word = True
        if None != c1 and word[1] != c1:
            invalid_word = True
        if None != c2 and word[2] != c2:
            invalid_word = True
        if None != c3 and word[3] != c3:
            invalid_word = True
        if None != c4 and word[4] != c4:
            invalid_word = True
       
        for letter in required_letters:
            if not letter in word_letters:
                invalid_word = True
                break
        for letter in spent_letters:
            if letter in word_letters:
                invalid_word = True
                break

        if not invalid_word:
            print(word)

