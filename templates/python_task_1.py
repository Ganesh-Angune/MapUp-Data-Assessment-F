#Question 1: Car Matrix Generation
import pandas as pd


def generate_car_matrix(df)->pd.DataFrame:
    """
    Creates a DataFrame  for id combinations.

    Args:
        df (pandas.DataFrame)

    Returns:
        pandas.DataFrame: Matrix generated with 'car' values, 
                          where 'id_1' and 'id_2' are used as indices and columns respectively.
    """
    # Write your logic here
    # Create a pivot table with 'id_1' as index, 'id_2' as columns, and 'car' as values
    car_matrix = df.pivot_table(index='id_1', columns='id_2', values='car', fill_value=0)

     # Set diagonal values to 0
    for index in car_matrix.index:
        car_matrix.loc[index, index] = 0

    return car_matrix


#Question 2: Car Type Count Calculation
def get_type_count(df)->dict:
    """
    Categorizes 'car' values into types and returns a dictionary of counts.

    Args:
        df (pandas.DataFrame)

    Returns:
        dict: A dictionary with car types as keys and their counts as values.
    """
    # Write your logic here
     # Add a new column 'car_type' based on conditions
    df['car_type'] = pd.cut(df['car'], bins=[-float('inf'), 15, 25, float('inf')],
                            labels=['low', 'medium', 'high'], right=False)
    
    # Calculate the count of occurrences for each car_type category
    type_counts = df['car_type'].value_counts().to_dict()
    
     # Sort the dictionary alphabetically based on keys
    sorted_type_counts = dict(sorted(type_counts.items()))

    return sorted_type_counts
    

#Question 3: Bus Count Index Retrieval
def get_bus_indexes(df)->list:
    """
    Returns the indexes where the 'bus' values are greater than twice the mean.

    Args:
        df (pandas.DataFrame)

    Returns:
        list: List of indexes where 'bus' values exceed twice the mean.
    """
    # Write your logic here
    def get_bus_indexes(df):
    # Calculate the mean value of the 'bus' column
    mean_bus = df['bus'].mean()

    # Identify indices where 'bus' values are greater than twice the mean
    bus_indexes = df[df['bus'] > 2 * mean_bus].index.tolist()

    # Sort the list in ascending order
    bus_indexes.sort()

    return bus_indexes


#Question 4: Route Filtering
def filter_routes(df)->list:
    """
    Filters and returns routes with average 'truck' values greater than 7.

    Args:
        df (pandas.DataFrame)

    Returns:
        list: List of route names with average 'truck' values greater than 7.
    """
    # Write your logic here
    # Filter routes based on the average of values in the 'truck' column
    routes_filtered = df.groupby('route')['truck'].mean().loc[lambda x: x > 7].index.tolist()

    # Sort the list of routes in ascending order
    routes_filtered.sort()

    return routes_filtered
    


#Question 5: Matrix Value Modification
def multiply_matrix(matrix)->pd.DataFrame:
    """
    Multiplies matrix values with custom conditions.

    Args:
        matrix (pandas.DataFrame)

    Returns:
        pandas.DataFrame: Modified matrix with values multiplied based on custom conditions.
    """
    # Write your logic here
     # Create a copy of the input matrix to avoid modifying the original
    modified_matrix = input_matrix.copy()

    # Apply the logic to modify values in the DataFrame
    for column in modified_matrix.columns:
        for index in modified_matrix.index:
            value = modified_matrix.at[index, column]
            if value > 20:
                modified_matrix.at[index, column] = round(value * 0.75, 1)
            else:
                modified_matrix.at[index, column] = round(value * 1.25, 1)

    return modified_matrix

    
#Question 6: Time Check

def time_check(df)->pd.Series:
    """
    Use shared dataset-2 to verify the completeness of the data by checking whether the timestamps for each unique (`id`, `id_2`) pair cover a full 24-hour and 7 days period

    Args:
        df (pandas.DataFrame)

    Returns:
        pd.Series: return a boolean series
    """
    # Write your logic here
import pandas as pd

def verify_timestamps(df):
    # Convert 'timestamp' column to datetime format
    df['timestamp'] = pd.to_datetime(df['timestamp'])

    # Extract day of the week and hour from timestamp
    df['day_of_week'] = df['timestamp'].dt.dayofweek
    df['hour'] = df['timestamp'].dt.hour

    # Create a mask for incorrect timestamps
    mask = ((df['day_of_week'] < 0) | (df['day_of_week'] > 6) | (df['hour'] < 0) | (df['hour'] > 23))

    # Create a boolean series with multi-index (id, id_2)
    incorrect_timestamps = df[mask].set_index(['id', 'id_2']).index.unique()

    # Create a boolean series indicating if each (id, id_2) pair has incorrect timestamps
    result_series = df.set_index(['id', 'id_2']).index.isin(incorrect_timestamps)

    return result_series
    return pd.Series()
