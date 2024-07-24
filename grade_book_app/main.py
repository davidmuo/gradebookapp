from grade_book import GradeBook

def main():
    gradebook = GradeBook()

    while True:
        print("\nGrade Book Menu:")
        print("1. Add Student")
        print("2. Add Course")
        print("3. Register Student for Course")
        print("4. Calculate Ranking")
        print("5. Search by Grade")
        print("6. Generate Transcript")
        print("7. Exit")
        choice = input("Choose an action: ")

        if choice == '1':
            email = input("Enter student's email: ")
            names = input("Enter student's names: ")
            gradebook.add_student(email, names)
            print(f"Student {names} added.")

        elif choice == '2':
            name = input("Enter course name: ")
            trimester = input("Enter course trimester: ")
            credits = int(input("Enter course credits: "))
            gradebook.add_course(name, trimester, credits)
            print(f"Course {name} added.")

        elif choice == '3':
            student_email = input("Enter student's email: ")
            course_name = input("Enter course name: ")
            grade = float(input("Enter grade (default 0.0): "))
            gradebook.register_student_for_course(student_email, course_name, grade)
            print(f"Student {student_email} registered for course {course_name}.")

        elif choice == '4':
            ranking = gradebook.calculate_ranking()
            print("\nStudent Ranking by GPA:")
            for rank, student in enumerate(ranking, start=1):
                print(f"{rank}. {student.names} ({student.email}) - GPA: {student.GPA}")

        elif choice == '5':
            min_grade = float(input("Enter minimum GPA: "))
            max_grade = float(input("Enter maximum GPA: "))
            students = gradebook.search_by_grade(min_grade, max_grade)
            print("\nStudents in the specified GPA range:")
            for student in students:
                print(f"{student.names} ({student.email}) - GPA: {student.GPA}")

        elif choice == '6':
            student_email = input("Enter student's email: ")
            transcript = gradebook.generate_transcript(student_email)
            if transcript:
                print(f"\nTranscript for {transcript['names']} ({transcript['email']}):")
                for course, grade in transcript['courses']:
                    print(f"{course}: {grade}")
                print(f"GPA: {transcript['GPA']}")
            else:
                print("Student not found.")

        elif choice == '7':
            print("Exiting Grade Book. Goodbye!")
            break

        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
