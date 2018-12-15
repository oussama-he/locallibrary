import csv
from random import randint, randrange


# with open('/home/oussama/dev-place/django_projects/locallibrary/catalog/BX-Books.csv') as books:
#     books_data = csv.DictReader(books, delimiter=';')
#
#     for i, book in enumerate(books_data):
#         """
#         names = book['Book-Author'].split(" ", 1)
#         print(f'author = Author(first_name="{names[0]}", last_name="{names[-1]}")')
#         print("author.save()")
#         """
#
#         """
#         authors_id = [12, 5, 11, 3, 10, 8, 4, 1, 6, 13, 2, 7, 9]
#         words = ['Building', 'mr', 'concerns', 'servants', 'in', 'he', 'outlived', 'am', 'breeding.', 'He', 'so', 'lain', 'good', 'miss', 'when', 'sell', 'some', 'at', 'if.', 'Told', 'hand', 'so', 'an', 'rich', 'gave', 'next.', 'How', 'doubt', 'yet', 'again', 'see', 'son', 'smart.', 'While', 'mirth', 'large', 'of', 'on', 'front.', 'Ye', 'he', 'greater', 'related', 'adapted', 'proceed', 'entered', 'an.', 'Through', 'it', 'examine', 'express', 'promise', 'no.', 'Past', 'add', 'size', 'game', 'cold', 'girl', 'off', 'how', 'old.']
#         title = book['Book-Title']
#         author = authors_id[i]
#         isbn = book['ISBN']
#         genre = randint(1, 5)
#         summary = " ".join(words[randint(1, len(words)-1)] for word in words) + '.'
#         # print(i)
#         print(f'book = Book(title="{title}", summary="{summary}", author=Author.objects.get(id={i}), isbn="{isbn}")')
#         print('book.save()')
#         if i > 10:
#             break
#         """

for x in range(55):
    loan_status = ['o', 'm', 'a', 'r']
    status = loan_status[randint(1, len(loan_status)-1)]
    book_id = randint(1, 12)
    print(f'book_instance = BookInstance(book=Book.objects.get(id={book_id}), status="{status}")')
    print('book_instance.save()')

"""
languages = ['English', 'Spanish', 'Portuguese', 'German']
for lang in languages:
    print(f'language = Language(name="{lang}")')
    print("language.save()")
"""

"""
genres = ['Science fiction', 'Action and Adventure', 'Horror', 'Health', 'Travel']
for genre in genres:
    print(f'genre = Genre(name="{genre}")')
    print('genre.save()')
"""


"""
OrderedDict([('ISBN', '0195153448'),
('Book-Title', 'Classical Mythology'),
('Book-Author', 'Mark P. O. Morford'), 
('Year-Of-Publication', '2002'), 
('Publisher', 'Oxford University Press'), ('Image-URL-S', 'http://images.amazon.com/images/P/0195153448.01.THUMBZZZ.jpg'), ('Image-URL-M', 'http://images.amazon.com/images/P/0195153448.01.MZZZZZZZ.jpg'), ('Image-URL-L', 'http://images.amazon.com/images/P/0195153448.01.LZZZZZZZ.jpg')])

"""

from datetime import datetime, timedelta, timezone

step = timedelta(days=1)
start = datetime(2017, 11, 15, tzinfo=timezone.utc)
end = datetime.utcnow()
for i in range(10):
    random_date = start + randrange((end - start) // step + 1) * step
    print(random_date)