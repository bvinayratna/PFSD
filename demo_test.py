'''create a collection of news articles having the keys as id, title, date, description and type
apply operations to search based on id, category or title'''

#articles = dict()
articles = dict()

articles = [{"id": 123, "title": "title_name1", "date": "01/01/2022", "description": "Book1", "type": "hard cover"},
            {"id": 124, "title": "title_name2", "date": "02/01/2022", "description": "Book2", "type": "paper back"},
            {"id": 125, "title": "title_name3", "date": "03/01/2022", "description": "Book3", "type": "hard cover"},
            {"id": 126, "title": "title_name4", "date": "04/01/2022", "description": "Book4", "type": "hard cover"},
            {"id": 127, "title": "title_name5", "date": "05/01/2022", "description": "Book5", "type": "paper back"}]

for na in articles:
    if na.get('id') == 123:
        print(na.get("type"))
        print(na["date"])
        print(na["title"])

#print(articles)