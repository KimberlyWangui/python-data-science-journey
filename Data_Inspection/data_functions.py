import pandas as pd

def data_inspection(filepath):
    """
    LOADING, PREVIEWING, AND INSPECTING DATA
    """
    # Check for  json, csv, or excel file
    df = pd.read_csv(filepath)
    print("--- PREVIEWING DATA ---")
    print(df.head())

    print("--- INSPECTING DATA ---")
    print(df.info())

    print("--- SHAPE OF DATA ---")
    print(df.shape)

    print("--- SUMMARY STATISTICS ---")
    print(df.describe())


def data_cleaning_duplicates(filepath):
    """
    CLEANING DATA
    """
    df = pd.read_csv(filepath)
    print("--- CHECKING FOR DUPLICATES ---")
    return df.duplicated().sum()