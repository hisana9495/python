frontend_students = {"Aiha", "liha", "heza"}
backend_students = {"heza", "uhan", "luah"}
backend_students.add("leen")
frontend_students.remove("liha")
both_courses = frontend_students & backend_students
print("Students in both courses:", both_courses)
only_backend = backend_students - frontend_students
print("Students only in Backend:", only_backend)
all_students = frontend_students | backend_students
print("Total unique students:", len(all_students))
print("All students:", all_students)
course_dict = {
    "Frontend": len(frontend_students),
    "Backend": len(backend_students)
}
for course, count in course_dict.items():
    print(f"Course: {course}, Students: {count}")
growth_dict = {course: count for course, count in course_dict.items()}
growth_dict["Fullstack"] = course_dict["Frontend"] + course_dict["Backend"]
print("Course dictionary with Fullstack:", growth_dict)