import time
import pandas as pd
import numpy as np
from collections import Counter
import sys

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
day_info = {'sunday':1, 'monday':2,'tuesday':3, 'wednesday':4, 'thursday':5, 'friday':6, 'saturday':7, 'all':8}

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    #city = ''
    #city = str(input("Please enter name of city you like to analyze, select from 'Chicago, New York City, Washington: "))
    #city = city.lower()
    while True:
        city = str(input("Please enter name of city you like the Statistics: select from 'Chicago, New York City, Washington: "))
        #city = city.lower()
        if city.lower() not in CITY_DATA.keys():
            print("You has enter wrong city. Please choose from chicago, new york city or washington, enter again")
        else:
            city=city.lower()
            break
    print('You choose {}'.format(city.title()))


    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs


    # TO DO: get user input for month (all, january, february, ... , june)
    #month = ''
    month_info = {'janaury':1, 'februay': 2, 'march': 3, 'april': 4, 'may': 5, 'june': 6, 'all': 7}
    while True:
        month = str(input("Choose month? Janaury, February,March,April,May,June or All?Please type full name of month "))
        #month = month.capitalize()
        if month.lower() not in month_info.keys():
            print("Sorry, Please type month between Janauary to June")
        else:
            month=month.lower()
            break
    print('You choose {}'.format(month.title()))

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    #day = ''
    day_info = {'sunday':1, 'monday':2,'tuesday':3, 'wednesday':4, 'thursday':5, 'friday':6, 'saturday':7, 'all':8}
    while True:
        day = int(input("Which day? Please type your response as an integer. eg. Sunday =1- or 8 for all: "))
        if day not in day_info.values():
            print(" Please type again by entering either the day of week in integer ex: 1 = Sunday")
        else:
           # day = day.lower()
            break
    print('You choose {}'.format(day))

    print('-'*40)
    return city,month,day
    #return CITY_DATA[city],month_info[month],day


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

    # extract month and day of week and hour from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday
    df['hour'] = df['Start Time'].dt.hour
    # filter by month if applicable
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june','all']
        #month = months.lower()
        month =  months.index(month) + 1
        df = df[ df['month'] == month ]

    # filter by day of week if applicable
    print("Day = %s" % day)
    if day != 8:
    # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day]
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    most_common_month = df['month'].value_counts().idxmax()
    print("The most common month is :", most_common_month)

    # TO DO: display the most common day of week
    most_common_day = df['day_of_week'].value_counts().idxmax()
    print("The most common day is:", most_common_day)

    # TO DO: display the most common start hour
    most_common_hour = df['hour'].value_counts().idxmax()
    print("The most common hour is:",most_common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
#user_types = df['User Type'].value_counts()
    common_start_station = df['Start Station'].mode()[0]
    print("The most common start station is:",common_start_station)


    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print("The most common start station is:",common_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    #common_start_end_station = df.apply(Counter, axis='Start Station').value_counts()
    common_start_end_station = df.groupby(['Start Station', 'End Station']).size().idxmax()
    #print(count)
    print("The most frequent combination of start station and end station is:",common_start_end_station)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_duration = df['Trip Duration'].sum()
    print("The total travel duration is: ",total_duration)

    # TO DO: display mean travel time
    mean_travel = df['Trip Duration'].mean()
    print("The mean travel time is:",mean_travel)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print("User Types:")
    print(user_types)

    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
        gender_types = df['Gender'].value_counts()
        print("Gender Types:")
        print(gender_types)

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        max_birth = df['Birth Year'].min()
        print("Earliest birth year is: %d" % max_birth)

        most_recent = df['Birth Year'].max()
        print("Most recent Birth year is: %d" % most_recent)

        common_birth = df['Birth Year'].mode()[0]
        print("The most common birth year is: %d" % common_birth)
    print("\nThis took %s seconds." % (time.time() - start_time))

    print('-'*40)
    #see raw data
def display_data(df):
    start_index = 0
    next_index = 5
    see_data = input("Do you want to see raw data? Please write Yes or No : ").lower()
    #elif see_data == 'yes':
    while see_data == 'yes':
        raw_data = df.iloc[start_index:next_index]
        print(raw_data)
        start_index = next_index
        next_index = next_index+5
        see_data = input("Do you want to see more 5 lines of raw data? Please write yes or no: ").lower()

    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        #print(city,month,day)
        df = load_data(city, month, day)
        #print(city,month,day)

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
