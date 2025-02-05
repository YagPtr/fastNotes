# Planero4ka

планировщик задач

## создать окружение

```bash
python -m venv venv
```

активировать окружение

```bash
source venv/Scripts/activate
```

Установить окружение из файла requirements.txt

```bash
pip instal -r requirements.txt
```

### скачать библиотеки

```bash
pip download -r requirements.txt
```

### установить на ПК без интернета

```bash

pip install --no-index --find-links O:\\0308\\СЕКТОР\ 30\\ПапкаДляОбщения\\библиотеки  -r requirements-Fast_api.txt

pip install --no-index --find-links /path/to/download/dir/  -r requirements.txt
```

pip install - это команда для установки пакетов с помощью менеджера пакетов pip.

--no-index - этот флаг указывает pip не использовать стандартный индекс пакетов (PyPI), а вместо этого искать пакеты в указанном месте.

--find-links /path/to/download/dir/ - этот флаг указывает pip, где искать пакеты. В данном случае, это локальный каталог, где хранятся скачанные пакеты.

-r requirements.txt - этот флаг указывает pip, что список пакетов для установки находится в файле requirements.txt. Этот файл обычно содержит список зависимостей проекта.

```bash
pip install pack.whe
```

### необходимые библиотеки

PyMuPDF: для считывания файла PDF по пути репозитория.

```bash
pip install pandas numpy matplotlib openpyxl
```

## Конвертировать ui в py

```bash
python -m PyQt5.uic.pyuic -x Okno_proverki.ui -o Okno_proverki.py
```

## Создать исполняемый файл

```bash
pyinstaller -w --onefile -i "./provero4ka.ico" --name "Provero4ka" backend/main.py
```

### Опции

-w, --windowed, --noconsole
Windows и Mac OS X: не предоставляют окно консоли для стандартного ввода-вывода.

-n NAME, --name NAME
Имя, которое нужно присвоить входящему в комплект приложению и файлу спецификации (по умолчанию: базовое имя первого скрипта)

-F, --onefile
Создайте исполняемый файл, состоящий из одного файла.

-i <ФАЙЛ.ico или FILE.exe,ИДЕНТИФИКАТОР или FILE.icns или Изображение или "НЕТ">, --icon <ФАЙЛ.ico или FILE.exe, ИДЕНТИФИКАТОР или ФАЙЛ.icns или изображение или "НЕТ">

FILE.ico: примените значок к исполняемому файлу Windows.
FILE.exe,ID: извлеките значок с идентификатором из exe.
FILE.icns: примените значок к пакету .app в Mac OS.
При вводе файла изображения, который не соответствует формату платформы (ico в Windows, icns на Mac), PyInstaller пытается использовать Pillow для перевода значка в правильный формат (если Pillow установлен). Используйте “NONE”, чтобы не применять какой-либо значок, тем самым заставляя ОС отображать какой-либо значок по умолчанию (по умолчанию: применить значок PyInstaller). Этот параметр можно использовать несколько раз.

## Планы на празвитие проекта

- проверять ост в ТТ
