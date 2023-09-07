# Run: python check_job_status.py
import json
# read the json file
dict = json.loads(open('job_status.json').read())
# print the status


if dict['status'] == 'Running':
    print('Job is running')
if dict['status'] == 'Completed':
    print('Job is completed')
    
while dict['status'] == 'Running':
    if dict['status'] == 'Running':
        print('Job is running')
    elif dict['status'] == 'Failed':
        print('Job is failed')
        break
    elif dict['status'] == 'Completed':
        print('Job is completed')
        break
