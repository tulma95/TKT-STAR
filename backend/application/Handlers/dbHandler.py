from ..Models.models import Book, Video, Recommendation, Tag, TagRecommendation
from flask import Flask, jsonify, Response

from application import app
from application import init_db, returnDB




class DBHandler():
    def get_books(self, app):
        with app.app_context():
            books = Book.query.all()

            return jsonify([book.serialize for book in books])

    def get_videos(self, app):
        with app.app_context():
            videos = Video.query.all()
            return jsonify([video.serialize for video in videos])

    def post_video(self, db, json):
        url = json.get('url')
        title = json.get('title')

        rec = Recommendation()
        video = Video(url=url, title=title, recommendation=rec)

        db.session.add(rec)
        db.session.add(video)
        db.session.commit()

        db.session.refresh(rec)

        if json.get('tags'):
            for tag in json.get('tags'):
                self.add_tag(self, rec, db, tag)

        return jsonify(video.serialize)

    def post_book(self, db, json):
        title = json.get('title')
        author = json.get('author')
        isbn = json.get('isbn')
        isRead = 0

        rec = Recommendation()
        book = Book(title=title, author=author, isbn=isbn,
                    isRead=isRead, recommendation=rec)

        db.session.add(rec)
        db.session.add(book)
        db.session.commit()

        db.session.refresh(rec)

        if json.get('tags'):
            for tag in json.get('tags'):
                self.add_tag(self, rec, db, tag)

        return jsonify(book.serialize)

    def update_book(self, db, book_id):
        book = db.session.query(Book).filter(Book.id == book_id).first()

        if book.isRead == False:
            book.isRead = True
        elif book.isRead == True:
            book.isRead = False

        db.session.commit()
        book = Book.query.get(book_id)

        return jsonify(book.serialize)

    def get_book(self, db, book_id):
        book = db.session.query(Book).filter(Book.id == book_id).first()
        if book == None:
            return Response("", status=404)

        return jsonify(book.serialize)

    def get_video(self, db, video_id):
        video = db.session.query(Video).filter(Video.id == video_id).first()
        if video == None:
            return Response("", status=404)

        return jsonify(video.serialize)

    def add_tag(self, rec, db, tag):
        tagObject = Tag(name=tag)
        db.session.add(tagObject)
        db.session.commit()

        db.session.refresh(tagObject)

        tagRec = TagRecommendation(
            tag_id=tagObject.id, recommendation_id=rec.id)
        db.session.add(tagRec)
        db.session.commit()

    def reset_database(self):
        db2 = returnDB()
        db2.drop_all()
        db2.create_all()
        db2.session.commit()
