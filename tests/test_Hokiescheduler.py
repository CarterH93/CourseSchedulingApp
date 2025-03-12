from scheduling_helper_code.HokieScheduler import *

def test_times_do_not_interfere():
    scheduler = Hokie_Scheduler()
    assert scheduler.times_do_not_interfere(time1=(datetime.time(11, 0), datetime.time(13, 0)), time2=(datetime.time(14, 0), datetime.time(16, 0))) == True
    assert scheduler.times_do_not_interfere(time1=(datetime.time(15, 0), datetime.time(16, 0)), time2=(datetime.time(14, 0), datetime.time(16, 0))) == False
    assert scheduler.times_do_not_interfere(time1=(datetime.time(15, 0), datetime.time(16, 30)), time2=(datetime.time(16, 0), datetime.time(16, 0))) == False

def test_schedules_do_not_interfere():
    scheduler = Hokie_Scheduler()
    assert scheduler.schedules_do_not_interfere({Day.MONDAY: {(datetime.time(11, 0), datetime.time(13, 0))}, Day.TUESDAY: {(datetime.time(14, 0), datetime.time(16, 0))}}, {Day.MONDAY: {(datetime.time(15, 0), datetime.time(16, 0))}, Day.TUESDAY: {(datetime.time(14, 0), datetime.time(16, 0))}}) == False
    assert scheduler.schedules_do_not_interfere({Day.MONDAY: {(datetime.time(13, 0), datetime.time(14, 0))}}, {Day.MONDAY: {(datetime.time(13, 25), datetime.time(14, 15))}}) == False

def test_does_not_interfere():
    scheduler = Hokie_Scheduler()
    course = VTCourse(None, { Day.MONDAY: {(datetime.time(11, 0), datetime.time(13, 0))}, Day.TUESDAY: {(datetime.time(14, 0), datetime.time(16, 0))}}, '2025', Semester.SPRING, 'test')
    past_courses = [VTCourse(None, { Day.MONDAY: {(datetime.time(15, 0), datetime.time(16, 0))}, Day.TUESDAY: {(datetime.time(14, 0), datetime.time(16, 0))}}, '2025', Semester.SPRING, 'test')]
    assert scheduler.does_not_interfere(course, past_courses) == False
    past_courses = [VTCourse(None, { Day.MONDAY: {(datetime.time(13, 0), datetime.time(14, 0))}}, '2025', Semester.SPRING, 'test')]
    assert scheduler.does_not_interfere(course, past_courses) == True