from scheduling_helper_code.HokieScheduler import *

#Simple test (Current Schedule)
scheduler = Hokie_Scheduler()
CS = VTClass('CS', '2025', Semester.SPRING, set())
CS.add_courses({'21565'})

Engineering = VTClass('Engineering', '2025', Semester.SPRING, set())
Engineering.add_courses({'14906'})

MATH = VTClass('MATH', '2025', Semester.SPRING, set())
MATH.add_courses({'17366'})

MUSIC = VTClass('MUSIC', '2025', Semester.SPRING, set())
MUSIC.add_courses({'18445'})

PHYSICS = VTClass('PHYSICS', '2025', Semester.SPRING, set())
PHYSICS.add_courses({'19107'})

LAB = VTClass('LAB', '2025', Semester.SPRING, set())
LAB.add_courses({'19100'})

scheduler.add_vtclass(CS)
scheduler.add_vtclass(Engineering)
scheduler.add_vtclass(MATH)
scheduler.add_vtclass(MUSIC)
scheduler.add_vtclass(PHYSICS)
scheduler.add_vtclass(LAB)

schedule = scheduler.create_schedules()
print(schedule)
print("done")


#More complex test

#Simple test (Current Schedule)
scheduler1 = Hokie_Scheduler()
CS = VTClass('CS', '2025', Semester.SPRING, set())
CS.add_courses({'21565'})

Engineering = VTClass('Engineering', '2025', Semester.SPRING, set())
Engineering.add_courses({'14885', '14887', '14890', '14892', '14893', '14895', '14897', '14902', '14903', '14904', '14905', '14906', '14907', '14908', '14909', '14911'})

MATH = VTClass('MATH', '2025', Semester.SPRING, set())
MATH.add_courses({'17366', '17367', '22143', '22144', '22145', '22146', '22147', '22148'})

MUSIC = VTClass('MUSIC', '2025', Semester.SPRING, set())
MUSIC.add_courses({'18445'})

PHYSICS = VTClass('PHYSICS', '2025', Semester.SPRING, set())
PHYSICS.add_courses({'19107'})

LAB = VTClass('LAB', '2025', Semester.SPRING, set())
LAB.add_courses({'19100'})

Break = VTBreak('No 8 ams', '2025', Semester.SPRING, {Day.MONDAY: {('8:00am', '9:00am')}, Day.TUESDAY: {('8:00am', '9:00am')}, Day.WEDNESDAY: {('8:00am', '9:00am')}, Day.THURSDAY: {('8:00am', '9:00am')}, Day.FRIDAY: {('8:00am', '9:00am')}})

scheduler1.add_vtclass(CS)
scheduler1.add_vtclass(Engineering)
scheduler1.add_vtclass(MATH)
scheduler1.add_vtclass(MUSIC)
scheduler1.add_vtclass(PHYSICS)
scheduler1.add_vtclass(LAB)
scheduler1.add_vtclass(Break)

schedule1 = scheduler1.create_schedules()
print(schedule1)
print(len(schedule1))
print("done")
scheduler1.readable_text_schedule()







