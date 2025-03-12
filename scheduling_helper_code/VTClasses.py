from vtt import *
import datetime
from collections import defaultdict

def convert_str_schedule(schedule: Dict[Day, Set[Tuple[str, str]]]):
    """
    Converts a dictionary representation of a course schedule with string times to a dictionary representation of a course schedule with time objects.

    Args:
        schedule (Dict[Day, Set[Tuple[str, str]]]): A dictionary representing the course schedule with days as keys and sets of time tuples as values.

    Returns:
        Dict[Day, Set[Tuple[datetime.time, datetime.time]]]: A dictionary representing the course schedule with days as keys and sets of time tuples as values.
    """

    updated_schedule = defaultdict(set) 
    for key in schedule:
        for time in schedule[key]:
            updated_schedule[key].add((convert_str_time(time[0]), convert_str_time(time[1])))
    return updated_schedule


    

def convert_str_time(date_time):
    """
    Converts a string representation of time to a time object.

    Args:
        date_time (str): A string representing the time in the format '%I:%M%p', 
                         where %I is the hour (01-12), %M is the minute (00-59), 
                         and %p is AM or PM.

    Returns:
        datetime.time: A time object representing the given time.
    """

    format = '%I:%M%p'
    datetime_str = datetime.datetime.strptime(date_time, format)

    return datetime_str.time()


class VTCourse(Course):
    """
    VTCourse is a wrapper class for Course that provides additional functionality
    for handling course schedules with time conversion.

    Attributes:
        course (Course): Course object with information from remote source. Set as None to create custom VTCourse.
        schedule (Dict[Day, Set[Tuple[str, str]]]): A dictionary representing the course schedule with days as keys and sets of time tuples as values.
        

    Methods:
        
    """

    def __init__(self, course: Course, schedule: Dict[Day, Set[Tuple[str, str]]], year: str, semester: Semester, name: str):
        if course == None:
            self.schedule = convert_str_schedule(schedule)
            self.year = year
            self.semester = semester
            self.name = name
            self.course = None
        else:
            self.course = course
            retrieved_schedule = course.get_schedule()  
            self.schedule = convert_str_schedule(retrieved_schedule)
            self.year = course.get_year()
            self.semester = course.get_semester()
            self.name = course.get_name()
    
    def get_schedule(self):
        """
        Returns the course schedule.

        Returns:
            Dict[Day, Set[Tuple[datetime.time, datetime.time]]]: A dictionary representing the course schedule with days as keys and sets of time tuples as values.
        """
        return self.schedule
        
    def get_year(self) -> str:
        return self.year

    def get_semester(self) -> Semester:
        return self.semester

    def get_crn(self) -> str:
        if self.course != None:
            return self.course.get_crn()
        else:
            return None

    def get_subject(self) -> str:
        if self.course != None:
            return self._course_data['subject']
        else:
            return None
        

    def get_code(self) -> str:
        if self.course != None:
            return self._course_data['code']
        else:
            return None
        

    def get_name(self) -> str:
        return self.name

    def get_type(self) -> SectionType:
        if self.course != None:
            return self._course_data['section_type']
        else:
            return None
        

    def get_modality(self) -> Modality:
        if self.course != None:
            return self._course_data['modality']
        else:
            return None
        

    def get_credit_hours(self) -> str:
        if self.course != None:
            return self._course_data['credit_hours']
        else:
            return None
        

    def get_capacity(self) -> str:
        if self.course != None:
            return self._course_data['capacity']
        else:
            return None
        

    def get_professor(self) -> str:
        if self.course != None:
            return self._course_data['professor']
        else:
            return None
        

    def has_open_spots(self) -> bool:
        if self.course != None:
            return True if search_timetable(self.get_year(), self.get_semester(),
                                        crn=self.get_crn(),
                                        status=Status.OPEN) else False
        else:
            return True
        



def crns_to_courses(year: str, semester: Semester, CRNs: Set[str]):
    courses = set()
    for crn in CRNs:
        course = get_crn(year, semester, crn)
        VT_course = VTCourse(course, None, course.get_year(), course.get_semester(), course.get_name())
        courses.add(VT_course)
    return courses


class VTClass:
    def __init__(self, name: str, year: str, semester: Semester, courses = set()):
        self.name = name
        self.courses = courses
        self.year = year
        self.semester = semester
    
    def get_name(self) -> str:
        return self.name
    
    def get_courses(self) -> Set[VTCourse]:
        return list(self.courses)
    
    def get_year(self) -> str:
        return self.year
    
    def get_semester(self) -> Semester:
        return self.semester
    
    def add_courses(self, courses: Set[str]):
        self.courses.update(crns_to_courses(self.year, self.semester, courses))
    

class VTBreak(VTClass):
    def __init__(self, name: str, year: str, semester: Semester, schedule: Dict[Day, Set[Tuple[str, str]]]):
         courses = { VTCourse(None, schedule, year, semester, name) }

         super().__init__(name, year, semester, courses)