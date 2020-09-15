dd= {}

def letter_count(str):
    for i in range(len(str)):
        if str[i] in dd:
            dd[str[i]] +=1
        else:
            dd[str[i]] = 1
    print(dd)

letter_count('asyncrhonus')

class Thesaurus:
    def __init__(self, string):
        self.string = string
        self.dictionary = {}

    def count_letters(self):
        for i in range(len(self.string)):
            if self.string[i] in self.dictionary:
                self.dictionary[self.string[i]] +=1
            else:
                self.dictionary[self.string[i]] = 1
        print(self.dictionary)

word = Thesaurus('asynchronus')
word.count_letters()


