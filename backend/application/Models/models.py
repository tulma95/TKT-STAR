from sqlalchemy.orm import relationship

from .. import db

class Recommendation(db.Model):
   __tablename__ = 'recommendation'
   id = db.Column(db.Integer, primary_key=True)
   book = relationship("Book", uselist=False, backref="recommendation")
   video = relationship("Video", uselist=False, backref="recommendation")

class Book(db.Model):
   __tablename__ = 'book'
   id = db.Column(db.Integer, primary_key=True)
   recommendation_id = db.Column(db.Integer, db.ForeignKey('recommendation.id'))
   title = db.Column(db.String(250), nullable=False)
   author = db.Column(db.String(250), nullable=False)
   isbn = db.Column(db.String(250), nullable=True)
   isRead = db.Column(db.Boolean, nullable =True)


   @property
   def serialize(self):
      return {
         'id': self.id,
         'title':self.title,
         'author':self.author,
         'isbn':self.isbn,
         'id':self.id,
         'isRead': False if self.isRead == 0 else True,
      }


class Video(db.Model):
   __tablename__ = 'video'
   id = db.Column(db.Integer, primary_key=True)
   recommendation_id = db.Column(db.Integer, db.ForeignKey('recommendation.id'))
   url = db.Column(db.String(250), nullable=False)
   title = db.Column(db.String(250), nullable=False)

   @property
   def serialize(self):
      return {
         'id': self.id,
         'url': self.url,
         'title': self.title,
      }

class Tag(db.Model):
   __tablename__ = 'tag'
   id = db.Column(db.Integer, primary_key=True)
   name = db.Column(db.String(250), nullable=False)

   @property
   def serialize(self):
      return {
         'id': self.url,
         'title': self.name
      }

class TagRecommendation(db.Model):
   __tablename__ = 'tagrecommendation'
   id = db.Column(db.Integer, primary_key=True)
   user_id = db.Column(db.Integer, db.ForeignKey('tag.id'), nullable=False)
   team_id = db.Column(db.Integer, db.ForeignKey('recommendation.id'), nullable=False)

   @property
   def serialize(self):
      return {
         'id': self.url,
         'user_id': self.user_id,
         'team_id': self.team_id
      }