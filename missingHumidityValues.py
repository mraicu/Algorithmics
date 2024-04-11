from sklearn import linear_model
from datetime import datetime

"""
    Predicting the Missing Humidity Values
Given humidity data for the days spanning from startDate to endDate inclusive, 
predict the hourly humidity data for each of the timestamps in timestamps.

    Function Description
Complete the function predictMissingHumidity in the editor below. 
The function must return an array of floating-point numbers where the value at each index i denotes the humidity at timestamps[i].

predictMissingHumidity() has the following parameter(s):
- startDate: string, The first day of humidity data in the format yyyy-mm-dd.
- endDate: string, The last day of humidity data in the format yyyy-mm-dd.
- knownTimestamps[knownTimestamps[0],...k nown Timestamps[m-1]]: an array of strings of timestamps in the format yyyy-mm-dd hh:00.
- humidity[humidity[0],...humidity[m-1]]: an array of floating-point numbers representing humidity[i] occurring at knownTimestamps[i].
- timestamps[timestamps[0],...timestamps[n- 1]]: an array of strings of timestamps to predict for in the format yyyy-mm-dd hh:00.

    Constraints
2013-01-01 ≤ startDate ≤ endDate ≤ 2015-01-01
1 ≤ m ≤ 3476
1 ≤ n ≤ 915
Input Format for Custom Testing
    Evaluation
The predicted humidity at a timestamp is considered to be correct if the absolute difference 
between the actual and predicted humidities is not greater than 0.25.
The accuracy of the prediction is defined as: (Total number of correct predictions)/(n).
The score for each test case is calculated as: accuracy × (test case weight).
The final score is the sum of all test case scores.
"""


def predictMissingHumidity(startDate, endDate, knownTimestamps, humidity, timestamps):
    """
    :param startDate: string, The first day of humidity data in the format yyyy-mm-dd
    :param endDate: string, The last day of humidity data in the format yyyy-mm-dd.
    :param knownTimestamps: an array of strings of timestamps in the format yyyy-mm-dd hh:00.
    :param humidity: an array of floating-point numbers representing humidity[i] occurring at knownTimestamps[i].
    :param timestamps: an array of strings of timestamps to predict for in the format yyyy-mm-dd hh:00
    :return: the predicted value for timestamps
    """
    X = [[k] for k in knownTimestamps]

    regressor = linear_model.LinearRegression()
    regressor.fit(X, humidity)

    predictions = regressor.predict([[p] for p in timestamps])

    return predictions


def string_to_timestamp(date_string):
    # define the format of the input string
    date_format = "%Y-%m-%d %H:%M"

    # convert the string to a datetime object
    datetime_object = datetime.strptime(date_string, date_format)

    # convert the datetime object to a timestamp
    timestamp = datetime.timestamp(datetime_object)

    return timestamp


knownTimestampsString = [
    "2013-01-01 00:00",
    "2013-01-01 01:00",
    "2013-01-01 02:00",
    "2013-01-01 03:00",
    "2013-01-01 04:00",
    "2013-01-01 05:00",
    "2013-01-01 06:00",
    "2013-01-01 08:00",
    "2013-01-01 10:00",
    "2013-01-01 11:00",
    "2013-01-01 12:00",
    "2013-01-01 13:00",
    "2013-01-01 16:00",
    "2013-01-01 17:00",
    "2013-01-01 18:00",
    "2013-01-01 19:00",
    "2013-01-01 20:00",
    "2013-01-01 21:00",
    "2013-01-01 23:00"
]

humidity = [
    0.62,
    0.64,
    0.62,
    0.63,
    0.63,
    0.64,
    0.63,
    0.64,
    0.48,
    0.46,
    0.45,
    0.44,
    0.46,
    0.47,
    0.48,
    0.49,
    0.51,
    0.52,
    0.52
]

timestampsString = [
    "2013-01-01 07:00",
    "2013-01-01 09:00",
    "2013-01-01 14:00",
    "2013-01-01 15:00",
    "2013-01-01 22:00"
]

knownTimestamps = [string_to_timestamp(string) for string in knownTimestampsString]
timestamps = [string_to_timestamp(string) for string in timestampsString]

predictions = predictMissingHumidity("2013-01-01", "2013-01-01", knownTimestamps, humidity, timestamps)

expectedOutput = [0.64,
                  0.55,
                  0.44,
                  0.44,
                  0.52]

# calculate error
err = sum(abs(predictions - expectedOutput)) / len(expectedOutput)

print("Error:", err)
