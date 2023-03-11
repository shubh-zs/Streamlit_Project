from openpyxl import Workbook, load_workbook 
upfile = r"C:\Users\TransTele\Desktop\2021-22\StreamLit\Parent_Notification\Sample Data\Student Attendance.xlsx"
wb_attendance = load_workbook(r"C:\Users\TransTele\Desktop\2021-22\StreamLit\Parent_Notification\Sample Data\Student Attendance.xlsx")
sheet = wb_attendance["Edit Data"]
roll_Number = {}
row = 1
for no in sheet["C"]:
    if(row != 1):
        if(no.value is not None):
            roll_Number[sheet["A"+str(row)].value] = no.value
    row +=1
print(roll_Number)