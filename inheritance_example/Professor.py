from BabsonPerson import BabsonPerson

from Person import Person





class Professor(BabsonPerson):

    pass



    def __init__(self, name, UGcourse):

        BabsonPerson.__init__(self, name)

        self.course = UGcourse
    
    def speak(self, utterance):

        newUtterance = 'In course' + self.course + 'we say'

        return BabsonPerson.speak(self, newUtterance + utterance)
    
    def lecture(self, topic):
        
        return self.speak('it is obvious that ' + topic)

def main():

    faculty = Professor('Zhi Li', 'MIS 3640')
    print(faculty.speak('Python is cool!'))
    print(faculty.lecture('Python is easy.'))

if __name__ == '__main__':
    
    main()