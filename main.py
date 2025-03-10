from vtt import *
course = get_crn('2025', Semester.SPRING, '18445')
subjects = get_subjects()
results = search_timetable('2025', Semester.SPRING, subject = 'MUS', code = 3314)
print(results[0].get_name())