class Grade:

    sum_grade = 0   #static variable
    grade_current_index = 0    #static variable

    def __init__(self,student_name, grade, topic):
        self.__student_name = student_name
        self.__grade = grade
        self.__topic = topic
        self.__grade_index = grade_index
        Grade.grade_current_index += 1
        Grade.sum_grade += self.__grade

    @staticmethod             #static method
    def get_avg(grade_current_index, sum_grade):
        return f' avg = ({sum_grade} / {grade_current_index})'

    @staticmethod           #static method
    def get_grade_current_index(grade_current_index):
        return Grade.grade_current_index

    @property                 #getter
    def grade(self):
        return self.__grade

    @grade.setter        #setter
    def grade(self,new_grade):
        if new_grade < 0 or new_grade > 100:
            print('this is not a real grade! not changing')
            return
        self.__grade = new_grade

    @property                  #getter
    def topic(self):
        return self.__topic

    @topic.setter            #detter
    def topic(self,new_topic):
        if new_topic != 'math' or new_topic != 'python' or new_topic != 'english':
            print('this topic iis not exist')
            return
        self.__topic = new_topic

    @property    #getter
    def student_name(self):
        return self.__student_name

    @property         #getter
    def grade_index(self):
        return self.__grade_index

    def is_grade_higher_than_avg(self, sum_grade):
        if __grade > Grade.sum_grade:
            return True
        return False

    def __str__(self):
        return str(self.__dict__)

    def __repr__(self):
        return str(self.__dict__)
