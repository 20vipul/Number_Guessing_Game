import csv


class CSVORM:
    """
    A simple read-only ORM for CSV files.
    This class allows you to list, get, and filter data in a CSV file.
    """

    def __init__(self, csv_file):
        """
        Initialize the CSVORM instance with the path to a CSV file.
        Args:
            csv_file (str): The path to the CSV file.
        """
        self.csv_file = csv_file

    def list(self):
        """
        This method makes a list of all the entries in CSV File
        """
        with open(self.csv_file, 'r') as file:
            reader = csv.DictReader(file)
            data = [row for row in reader]
        return data

    def get(self, identity):
        """
        This Method gets a row with a unique ID
        and Returns the Entire Row (case-insensitive)
        """
        identity = int(identity)
        with open(self.csv_file, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if int(row['ID']) == identity:
                    return row
        return None

    def filter(self, column, value):
        """
        This Method takes a column and a specific value of that column
        and returns the information associated with that value (case-insensitive)
        """
        value = value.lower()  # Convert user input to lowercase
        with open(self.csv_file, 'r') as file:
            reader = csv.DictReader(file)
            reader.fieldnames = [F.lower() for F in reader.fieldnames]
            data = [row for row in reader if row.get(column).lower() == value]
            data_title = [{key.title(): val for key, val in row.items()} for row in data]
        return data_title


def main():
    # Ask the user to enter the CSV file path
    print("Sample path: C:\\Users\\Palash\\Desktop\\ORM.csv")
    csv_file = input("Enter the path to the CSV file: ")
    orm = CSVORM(csv_file)

    print("Listing all rows:")
    print(orm.list())

    print("\nGetting a specific row by ID:")
    id_to_get = int(input("Enter an ID to retrieve: "))
    print(orm.get(id_to_get))

    print("\nFiltering rows by a specific column and value:")
    column_filter = input("Enter the column name to filter: ")
    value_filter = input(f"Enter the value to filter in the '{column_filter}' column: ")
    print(orm.filter(column_filter, value_filter))


if __name__ == '__main__':
    main()
