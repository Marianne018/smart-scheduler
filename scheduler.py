
# list for all exam schedules
exam_schedule = []


# add a new exam
def add_exam():
    name = input("\nEnter exam name: ")
    date = input("Enter exam date (YYYY-MM-DD): ")
    time = input("Enter exam time (HH:MM AM/PM): ")
    room = input("Enter assigned room: ")


    # Add the exam
    exam = {
        "name": name,
        "date": date,
        "time": time,
        "room": room
    }
    exam_schedule.append(exam)
   
    print("Exam is added successfully.\n")

# display all the exams
def view_exams():
    if not exam_schedule:
        print("No exams scheduled.\n")
        return

    print("\nScheduled Exams:")
    for i, exam in enumerate(exam_schedule, start=1):
        print(f"{i}. {exam['name']} - {exam['date']} at {exam['time']} in Room {exam['room']}")
    print()

# edit an exam
def edit_exam():
    view_exams()
    if not exam_schedule:
        return

#Ask the user which exam number to edit
    try:
        index = int(input("Enter exam number to edit: ")) - 1
        if index < 0 or index >= len(exam_schedule):
            print("Invalid exam number.\n")
            return

# Edit an existing exam detail. Blank input means current value remains
        current = exam_schedule[index]
        print("Leave blank to keep current value.")
        name = input("Enter new exam name: ") or current['name']
        date = input("Enter new date (YYYY-MM-DD): ") or current['date']
        time = input("Enter new time (HH:MM AM/PM): ") or current['time']
        room = input("Enter new assigned room: ") or current['room']

       
        # Update exam
        exam_schedule[index] = {
            "name": name,
            "date": date,
            "time": time,
            "room": room
        }

        print("Exam updated successfully.\n")

    except ValueError:
        print("Please enter a valid number.\n")

# delete an exam
def delete_exam():
    view_exams()
    if not exam_schedule:
        return

    try:
 # Ask user which exam to delete
        index = int(input("Enter exam number to delete: ")) - 1
# Check if input is valid
        if index < 0 or index >= len(exam_schedule):
            print("Invalid exam number.\n")
            return

# Remove the exam entry from the list
        removed = exam_schedule.pop(index)
        print(f"Removed exam: {removed['name']}\n")

    except ValueError:
        print("Please enter a valid number.\n")

# The simplified main menu
def main():
    while True:
        print("----- SMART SCHEDULER MENU -----")
        print("A. Add a new exam")
        print("B. View all exams")
        print("C. Edit an exam")
        print("D. Delete")
        print("E. Exit")

# Ask for users choice              
        choice = input("Enter your choice (A-E): ")

# calling the corresponding choices
        if choice == "A":
            add_exam()
        elif choice == "B":
            view_exams()
        elif choice == "C":
            edit_exam()
        elif choice == "D":
            delete_exam()
        elif choice == "E":
            print("Exiting Smart Scheduler. Goodbye.")
            break
        else:
            print("Invalid choice. Please try again.\n")

# Run the program
if __name__ == "__main__":
    main()