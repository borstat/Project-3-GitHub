import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')

    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a     while loop to handle invalid inputs
    while True:
        city = input("Enter a city (chicago, new york city, washington): ").lower()
        if city in CITY_DATA:
            break
        else:
            print("Invalid city. Please try again.")

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input("Enter a month (all, january, february, ..., june): ").lower()
        valid_months = ["all", "january", "february", "march", "april", "may", "june"]
        if month in valid_months:
            break
        else:
            print("Invalid month. Please try again.")


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input("Enter a day of the week (all, monday, tuesday, ... sunday): ").lower()
        valid_days = ["all", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
        if day in valid_days:
            break
        else:
            print("Invalid day. Please try again.")

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
    filename = CITY_DATA[city]
    df = pd.read_csv(filename)

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
    
        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # Convert the 'Start Time' column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    # TO DO: display the most common month
    months = ['january', 'february', 'march', 'april', 'may', 'june']
    most_common_month = df['month'].mode()[0]
    print("Most common month:", most_common_month)

    # TO DO: display the most common day of week
    most_common_day = df['day_of_week'].mode()[0]
    print("Most common day of week:", most_common_day)

    # Display earliest, most recent, and most common start hour
    print('Earliest start time:', df['Start Time'].min())
    print('Most recent start time:', df['Start Time'].max())
    print('Most common start hour:', df['Start Time'].dt.hour.mode()[0]) 

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
   
    # Display most commonly used start and end stations, and most frequent combination
    print('Most commonly used start station:', df['Start Station'].mode()[0])
    print('Most commonly used end station:', df['End Station'].mode()[0])
    print('Most frequent combination of start station and end station trip:',
          (df['Start Station'] + ' to ' + df['End Station']).mode()[0])

 
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # Display total and average trip duration
    print('Total travel time:', df['Trip Duration'].sum())
    print('Average travel time:', df['Trip Duration'].mean())
 
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print(df['User Type'].value_counts())

    # Check if 'Gender' column exists, then display counts of gender
    if 'Gender' in df:
        print(df['Gender'].value_counts())

    # Check if 'Birth Year' column exists, then display earliest, most recent, and most     common year of birth
    if 'Birth Year' in df:
        print('Earliest year of birth:', df['Birth Year'].min())
        print('Most recent year of birth:', df['Birth Year'].max())
        print('Most common year of birth:', df['Birth Year'].mode()[0])



def raw_data(df):  # Pass the DataFrame as an argument

    row_index = 0

    while True:
        show_data = input("Do you want to see 5 lines of raw data? (yes/no): ")

        if show_data.lower() == 'yes':
           end_index = min(row_index + 5, len(df)) 
           print(df[row_index:end_index])
           row_index = end_index  

         if row_index >= len(df):
            print("No more data to display.")
                break
        else:
            print("Thank you for using the program!")
            break  



def main():
    while True:
        city, month, day = get_filters()
        print("You selected {}, {}, and {}.".format(city.title(), month.title(),         day.title()))
        
        df = load_data(city, month, day)
        #print(df)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
