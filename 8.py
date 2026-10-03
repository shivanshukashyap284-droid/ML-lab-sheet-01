# Program 8: Create and execute your first Python program in Jupyter Notebook

def greet_and_calculate():
    print("Hello, World!")
    student_name = "Student"
    print(f"Welcome {student_name} to the Data Science Lab")

    num_a, num_b = 10, 20
    print("Sum of", num_a, "and", num_b, "is:", num_a + num_b)

if __name__ == "__main__":
    greet_and_calculate()
