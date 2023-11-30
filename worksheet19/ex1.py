import csv

def display_data_html(file, htmlfile, htmltitle):

    # open the csv file and get the data
    data = get_datalist_from_csv(file)

    # if file not found, raise FileNotFoundError
    if data == "FileNotFoundError":
        raise FileNotFoundError

    with open(htmlfile, 'w') as html:
        html.write('<html>\n')
        html.write('<title>' + htmltitle + '</title>\n')
        html.write('<center>\n')
        html.write('<h1>' + htmltitle + '</h1>\n')

        # generate the html table
        html_table = create_html_table_with_data(data)
        html.write(html_table)
        html.write('</center>\n')
        html.write('</html>\n')

    print(f'{htmlfile} generated.')

# split data in csv file to header and data, and return the data
# if file is not found, return "FileNotFoundError"
def get_datalist_from_csv(csvfile):
    try:
        with open(csvfile, "r") as data:
            data.readline()
            reader = csv.reader(data)
            datalist = list(reader)
            return datalist
    except FileNotFoundError:
        return "FileNotFoundError"

# return integer if a number, else return existing value
def check_value(value):
    try:
        value = int(value)
    except ValueError:
        pass
    return value

# calculate total value in data(list), ignore non-number
def total_row(data):
    total = 0
    for i in data:
        if isinstance(i, int):
            total = total + i

    return total

# convert to integer, or 0 if non-number
def convert_to_integer(data):
    try:
        return int(data)
    except ValueError:
        return 0

# create the table and put the data in the table
# adding new column for the total of each row
# also adding new row for the total of each column
def create_html_table_with_data(data):
    # concatenating the string in html format for the html page
    html_string = "<style>\n"
    html_string += "table, th, td {\n border: 1px solid black;\n"
    html_string += "border-collapse: collapse; text-align:center\n"
    html_string += "}\n"
    html_string += "</style>\n"
    html_string += "<table>\n"

    # for the table header
    html_string += "<tr>\n"
    html_string += "<th>Date</th>\n"
    html_string += "<th>Staff</th>\n"
    html_string += "<th>Student</th>\n"
    html_string += "<th>Other</th>\n"
    html_string += "<th>Total</th>\n"
    html_string += "</tr>\n"

    # variables to store sum for each column and grand total
    sum_col1 = 0
    sum_col2 = 0
    sum_col3 = 0
    grand_total = 0

    # read all data items in data and formatting it with html tags
    for record in data:
        html_string += "<tr>\n"
        for datum in record:
            html_string += "<td>" + datum + "</td>\n"

        # from second column in each row, convert the data to int
        # so that can use the sum() function
        y = [check_value(x) for x in record[1:]]

        # calculate the sum for each row, add the value to html
        sum_row = total_row(y)
        html_string += "<td>" + str(sum_row) + "</td>\n"

        # for grand total
        grand_total += sum_row

        # calculate the sum for each column, column 0 is date
        sum_col1 += convert_to_integer(record[1])
        sum_col2 += convert_to_integer(record[2])
        sum_col3 += convert_to_integer(record[3])
        html_string += "</tr>\n"

    # add the row for the totals and format it to bold
    html_string += "<tr>\n"
    html_string += "<td><b>Grand Total</b></td>\n"
    html_string += "<td><b>" + str(sum_col1) + "</b></td>\n"
    html_string += "<td><b>" + str(sum_col2) + "</b></td>\n"
    html_string += "<td><b>" + str(sum_col3) + "</b></td>\n"
    html_string += "<td><b>" + str(grand_total) + "</b></td>\n"
    html_string += "</tr>\n"

    html_string += "</table>\n\n"
    return html_string

if __name__ == "__main__":
    display_data_html("covid_oct_2020.csv", "oct.html",
                      "UoL covid cases in Oct 2020")



