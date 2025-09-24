python_students={"Alice", "Bob", "Charlie"}
data_science_students={"Bob", "David", "Eve"}

python_students.add("Frank")

data_science_students.remove("Eve")

both_courses=python_students&data_science_students
print(both_courses)

only_python=python_students-data_science_students
print(only_python)

all_students=python_students|data_science_students
print(all_students)

course_dict={"python":len(python_students),
             "data_science":len(data_science_students)}
print("course dictionary:",course_dict)


