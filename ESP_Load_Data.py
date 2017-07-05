import datetime
from openpyxl import *
wb = load_workbook(filename = 'ESP_Load_Data-Copy.xlsx')
ws = wb.active
print ws
