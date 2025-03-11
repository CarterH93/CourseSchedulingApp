from scheduling_helper_code.VTClasses import *
class Hokie_Scheduler:
    def __init__(self):
        self.vtclasses = Set[VTClass]()

    def add_vtclass(self, vtclass: VTClass):
        self.vtclasses.add(vtclass)

    def create_schedules(self) -> Set[Set[VTCourse]]:
        #TODO #7 return lists of lists of courses for schedule
        pass

    def readable_text_schedule(self) -> str:
        #TODO #8 return a string representation of the schedule
        pass



    