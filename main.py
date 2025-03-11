from vtt import *
from scheduling_helper_code.get_music_class import *
from scheduling_helper_code.VTCourse import *
# can fnd course via CRN.
course = get_crn('2025', Semester.SPRING, '18445')

#print(get_music_class()[0].get_schedule())

customCourse = VTCourse(None, { Day.MONDAY: {('10:00pm', '11:00am'), ('11:00am', '12:00pm')} })
print(customCourse.get_schedule())


