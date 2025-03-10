from vtt import *
def get_music_class():
    # Need the subject and course number to be able to find course.
    results = search_timetable('2025', Semester.SPRING, subject = 'MUS', code = 3314)
    return results