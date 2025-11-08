class Student:
    instances = {}

    def __init__(self, name, score, i, j):
        self.name = name
        self.score = score
        self.i = i
        self.j = j

    def set_score(self, score:int): # -> None 
        self.score = score

    def get_message(self): # -> str
        return f"{self.name} at ({self.i}, {self.j}) scored {self.score}"


class PotatosClass:


    def __init__(self, n, m):
        self.seats = [[None]*m for _ in range(n)]
        self.students = dict()
        self.n = n
        self.m = m
    def record_students(self):
        for i in range(self.n*self.m):
            name, score, i, j = input().split()

            score, i, j = int(score), int(i), int(j)

            student = Student(name, score, i, j)
            self.students[name] = self.seats[i][j] = student

    def command_score(self, stu_name:str, new_score:int): # -> None
        self.students[stu_name].set_score(new_score)

    def command_rotate(self, i:int, j:int, width:int): # -> None
        dest = [row[:] for row in self.seats]

        for x in range(width):
            for y in range(width):
                
                dest[i + y][j + (width - 1 - x)] = self.seats[i + x][j + y]
                
                student = dest[i + y][j + (width - 1 - x)]
                if student:
                    student.i = i + y
                    student.j = j + (width - 1 - x)
        
        self.seats = dest

    def get_best_student(self): # -> Student
        return max(self.students.values(), key=lambda s: s.score)
    
        # return reduce(lambda acc, x: acc if acc.score > x.score else x, self.students.values())


n, m, k = map(int, input().split())

course = PotatosClass(n, m)
course.record_students()

for i in range(k):
    commands = input().split()

    if(commands[0] == "score"):
        course.command_score(commands[1], int(commands[2]))
    elif(commands[0] == "rotate"):
        course.command_rotate(int(commands[1]), int(commands[2]), int(commands[3]))

print(course.get_best_student().get_message())