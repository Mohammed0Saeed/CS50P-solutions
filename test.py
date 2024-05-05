import csv

def addTeacherToCsv(fileName):
    class teacher:
        name = '',
        subjects = [],
        course = [],
        history = []

    teacher.name = input("Enter a name: ")
    teacher.subjects = input("Enter the subjects: ").split(",")
    teacher.course = input("Enter the letter of the course: ").split(",")
    teacher.history.append("N/A")

    with open(fileName, "a", newline="") as teachersList:
        writer = csv.DictWriter(teachersList, fieldnames=["name", "subjects", "course", "history"])
        writer.writerow(
            {"name": teacher.name, "subjects": teacher.subjects, "course": teacher.course, "history": teacher.history})

def editTeacherInCsv(fileName):
    # load the file to this array
    fileList = []

    # 
    with open(fileName) as teacherList:
        reader = csv.DictReader(teacherList, fieldnames=["name", "subjects", "course", "history"])
        for row in reader:
            fileList.append(row)

    key = input("Key: ")

    for row in fileList:
        if row['name'] == key:
            print("Element exists!")
            edit = input("Edit: ")

            match edit:
                case "name":
                    row['name'] = input("new name: ")
                case "subjects":
                    row['subjects'] = input("new subjects: ")
                case "course":
                    row['course'] = input("new courses: ")
                case "history":
                    row['history'] = input("edit history: ")
                case _:
                    raise ValueError
            break


    with open(fileName, "w", newline='') as teacherFile:
        writer = csv.DictWriter(teacherFile, fieldnames=['name', 'subjects', 'course', 'history'])
        for row in fileList:
            writer.writerow({
                'name': row['name'],
                'subjects': row['subjects'],
                'course': row['course'],
                'history': row['history']
            })




editTeacherInCsv("teachers.csv")