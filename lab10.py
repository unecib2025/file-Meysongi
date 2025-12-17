#1
with open("users.txt", "r", encoding="utf-8") as f:
    for line in f:
        print(line.strip())


#2
with open("passwords.txt", "r", encoding="utf-8") as fin, \
     open("weak.txt", "w", encoding="utf-8") as fout:
    for pwd in fin:
        pwd = pwd.strip()
        if len(pwd) < 8:
            fout.write(pwd + "\n")


#3
with open("ips.txt", "r", encoding="utf-8") as fin:
    unique_ips = set(line.strip() for line in fin if line.strip())

with open("unique_ips.txt", "w", encoding="utf-8") as fout:
    for ip in unique_ips:
        fout.write(ip + "\n")


#4
with open("log.txt", "r", encoding="utf-8") as f:
    count = sum(1 for _ in f)

print(count)


#5
with open("ports.txt", "r", encoding="utf-8") as fin, \
     open("blocked_ports.txt", "w", encoding="utf-8") as fout:
    for line in fin:
        port = int(line.strip())
        if port < 1024:
            fout.write(str(port) + "\n")


#6
with open("auth.log", "r", encoding="utf-8") as fin, \
     open("failed.txt", "w", encoding="utf-8") as fout:
    for line in fin:
        user, status = line.strip().split()
        if status != "success":
            fout.write(line)


#7
with open("traffic.txt", "r", encoding="utf-8") as fin, \
     open("alert.txt", "w", encoding="utf-8") as fout:
    for line in fin:
        value = int(line.strip())
        if value > 1000:
            fout.write(str(value) + "\n")


#8
with open("commands.txt", "r", encoding="utf-8") as fin, \
     open("safe.txt", "w", encoding="utf-8") as fout:
    for cmd in fin:
        if "rm" not in cmd:
            fout.write(cmd)


#9
with open("users.txt", "r", encoding="utf-8") as f:
    users = f.readlines()

with open("report.txt", "w", encoding="utf-8") as fout:
    fout.write(f"Всего пользователей: {len(users)}")


#10
with open("full_log.txt", "w", encoding="utf-8") as fout:
    for name in ["log1.txt", "log2.txt"]:
        with open(name, "r", encoding="utf-8") as fin:
            fout.write(fin.read())


""" Контрольные вопросы — ответы
1. open() — открывает файл для чтения или записи и возвращает файловый объект.
2. 'r' — чтение, 'w' — запись с перезаписью, 'a' — добавление в конец.
3. В режиме 'w' файл очищается или создаётся заново.
4. read() читает весь файл одной строкой, readlines() — список строк.
5. with автоматически закрывает файл, даже если возникла ошибка.
6. Использовать режим 'a' (append).
7. Анализ логов, проверка пользователей, выявление атак, аудит доступа, отчёты безопасности.
"""