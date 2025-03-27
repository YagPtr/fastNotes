def logEvent(e):
    # Запись в файл
    with open("log.data", "a", encoding="utf-8") as file:
        file.write(str(e)+"\n")



 