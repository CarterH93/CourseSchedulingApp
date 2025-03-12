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

def test_crns_to_courses():

    assert crns_to_courses('2025', Semester.SPRING, ['18445']).pop().get_crn() == '18445'
    assert crns_to_courses('2025', Semester.SPRING, ['18445']).pop().get_name() == 'Instrumental Ensemble Music'
    assert len(crns_to_courses('2025', Semester.SPRING, ['18445', '17366', '14906'])) == 3

def test_VTClass_add_courses():
    vtclass = VTClass('test', '2025', Semester.SPRING, set())
    vtclass.add_courses({'18445'})
    assert vtclass.get_courses()[0].get_crn() == '18445'
    assert vtclass.get_courses()[0].get_name() == 'Instrumental Ensemble Music'
    vtclass.add_courses({'14906', '17366'})
    assert len(vtclass.get_courses()) == 3

def test_VTBreak():
    schedule = { Day.MONDAY: {('10:00am', '11:00am'), ('11:00am', '3:00pm')}, Day.TUESDAY: {('8:00am', '9:00am')} }
    vtbreak = VTBreak('test', '2025', Semester.SPRING, schedule)
    assert vtbreak.get_courses().pop().get_schedule()[Day.MONDAY] == { (datetime.time(10, 0), datetime.time(11, 0)), (datetime.time(11, 0), datetime.time(15, 0)) }
    assert vtbreak.get_year() == '2025'
    assert vtbreak.get_semester() == Semester.SPRING