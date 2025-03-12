from scheduling_helper_code.HokieScheduler import *

#Create Hokie_scheduler class
scheduler = Hokie_Scheduler()


#Create Classes
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

BIT = VTClass('BIT', '2025', Semester.SPRING, set())
BIT.add_courses({'11887', '11888', '11889'})

CINE = VTClass('CINE', '2025', Semester.SPRING, set())
CINE.add_courses({'13075', '13076', '21932'})

#Create breaks
Break = VTBreak('No 8 ams', '2025', Semester.SPRING, {Day.MONDAY: {('8:00am', '9:00am')}, Day.TUESDAY: {('8:00am', '9:00am')}, Day.WEDNESDAY: {('8:00am', '9:00am')}, Day.THURSDAY: {('8:00am', '9:00am')}, Day.FRIDAY: {('8:00am', '9:00am')}})

afternoon = VTBreak('afternoon', '2025', Semester.SPRING, {Day.MONDAY: {('5:00pm', '11:00pm')}, Day.TUESDAY: {('5:00pm', '11:00pm')}, Day.WEDNESDAY: {('5:00pm', '11:00pm')}, Day.THURSDAY: {('5:00pm', '11:00pm')}, Day.FRIDAY: {('5:00pm', '11:00pm')}})


#Add classes and breaks to scheduler

scheduler.add_vtclass(CS)
scheduler.add_vtclass(Engineering)
scheduler.add_vtclass(MATH)
scheduler.add_vtclass(MUSIC)
#scheduler.add_vtclass(PHYSICS)
#scheduler.add_vtclass(LAB)
scheduler.add_vtclass(BIT)
#scheduler.add_vtclass(Break)
scheduler.add_vtclass(CINE)
scheduler.add_vtclass(afternoon)


#Main function to call to generate schedule
scheduler.create_schedule_to_text_file()







