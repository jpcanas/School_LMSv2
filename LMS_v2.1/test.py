import sqlite3
import calendar

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



sem1Subject = [('CORE', '21st Century Literature from the Philippines and the World', 1), ('CORE', 'Earth and Life Science', 1), ('CORE', 'General Mathematics', 1), ('CORE', 'Komunikasyon at Pananaliksik sa Wika at Kulturang Pilipino', 1), ('CORE', 'Oral Communication in Context', 1), ('CORE', 'Personal Development', 1), ('CORE', 'Physical Education and Health (Grade 11)', 1), ('SPECIALIZED', 'Bread and Pastry Production', 1)]
count = len(sem1Subject)
#conn = sqlite3.connect(r"C:\Users\June\Desktop\Python_training\Projects\School_LMSv2\LMS_v2.1\data\MNHS_2023-2024_G11_TOPAZ.db")
samp = [(1, "Name1", "samp1"), (2, "Name2", "samp2"), (3, "Name3", "samp3"), (4, "Name4", "samp4"), (5, "Name5", "samp5")]

test = [89, 89, 89.0, 84, 84, 84.0, 90, 90, 90.0, 70, '', None, 80, 80, 80.0, 71, '', None, 97, 97, 97.0, 72, '', None,  9, 1, 1]
final = [89, 89, 89.0, 84, 84, 84.0, 90, 90, 90.0, 70, '', None, 80, 80, 80.0, 71, '', None, 97, 97, 97.0, 72, '', None, 81.625, None, None, 9, 1, 1]
s = ('89', '89', '84', '84', '90', '90', '', '', '80', '80', '', '', '97', '97', '', '', 9, 1, 1)


def updateQueryShs(gradesWithFinal):
    subjectCount = gradesWithFinal[-3] - 1
    sem = gradesWithFinal[-1]
    createQuery = f"UPDATE gradesSem{sem}Table \nSET "

    if sem == 1:
        for i in range(subjectCount):
            createQuery += f"subj{i + 1}Q1Sem{sem} = ?, subj{i + 1}Q2Sem{sem} = ?, subj{i + 1}FinalSem{sem} = ?,\n"

        createQuery += f"aveQ1Sem{sem} = ?, aveQ2Sem{sem} = ?, genAveSem{sem}  = ?,\n"
    else:
        for i in range(subjectCount):
            createQuery += f"subj{i + 1}Q3Sem{sem} = ?, subj{i + 1}Q4Sem{sem} = ?, subj{i + 1}FinalSem{sem} = ?,\n"

        createQuery += f"aveQ3Sem{sem} = ?, aveQ4Sem{sem} = ?, genAveSem{sem} = ?,\n"

    createQuery +=  createQuery[:-2]  # remove last two characters( [/n] ,)
    createQuery += "\nWHERE  oid = :oid"

    gradesWithFinal.pop(-3)   # remove subject count data
    gradesWithFinal.pop(-1)  # remove sem data

    print(createQuery)
    return gradesWithFinal


n = updateQueryShs(final)
print(n)


