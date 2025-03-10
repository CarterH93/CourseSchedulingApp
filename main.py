from vtt import *
from scheduling_helper_code.get_music_class import *
# can fnd course via CRN.
course = get_crn('2025', Semester.SPRING, '18445')

print(get_music_class()[0].get_name())
