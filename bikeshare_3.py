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
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        cities = ['chicago', 'new york city', 'washington']
        city = input("Which City's Data Would You Like to Analyze (Chicago, New York City or Washington)\n").lower()
        if city == 'chicago':
            print("Chicago! The Windy City! Let's See What's Next")
            break
        if city == 'new york city':
            print("NYC! The Empire State! Let's See What's Next")
            break
        if city == 'new york city':
            print("Washington! USA! USA! USA! Let's See What's Next")
            break
        else:
            print("Looks Like You're a Bad Speller Too. Please Check Spelling and Try Again.")

    
   
    # get user input for month (all, january, february, ... , june)
    while True:
        months = ['January', 'February', 'March', 'April', 'May', 'June', 'All']
        month = input("Which Month Would You Like to View? (January, Feruary, March, April, May, June or All)").title()
        if month in months:
            break
        else:
            print("I've Never Heard of That Month. Please Check Spelling and Try Again")
    

    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'All']
        day = input("Which Day Would You Like to View? (Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday or All)").title()
        if day in days:
            break
        else:
            print("I've Never Heard of That Day. Please Try Again")

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

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name


    # filter by month if applicable
    if month != 'All':
        # use the index of the months list to get the corresponding int
        months = ['January', 'February', 'March', 'April', 'May', 'June']
        month = months.index(month)+1
    
        # filter by month to create the new dataframe
        df = df[df['month']==month] 

    # filter by day of week if applicable
    if day != 'All':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week']==day]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    if month =='All':
        common_month = df['month'].mode()[0]
        months = ['January','February','March','April','May','June']
        common_month = months[common_month-1]
        print("The Most Popular Month Is",common_month)

    # display the most common day of week
    if day =='All':
        common_day = df['day_of_week'].mode()[0]
        print("The Most Popular Day Of The Week Is",common_day)


    # display the most common start hour
    df['Start Hour'] = df['Start Time'].dt.hour
    common_hour = df['Start Hour'].mode()[0]
    print("The popular Start Hour Is {}:00 hrs".format(common_hour))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print("The most commonly used Start Station is {}".format(common_start_station))


    # display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print("The most Commonly Used End Station Is {}".format(common_end_station))

    # display most frequent combination of start station and end station trip
    df['combination'] = df['Start Station']+" "+"to"+" "+ df['End Station']
    freq_combo = df['combination'].mode()[0]
    print("The Most Frequent Combination Of Start and End Station Is {} ".format(freq_combo))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_duration = df['Trip Duration'].sum()
    minute,second = divmod(total_duration, 60)
    hour,minute = divmod(minute, 60)
    print("The Total Trip Duration Is {} Hour(s) {} Minute(s) and {} Second(s)".format(hour, minute, second))


    # display mean travel time
    average_duration = round(df['Trip Duration'].mean())
    m,sec = divmod(average_duration, 60)
    if m > 60:
        h,m = divmod(m, 60)
        print("The Total Trip Duration is {} Hour(s) {} Minute(s) {} and Second(s)".format(h,m,sec))
    else:
        print("The Total Trip Duration is {} Minute(s) and {} Second(s)".format(m,sec))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_counts = df['User Type'].value_counts()
    print("The User Types Are:\n", user_counts)


    # Display counts of gender
    if city.title() == 'Chicago' or city.title() == 'New York City':
        gender_counts = df['Gender'].value_counts()
        print("\nThe Counts By Gender Are:\n",gender_counts)


    # Display earliest, most recent, and most common year of birth
        earliest = int(df['Birth Year'].min())
        print("\nThe Oldest Rider Was Born in",earliest)
        most_recent = int(df['Birth Year'].max())
        print("The Youngest Rider Was born in",most_recent)
        common = int(df['Birth Year'].mode()[0])
        print("The Average Rider Was Born in",common)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
