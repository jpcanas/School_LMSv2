from openpyxl import load_workbook
from openpyxl.styles import Font
import xlrd

#=============================== MODULE FOR IMPORTING DATA FROM DEPED LIS SCHOOL FORM 1 and ZIP ARCHIVE GENERATED BY THIS APP ===================================

#-------- Excel 97-2003 version (*.xls)
#-------- Excel latest version 2019 up (*.xlsx)
mnthDic = {'01':'January','02':'February','03':'March','04':'April','05':'May','06':'June','07':'July','08':'August',
				'09':'September','10':'October','11':'November','12':'December'}
# path = 'C:/LMS_appVer2/sampleData/SF1_2021_Grade 7 (Year I) - PEARL.xls'
# pathSHS = 'C:/LMS_appVer2/sampleData/School Form 1 (SF 1).xls'

def learnerJHS_SF1(sf1path):

	sf1book =  xlrd.open_workbook(sf1path)  
	sf1_sheet = sf1book.sheet_by_index(0)
	tempProfile = []
	row = 6 
	try:
		for gender in range(2): #----------- loop for Male group and Female group ---------------

			row += gender
			while len(str(int(sf1_sheet.cell_value(row,0)))) == 12:
				ind_data = []
				ind_data.append(str(int(sf1_sheet.cell_value(row,0))))           #------------ LRN --------------

				fullName = sf1_sheet.cell_value(row,2)			#------------ Full Name --------------  
				splitName = fullName.rsplit(",",2)

				ind_data.append(splitName[0])								#------------ Last Name -------------- 
				ind_data.append(splitName[1])								#------------ First Name -------------- 

				if len(splitName) == 3:
					ind_data.append(splitName[2])							#------------ Middle Initial if any ----------
				else:
					ind_data.append('')

				ind_data.append('')										#------------ Name Extension ------------------

				if (sf1_sheet.cell_value(row,6)) == 'M':
					ind_data.append('MALE')									#------------ MALE or FEMALE --------------
				else:
					ind_data.append('FEMALE')

				ind_data.append(sf1_sheet.cell_value(row,9))    			#------------ Age --------------

				brgy = sf1_sheet.cell_value(row,17)				#------------ Barangay --------------
				mun =  sf1_sheet.cell_value(row,20)				#------------ Municipality --------------
				prov = sf1_sheet.cell_value(row,22)				#------------ Province -------------

				ind_data.append((brgy + ', ' + mun + ', ' + prov))			#------------- Complete Address ----------------

				try:
					mdate = str(sf1_sheet.cell_value(row,7))		#------------ Bday Number format --------------
					mdatesplit = mdate.rsplit("-",2)
					
					dateformat = (f"{mnthDic.get(mdatesplit[0])} {mdatesplit[1]} {mdatesplit[2]}")
					ind_data.append(dateformat)									#------------ Date of Birth Normal Format ------------------
									
				except Exception:
					print(f'Date of Birth of {splitName[0]}, {splitName[1]} has different date format')
					ind_data.append(mdate)

				ind_data.append(sf1_sheet.cell_value(row,31))				#------------ Mother's Name --------------
				ind_data.append(sf1_sheet.cell_value(row,27))				#------------ Father's Name --------------
				ind_data.append(sf1_sheet.cell_value(row,36))				#------------ Guardian's Name --------------
				ind_data.append("")											#------------ Modality --------------	
				ind_data.append("")											#------------ Eligibility --------------		

				tempProfile.append(ind_data)
				row += 1

		return tempProfile

	except Exception as e:
		print(e)

def depInfoJHS_SF1(sf1path):

	try:
		dep = []
		sf1book =  xlrd.open_workbook(sf1path)  
		sf1_sheet = sf1book.sheet_by_index(0)

		schoolYear = sf1_sheet.cell_value(3,19)
		grade = sf1_sheet.cell_value(3,30)
		gradeLevel = grade.split(" ",2)
		section = sf1_sheet.cell_value(3,38)

		dep.extend([schoolYear, gradeLevel[1], section])
		
		return dep

	except:
		print("Error in displaying department info")

# def dateFormartChecker():
# 	sf1book =  xlrd.open_workbook(path)  
# 	sf1_sheet = sf1book.sheet_by_index(0)
# 	row = 6 
# 	dashCount = 0
# 	slashCount = 0
# 	dash  = False		# Date format separator for dash (-)
# 	slash = False		# Date format separator for slash (/)

