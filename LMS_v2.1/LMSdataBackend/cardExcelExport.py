import mainDb_Create
import schoolClass_CRUD
import profile_CRUD
import schoolDaysPerMonth_CRUD
import gradeJHS_CRUD
import gradeSHS_CRUD
import semesterSubjects_CRUD
import attendance_CRUD
import observedValues_CRUD

import os
from absPath import resource_path
from openpyxl import load_workbook
from openpyxl.styles import Font


class ReportCardExport:
    def __init__(self):
        self.activeClass = mainDb_Create.viewDbNames(1)[0]
        self.className = self.activeClass[1]
        self.classData = schoolClass_CRUD.viewClassData(self.className)[0]
        self.schoolMonthData = schoolDaysPerMonth_CRUD.viewDaysPerMonthData(self.className, 1)[0]
        self.schoolDaysData = schoolDaysPerMonth_CRUD.viewDaysPerMonthData(self.className, 2)[0]  # No. of school days per month
        self.attendanceData = attendance_CRUD.viewAttendanceData(self.className)
        self.ovData = observedValues_CRUD.viewObValData(self.className)

        if self.classData[1] == 'JUNIOR HIGH SCHOOL':
            self.cardTemplate = load_workbook(resource_path("templates\\card_temp_JHSver2.xlsx"))
            self.jhsGrades = gradeJHS_CRUD.viewGradesJHSData(self.className)
        else:
            self.shsGradesSem1 = gradeSHS_CRUD.viewGradesSHSData(self.className, 1)
            self.shsGradesSem2 = gradeSHS_CRUD.viewGradesSHSData(self.className, 2)
            self.shsSubjectSem1 = semesterSubjects_CRUD.viewSemSubjects(self.className, 1)
            self.shsSubjectSem2 = semesterSubjects_CRUD.viewSemSubjects(self.className, 2)
            self.cardTemplate = load_workbook(resource_path("templates\\card_temp_SHSver2.xlsx"))

        self.frontTemplate = self.cardTemplate['Front']
        self.backTemplate = self.cardTemplate['Back']
        self.cardFolderName = f"G{self.classData[5]}-{self.classData[6]}_Report_Card_{self.classData[2]}"

        self.learner1 = ''
        self.learner2 = ''
        self.learner3 = ''

    # <editor-fold desc="data to excel">
    def classDataToExcel(self):
        for cellColumn1 in range(4, 61, 28):
            self.frontTemplate.cell(row=14, column=cellColumn1, value=self.classData[5])  # entries for grade (3x) (3 cells) - (row = 14)
        for cellColumn2 in range(14, 71, 28):
            self.frontTemplate.cell(row=14, column=cellColumn2, value=self.classData[6])  # - entries for section (3x) (3 cells) - (row = 14)

        if self.classData[1] == 'SENIOR HIGH SCHOOL':
            for cellColumn3 in range(6, 63, 28):
                self.frontTemplate.cell(row=15, column=cellColumn3, value=self.classData[8])  # entries for Strand (3x) (3 cells) - (row = 15)
                self.frontTemplate.cell(row=16, column=cellColumn3, value=self.classData[2])  # entries for School Year (3x) (3 cells) - (row = 16)
        else:
            for cellColumn3 in range(6, 63, 28):
                self.frontTemplate.cell(row=15, column=cellcol3, value=self.classData[2])  # entries for School Year (3x) (3 cells) - (row = 15)

        for cellColumn4 in range(1, 58, 28):
            self.frontTemplate.cell(row=47, column=cellColumn4, value=self.classData[7])   # - entries for Adviser (3x) (3 cells) - (row = 47)
        for cellColumn5 in range(14, 71, 28):
            self.frontTemplate.cell(row=49, column=cellColumn5, value=self.classData[4])  # - entries for School Head (3x) (3 cells) - (row = 49)

    def monthDataToExcel(self):
        monthDatas = self.schoolMonthData[1:-1]
        schoolDaysDatas = self.schoolDaysData[1:]
        for c in range(11, 76, 28):
            for monthColumn, month in enumerate(monthDatas):
                self.backTemplate.cell(row=29, column=(monthColumn + c), value=month)

            for schoolDaysColumn, schoolDays in enumerate(schoolDaysDatas):
                if schoolDays is None:
                    schoolDays = ""
                self.backTemplate.cell(row=33, column=(schoolDaysColumn + c), value=schoolDays)

    def attendanceToExcel(self, learnerId,  columnAtt):
        learnerAttendance = [item for item in self.attendanceData if item[0] == learnerId][0]
        if len(learnerAttendance) > 0:
            for c_pres, present in enumerate(learnerAttendance[5:18]):  # Number of Days Present
                self.backTemplate.cell(row=34, column=(c_pres + columnAtt), value=present)

            for c_abs, absent in enumerate(learnerAttendance[18:]):  # Number of Days Absent
                self.backTemplate.cell(row=35, column=(c_abs + columnAtt), value=absent)

    def valuesToExcel(self, learnerId, columnValues):
        learnerValues = [item for item in self.ovData if item[0] == learnerId][0]
        rowValues = 5
        for valuesStep in range(9, 41, 4):  # step 9, 13, 17, 21, 25, 29, 33, 37, 41 (4 column step)
            for c_values, valuesValue in enumerate(learnerValues[(valuesStep - 4):valuesStep]):  # valuesValue start [5:9], [9:13], [13:17], [17:21], [21:25], [29:33], [33:37],[37:41]
                self.backTemplate.cell(row=rowValues, column=(columnValues + (c_values * 2)), value=valuesValue)
            if valuesStep <= 21:
                rowValues += 2  # increment merge row cell by 2 (cell row 5,7,9,11,13)
            else:
                rowValues += 3  # increment merge row cell by 3 (cell row 16,19)

    def shsSubjectToExcel(self):
        if len(self.shsSubjectSem1) > 0:
            sem1SubjCount = 0  # SHS subject counter (only 10 allowed)
            for subjectRow, s1 in enumerate(self.shsSubjectSem1):
                for excelColumn in range(1, 58, 28):
                    if sem1SubjCount < 30:  # SHS subjects total of 30 (10 subjects each student)
                        if len(s1[2]) > 54:  # If text length of subject is more than 54, reduce font size
                            self.frontTemplate.cell(row=(subjectRow + 20), column=excelColumn, value=s1[2])\
                                .font = Font(name='Cambria', size=7)
                        else:
                            self.frontTemplate.cell(row=(subjectRow + 20), column=excelColumn, value=s1[2])

                        sem1SubjCount += 1

        if len(self.shsSubjectSem2) > 0:
            sem2SubjCount = 0  # SHS subject counter (only 10 allowed)
            for subjectRow, s2 in enumerate(self.shsSubjectSem2):
                for excelColumn in range(1, 58, 28):
                    if sem2SubjCount < 30:  # SHS subjects total of 30 (10 subjects each student)
                        if len(s2[2]) > 54:  # If text length of subject is more than 54, reduce font size
                            self.frontTemplate.cell(row=(subjectRow + 34), column=excelColumn, value=s2[2]) \
                                .font = Font(name='Cambria', size=7)
                        else:
                            self.frontTemplate.cell(row=(subjectRow + 34), column=excelColumn, value=s2[2])

                        sem2SubjCount += 1

    def learnerEntry1(self):  # First student entry
        if len(self.learner1) > 0:
            self.frontTemplate.cell(row=12, column=4, value=self.learner1[1])  # Name entry
            self.frontTemplate.cell(row=12, column=24, value=self.learner1[4])  # Age entry
            self.frontTemplate.cell(row=13, column=4, value=self.learner1[3])  # Sex entry
            self.frontTemplate.cell(row=13, column=14, value=self.learner1[2])  # LRN entry

            self.attendanceToExcel(self.learner1[0], 11)
            self.valuesToExcel(self.learner1[0], 20)

        # if classData[1] == "SENIOR HIGH SCHOOL":
        #     shsgradesEnt(entry, entrySem2, 19)
        # else:
        #     jhsEnt(entry, 9)  ########### column (9,11,13,15) ##############

    def learnerEntry2(self):  # Second student entry
        if len(self.learner2) > 0:
            self.frontTemplate.cell(row=12, column=32, value=self.learner2[1])  # Name entry
            self.frontTemplate.cell(row=12, column=52, value=self.learner2[4])  # Age entry
            self.frontTemplate.cell(row=13, column=32, value=self.learner2[3])  # Sex entry
            self.frontTemplate.cell(row=13, column=42, value=self.learner2[2])  # LRN entry

            self.attendanceToExcel(self.learner2[0], 39)
            self.valuesToExcel(self.learner2[0], 48)
        #
        # if classData[1] == "SENIOR HIGH SCHOOL":
        #     shsgradesEnt(entry, entrySem2, 47)
        # else:
        #     jhsEnt(entry, 37)  ########### column (37,39,41,43) ##############

    def learnerEntry3(self):  # Third student entry
        if len(self.learner3) > 0:
            self.frontTemplate.cell(row=12, column=60, value=self.learner3[1])  # Name entry
            self.frontTemplate.cell(row=12, column=80, value=self.learner3[4])  # Age entry
            self.frontTemplate.cell(row=13, column=60, value=self.learner3[3])  # Sex entry
            self.frontTemplate.cell(row=13, column=70, value=self.learner3[2])  # LRN entry

            self.attendanceToExcel(self.learner3[0], 67)
            self.valuesToExcel(self.learner3[0], 76)
        #
        # if classData[1] == "SENIOR HIGH SCHOOL":
        #     shsgradesEnt(entry, entrySem2, 75)
        # else:
        #     jhsEnt(entry, 65)  ########### column (65,67,69,71) ###############

    def learnerDelete2(self):  # Deleting second student entry
        self.frontTemplate.cell(row=12, column=32, value="")
        self.frontTemplate.cell(row=12, column=52, value="")  # deleting name,age,sex,LRN
        self.frontTemplate.cell(row=13, column=32, value="")
        self.frontTemplate.cell(row=13, column=42, value="")

        for attDel2 in range(13):
            self.backTemplate.cell(row=33, column=(attDel2 + 39), value="")
            self.backTemplate.cell(row=34, column=(attDel2 + 39), value="")  # deleting attendance
            self.backTemplate.cell(row=35, column=(attDel2 + 39), value="")

        for rowDel in range(5, 14, 2):
            for columnDel in range(48, 55, 2):
                self.backTemplate.cell(row=rowDel, column=columnDel, value="")

        for rowDel2 in range(16, 20, 3):  # deleting Observe Values
            for columnDel in range(48, 55, 2):
                self.backTemplate.cell(row=rowDel2, column=columnDel, value="")

    def learnerDelete3(self):  # Deleting third student entry
        self.frontTemplate.cell(row=12, column=60, value="")
        self.frontTemplate.cell(row=12, column=80, value="")  # deleting name,age,sex,LRN
        self.frontTemplate.cell(row=13, column=60, value="")
        self.frontTemplate.cell(row=13, column=70, value="")

        for attDel3 in range(13):
            self.backTemplate.cell(row=33, column=(attDel3 + 67), value="")
            self.backTemplate.cell(row=34, column=(attDel3 + 67), value="")  # deleting attendance
            self.backTemplate.cell(row=35, column=(attDel3 + 67), value="")

        for rowDel in range(5, 14, 2):
            for columnDel in range(76, 83, 2):  # deleting Observe Values
                self.backTemplate.cell(row=rowDel, column=columnDel, value="")

        for rowDel2 in range(16, 20, 3):
            for columnDel in range(76, 83, 2):
                self.backTemplate.cell(row=rowDel2, column=columnDel, value="")
    ...

    # </editor-fold>
    def pathToSave(self, path):
        newPath = os.path.join(path, self.cardFolderName)
        if not os.path.exists(newPath):
            os.makedirs(newPath)

        return newPath

    def groupGradesData(self):  # split grades data list into chunks with 3 elements
        tempData = self.shsGradesSem1
        for x in range(0, len(tempData), 3):  # Iteration start from 0 database list index up to length of data, with 3 steps
            chunk = tempData[x: 3 + x]  # loop is by 3 elements iteration (gradesData[0:3]) // from 0-3, then 4-6, and so on

            if len(chunk) < 3:  # If remaining elements is less than 3, it will be added by '' element
                chunk = chunk + ['' for y in range(3 - len(chunk))]
            yield chunk

    def exportCard(self, gradesData, path):
        groupedDatas = list(self.groupGradesData())
        filePath = self.pathToSave(path)
        print("Exporting...")
        for groupedData in groupedDatas:  # Iterating/separating list into 3 elements/learners
            count = 0  # counter variable for iterating 3 learners (initial value)
            blankEntry = 0  # counter variable for empty value (no learner's data)
            for gradesData in groupedData:
                count += 1
                match count:
                    case 1:
                        self.learner1 = list(gradesData)  # First learner with entry
                        if len(self.learner1) != 0:
                            # ent1sem2 = sem2List(ent1[0])  # sem2 grade data for SHS
                            self.name1 = self.learner1[1].rsplit(",", 2)
                        else:
                            blankEntry += 1

                    case 2:
                        self.learner2 = list(gradesData)  # Second learner with entry
                        if len(self.learner2) != 0:
                            # ent2sem2 = sem2List(ent2[0])  # sem2 grade data for SHS
                            self.name2 = self.learner2[1].rsplit(",", 2)
                        else:
                            blankEntry += 1

                    case 3:
                        self.learner3 = list(gradesData)  # Third learner with entry
                        if len(self.learner3) != 0:
                            # ent3sem2 = sem2List(ent3[0])  # sem2 grade data for SHS
                            self.name3 = self.learner3[1].rsplit(",", 2)
                        else:
                            blankEntry += 1

            match blankEntry:
                case 0:
                    filename3 = f"{self.name1[0]}_{self.name2[0]}_{self.name3[0]}.xlsx"  # file name for card (3 learners)
                    self.classDataToExcel()
                    self.monthDataToExcel()
                    if self.classData[1] == 'SENIOR HIGH SCHOOL':
                        self.shsSubjectToExcel()

                    self.learnerEntry1()
                    self.learnerEntry2()
                    self.learnerEntry3()
                    self.cardTemplate.save(filePath + "\\" + filename3)

                case 1:
                    filename2 = f"{self.name1[0]}_{self.name2[0]}.xlsx"  # file name for card (2 learners)
                    self.classDataToExcel()
                    self.monthDataToExcel()
                    if self.classData[1] == 'SENIOR HIGH SCHOOL':
                        self.shsSubjectToExcel()

                    self.learnerEntry1()
                    self.learnerEntry2()
                    self.learnerDelete3()  # deleting previous entry (third learner)
                    self.cardTemplate.save(filePath + "\\" + filename2)

                case 2:
                    filename1 = f"{self.name1[0]}.xlsx"   # file name for card (1 learner)
                    self.classDataToExcel()
                    self.monthDataToExcel()
                    if self.classData[1] == 'SENIOR HIGH SCHOOL':
                        self.shsSubjectToExcel()

                    self.learnerEntry1()
                    self.learnerDelete2()  # deleting previous entry (second learner)
                    self.learnerDelete3()  # deleting previous entry (third learner)
                    self.cardTemplate.save(filePath + "\\" + filename1)

        print("Done. Check directory")


v = ReportCardExport()
samplePath = "C:\\Users\\June\\Documents\\LMSApp_sample_Data"

v.exportCard("", samplePath)
