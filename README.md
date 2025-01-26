# qa_python
#Описание тест кейсов
      #Кейс, который уже был написан для примера:
Описание: в указанном кейсе была ошибка, исправила assert len(collector.get_books_genre()) == 2. Кейс написан для метода add_new_book метода, а в assert в прекоде был get_book_rating(), что неправильно
     #Кейс1 для метода add_new_book:
test_add_new_book_duplicate – добавление дубликата
     #Кейс 2 дляя метода add_new_book:
test_add_new_book_exceed_max_length – проверка на добавление книги с названием более 40 символов
     #Кейс 3 для метода set_book_genre:
test_set_book_genre – проверка, что жанр для книги устанавливается
    #Кейс 4 для метода get_book_genre:
test_get_book_genre_nonexistent – проверка, что установка жанра для несуществующей книги не изменяет словарь. Сделала is None, т.к показалось, что это правильнее, более строгая проверка так сказать.
     #Кейс 5 для метода get_books_with_specific_genre:
test_get_books_with_specific_genre – проверка получения книг по жанру
     #Кейс 6 для метода get_books_genre:
test_get_books_genre_returns_dict – проверка, что возвращается действительно словарь. Если это не так, тест выдаст ошибку с сообщением о том, какой тип был получен. 
     #Кейс 7 для метода get_books_for_children:
test_get_books_for_children – проверка, получения книг, которые подходят детям
      #Кейс 8 для метода add_book_in_favorites:
test_add_book_in_favorites – проверка добавления книги в избранное
      #Кейс 9 для метода test_delete_book_from_favorites:
test_delete_book_from_favorites – проверка удаления книги из избранного
      #Кейс 10 для метода get_list_of_favorites_books:
test_get_list_of_favorites_books_empty – проверка, что список избранного пуст, если ничего не добавлено
      #Кейс 11 (параметизированный) для метода set_book_genre:
test_set_book_genre_for_existing_book – проверка установки жанра для существующих книг

