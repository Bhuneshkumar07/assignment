# Assignment 1: Python Basics (Simple Language)

print("========== 1) Data Types (Theory with Examples) ==========")

print("Integer (int): Whole number without decimal")
a = 10
print("Example:", a)

print("\nFloat (float): Number with decimal")
b = 10.5
print("Example:", b)

print("\nString (str): Text written inside quotes")
name_example = "Gargi"
print("Example:", name_example)

print("\nBoolean (bool): Shows True or False")
is_student = True
print("Example:", is_student)


print("\n========== 2) Variables: name, age, city ==========")

name = "Gargi"
age = 20
city = "Jaipur"

print("Name:", name)
print("Age:", age)
print("City:", city)


print("\n========== 3) Take user name input ==========")

user_name = input("Enter your name: ")
print("Uppercase:", user_name.upper())
print("Total number of characters:", len(user_name))


print("\n========== 4) String Methods (Theory + Examples) ==========")

print("1) upper(): Makes all letters uppercase")
print("Example:", "hello".upper())

print("\n2) lower(): Makes all letters lowercase")
print("Example:", "HELLO".lower())

print("\n3) title(): Makes first letter of each word capital")
print("Example:", "gargi jaipur".title())

print("\n4) replace(old, new): Replaces a word with another word")
print("Example:", "I love python".replace("python", "java"))

print("\n5) strip(): Removes spaces at start and end")
print("Example:", "   hello   ".strip())


print("\n========== 5) Fruits List ==========")

fruits = ["apple", "mango", "banana", "orange", "grapes"]
print("Complete list:", fruits)
print("First element:", fruits[0])
print("Last element:", fruits[-1])
print("Total number of items:", len(fruits))


print("\n========== 6) Update Numbers List ==========")

numbers = [10, 20, 30, 40, 50]
print("Original list:", numbers)

numbers.append(60)   # Adds 60 at the end
numbers.remove(20)   # Removes the first occurrence of 20

print("Updated list:", numbers)


print("\n========== 7) Artificial Intelligence (AI) ==========")

print("AI means Artificial Intelligence.")
print("AI is the technology that helps computers think, learn, and make decisions like humans.")

print("\nImportance of AI:")
print("1) It saves time by doing tasks fast.")
print("2) It helps in solving complex problems.")
print("3) It improves accuracy in many systems.")

print("\nAny 4 real-life applications of AI:")
print("1) Chatbots like customer support")
print("2) Recommendation systems (YouTube/Netflix) ")
print("3) Image recognition (face unlock / photo tagging)")
print("4) Voice assistants (Alexa/Siri) ")


print("\n========== 8) Identify AI examples (with reasons) ==========")

print("1) ChatGPT")
print("- YES, it is AI because it understands and generates human-like text using machine learning.")

print("\n2) Google Maps route prediction")
print("- YES, it is AI because it uses data and predictions to suggest the best route.")

print("\n3) Calculator")
print("- NO, it is not AI because it only performs fixed mathematical operations (no learning or thinking).")

print("\n4) Netflix recommendations")
print("- YES, it is AI because it learns what you like and suggests movies/series.")

print("\n5) Voice assistants (Alexa/Siri)")
print("- YES, it is AI because it understands your voice and responds using AI models.")


