from scheduling_helper_code.VTClasses import *
def test_convert_str_time():

    assert convert_str_time('10:00am') == datetime.time(10, 0)
    assert convert_str_time('5:00pm') == datetime.time(17, 0)

def test_convert_str_schedule():
    schedule = { Day.MONDAY: {('10:00am', '11:00am'), ('11:00am', '3:00pm')}, Day.TUESDAY: {('8:00am', '9:00am')} }
    updated_schedule = convert_str_schedule(schedule)
    assert updated_schedule[Day.MONDAY] == { (datetime.time(10, 0), datetime.time(11, 0)), (datetime.time(11, 0), datetime.time(15, 0)) }
    assert updated_schedule[Day.TUESDAY] == { (datetime.time(8, 0), datetime.time(9, 0))}

def test_VTCourse():
    course = VTCourse(None, { Day.MONDAY: {('10:00am', '11:00am'), ('11:00am', '3:00pm')}}, '2025', Semester.SPRING, 'test') 
    assert course.get_schedule()[Day.MONDAY] == { (datetime.time(10, 0), datetime.time(11, 0)), (datetime.time(11, 0), datetime.time(15, 0)) }

def test_crns_to_VTClass():

    assert crns_to_VTClass('test', '2025', Semester.SPRING, {'19100'}).get_courses().pop().get_crn() == '19100'
    assert len(crns_to_VTClass('test', '2025', Semester.SPRING, {'19100', '14906', '18445'}).get_courses()) == 3

