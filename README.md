# ColorNote Decryptor

## Назначение

Это приложение предназначено для просмотра файлов резеврных копий (\*.doc), которые генерируются программой **ColorNote** для Android.

## Использование

После запуска приложения необходимо просто перетащить файл ColorNote в окно программы.

## Особенности реализации

Для дешифровки записей ColorNote использовались наработки вот этого проекта [decode-ColorNote | https://github.com/fcoiffie/decode-ColorNote] 

Иконка для проекта "post-it.png" взята с этой страницы https://www.flaticon.com/free-icon/post-it_889648?term=note&page=1&position=4&page=1&position=4&related_id=889648&origin=search


**Сборка приложения**

Для сборки автономного приложения требуется установить модуль **pyinstaller** и выполнить команду:  

```cmd
pyinstaller --onefile --noconsole main.py
```


