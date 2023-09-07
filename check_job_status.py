# Run: python check_job_status.py
import json
# read the json file
dict = json.loads(open('job_status.json').read())
# print the status


if dict['status'] != 'Completed':
    print('Job is not completed')
    raise Exception('Job is not completed')
else:
    print('Job is completed')