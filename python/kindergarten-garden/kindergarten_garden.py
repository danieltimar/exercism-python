class Garden(object):

    DEFAULT_STUDENTS = ["Alice", "Bob", "Charlie", "David",
                "Eve", "Fred", "Ginny", "Harriet",
                "Ileana", "Joseph", "Kincaid", "Larry"]

    all_plants = {"G": "Grass", "C": "Clover", "V": "Violets", "R": "Radishes"}

    def __init__(self, diagram, students=DEFAULT_STUDENTS):
        self.students = students

        self.diagrams_by_row = diagram.split("\n")

    def plants(self, student):

        student_position = sorted(self.students).index(student)
        plant_codes_of_student = []

        for row in self.diagrams_by_row:
            plant_codes_of_student.extend([row[student_position * 2], row[student_position * 2 + 1]])

        plant_names = [self.all_plants[pc] for pc in plant_codes_of_student]
        return plant_names
