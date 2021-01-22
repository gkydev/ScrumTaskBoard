
def calculateEstimatedTime(input_text):
    splitted_words = input_text.split(" ")
    result = len(splitted_words) /3 
    if result < 1:
        result = 1
    return result