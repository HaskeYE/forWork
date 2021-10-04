# This is first task of couple given to me
# It writes all needed values to .txt file and they are easy to read there
# Some useful imports down there
import psutil
import subprocess
import time
import os

# As was said in task - gaining values from the command line with some instructions
file = input("write FULL way to file:\n")
interval = input("Time interval of checkings:\n")

# Creating or using existing file to write down our results
if os.path.exists("FileForFirst.txt"):
    txt = open("FileForFirst.txt", "a")
else:
    txt = open("FileForFirst.txt", "w+")

txt.write("\n!!!Начало новой сессии записи статистики!!!\n\n")

# Process creation and its PID receiving
proc = subprocess.Popen(file)
p = psutil.Process(proc.pid)
# Iterator starting for 0 because first measurement isn't accurate
i = 0
# try block preventing exceptions when we are closing our process manually
try:
    while p.status() == psutil.STATUS_RUNNING:
        # Вывод здесь был сделан немного вольно, так как точно не сказано как именно должна быть
        # представлена информация, так что сделал  удобной для человеческого глаза
        txt.write("Измерение № " + str(i) + "\nЗагрузка CPU: " + str(p.cpu_percent()) + "%" +
                  "\nПотребление памяти: Working Set: " + str(p.memory_info()[4]) + " байт  " + "Private Bytes: " +
                  str(p.memory_info()[11]) + "байт" + "\nКоличество открытых хендлов: " + str(p.num_handles()) + "\n")
        # Здесь использованы 4 и 11 значения массива memory_info, т.к. они отвечают за нужные нам величины

        # The best and easiest solution I think - no need for schedulers or other things -
        # because python will only block itself - not our process
        i += 1
        time.sleep(float(interval))
except:
    print("Приложение было закрыто")
finally:
    # Closing our text file - in other way info would be lost
    txt.close()
# C:\Games\BsgLauncher\BsgLauncher.exe
