import json

import numpy as np
import pandas as pd

backup_json = open('json/anonymized-backup.json', 'rb')
backup_data = json.load(backup_json)

courses = []
reviews = []
users = []

for course_id, course in backup_data['courses'].items():
    average = course['average']
    courses.append({
        'id': course_id,
        'difficulty': average['difficulty'],
        'rating': average['rating'],
        'workload': average['workload']
    })

for review_key, review in backup_data['reviews'].items():
    reviews.append(review)

df_courses = pd.DataFrame(courses)
df_reviews = pd.DataFrame(reviews)

# print(df_courses.head())
# print(df_reviews.tail())

df_courses.to_pickle("pickle/courses.pickle")
df_reviews.to_pickle("pickle/reviews.pickle")
