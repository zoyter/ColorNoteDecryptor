# ColorNote Decryptor

## Назначение

Это приложение предназначено для просмотра файлов резеврных копий (\*.doc), которые генерируются программой **ColorNote** для Android.

## Использование

После запуска приложения необходимо просто перетащить файл ColorNote в окно программы.

## Использованные ресурсы

- Проект [decode-ColorNote](https://github.com/fcoiffie/decode-ColorNote) для дешифровки записей ColorNote
- Изображение [post-it.png]( https://www.flaticon.com/free-icon/post-it_889648?term=note&page=1&position=4&page=1&position=4&related_id=889648&origin=search) в качестве иконки приложения


## Сборка приложения

Для сборки автономного приложения требуется установить модуль **pyinstaller** и выполнить команду:  

```cmd
pyinstaller --onefile --noconsole main.py
```


