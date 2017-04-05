from datetime import timedelta, date
import itertools
import csv


def daterange(start_date, end_date):
    for n in range(int ((end_date - start_date).days)):
        yield start_date + timedelta(n)


with open('teachers.csv', encoding = "ISO-8859-1") as f:
  reader = csv.reader(f)
  teachers = list(reader)

# Define Teachers for testing
# teachers = list(range(1, 30))

# Define Teacher Iterator
teacher_iterator = itertools.cycle(teachers)

# Define Date Range
start_date = date(2017, 4, 5)
end_date = date(2017, 4, 10)
print('date range: ' + str(start_date) + ' -> ' + str(end_date))

# Define slots per day
daily_slots = 3

# Define teachers per slot
teachers_per_slot = 4

# Calculate teachers per day
daily_teachers = daily_slots * teachers_per_slot

schedule_dictionary = {}

# Print daily schedule
for single_date in daterange(start_date, end_date):
	teacher_list = []
	
	# Iterate over teachers
	for teacher in itertools.islice(teacher_iterator, 0, daily_teachers):
		teacher_list.append(teacher)

	# Add entry to schedule dictionay
	schedule_dictionary[single_date] = teacher_list