def main():
    # Prompts users for input
    user_input = input("Enter a list of integers separated by spaces: ")

    # Split the input string into individual components and converts them to integers
    try:
        integer_list = [int(num) for num in user_input.split()]

        #Compute te sum of integers in the list
        total_sum = sum(integer_list)

        #Display the result
        print(f"The sum of integers is: {total_sum}")
    except ValueError:
        print("Please enter valid integers only.")

if __name__ == "__main__":
    main()