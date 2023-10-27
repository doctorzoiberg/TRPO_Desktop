# TRPO_Desktop

## Сборка

Для сборки приложения необходимо установить Pyinstaller:
```bash
pip/pip3 install pyinstaller
```

Сборка одним файлом:
```bash
pyinstaller --onefile app/main.py
```
Исполняемый файл будет располагаться в папке ./dist

## Запуск тестов

Запуск тестов осуществляется с помощью Docker. Для первого запуска тестирования нужно использовать команду:
```bash
docker-compose up
```
Для последующих запусков:
```bash
docker-compose build --no-cache
docker-compose up
```
