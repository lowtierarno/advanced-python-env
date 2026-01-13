import json

def pepepe(input_file, output_file):
    try:
        # 1. Read the JSON file
        with open(input_file, 'r', encoding='utf-8') as f:
            students = json.load(f)

        # 2. Calculate average grade per student
        for student in students:
            grades = student.get('grades', [])
            if grades:
                average = sum(grades) / len(grades)
            else:
                average = 0
            
            # Add the new key to the student dictionary
            student['average_grade'] = round(average, 2)

        # 3. Write updated data to a NEW JSON file (preserving original)
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(students, f, indent=4)

        print(f"Saved to {output_file}")

    except FileNotFoundError:
        print(f"The file {input_file} was not found.")
    except json.JSONDecodeError:
        print(f"Failed to decode JSON from {input_file}.")

if __name__ == "__main__":
    pepepe('Week-5/students.json', 'Week-5/students_updated.json')