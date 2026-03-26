import psutil
import os
import json

# Sekcja CPU 
# cpu_usage_per_core = psutil.cpu_percent(interval=1, percpu=True)
# for i, usage in enumerate(cpu_usage_per_core):
#    print(f"Rdzeń {i}: {usage}%")

cpu_cores = psutil.cpu_count(logical=False)

# Użycie CPU (bez błędu)
cpu_usage = psutil.cpu_percent(interval=1)

# Sekcja RAM
mem = psutil.virtual_memory()
memory_total = mem.total / (1024**3)
memory_total = round(memory_total, 2)
memory_avaible = mem.available / (1024**3)
memory_avaible = round(memory_avaible, 2)
memory_usage = mem.percent

# Sekcja Disk
disk = psutil.disk_usage('/')
disk_usage = disk.percent

#testowy wydruk danych
print(memory_total)

# Zapis danych do pliku 'data.py'
with open('data.py', 'w') as file:
    file.write(f"memory_total = {memory_total}\n")
    file.write(f"memory_available = {memory_avaible}\n")
    file.write(f"memory_usage = {memory_usage}\n")
    file.write(f"cpu_usage = {cpu_usage}\n")


print("Dane zostały zapisane do pliku data.py.")