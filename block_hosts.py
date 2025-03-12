import time
from datetime import datetime

# Вывод текущего времени
now = datetime.now()
print(f'Текущее время: {now.strftime("%H:%M:%S")}')

# Время блокировки
start_time = datetime(now.year, now.month, now.day, 15)# Начало блокировки 
finish_time = datetime(now.year, now.month, now.day, 16)# Конец блокировки 

print(f'Сайты будут заблокированы с {start_time.strftime("%H:%M")} до {finish_time.strftime("%H:%M")}')

# Файл hosts
hosts = r'C:\Windows\System32\drivers\etc\hosts'
# hosts = '/etc/hosts'  # Для Linux/macOS
redirect_url = '127.0.0.1'
blocked_sites = ['www.youtube.com', 'youtube.com', 'www.vk.com', 'vk.com', 'www.nambafood.kg', 'nambafood.kg']

try:
    while True:
        now = datetime.now()

        if start_time <= now <= finish_time:
            print('🔴 Доступ ограничен!')

            with open(hosts, 'r+') as file:
                src = file.readlines()
                file.seek(0)

                for site in blocked_sites:
                    if not any(site in line for line in src):
                        file.write(f'{redirect_url} {site}\n')

                file.writelines(src)
                file.truncate()
        else:
            print('🟢 Доступ открыт!')
            with open(hosts, 'r+') as file:
                src = file.readlines()
                file.seek(0)

                for line in src:
                    if not any(site in line for site in blocked_sites):
                        file.write(line)
                
                file.truncate()

        time.sleep(5)

except KeyboardInterrupt:
    print('\nСкрипт остановлен!')
