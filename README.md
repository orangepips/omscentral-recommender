# omscentral-recommender

## Methods

https://www.kaggle.com/gspmoreira/recommender-systems-in-python-101


## Data Format

[print_json_structure.py] reads [data/anonymized-backup.json] and prints the following to standard out

    <root>: <class 'dict'> (5 of 5 keys shown)
        alerts: <class 'dict'> (1 of 1 keys shown)
            -L3fWRFKuNaYi9VolwNq: <class 'dict'> (5 of 5 keys shown)
                active: 1 <class 'int'>
                created: 1516853642278 <class 'int'>
                slack: 1 <class 'int'>
                text: We're collecting new data... go edit your reviews :) <class 'str'>
                type: info <class 'str'>
        courses: <class 'dict'> (2 of 51 keys shown)
            CS-6035: <class 'dict'> (2 of 2 keys shown)
                average: <class 'dict'> (3 of 3 keys shown)
                    difficulty: 2.375 <class 'float'>
                    rating: 3.8941176470588235 <class 'float'>
                    workload: 8.557692307692308 <class 'float'>
                reviews: <class 'dict'> (2 of 104 keys shown)
                    -K2Q2yCgljbQ2jEFLXh_: True <class 'bool'>
                    -K2Q2yCgljbQ2jEFLXha: True <class 'bool'>
            CS-6200: <class 'dict'> (2 of 2 keys shown)
                average: <class 'dict'> (3 of 3 keys shown)
                    difficulty: 3.6 <class 'float'>
                    rating: 4.493333333333333 <class 'float'>
                    workload: 18.516129032258064 <class 'float'>
                reviews: <class 'dict'> (2 of 125 keys shown)
                    -K2Q2yE7gwOH6xtwfUSZ: True <class 'bool'>
                    -K2Q2yE7gwOH6xtwfUS_: True <class 'bool'>
        reviews: <class 'dict'> (2 of 2048 keys shown)
            -K2Q2yAnCsH4KiqDwVy4: <class 'dict'> (8 of 8 keys shown)
                author: c36c1a3f-6655-4f31-b0a4-971fdc87fbe6 <class 'str'>
                course: CS-6505 <class 'str'>
                created: 2015-11-05T06:00:00+00:00 <class 'str'>
                difficulty: 5 <class 'int'>
                semester: 2014-3 <class 'str'>
                text: I dropped it this semester so I can take it by itself. This one ... (truncated at 64 characters) <class 'str'>
                updated: 2015-11-05T06:00:00+00:00 <class 'str'>
                workload: 15 <class 'int'>
            -K2Q2yB0CRMfIqurAR3d: <class 'dict'> (8 of 8 keys shown)
                author: c36c1a3f-6655-4f31-b0a4-971fdc87fbe6 <class 'str'>
                course: CS-6505 <class 'str'>
                created: 2015-11-05T06:00:00+00:00 <class 'str'>
                difficulty: 5 <class 'int'>
                semester: 2014-3 <class 'str'>
                text: Very theoretical course. Programming assingments in Python. 'Opt... (truncated at 64 characters) <class 'str'>
                updated: 2015-11-05T06:00:00+00:00 <class 'str'>
                workload: 15 <class 'int'>
        settings: <class 'dict'> (2 of 2 keys shown)
            cacheLength: 0 <class 'int'>
            maintenance: 0 <class 'int'>
        users: <class 'dict'> (2 of 2049 keys shown)
            009c63e6-7f63-4bcb-9797-77b28f20b8d8: <class 'dict'> (9 of 9 keys shown)
                anonymous: False <class 'bool'>
                authProvider: password <class 'str'>
                created: 2016-06-23T16:22:10+00:00 <class 'str'>
                email: 009c63e6-7f63-4bcb-9797-77b28f20b8d8 <class 'str'>
                name: 009c63e6-7f63-4bcb-9797-77b28f20b8d8 <class 'str'>
                profileImageUrl: 009c63e6-7f63-4bcb-9797-77b28f20b8d8 <class 'str'>
                reviews: <class 'dict'> (2 of 3 keys shown)
                    -KKy6tWKut0ux36UpCR3: True <class 'bool'>
                    -KimZ0zx2FnCdhufVYCL: True <class 'bool'>
                specialization: 3 <class 'int'>
                updated: 2017-04-01T23:47:45Z <class 'str'>
            00be4fc3-c639-4f23-a47d-24a89bce6abb: <class 'dict'> (7 of 7 keys shown)
                anonymous: False <class 'bool'>
                authProvider: password <class 'str'>
                created: 2015-11-18T20:17:15+00:00 <class 'str'>
                email: 00be4fc3-c639-4f23-a47d-24a89bce6abb <class 'str'>
                name: 00be4fc3-c639-4f23-a47d-24a89bce6abb <class 'str'>
                profileImageUrl: 00be4fc3-c639-4f23-a47d-24a89bce6abb <class 'str'>
                specialization: 3 <class 'int'>