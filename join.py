import pandas as pd


def join(file_path_1, file_path_2, column1, column2):
    df1 = pd.read_csv(file_path_1)
    df2 = pd.read_csv(file_path_2)
    #df2.rename(columns = {column2: column1}, inplace = True)
    df3 = pd.merge(df1, df2, 
                    left_on = column1,
                    right_on = column2)

    df3.drop(column2, axis=1, inplace=True)
    print(df3)

    df3.to_csv('mergify_final_table.csv', index=False)

