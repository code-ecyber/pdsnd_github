import time
import pandas as pd
import numpy as np
import csv

CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}

city = ['chicago', 'washington', 'new york city']

months = ['january', 'february', 'march', 'april', 'may', 'june', 'all']

days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday'] 

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input('Please enter city, either washington, chicago, or new york city: ').lower()
        if city not in CITY_DATA:
            print("City is invalid, please choose one of the three suggested cities.")
            continue
        else:
            break

    # get user input for month (all, january, february, ... , june)
    while True:
        month = input('Which month would you like to select for this statistic?: ')
        if month not in months:
            print("Month is invalid, please enter a valid month.")
            continue
        else:
            break
    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input('Please input the day in which you would like statistics for.: ')
        if day not in days:
            print("Day is invalid, please enter a valid day.")
            continue
        else:
            break		
    print('-'*40)
    return city, month, day 


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
   # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month, day of week, and hour from Start Time to create new columns(month, day_of_week, hour)
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day
    df['hour'] = df['Start Time'].dt.hour

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int, filter by month to create the new dataframe
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df[df['day_of_week'] == day.title()]
        return df
	#filter by hour if applicable
    if hour != 'all':
       #filter by hour to create new df
       df = df[df['hour'] == hour]
       return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    common_month = df['month'].mode()[0]    
    print('The most common month is', common_month)
    # display the most common day of week
    common_day = df['day_of_week'].mode()[0]
    print('The most common day is', common_day)
    # display the most common start hour
    common_hour = df['hour'].mode()[0]
    print('The most common hour is', common_hour)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    common_st_station = df['Start Station'].mode()[0]
    print('The most common start station is', common_st_station)
    # display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print('The most common end station is', common_end_station)
    # display most frequent combination of start station and end station trip
    frequent_combo_st_end = df.groupby(['Start Station', 'End Station']).count().idxmax()
    print('The most frequent start and end street combination is', frequent_combo_st_end)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    trip_duration = df["Trip Duration"]
    print('The total trip duration is', trip_duration)

    # display mean travel time
    trip_duration_mean = df["Trip Duration"]
    trip_duration_mean.mean()
    print('the mean travel time is', trip_duration_mean)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""
    print('\nCalculating User Stats...\n')
    start_time = time.time()
    # Display counts of user types
    user_type = df['User Type'].value_counts()
    print('The count of user type is', user_type)
    # Display counts of gender
    if "Gender" in df.columns:
        gender_type = df['Gender'].value_counts()
        print('The gender types are below.')
    else:
        print("Gender column does not exist")
    # Display most common year of birth
    if "Birth Year" in df.columns:
        birth_year = df['Birth Year'].mode()
        print('The most common year of birth is', birth_year)
    else:
        print("The birth year column doesn't exist")
    # Display earliest year of birth
    if "Birth Year" in df.columns:
        birth_year_min = df['Birth Year'].min()
        print('The earliest year of birth is', birth_year_min)
    else:
        print("The birth year column doesn't exist")
    # Display most recent year of birth
    if "Birth Year" in df.columns:
        birth_year_max = df['Birth Year'].max()
        print('The most recent birth year is', birth_year_max)
    else:
        print("The birth year column doesn't exist.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):
    #ask for raw data first 5 and then next 5 raw data rows
    while True:
        view_input_five = input('\nWould you like to see first 5 rows of data? Please enter yes or no:').lower()
        if view_input_five in ('yes', 'y'):
            n = 0
            print(df.iloc[n:n+5])
        n += 5
        break
    while True:
        view_more_data = input('Would you like to see next 5 rows of data? Please enter yes or no:').lower()
        if view_more_data != ('yes', 'y'):
            m = 1
            print(df.iloc[m:m+10])
        m += 20
        break
        print(view_more_data)
    return

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
