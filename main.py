from vtt import *
# can fnd course via CRN.
course = get_crn('2025', Semester.SPRING, '18445')
# Need the subject and course number to be able to find course.
results = search_timetable('2025', Semester.SPRING, subject = 'MUS', code = 3314)

print(results[0].get_name())
