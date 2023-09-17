import sqlite3
import calendar
from LMSdataBackend import schoolDaysPerMonth_CRUD, gradeSHS_CRUD, attendance_CRUD, observedValues_CRUD, gradeJHS_CRUD
from absPath import resource_path

daysPerMonth_data = (
    "September", "October", "November", "December", "January", "February", "March", "April", "May",
    "June", "July", "August", None, 1)

# conn = sqlite3.connect(
#     r"C:\Users\June\Desktop\Python_training\Projects\School_LMSv2\LMS_v2.1\data\MNHS_2022-2023_G8_SAPPHIRE.db")
#
#
# conn.commit()
# conn.close()

# monthID = 2

# p =  [('MANTALISAY NATIONAL HIGH SCHOOL', '309711', 'LIBMANAN', 'CAMARINES SUR', 'V'),
#       ('SENIOR HIGH SCHOOL', '2023-2024', 'August', 'MARITES P. AUREUS', '11', 'TOPAZ', 'MONETTE S. LUNAR', 'TVL - BPP, BNC, Dressmaking')]

# m = list(calendar.month_name)
# inputMonth = "January"
# startIndex = m.index(inputMonth)
#
# monthNameData = m[startIndex:] + m[1:startIndex]


sem1Subject = [('CORE', '21st Century Literature from the Philippines and the World', 1),
               ('CORE', 'Earth and Life Science', 1), ('CORE', 'General Mathematics', 1),
               ('CORE', 'Komunikasyon at Pananaliksik sa Wika at Kulturang Pilipino', 1),
               ('CORE', 'Oral Communication in Context', 1), ('CORE', 'Personal Development', 1),
               ('CORE', 'Physical Education and Health (Grade 11)', 1),
               ('SPECIALIZED', 'Bread and Pastry Production', 1)]
count = len(sem1Subject)
# conn = sqlite3.connect(r"C:\Users\June\Desktop\Python_training\Projects\School_LMSv2\LMS_v2.1\data\MNHS_2023-2024_G11_TOPAZ.db")
samp = [(1, "Name1", "samp1"), (2, "Name2", "samp2"), (3, "Name3", "samp3"), (4, "Name4", "samp4"),
        (5, "Name5", "samp5")]

test = [89, 89, 89.0, 84, 84, 84.0, 90, 90, 90.0, 70, '', None, 80, 80, 80.0, 71, '', None, 97, 97, 97.0, 72, '', None,
        9, 1, 1]
final = [89, 89, 89.0, 84, 84, 84.0, 90, 90, 90.0, 70, '', None, 80, 80, 80.0, 71, '', None, 97, 97, 97.0, 72, '', None,
         81.625, None, None, 9, 1, 1]
sweet = ('89', '89', '84', '84', '90', '90', '', '', '80', '80', '', '', '97', '97', '', '', 9, 1, 1)

t = ['12', '20', None, '18', None, None, None, None, None, None, None, None, '2', '11', None, None, None, '3', '12',
     '4', None, None, None, None, None, '0', 1]
school = ['24', None, '25', '21', None, '19', '18', '20', '19', '20', None, None, '170']
presTotal = 0
absTotal = 0
schoolDaysTotal = 0

s1 = gradeSHS_CRUD.viewGradesSHSData('MNHS_2023-2024_G11_TOPAZ', 1)
s2 = gradeSHS_CRUD.viewGradesSHSData('MNHS_2023-2024_G11_TOPAZ', 2)
v = schoolDaysPerMonth_CRUD.viewDaysPerMonthData('MNHS_2023-2024_G11_TOPAZ', 2)[0]
a = attendance_CRUD.viewAttendanceData('MNHS_2023-2024_G11_TOPAZ')
ov = observedValues_CRUD.viewObValData('MNHS_2023-2024_G11_TOPAZ')
jhs = gradeJHS_CRUD.viewGradesJHSData('MNHS_2022-2023_G8_SAPPHIRE')

def joinSem1Sem2Data():
    sem1GradesBasic = []
    sem2GradesBasic = []
    for s in s1:
        sList = list(s)
        sTuple = tuple(sList[:5])
        sem1GradesBasic.append(sTuple)
    for r in s2:
        rList = list(r)
        rTuple = tuple(rList[:5])
        sem2GradesBasic.append(rTuple)

    sem1Set = set(sem1GradesBasic)
    sem2Set = set(sem2GradesBasic)
    sem1sem2Datas = list(sem1Set.union(sem2Set))
    sem1sem2Sorted = sorted(sem1sem2Datas, key=lambda item: item[1])
    # sem1sem2Sorted = sem1sem2Datas.sort(key=lambda item: item[0])
    print(sem1sem2Sorted)


print(jhs)
