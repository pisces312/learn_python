from pandas import DataFrame, Series
import numpy as np

#################
# Syntax Reminder:
#
# The following code would create a two-column pandas DataFrame
# named df with columns labeled 'name' and 'age':
#
# people = ['Sarah', 'Mike', 'Chrisna']
# ages  =  [28, 32, 25]
# df = DataFrame({'name' : Series(people),
#                 'age'  : Series(ages)})


def create_dataframe():
    '''
    Create a pandas dataframe called 'olympic_medal_counts_df' containing
    the data from the table of 2014 Sochi winter olympics medal counts.  

    The columns for this dataframe should be called 
    'country_name', 'gold', 'silver', and 'bronze'.  

    There is no need to  specify row indexes for this dataframe 
    (in this case, the rows will automatically be assigned numbered indexes).

    You do not need to call the function in your code when running it in the
    browser - the grader will do that automatically when you submit or test it.
    '''

    countries = ['Russian Fed.', 'Norway', 'Canada', 'United States',
                 'Netherlands', 'Germany', 'Switzerland', 'Belarus',
                 'Austria', 'France', 'Poland', 'China', 'Korea',
                 'Sweden', 'Czech Republic', 'Slovenia', 'Japan',
                 'Finland', 'Great Britain', 'Ukraine', 'Slovakia',
                 'Italy', 'Latvia', 'Australia', 'Croatia', 'Kazakhstan']

    gold = [13, 11, 10, 9, 8, 8, 6, 5, 4, 4, 4, 3,
            3, 2, 2, 2, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0]
    silver = [11, 5, 10, 7, 7, 6, 3, 0, 8, 4, 1, 4,
              3, 7, 4, 2, 4, 3, 1, 0, 0, 2, 2, 2, 1, 0]
    bronze = [9, 10, 5, 12, 9, 5, 2, 1, 5, 7, 1, 2,
              2, 6, 2, 4, 3, 1, 2, 1, 0, 6, 2, 1, 0, 1]

    # Option 1: Cast values to Series object
    # olympic_medal_counts = {'country_name': Series(countries),
    #                         'gold': Series(gold),
    #                         'silver': Series(silver),
    #                         'bronze': Series(bronze)}

    # Option 2:
    olympic_medal_counts = {'country_name': countries,
                            'gold': gold,
                            'silver': silver,
                            'bronze': bronze}

    olympic_medal_counts_df = DataFrame(olympic_medal_counts)

    return olympic_medal_counts_df


def avg_bronze_at_least_one_gold(df):
    '''
    Compute the average number of bronze medals earned by countries who 
    earned at least one gold medal.  

    Save this to a variable named avg_bronze_at_least_one_gold. You do not
    need to call the function in your code when running it in the browser -
    the grader will do that automatically when you submit or test it.

    HINT-1
    You can retrieve all of the values of a Pandas column from a 
    data frame, df, as follows
    df['column_name']

    HINT-2
    The numpy.mean function can accept as an argument a single
    Pandas column. 

    For example, numpy.mean(df[col_name]) would return the 
    mean of the values located in col_name of a dataframe df.
    '''

    # Option 1:
    avg_bronze_at_least_one_gold = np.mean(df[df.gold >= 1].bronze)
    # Option 2:
    # avg_bronze_at_least_one_gold=np.mean(df[df['gold']>=1].bronze)
    # Option 3:
    # avg_bronze_at_least_one_gold=np.mean(df['bronze'][df['gold']>=1])

    return avg_bronze_at_least_one_gold


def avg_medal_count(df):
    '''
    Using the dataframe's apply method, create a new Series called 
    avg_medal_count that indicates the average number of gold, silver,
    and bronze medals earned amongst countries who earned at 
    least one medal of any kind at the 2014 Sochi olympics.  Note that
    the countries list already only includes countries that have earned
    at least one medal. No additional filtering is necessary.

    '|' is or
    '''

    # Option 1:
    # the order doesn't matter
    at_least_one_medal = df[(df.gold >= 1) | (df.silver >= 1) | (
        df.bronze >= 1)][['gold', 'silver', 'bronze']]

    # Option 2:
    # at_least_one_medal=df[['gold','silver','bronze']][(df.gold>=1)|(df.silver>=1)|(df.bronze>=1)]

    # Option 3:
    # or not specify columns, it will calculate all numerical columns
    # at_least_one_medal=df[(df.gold>=1)|(df.silver>=1)|(df.bronze>=1)]

    avg_medal_count = np.mean(at_least_one_medal)

    return avg_medal_count


if __name__ == '__main__':
    df = create_dataframe()
    print(df)
    avg_bronze_at_least_one_gold = avg_bronze_at_least_one_gold(df)
    print(avg_bronze_at_least_one_gold)
    avg_medal_count = avg_medal_count(df)
    print(avg_medal_count)
