# Contact Info Written to Excel
import xlwt
from xlwt import Workbook
from xlutils.copy import copy

rowNumber = 1


# Creates an Excel File for all the Contact Inforamtion (RUN THIS FIRST)
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
    w = copy('Patient Contact Information.xls')
    w.get_sheet(0).write(rowNumber, 0, last)
    w.get_sheet(0).write(rowNumber, 1, first)
    w.get_sheet(0).write(rowNumber, 2, middle)
    w.get_sheet(0).write(rowNumber, 3, email)
    w.get_sheet(0).write(rowNumber, 4, phone)
    ++rowNumber
    w.save('Patient Contact Information.xls')
