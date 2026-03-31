#  Text Analysis Program for News Article
# This program reads a news article from a text file and performs various analyses on the content, including:
# 1. Counting the occurrences of a specific word
# 2. Identifying the most common word in the article
# 3. Calculating the average word length
# 4. Counting the number of paragraphs
# 5. Counting the number of sentences
import re

# Count Specific word
def count_specific_word(text, word):
    words = re.findall(r'\b\w+\b', text.lower())
    return words.count(word.lower())

# Identify the most common word in the article
def identify_most_common_word(text):
    words = re.findall(r'\b\w+\b', text.lower())
    
    if not words:
        return None

    word_counts = {}

    for word in words:
        word_counts[word] = word_counts.get(word, 0) + 1

    most_common = max(word_counts, key=word_counts.get)
    return most_common

# Calculate average word length
def calculate_average_word_length(text):
    words = re.findall(r'\b\w+\b', text)
    total_length = sum(len(word) for word in words)
    return total_length / len(words) if words else 0

# Calculate the number of paragraphs in the article
def count_paragraphs(text):
    paragraphs = re.split(r'\n\s*\n', text.strip())
    return len(paragraphs)

# Count the number of sentences in the article
def count_sentences(text):
    if not text.strip():
        return 1  

    sentences = re.split(r'[.!?]+', text.strip())
    return len([s for s in sentences if s.strip()])

def main():
    # Read the article from a text file
    with open("NewsArticle.txt", "r", encoding="utf-8") as file:
        content = file.read()
        

    while True:
        print("\nText Analysis Menu")
        print("1. Count Specific Word")
        print("2. Identify Most Common Word")
        print("3. Calculate Average Word Length")
        print("4. Count Paragraphs")
        print("5. Count Sentences")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            word = input("Enter the word to count: ")
            count = count_specific_word(content, word)
            print(f"The word '{word}' appears {count} times in the article.")
        elif choice == '2':
            common_word = identify_most_common_word(content)
            print(f"The most common word is '{common_word}'.")
        elif choice == '3':
            avg_length = calculate_average_word_length(content)
            print(f"The average word length in the article is {avg_length:.2f} characters.")
        elif choice == '4':
            paragraphs = count_paragraphs(content)
            print(f"The article contains {paragraphs} paragraphs.")
        elif choice == '5':
            sentences = count_sentences(content)
            print(f"The article contains {sentences} sentences.")
        elif choice == '6':
            print("Exiting Text Analysis Menu.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()