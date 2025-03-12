from scheduling_helper_code.VTClasses import *
class Hokie_Scheduler:
    def __init__(self):
        self.vtclasses = set[VTClass]()
        self.courseCombinations = set[frozenset[VTCourse]]()

    def add_vtclass(self, vtclass: VTClass):
        self.vtclasses.add(vtclass)

    def create_schedules(self) -> set[frozenset[VTCourse]]:

        vtclasses = list(self.vtclasses)
        self.recursive_schedule_check(0, vtclasses, list[VTCourse]())
        return self.courseCombinations

    def recursive_schedule_check(self, index: int, VTClasses: List[VTClass], past_courses: list[VTCourse]):
        courses = VTClasses[index].get_courses()
        for course in courses:
            if index == len(VTClasses) - 1:
                #we are at the end of the list of VTClasses
                #Check if this course creates a valid schedule.
                if self.does_not_interfere(course, past_courses):
                    schedule_course_combination = past_courses.copy()
                    schedule_course_combination.append(course)
                    self.courseCombinations.add(frozenset(schedule_course_combination))
            else:
                #We can still continue the recursion. Add current index of VTClasses and past courses to past_courses_addition
                past_courses_addition = past_courses.copy()
                past_courses_addition.append(course)
                #+1 the index of next class.
                self.recursive_schedule_check(index + 1, VTClasses, past_courses_addition)
        
    #TODO #10 FIX THIS. Right now this only compares the last course to the other courses. Need to check every course against every other course.
    def does_not_interfere(self, VTCourse: VTCourse, past_courses: List[VTCourse]) -> bool:
        for course in past_courses:
            if not self.schedules_do_not_interfere(VTCourse.get_schedule(), course.get_schedule()):
                return False
        if len(past_courses) == 1:
            return True
        else:
            return True and self.does_not_interfere(past_courses[-1], past_courses[:-1])
          
    

    def schedules_do_not_interfere(self, schedule1: Dict[Day, Set[Tuple[datetime.time, datetime.time]]], schedule2: Dict[Day, Set[Tuple[datetime.time, datetime.time]]]) -> bool:
        for day in schedule1:
            for time in schedule1[day]:
                if day in schedule2:
                    for time2 in schedule2[day]:
                     if not self.times_do_not_interfere(time, time2):
                         return False
        return True
    

    def times_do_not_interfere(self, time1: Tuple[datetime.time, datetime.time], time2: Tuple[datetime.time, datetime.time]) -> bool:
        print(f"Comparing times: {time1} and {time2}")  # Debug print statement
        if time1[1] <= time2[0] or time1[0] >= time2[1]:
            return True
        return False
    


    def readable_text_schedule(self) -> str:

        schedule = self.create_schedules()

        for course_combination in schedule:
            for course in course_combination:
                print(course.get_name() + course.get_crn())
            print("\n")


