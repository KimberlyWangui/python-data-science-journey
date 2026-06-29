import pandas as pd
import matplotlib.pyplot as plt

def load_data(filepath):
    """"LOADING DATA
    """
    df = pd.read_csv(filepath)
    return df

def data_inspection(df):
    """
    LOADING, PREVIEWING, AND INSPECTING DATA
    """
    print("--- PREVIEWING DATA ---")
    print(df.head())

    print("--- INSPECTING DATA ---")
    print(df.info())

    print("--- SHAPE OF DATA ---")
    print(df.shape)

    print("--- SUMMARY STATISTICS ---")
    print(df.describe())


def data_cleaning_duplicates(df):
    """
    CLEANING DATA
    """
    print("--- CHECKING FOR DUPLICATES ---")
    return df.duplicated().sum()

def data_cleaning_missing_values(df):
    """
    CLEANING DATA
    """
    print("--- CHECKING FOR MISSING VALUES ---")
    return df.isnull().sum()

# Impute numerical columns with mean
def data_cleaning_impute_numerical(df, column_name):
    print("--- IMPUTING NUMERICAL COLUMNS WITH MEAN ---")
    df = df[column_name].fillna(df[column_name].mean())
    return df

# Impute numerical columns with 0
def data_cleaning_impute_numerical_with_zero(df, column_name):
    print("--- IMPUTING NUMERICAL COLUMNS WITH 0 ---")
    df = df[column_name].fillna(0)
    return df

# Impute numerical columns with median
def data_cleaning_impute_numerical_with_median(df, column_name):
    print("--- IMPUTING NUMERICAL COLUMNS WITH MEDIAN ---")
    df = df[column_name].fillna(df[column_name].median())
    return df

# Checking and removing outliers
def check_removing_outliers(df, column_name):
    return plt.boxplot(df[column_name])
