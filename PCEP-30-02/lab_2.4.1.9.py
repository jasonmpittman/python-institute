__author__ = "Jason M. Pittman"
__copyright__ = "Copyright 2024"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"

"""
Expected output:
7.38 miles is 11.88 kilometers
12.25 kilometers is 7.61 miles

"""

if __name__ == '__main__':
    kilometers = 12.25
    miles = 7.38

    miles_to_kilometers = miles * 1.61
    kilometers_to_miles = kilometers / 1.61

    print(miles, "miles is", round(miles_to_kilometers, 2), "kilometers")
    print(kilometers, "kilometers is", round(kilometers_to_miles, 2), "miles")