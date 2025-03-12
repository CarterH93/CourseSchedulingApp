from scheduling_helper_code.VTClasses import *
class Hokie_Scheduler:
    def __init__(self):
        self.vtclasses = set[VTClass]()

    def add_vtclass(self, vtclass: VTClass):
        self.vtclasses.add(vtclass)

    def create_schedules(self) -> set[Set[VTCourse]]:
        #TODO #7 return lists of lists of courses for schedule

        vtclasses = list(self.vtclasses)

        for VTClassIndex in range(len(vtclasses)):
            for VTCourseIndex in range(len(vtclasses[VTClassIndex].get_courses())):
                pass



    def readable_text_schedule(self) -> str:
        #TODO #8 return a string representation of the schedule
        pass


    def does_not_interfere(self, VTClasses: list[VTClass], FirstVTClassIndex: int, FirstVTCourseIndex: int, SecondVTClassIndex: int, SecondVTCourseIndex: int) -> bool:
        firstCourse = VTClasses[FirstVTClassIndex].get_courses()[FirstVTCourseIndex]
        secondCourse = VTClasses[SecondVTClassIndex].get_courses()[SecondVTCourseIndex]
        return self.schedules_do_not_interfere(firstCourse.get_schedule(), secondCourse.get_schedule())
          
    

    def schedules_do_not_interfere(self, schedule1: Dict[Day, Set[Tuple[datetime.time, datetime.time]]], schedule2: Dict[Day, Set[Tuple[datetime.time, datetime.time]]]) -> bool:
        for day in schedule1:
            for time in schedule1[day]:
                for time2 in schedule2[day]:
                    if self.times_do_not_interfere(time, time2) == False:
                        return False
        return True

    def times_do_not_interfere(self, time1: Tuple[datetime.time, datetime.time], time2: Tuple[datetime.time, datetime.time]) -> bool:
        if time1[1] < time2[0] or (time1[0] > time2[1]):
            return True
        return False
   