# Run: python check_job_status.py

# import the required libraries
import json
import os
import argparse
import time


#new logic


parser = argparse.ArgumentParser()
parser.add_argument("--name",dest='name', type=str)
args = parser.parse_args()
job_id = args.name
print('job id is', job_id)

while True:    
    value=os.popen(f'az ml job show -n {job_id} \
                    -w learnML -g myResourcegroupforML').read()
    status=json.loads(value)['status']
    if status == 'Running':
        print('Job is running')
        time.sleep(60)
    elif status == 'Failed':
        print('Job is failed')
        break
    elif status == 'Completed':
        print('Job is completed')
        break

# old logic
"""# read the json file
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
        break"""
