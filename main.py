import csv
import unidecode


def grab_input_filename() -> str:
    return input('Input Filename [input.csv]: ') or 'input.csv'


def read_input_file() -> list:
    with open(filename, 'rt', encoding='utf-8-sig') as csv_file:
        reader = csv.reader(csv_file, quoting=csv.QUOTE_NONE, doublequote=False)
        return list(reader)


def grab_column() -> int:
    return max(0, int(input("Column position [default 1]: ") or "1") - 1)


def grab_contains_text() -> list:
    compare_filename = input('Compare File [names.csv]: ') or 'names.csv'
    with open(compare_filename, 'rt', encoding='utf-8-sig') as csv_file:
        reader = csv.reader(csv_file, quotechar='"', quoting=csv.QUOTE_NONE)
        compare_against_list = []
        for row in reader:
            compare_against_list.append(row[0].upper())

        return compare_against_list


def compare_list() -> list:
    matching_rows = [input_list[0]]
    input_list.pop(0)
    for row in input_list:
        comparing_cell = unidecode.unidecode(row[column_index].upper())
        comparing_cell = comparing_cell.replace('"', '')
        comparing_cell = comparing_cell.split(' ')
        for comparison in comparison_list:
            if unidecode.unidecode(comparison.upper()) in comparing_cell:
                matching_rows.append(row)
                break

    return matching_rows


def output_to_file():
    with open('ouput.csv', mode='w') as csv_file:
        writer = csv.writer(csv_file)
        for row in output_rows:
            for index, column in enumerate(row):
                row[index] = column.replace('"', '')

            writer.writerow(row)


if __name__ == '__main__':
    filename = grab_input_filename()
    column_index = grab_column()
    comparison_list = grab_contains_text()
    input_list = read_input_file()
    output_rows = compare_list()
    output_to_file()
    print(f'Found {max(0, len(output_rows))} rows, outputting to output.csv')