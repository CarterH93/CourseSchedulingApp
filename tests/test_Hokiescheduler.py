from scheduling_helper_code.HokieScheduler import *

def test_times_do_not_interfere():
    scheduler = Hokie_Scheduler()
    assert scheduler.times_do_not_interfere(time1=(datetime.time(11, 0), datetime.time(13, 0)), time2=(datetime.time(14, 0), datetime.time(16, 0))) == True
    assert scheduler.times_do_not_interfere(time1=(datetime.time(15, 0), datetime.time(16, 0)), time2=(datetime.time(14, 0), datetime.time(16, 0))) == False

def test_schedules_do_not_interfere():
    scheduler = Hokie_Scheduler()
    assert scheduler.schedules_do_not_interfere({Day.MONDAY: {(datetime.time(11, 0), datetime.time(13, 0))}, Day.TUESDAY: {(datetime.time(14, 0), datetime.time(16, 0))}}, {Day.MONDAY: {(datetime.time(15, 0), datetime.time(16, 0))}, Day.TUESDAY: {(datetime.time(14, 0), datetime.time(16, 0))}}) == False
    assert scheduler.schedules_do_not_interfere({Day.MONDAY: {(datetime.time(11, 0), datetime.time(13, 0))}, Day.TUESDAY: {(datetime.time(14, 0), datetime.time(16, 0))}}, {Day.MONDAY: {(datetime.time(15, 0), datetime.time(16, 0))}, Day.TUESDAY: {(datetime.time(17, 0), datetime.time(18, 0))}}) == True

def test_does_not_interfere():
    scheduler = Hokie_Scheduler()
    vtclass1 = VTClass('test1', '2025', Semester.SPRING)
    vtclass1.add_courses({'18445'})
    vtclass2 = VTClass('test2', '2025', Semester.SPRING)
    vtclass2.add_courses({'14906'})
    scheduler.add_vtclass(vtclass1)
    scheduler.add_vtclass(vtclass2)
    assert scheduler.does_not_interfere([vtclass1, vtclass2], 0, 0, 1, 0) == False