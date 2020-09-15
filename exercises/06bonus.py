class Exercises:
    def __init__(self, string):
        self.string = string
        self.dictionary = {}

    def letter_count(self):
        for eachletter in self.string:
            keys = self.dictionary.keys()
            if eachletter in keys:
                self.dictionary[eachletter] += 1
            else:
                self.dictionary[eachletter] = 1
        return self.dictionary


letter = Exercises('banana')
print(letter.letter_count())