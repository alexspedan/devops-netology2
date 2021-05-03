#!/usr/bin/env python3

import os

#a = input("enter DIR: ")
git_directory = '/home/alexsp/devops-netology'
path = os.path.abspath(os.curdir)
bash_command = ['cd ' + git_directory, "git status -s"]
result_os = os.popen(' && '.join(bash_command)).read()
is_change = False

for result in result_os.split('\n'):
    if result.find('??') !=-1:
        prepare_result_untraceable = result.replace('??', 'Untraceable:' +git_directory+ '/')
        print( prepare_result_untraceable)
    elif result.find('A') !=-1:
        prepare_result_added = result.replace('A', 'Added:')
        print(prepare_result_added)
    elif result.find('M') !=-1:
        prepare_result_modified = result.replace('M', 'Modified:')
        print(prepare_result_modified)


