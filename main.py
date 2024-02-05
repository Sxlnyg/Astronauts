import gspread

from collections import Counter

gc = gspread.service_account(filename='creds.json',
                             scopes=gspread.auth.DEFAULT_SCOPES)
spreadsheet = gc.open('astronauts')
worksheet = spreadsheet.worksheet('astronauts')


def main():
    sheet_data = worksheet.get_all_values()
    birth_months = [int(entry[4].split('/')[0]) for entry in sheet_data[1:]]
    month_counts = Counter(birth_months)
    sorted_months = sorted(month_counts.items(), key=lambda x: x[1], reverse=True)
    top_three_months = sorted_months[:3]
    total_births = sum(month_counts.values())
    print("A három leggyakoribb születési hónap az űrhajósok között:")
    for month, count in top_three_months:
        percentage = (count / total_births) * 100
        print(f"{month}. hónap: {percentage:.1f}%")

main()