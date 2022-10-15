import pandas as pd


def main():
    df = pd.read_excel(io='input/Berlin.xlsx')
    df = df[['Address', 'Viewed', 'Applied']]
    print(df)


if __name__ == '__main__':
    main()
