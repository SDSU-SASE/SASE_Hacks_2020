# Contact Info Written to Excel
import xlwt
from xlwt import Workbook
from xlrd import open_workbook
from xlutils.copy import copy

rowNumber = 1


# Creates an Excel File for all the Contact Information (RUN THIS FIRST)
def create_excel():
    wb = Workbook()
    sheet1 = wb.add_sheet('Contact Information')
    sheet1.write(0, 0, 'Last Name')
    sheet1.write(0, 1, 'First Name')
    sheet1.write(0, 2, 'Middle Name')
    sheet1.write(0, 3, 'Email')
    sheet1.write(0, 4, 'Phone Number')
    wb.save('Patient Contact Information.xls')


# Edits Said Excel File and then Increments the Row for the Next Function Call
def edit_excel(last, first, middle, email, phone):
    w = open_workbook('Patient Contact Information.xls')
    w_copy = copy(w)
    w_copy.get_sheet(0).write(rowNumber, 0, last)
    w_copy.get_sheet(0).write(rowNumber, 1, first)
    w_copy.get_sheet(0).write(rowNumber, 2, middle)
    w_copy.get_sheet(0).write(rowNumber, 3, email)
    w_copy.get_sheet(0).write(rowNumber, 4, phone)
    ++rowNumber
    w_copy.save('Patient Contact Information.xls')


print("Creating Excel")
create_excel()

print("Enter First Name")
firstName = input()

print("Enter Last Name")
lastName = input()

print("Enter Middle Name")
middleName = input()

print("Enter Email")
email = input()

print("Enter Phone")
phone = input()

edit_excel(lastName, firstName, middleName, email, phone)
print("Done")