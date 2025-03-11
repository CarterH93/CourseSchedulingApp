from VTCourse import *
import datetime
from vtt import *

def crns_to_VTClass(name: str, year: str, semester: Semester, CRNs: Set[str]):
    """
    Converts a set of CRNs to a set of VTCourses.

    Args:
        CRNs (Set[str]): A set of CRNs.

    Returns:
        Set[VTCourse]: A set of VTCourses.
    """
    courses = set()
    for crn in CRNs:
        course = get_crn(year, semester, crn)
        courses.add(course)
    return VTClass(name, courses)


class VTClass:
    def __init__(self, name: str, courses: Set[VTCourse]):
        self.name = name
        self.courses = courses
    
    def get_name(self) -> str:
        return self.name
    
    def get_courses(self) -> Set[VTCourse]:
        return self.courses
    

class VTBreak(VTClass):
    def __init__(self, name: str, schedule: Dict[Day, Set[Tuple[str, str]]]):
         courses = { VTCourse(None, schedule, None, None, name) }

         super().__init__(name, courses)