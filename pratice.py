import os 
import psutil 
import csv
import json

# going though all the process with set criterias and putting it into process_info
process_info =[]
for proc in psutil.process_iter(['pid', 'name', 'username', 'exe', 'cpu_percent', 'memory_info']):
    process = [proc.info]
    process_info.append(process)

#checking if information is accurate in process_info
# print(process_info)


##print(process_info)
# trying to print all the names
# for process in process_info:
#     print([[process[0]['name']]])

## creating a new csv to import info
with open('process.csv','w',newline='') as f:
    # what we are writing to
    w = csv.writer(f)
    # writing first colomn 
    w.writerow(['pid','Name','Executable path','CPU percent usage','Memory Info (Resident Set Size, Virtual Memory Size, Shared, Text, Library, Data, Dirty)'])
    # adding info based on the colmun and keep adding all prcoess in the list (process_info)
    for process in process_info:
        w.writerow([process[0]['pid'], process[0]['name'], process[0]['exe'], process[0]['cpu_percent'], process[0]['memory_info']])

print('ran successfully')





########################## Junk Code, used for testing purposes ###################################################


# prcoess ID, name, path, CPUs usage, mem usage
# with open ('test.csv', 'w') as csvfile:
#     writer = csv.writer(csvfile)
# for proc in psutil.process_iter(['pid', 'name', 'username', 'cpu_times', 'memory_info', 'cmdline']):
#     print (proc.info)


# for proc in psutil.process_iter(['pid', 'name', 'username', 'cpu_times', 'memory_info', 'cmdline']):
#     response.append(proc.info)

# procsess = psutil.process_iter(['pid', 'name', 'exe', 'cpu_percent', 'memory_info'])
# processes = psutil.process_iter()
# for x in processes:
#     print(processes.name(), processes.pid)

# with open('prcoess.csv','w') as f:
#     f.write('pid', 'name', 'exe', 'cpu_percent', 'memory_info')
#     for prcess in psutil.process_iter(['pid', 'name', 'exe', 'cpu_percent', 'memory_info']):
#         f.write(prcess.info)
# with open ('example.csv', 'w', newline ='') as csvfile:
#     writer = csv.writer(csvfile)

#     writer.writerow(['pid', 'name', 'exe', 'cpu', 'mem'])

