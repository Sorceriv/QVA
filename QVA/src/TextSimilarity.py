from thefuzz import fuzz
from thefuzz import process

# print(fuzz.token_sort_ratio("fuzzy wuzzy was a bear", "wuzzy fuzzy was a bear"))
# #lower the fudge out of dis letters
# test_input = ["TIBCO Enterprise", "TIPCO Service vulnerability", "Buffer Overflow Vulnerability Tipco Message", "TIPCO Message", "NONSENSE TEXT"]
# print(process.extract("TIBCO Enterprise Message Service Buffer Overflow Vulnerability", test_input, scorer=fuzz.partial_token_set_ratio, limit=10))

def checkSimilarity(inputText, secondaryTexts):
    inputText = inputText.lower()
    newSecondaryTexts = []
    for text in secondaryTexts:
        newSecondaryTexts.append(text.lower())
        
    return process.extract(inputText, newSecondaryTexts, scorer=fuzz.partial_token_sort_ratio, limit=5)