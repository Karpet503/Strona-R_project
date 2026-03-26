import psutil
import os

# Sekcja CPU 
cpu_usage_per_core = psutil.cpu_percent(interval=1, percpu=True)
for i, usage in enumerate(cpu_usage_per_core):
    print(f"Rdzeń {i}: {usage}%")

print(f"Liczba fizycznych rdzeni Procesora: {psutil.cpu_count(logical=False)}")

# Użycie CPU (bez błędu)
print(f"Użycie CPU: {psutil.cpu_percent(interval=1)}%")

# Sekcja RAM
mem = psutil.virtual_memory()
print(f"Całkowita pamięć RAM: {mem.total / (1024**3):.2f} GB")
print(f"Dostępna pamięć RAM: {mem.available / (1024**3):.2f} GB")
print(f"Użycie RAM: {mem.percent}%")

# Sekcja Disk
disk = psutil.disk_usage('/')
print(f"Użycie dysku: {disk.percent}%")

