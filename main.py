from vtt import *
# can fnd course via CRN.
course = get_crn('2025', Semester.SPRING, '18445')


def get_music_class():
    # Need the subject and course number to be able to find course.
    results = search_timetable('2025', Semester.SPRING, subject = 'MUS', code = 3314)
    return results

print(get_music_class()[0].get_name())
