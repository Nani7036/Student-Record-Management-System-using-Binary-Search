def binary_search(students, target):
    low = 0
    high = len(students) - 1

    while low <= high:
        mid = (low + high) // 2
        if students[mid][0] == target:
            return students[mid]
        elif students[mid][0] < target:
            low = mid + 1
        else:
            high = mid - 1

    return None


if __name__ == "__main__":
    print(" Student Record Management System\n")

    n = int(input("Enter number of students: "))
    students = []

    for _ in range(n):
        roll = int(input("Enter Roll Number: "))
        name = input("Enter Name: ")
        students.append((roll, name))

    
    students.sort(key=lambda x: x[0])

    print("\nSorted Student Records (by Roll Number):")
    for s in students:
        print(f"Roll No: {s[0]} | Name: {s[1]}")

    target = int(input("\nEnter roll number to search: "))
    result = binary_search(students, target)

    if result:
        print(f"\n  Student Found: Roll No {result[0]} | Name: {result[1]}")
    else:
        print("\n  Student Not Found.")
