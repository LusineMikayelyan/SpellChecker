import re
from nltk.corpus import brown


class SpellChecker:
    def __init__(self):
        self.my_dict = brown.words()

    def check_sentence(self, sentence):
        rgx = re.compile("([\w][\w']*\w)")

        result = []
        for item in rgx.findall(sentence):
            if item not in self.my_dict:
                result.append(item)

        return result


if __name__ == '__main__':
    data = "A complete sentence must hav, at minimum, thoooe things: a subject, verb, ddand an object. " \
           "The subject is typically a noun or a pronoun. Aniid, if there's a subject, there's bound to be " \
           "a veyyyrb because all veroobs need a subject. Finally, the object of a sentence is the thing that's " \
           "being acted upon by ooothe subject."

    o = SpellChecker()
    print(o.check_sentence(data))
