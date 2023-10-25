"Module to process user input"
import nltk
import nltk.sentiment.util

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

def analyze_input(message: str) -> tuple:
    """Function to analyze negation in user input
    
    Returns a tuple containing four boolean values"""
    words = nltk.word_tokenize(message.lower())

    tagged_words = nltk.sentiment.util.mark_negation(words, double_neg_flip = True)

    correct_words = ["correct", "incorrect_NEG", "wrong_NEG"]
    incorrect_words = ["correct_NEG", "incorrect", "wrong"]
    low_words = ["low", "small", "bigger", "higher", "larger",
                 "high_NEG", "big_NEG", "large_NEG", "lower_NEG", "smaller_NEG"]
    high_words = ["low_NEG", "small_NEG", "bigger_NEG", "higher_NEG", "larger_NEG",
                  "high", "big", "large", "lower", "smaller"]

    correct: bool = any(_ in tagged_words for _ in correct_words)
    too_low: bool = any(_ in tagged_words for _ in low_words)
    too_high: bool = any(_ in tagged_words for _ in high_words)
    conflicting: bool = ((correct and any(_ in tagged_words for _ in incorrect_words))
                        or (too_high and too_low))

    return correct, too_low, too_high, conflicting

def test() -> None:
    "Test the analyze_input function"
    print(analyze_input("don't go any lower!"))
    print(analyze_input("the answer is larger"))
    print(analyze_input("this is too small"))
    print(analyze_input("this is not large enough"))
    print(analyze_input("this is not big. It is too small"))
    print(analyze_input("not correct"))
    print(analyze_input("correct"))
    print(analyze_input("too big, too small"))
    print(analyze_input("this is both correct and incorrect"))
    print(analyze_input("too high"))
    print(analyze_input("not high, but not low either")) # FAIL
    print(analyze_input("neither too high nor too low")) # FAIL

if __name__ == "__main__":
    test()
