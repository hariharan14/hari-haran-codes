# TODO: Files and Directories
from pathlib import Path

# path = Path()  # empty to use the current directory
# path1 = Path('C:/Users/Hari/PycharmProjects/hari-haran-codes/tests/basics_of_python') # absolute path of current directory, like this we can use any path
# print(path.exists())
# print(path1.exists())
#
# path2 = Path("local_venv") # relative path
# print(path2.exists())

# path3 = Path("emails")
# path3.mkdir() # creates a folder in the current directory, also cannot create a directory if its already created - Cannot create a file when that file already exists: 'emails'
# path3.rmdir() # removes the directory, also cant remove if its not there - The system cannot find the file specified: 'emails'

# working with current directory i.e. basics_of_python
# path = Path()
# print(path.glob("*")) # it will create generative objects which we can iterate thru and print the files
# for files in path.glob("*"):
#     print(files) # print literally all the files
# print("\n")
# for files in path.glob("*.*"):
#     print(files) # prints files having dot extension
# print("\n")
# for files in path.glob("*.txt"):
#     print(files) # prints nothing
# print("\n")
# for files in path.glob("*.py"):
#     print(files)
# print("\n")

# TODO: Automating Spreadsheets - to decrease the price in the 3rd column by 10% which we can multiply by 0.9
# import openpyxl as xl
#
# def process_workbook(name):
#     wb = xl.load_workbook(name) # load_workbook is a method available inside excel.py and not a method of ExcelReader
#     sheet = wb['Sheet1']
#     # cell = sheet['A1'] # accessing the cell directly with coordinates
#     cell = sheet.cell(1, 1) # cell is a method of WorkSheet
#     # print(cell) # prints the cell for the sheet1 - <Cell 'Sheet1'.A1>
#     # print(cell.value) # value is a method of Cell
#
#     for row in range(2, sheet.max_row + 1): # max_row is a method of WorkSheet to find the max rows in the given sheet
#         cell = sheet.cell(row, 3)
#         print(cell.value) # prints the values of the 3rd column excluding the title
#         corrected_val = cell.value * 0.9
#         corrected_val_cell = sheet.cell(row, 4)
#         corrected_val_cell.value = corrected_val
#
#     from openpyxl.chart import BarChart, Reference
#
#     values = Reference(sheet, min_row=2, max_row=sheet.max_row, min_col=4, max_col=4)
#
#     bar = BarChart() # bar is the instance of the class BarChart
#     bar.add_data(values) # add_data is a method of ChartBase
#     sheet.add_chart(bar, 'e2') # add_chart is a method of WorkSheet
#
#     wb.save("2.xlsx")
#
# enter = input(">")
# process_workbook(enter)