def main():
    # Function to get a set of integers from user input
    def get_set(prompt):
        while True:
            user_input = input(prompt)
            try:
                # Convert the input string into a set of integers
                return set(int(num) for num in user_input.split())
            except ValueError:
                print("Please enter valid integers separated by spaces.")

    # Get two sets of integers from the user
    set1 = get_set("Enter the first set of integers (separated by spaces): ")
    set2 = get_set("Enter the second set of integers (separated by spaces): ")

    # Create a new set that contains only the common elements
    common_elements = set1.intersection(set2)

    # Print the results
    print("\nCommon elements in both sets:")
    print(common_elements)

if __name__ == "__main__":
    main()