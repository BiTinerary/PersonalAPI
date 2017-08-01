import gspread, datetime, sys, re, os
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds']
credentials = ServiceAccountCredentials.from_json_keyfile_name('%s/customScripts/GspreadTimeClock-d5dad30dfff8.json' % os.getcwd(), scope)
gc = gspread.authorize(credentials)
sheet = gc.open('Time Sheet')
worksheet = sheet.get_worksheet(0) # process, work on the first tab within above spreadsheet.

names = ['Izaac','Izaac','Izaac']

def writeToLog(input):
	with open('%s/customScripts/TimeSheetLog.csv' % os.getcwd(), 'a') as timeSheet:
		timeSheet.write(input)

def WhosPunchingCard(intIn): # pass integer variable from selected radio button
	if intIn == 1:
		return names[0] # depending on integer, pass name of employee from names array
	elif intIn == 2:
		return names[1] # could easily be employee ID number
	elif intIn == 3:
		return names[2]

def getRowColumnTuple(self): # ugly code for stripping/regex/parsing hardcoded info from the google sheets.
	self = str(self) # 
	findRegex = str(worksheet.find(self)) 
	stringy = "'" #google response fluff
	stripSyntax = findRegex.rstrip('%s%s%s>' % (stringy, self, stringy)) #strip excess characters from Google's response.
	stripMoreSyntax = stripSyntax.lstrip('<Cell ') # strip Google response, to bare minimum info.
	
	rowRegex = re.compile(r'R(\d{2}|\d)') # regex parameters for parsing googles API internal response. 
	colRegex = re.compile(r'C(\d{2}|\d)')
	searchRow = rowRegex.search(stripMoreSyntax) # actually search, using regex as cross reference.
	searchCol = colRegex.search(stripMoreSyntax)
	finalRowLocation = searchRow.group() # string output of regex search, when matched.
	finalColumnLocation = searchCol.group()

	justTheRowInt = str(finalRowLocation).lstrip('R') # take off R/C string character, leave value. 
	justTheColInt = str(finalColumnLocation).lstrip('C')
	
	return int(justTheRowInt), int(justTheColInt) # return row, column tuple of found/matched cells corresponding to employee name, and todays date on the spreadsheet.

def getRowOrColumnWithTodaysDate(): #pass specially formatted datetime to row/column function. Which gets coordinates of cell corresponding to todays date.
	todayToTuple = getRowColumnTuple(str(datetime.date.today().strftime('X%m/X%d/20%y').replace('X0', '').replace('X', '')))
	return todayToTuple

def militaryTimestampWithNoSeconds(): # return current time. For clock in/out stamp.
	return datetime.datetime.now().strftime('%H:%M')

def getClockInCellAndEdit(intIn): # the final goods! line 61 is google API command being passed, coordinates of cell with todays date, employee column and current time.
	employeesColumn = getRowColumnTuple(WhosPunchingCard(intIn))[1] # get row/column coordinates of employee who is punching time card.
	worksheet.update_cell(getRowOrColumnWithTodaysDate()[0], employeesColumn, militaryTimestampWithNoSeconds()) # passing column of cell, row of cell, and what to update it with.
	#print(str(names[intIn-1])) #debug, sanity check.
	namePunchAction = 'Name: %s\nDate: %s\nTime: %s\nAction: ClockIn\n' % (str(names[intIn-1]), datetime.date.today().strftime('%m/%d/%y'), militaryTimestampWithNoSeconds())
	writeToLog(namePunchAction)
	return namePunchAction

def getClockOutCellAndEdit(intIn): # Final goods, for clock out.
	employeesColumn = int(getRowColumnTuple(WhosPunchingCard(intIn))[1]) + 1 # Same as clock in but plus one. eg. Clock in is on column 5, clock out is column 6. 
	worksheet.update_cell(getRowOrColumnWithTodaysDate()[0], employeesColumn, militaryTimestampWithNoSeconds())
	#print(str(names[intIn-1])) #debug, sanity check.
	namePunchAction = 'Name: %s\nDate: %s\nTime: %s\nAction: ClockOut\n' % (str(names[intIn-1]), datetime.date.today().strftime('%m/%d/%y'), militaryTimestampWithNoSeconds())
	writeToLog(namePunchAction)
	return namePunchAction

def clockInOrOut(argInput):
	#argInput = sys.argv[1]
	if argInput == 'clockin':
		return getClockInCellAndEdit(1)
	elif argInput == 'clockout':
		return getClockOutCellAndEdit(1)


try:
	print clockInOrOut(sys.argv[1])
except:
	print "Date Not Found! Newest Spreadsheet available?"
	print "Writing to log"
	workSheetName = re.findall(r"'(.*?)'", str(worksheet))
	print worksheet
	print workSheetName[0]
