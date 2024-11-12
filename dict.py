def main():
    #Create and initialize an empty dictionary
    person_info = {}

    #Prompt user for info
    name = input("Enter your name: ")
    age = input("Enter your age: ")
    favorite_color = input("Enter your favorite color: ")

    #Store info in the dictionary
    person_info['name'] = name
    person_info['age'] = age
    person_info['favorite_color'] = favorite_color

    #Print to console
    print("\nPerson Information:") #Causes output to move to a new line
    print(person_info)

if __name__ == "__main__":
    main()