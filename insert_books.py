from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["book_recommendation"]

books = {
    "happy": [
        {"title": "The Secret Garden", "genre": "Classic", "image_url": "http://images.amazon.com/images/P/0812505018.01.MZZZZZZZ.jpg"},
        {"title": "Anne of Green Gables", "genre": "Fiction", "image_url": "http://images.amazon.com/images/P/055321313X.01.MZZZZZZZ.jpg"},
        {"title": "The Little Prince", "genre": "Fantasy", "image_url": "http://images.amazon.com/images/P/0156528207.01.MZZZZZZZ.jpg"},
        {"title": "Pride and Prejudice", "genre": "Classic Novel", "image_url": "http://images.amazon.com/images/P/055321215X.01.MZZZZZZZ.jpg"},
        {"title": "Harry Potter and the Sorcerer's Stone", "genre": "Fantasy", "image_url": "http://images.amazon.com/images/P/059035342X.01.MZZZZZZZ.jpg"},
        {"title": "The Hobbit", "genre": "Fantasy", "image_url": "http://images.amazon.com/images/P/0395177111.01.MZZZZZZZ.jpg"},
        {"title": "Little Women", "genre": "Classic", "image_url": "http://images.amazon.com/images/P/0451523415.01.MZZZZZZZ.jpg"},
        {"title": "Charlie and the Chocolate Factory", "genre": "Children's", "image_url": "http://images.amazon.com/images/P/0141301155.01.MZZZZZZZ.jpg"},
        {"title": "Matilda", "genre": "Children's", "image_url": "http://images.amazon.com/images/P/014034294X.01.MZZZZZZZ.jpg"},
        {"title": "Winnie-the-Pooh", "genre": "Children's", "image_url": "http://images.amazon.com/images/P/041619513X.01.MZZZZZZZ.jpg"}
    ],
    "sad": [
        {"title": "The Kite Runner", "genre": "Historical Fiction", "image_url": "http://images.amazon.com/images/P/1573222453.01.MZZZZZZZ.jpg"},
        {"title": "The Nightingale", "genre": "Historical Fiction", "image_url": "http://images.amazon.com/images/P/0747204233.01.MZZZZZZZ.jpg"},
    ],

    "angry": [
        {"title": "1984", "genre": "Dystopian", "image_url": "http://images.amazon.com/images/P/0704339838.01.MZZZZZZZ.jpg"},
        {"title": "Fahrenheit 451", "genre": "Dystopian", "image_url": "http://images.amazon.com/images/P/3257208626.01.MZZZZZZZ.jpg"},
        {"title": "The Catcher in the Rye", "genre": "Classic", "image_url": "http://images.amazon.com/images/P/0316769487.01.MZZZZZZZ.jpg"},
        {"title": "Brave New World", "genre": "Dystopian", "image_url": "http://images.amazon.com/images/P/0060901012.01.MZZZZZZZ.jpg"},
        {"title": "Animal Farm", "genre": "Political Satire", "image_url": "http://images.amazon.com/images/P/0451526341.01.MZZZZZZZ.jpg"},
        {"title": "Lord of the Flies", "genre": "Classic", "image_url": "http://images.amazon.com/images/P/0399501487.01.MZZZZZZZ.jpg"},
        {"title": "A Clockwork Orange", "genre": "Dystopian", "image_url": "http://images.amazon.com/images/P/0393312836.01.MZZZZZZZ.jpg"},
        {"title": "Fight Club", "genre": "Thriller", "image_url": "http://images.amazon.com/images/P/0805062971.01.MZZZZZZZ.jpg"},
        {"title": "The Road", "genre": "Post-Apocalyptic", "image_url": "http://images.amazon.com/images/P/0140185216.01.MZZZZZZZ.jpg"},
        {"title": "We Need to Talk About Kevin", "genre": "Psychological Fiction", "image_url": "http://images.amazon.com/images/P/1582432678.01.MZZZZZZZ.jpg"}
    ],
    "cool": [
        {"title": "To Kill a Mockingbird", "genre": "Classic", "image_url": "http://images.amazon.com/images/P/0446310786.01.MZZZZZZZ.jpg"},
        {"title": "Moby-Dick", "genre": "Adventure", "image_url": "http://images.amazon.com/images/P/0140390847.01.MZZZZZZZ.jpg"},
        {"title": "Life of Pi", "genre": "Adventure", "image_url": "http://images.amazon.com/images/P/0151008116.01.MZZZZZZZ.jpg"},
        {"title": "The Call of the Wild", "genre": "Adventure", "image_url": "http://images.amazon.com/images/P/0451527038.01.MZZZZZZZ.jpg"},
        {"title": "Into the Wild", "genre": "Biography", "image_url": "http://images.amazon.com/images/P/0385486804.01.MZZZZZZZ.jpg"},
        {"title": "The Old Man and the Sea", "genre": "Classic", "image_url": "http://images.amazon.com/images/P/0020519109.01.MZZZZZZZ.jpg"},
        {"title": "The Alchemist", "genre": "Philosophical Fiction", "image_url": "http://images.amazon.com/images/P/0062502174.01.MZZZZZZZ.jpg"},
        {"title": "Siddhartha", "genre": "Philosophical Fiction", "image_url": "http://images.amazon.com/images/P/0553208845.01.MZZZZZZZ.jpg"},
        {"title": "Walden", "genre": "Philosophy", "image_url": "http://images.amazon.com/images/P/055321246X.01.MZZZZZZZ.jpg"},
        {"title": "Zen and the Art of Motorcycle Maintenance", "genre": "Philosophical Fiction", "image_url": "http://images.amazon.com/images/P/0553277472.01.MZZZZZZZ.jpg"}
    ]
}

# Insert books into the database
for emotion, book_list in books.items():
    collection = db[emotion]
    collection.insert_many(book_list)

print("Books for each emotion have been inserted successfully!")