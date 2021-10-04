# Второе задание
# Условия останова программы в задании не было - поэтому не реализовано
import os
import shutil
import time

try:
    # Ввод всех нужных нам данных с консоли
    # Проверка на существование оригинальной директории и заодно вывод фразы о том, что программа начинает свою работу
    root_src_dir = input("Укажите, пожалуйста, путь к каталогу с которого будет производится копирование: \n")
    root_dst_dir = input("Укажите, пожалуйста, путь к каталогу в который будет произведено копирование: \n")
    if os.path.exists(root_src_dir):
        logfile = input("Укажите, пожалуйста, путь к каталогу логирования: \n")
    else:
        print("Каталога-источника не существует")
        FileNotFoundError

    while True:
        # проверка на существование файла, куда будут записаны наши логи
        if os.path.exists(str(logfile)):
            txt = open(str(logfile), "a")
        else:
            txt = open(str(logfile), "w+")
        print("\nНачинаю\n")
        txt.write("\nНачинаю\n")
        # Вход в дерево просмотра со стороны рут директории - получаем дерево и второй строчкой
        # получаем название первой директории в каталоге-копии путем замещения строки вплоть до первого вхождения,
        # которое как раз и будет названием нужной папки-копии, так как до этого путь будет идентичен
        for src_dir, dirs, files in os.walk(root_src_dir):
            dst_dir = src_dir.replace(root_src_dir, root_dst_dir, 1)
            if not os.path.exists(dst_dir):
                os.makedirs(dst_dir)
                print("Создана директория " + str(dst_dir))
                txt.write("Создана директория " + str(dst_dir) + "\n")

            # Эта часть кода отвечает за создание новых файлов
            # в директории-копии и их обновление. обновляются при каждой "синхронизации"
            for file_ in files:
                src_file = os.path.join(src_dir, file_)
                dst_file = os.path.join(dst_dir, file_)
                if os.path.exists(dst_file):
                    os.remove(dst_file)
                shutil.copy(src_file, dst_dir)
                print("Создан или обновлен файл " + str(src_file))
                txt.write("Создан или обновлен файл " + str(src_file) + "\n")

        # Похожий цикл входа в дерево, но уже со стороны каталога-копии и для удаления папок и файлов
        for dst_dir, dirs, files in os.walk(root_dst_dir):
            src_dir = dst_dir.replace(root_dst_dir, root_src_dir, 1)
            if not os.path.exists(src_dir):
                shutil.rmtree(dst_dir)
                print("Удалена директория" + str(dst_file))
                txt.write("Удалена директория" + str(dst_file) + "\n")

            # Часть кода, отвечающая непосредственно за удаление несуществующих файлов
            for file_ in files:
                src_file = os.path.join(src_dir, file_)
                dst_file = os.path.join(dst_dir, file_)
                if not os.path.exists(src_file):
                    os.remove(dst_file)
                    print("Удален файл " + str(dst_file))
                    txt.write("Удален файл " + str(dst_file) + "\n")
        txt.close()
        time.sleep(20)
except FileNotFoundError:
    print("Неверный путь к файлу")
except ValueError:
    print("Неверный путь к файлу логирования")
finally:
    txt.close()
