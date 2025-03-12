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
            if len(self.courseCombinations) >= 100:
                #We have found 100 possible schedules. Stop the recursion.
                return
            elif index == len(VTClasses) - 1:
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
       # print(f"Comparing times: {time1} and {time2}")  # Debug print statement
        if time1[1] <= time2[0] or time1[0] >= time2[1]:
            return True
        return False
    
    


    def readable_text_schedule(self) -> str:

        schedule = self.create_schedules()

        with open("results", "w") as file:
            if len(schedule) == 0:
                file.write("No possible schedules found")
            elif len(schedule) == 100:
                file.write("More than 100 possible schedules found. Try narrowing your search parameters. Will only show 100 schedule combinations.")
            else:
                file.write(f"{len(schedule)} possible schedules found")
            file.write("\n")
            file.write("\n")
            for course_combination in schedule:
                file.write("Potential Course Combination:")
                file.write("\n")
                file.write("\n")
                for course in course_combination:
                    file.write(course.get_name() + "  " + "CRN: " + course.get_crn())
                    file.write("\n")
                    file.write(course.readable_schedule())
                    file.write("\n")
                file.write("\n")
                file.write("--------------------------------")
                file.write("\n")
                file.write("\n")
            file.close()

        if len(schedule) == 0:
            print("No possible schedules found")
        elif len(schedule) == 100:
            print("More than 100 possible schedules found. Try narrowing your search parameters. Will only show 100 schedule combinations.")
        else:
            print(f"{len(schedule)} possible schedules found")

        print("See saved file named results for full schedule combinations")


