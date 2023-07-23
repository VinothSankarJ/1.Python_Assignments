class MultiFunctions():
    def Eligible():
        gender = input("Your Gender: ")
        age = int(input("Your Age: "))

        if gender.lower() == "male" and age > 18:
            print("ELIGIBLE")
        else:
            print("NOT ELIGIBLE")
    def triangle():
        height = float(input("Height: "))
        breadth = float(input("Breadth: "))

        area = (height * breadth) / 2
        print("Area of triangle:", area)

        height1 = float(input("Height1: "))
        height2 = float(input("Height2: "))
        breadth2 = float(input("Breadth: "))

        perimeter = height1 + height2 + breadth2
        print("Perimeter of triangle:", perimeter)
    def percentage():
        subject1 = 23
        subject2 = 45
        subject3 = 34
        subject4 = 23
        subject5 = 23

        total = subject1 + subject2 + subject3 + subject4 + subject5
        percentage = total / 500 * 100

        print(f"Subject1 = {subject1}")
        print(f"Subject2 = {subject2}")
        print(f"Subject3 = {subject3}")
        print(f"Subject4 = {subject4}")
        print(f"Subject5 = {subject5}")
        print(f"Total: {total}")
        print(f"Percentage: {percentage}")
    def OddEven():
        num = int(input("Enter a number: "))

        if num % 2 == 0:
            print(num, "is an Even number")
        else:
            print(num, "is an Odd number")
    def Subfields():
        subfields = [
            "Machine Learning",
            "Neural Networks",
            "Vision",
            "Robotics",
            "Speech Processing",
            "Natural Language Processing"
        ]

        print("Sub-fields in AI are:")
        for subfield in subfields:
            print(subfield)