# This is first task of couple given to me
# It writes all needed values to FileForFirst.txt file and they are easy to read there
# Some useful imports down there
import psutil
import subprocess
import time
import os

# As was said in task - gaining values from the command line with some instructions
file = input("write FULL way to file:\n")
if os.path.exists(file):
    interval = input("Time interval of checkings:\n")
else:
    FileNotFoundError
# Creating or using existing file to write down our results
if os.path.exists("FileForFirst.txt"):
    txt = open("FileForFirst.txt", "a")
else:
    txt = open("FileForFirst.txt", "w+")

# Iterator starting for 0 because first measurement isn't accurate
i = 0
# try block preventing exceptions when we are closing our process manually and some others
try:
    # Данная строка необходима для того, чтобы сразу по-возможности
    # избежать работы цикла опроса впустую и быстрейшего выскакивания в ошибку
    test = float(interval)

    # Process creation and its PID receiving
    proc = subprocess.Popen(file)
    p = psutil.Process(proc.pid)
    interval = str(interval)

    # Возможно немного странное расположение для данной строки, однако необходимо для того,
    # чтобы программа не вписывала в итоговый файл данную строку без последующих данных при выскакивании в ошибку
    txt.write("\n!!!Начало новой сессии записи статистики!!!\n\n")

    while p.status() == psutil.STATUS_RUNNING:
        # (Здесь начну на русском, так как все, что относится к выводу будет дальше на именно на русском)
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

except FileNotFoundError:
    print("Неверный путь к файлу")
except ValueError:
    print("Неверное значение интервала")
except Exception:
    print("Приложение было закрыто")

finally:
    # Closing our text file - in other way info would be lost
    txt.close()
# C:\Games\BsgLauncher\BsgLauncher.exe
# При неправильном вводе пути программа запросит также ещё временной интервал а потом только вылетит
