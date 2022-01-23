import os
import art
import pandas as pd


contaminates_to_keep = [
    'Tetrachloroethene',
    'Trichloroethene',
    'cis-1,2-Dichloroethene',
    'trans-1,2-Dichloroethene',
    'Vinyl chloride'
]


def transform_csv(filepath):
    # Read the CSV into variable data using pandas
    df_csv = pd.DataFrame(pd.read_csv(filepath))
    # Drop the 'Units' column from the CSV
    # df_csv.columns.drop('Units')
    df_csv.drop('Units', axis=1, inplace=True)
    # Transpose the CSV (in place)
    for index, row in df_csv.iterrows():
        # Remove all spaces from the row (using strip) and see
        # if it exists in the list of things to keep
        row_str = str(row[0]).strip()
        if row_str not in contaminates_to_keep:
            print(f'Drop {row_str}')
            df_csv.drop(index, inplace=True)
        else:
            print(f'Keep {row[0]}')
    df_csv = df_csv.T
    # Write (save) the edited CSV to 'nomowork.csv'
    print(df_csv)
    df_csv.to_csv('nomowork.csv', header=False)


def main():
    filepath = input("Enter CSV file path: ")

    # Idiot proofing
    if '.csv' not in filepath:
        print('Please provide a CSV file')
        return

    # Ensure the file provided is real
    if not os.path.exists(filepath):
        print(f'File "{filepath}" does not exist')
        return

    # Open the file at the path provided by the user since
    # we know 1) it ends in CSV and 2) it exists.
    transform_csv(filepath)


if __name__ == '__main__':
    print(art.text2art('Nomowork'))
    main()
