import gspread
from pprint import pprint

gc = gspread.service_account(filename='creds.json',
                             scopes=gspread.auth.DEFAULT_SCOPES)
spreadsheet = gc.open('astronauts')
worksheet = spreadsheet.worksheet('astronauts')

def main():
    sheet_data = worksheet.get_all_values()