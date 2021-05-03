#!/usr/bin/env python3

import os

git_directory = input("enter DIR: hint: /home/alexsp/devops-netology/")

check_file = os.path.exists(git_directory +'.git')
print(check_file)
bash_command = ['cd ' + git_directory, "git status -s"]
result_os = os.popen(' && '.join(bash_command)).read()
is_change = False

while check_file == True:

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
    break

else:
    print('The directory is not valid GIT directory')
