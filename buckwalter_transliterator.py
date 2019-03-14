# reverse argument determines wether your transliteration is from normal arabic text to Buckwalter coded one (reverse = 0)
# or vice-versa (reverse = 1)


def BuckWalter_Transliterator(sentence, reverse=0):
    buckwalter_dictionary = {' ': ' ', '\u0621': "'", '\u0622': '|', '\u0623': '>', '\u0624': '&', '\u0625': '<', '\u0626': '}', '\u0627': 'A', '\u0628': 'b', '\u0629': 'p', '\u062A': 't', '\u062B': 'v', '\u062C': 'j', '\u062D': 'H', '\u062E': 'x', '\u062F': 'd', '\u0630': '*', '\u0631': 'r', '\u0632': 'z', '\u0633': 's', '\u0634': '$', '\u0635': 'S', '\u0636': 'D',
                             '\u0637': 'T', '\u0638': 'Z', '\u0639': 'E', '\u063A': 'g', '\u0640': '_', '\u0641': 'f', '\u0642': 'q', '\u0643': 'k', '\u0644': 'l', '\u0645': 'm', '\u0646': 'n', '\u0647': 'h', '\u0648': 'w', '\u0649': 'Y', '\u064A': 'y', '\u064B': 'F', '\u064C': 'N', '\u064D': 'K', '\u064E': 'a', '\u064F': 'u', '\u0650': 'i', '\u0651': '~', '\u0652': 'o'}

    if reverse == 0:
        dict = buckwalter_dictionary
    elif reverse == 1:
        dict = {v: k for k, v in buckwalter_dictionary.items()}
    n_s = ""
    for char in sentence:
        if char in dict:
            n_s += dict[char]
        else:
            n_s += char

    return n_s
