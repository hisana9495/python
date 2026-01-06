python_students = {"riya", "Benny", "aju"}
data_science_students = {"aju", "David", "alib"}
python_students.add("james")
data_science_students.remove("alib")
both_courses = python_students & data_science_students
print("Students in both courses:", both_courses)
only_python = python_students - data_science_students
print("Students only in Python:", only_python)
all_students = python_students | data_science_students
print("All students:", all_students)
course_dict = {
    "Python": len(python_students),
    "Data Science": len(data_science_students)
}
for course, count in course_dict.items():
    print(f"Course: {course}, Students: {count}")
growth_dict = {course: count * 2 for course, count in course_dict.items()}
print("Growth projection:", growth_dict)