# 	newBDayDash = []
# 	newBDaySlash = []

# 	for gender in range(2):
# 		row += gender
# 		while len(str(int(sf1_sheet.cell_value(row,0)))) == 12:
# 			mdate = str(sf1_sheet.cell_value(row,7))		#------------ Bday Number format --------------
# 			for s in mdate[:3]:
# 				if s == "-":
# 					dashCount += 1
# 				elif s == "/":
# 				    slashCount += 1
# 				else:
# 					pass

# 			print(mdate)
# 			# mdatesplit = mdate.rsplit("-",2)
# 			row += 1

# 	print(dashCount)
# 	print(slashCount)
# 	if (dashCount > slashCount):
# 		dashCount = True
# 	elif (slashCount > dashCount):
# 		slashCount = True
# 	elif ((slashCount == 0) and (dashCount == 0)): 
# 		print("All birthdate are unsupported format")
# 	else:   ### equal numbers ##
# 		pass

def learnerSHS_SF1(sf1path):

	sf1bookshs =  xlrd.open_workbook(sf1path)  
	sf1_sheetshs = sf1bookshs.sheet_by_index(0)
	tempProfileSHS = []	
	shsrow = 19 

	try:
		for gender in range(2): #----------- loop for Male group and Female group ---------------

			shsrow += gender
			while len(str(int(sf1_sheetshs.cell_value(shsrow,0)))) == 12:
				shsind_data = []
				shsind_data.append(str(int(sf1_sheetshs.cell_value(shsrow,0))))           #------------ LRN --------------

				fullName = sf1_sheetshs.cell_value(shsrow,2)						#------------ Full Name --------------  
				splitName = fullName.rsplit(",",2)

				mdname = splitName[1].rsplit(" ",2)
			
				shsind_data.append(splitName[0])									#------------ Last Name -------------- 
				shsind_data.append(mdname[0])										#------------ First Name -------------- 

				shsind_data.append(mdname[1])										#------------ Middle Name if any ----------

				shsind_data.append("")											    #------------ Name Extension ------------------

				if (sf1_sheetshs.cell_value(shsrow,10)) == 'M':
					shsind_data.append('MALE')										#------------ MALE or FEMALE --------------
				else:
					shsind_data.append('FEMALE')

				shsind_data.append(sf1_sheetshs.cell_value(shsrow,14))				#------------ Age --------------

				brgy = sf1_sheetshs.cell_value(shsrow,25)				#------------ Barangay --------------
				mun =  sf1_sheetshs.cell_value(shsrow,30)				#------------ Municipality --------------
				prov = sf1_sheetshs.cell_value(shsrow,32)				#------------ Province -------------

				shsind_data.append((brgy + ', ' + mun + ', ' + prov))			#------------- Complete Address ----------------

				try:
					mdate = str(sf1_sheetshs.cell_value(shsrow,11))		#------------ Bday Number format --------------
					mdatesplit = mdate.rsplit("/",2)
					
					dateformat = (f"{mnthDic.get(mdatesplit[0])} {mdatesplit[1]} {mdatesplit[2]}")
					shsind_data.append(dateformat)									#------------ Date of Birth Normal Format ------------------
									
				except Exception:
					print(f'Date of Birth of {splitName[0]}, {mdname[0]} has different date format')
					shsind_data.append(mdate)

				shsind_data.append(sf1_sheetshs.cell_value(shsrow,41))				#------------ Mother's Name --------------
				shsind_data.append(sf1_sheetshs.cell_value(shsrow,36))				#------------ Father's Name --------------
				shsind_data.append(sf1_sheetshs.cell_value(shsrow,43))				#------------ Guardian's Name --------------
				shsind_data.append("")												#------------ Modality --------------
				shsind_data.append("")												#------------ Eligibilty --------------

				tempProfileSHS.append(shsind_data)

				gradesName = shsind_data[1] + ', ' + shsind_data[2] 
						
				shsrow += 1

		return tempProfileSHS

	except Exception as e:
		print(e)

def depInfoSHS_SF1(sf1path):

	try:
		dep = []
		sf1book =  xlrd.open_workbook(sf1path)  
		sf1_sheet = sf1book.sheet_by_index(0)

		schoolYear = sf1_sheet.cell_value(8,18)
		grade = sf1_sheet.cell_value(8,29)
		section = sf1_sheet.cell_value(15,8)

		dep.extend([schoolYear, grade, section])
		
		return dep

	except:
		print("Error in displaying department info")

