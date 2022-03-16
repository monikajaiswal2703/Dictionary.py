batch1_students = ["Shivam", "Rahul", "Kavay", "Dhannu", "Deepanshu", "Nitin", "Manoj", "Shakrudin", "Tara", "Suraj", "Krishna"]
students_file = open("navgurukul_students.html", "w")
students_file.write("\n")
students_file.write("\n")
students_file.write("\n")
students_file.write("\n")
students_file.write("\n")
students_file.write("")
for student in batch1_students:
    students_file.write(" + student + \n")
    students_file.write("\n")
students_file.write("\n")
students_file.write("\n")
students_file.close()

my_file3 = open("test_file.txt", "w")
my_file3.write("Yahan main kuch likha")
my_file3.write("\nYaha maine kuch aur bhi likha.")
my_file3.close()