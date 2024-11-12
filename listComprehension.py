def main():
    # Store a list of words
    words = [
        "apple", "banana", "cherry", "date", "fig", 
        "grape", "kiwi", "mango", "peach", "plum"
    ]
    
    # Use list comprehension to create a new list with words that have an odd number of characters
    odd_length_words = [word for word in words if len(word) % 2 != 0]

    # Print the results
    print("Original list of words:")
    print(words)
    print("\nWords with an odd number of characters:")
    print(odd_length_words)

if __name__ == "__main__":
    main()