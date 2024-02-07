from collections import Counter


def data_read():
    sheet_data = []
    with open('astronauts.csv', 'r') as file:
        for line in file:
            sheet_data.append(line.strip().split(','))
    return sheet_data


def main():
    birth_months = [int(entry[4].split('/')[0]) for entry in data_read()[1:]]
    month_counts = Counter(birth_months)
    sorted_months = sorted(month_counts.items(), key=lambda x: x[1], reverse=True)
    top_three_months = sorted_months[:3]
    total_births = sum(month_counts.values())
    print("A három leggyakoribb születési hónap az űrhajósok között:")
    for month, count in top_three_months:
        percentage = (count / total_births) * 100
        print(f"{month}. hónap: {percentage:.1f}%")


main()
