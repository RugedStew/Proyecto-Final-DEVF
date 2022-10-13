from flask_sqlalchemy import  SQLAlchemy

db = SQLAlchemy()

class confirmed(db.Model):
    rowid = db.Column(db.Integer, primary_key=True)
    Date = db.Column(db.Date)
    France = db.Column(db.Integer)
    Canada = db.Column(db.Integer)
    Mexico = db.Column(db.Integer)
    Germany = db.Column(db.Integer)
    Brazil = db.Column(db.Integer)

    def __str__(self):
        return '''\nDate: {}. 
        \nFrance: {}. 
        \nCanada: {}. 
        \nMexico: {}
        \nGermany: {}
        \nBrazil: {}
        '''.format(
            self.Date,
            self.France,
            self.Canada,
            self.Mexico,
            self.Germany,
            self.Brazil
        )

    def serialize(self):
        return {
            "rowid":self.rowid,
            "Date":self.Date,
            "France":self.France,
            "Canada":self.Canada,
            "Mexico":self.Mexico,
            "Germany":self.Germany,
            "Brazil":self.Brazil
        }    

class recovered(db.Model):
    __bind_key__ = 'recovered'
    rowid = db.Column(db.Integer, primary_key=True)
    Date = db.Column(db.Date)
    France = db.Column(db.Integer)
    Canada = db.Column(db.Integer)
    Mexico = db.Column(db.Integer)
    Germany = db.Column(db.Integer)
    Brazil = db.Column(db.Integer)

    def __str__(self):
        return '''\nDate: {}. 
        \nFrance: {}. 
        \nCanada: {}. 
        \nMexico: {}
        \nGermany: {}
        \nBrazil: {}
        '''.format(
            self.Date,
            self.France,
            self.Canada,
            self.Mexico,
            self.Germany,
            self.Brazil
        )

    def serialize(self):
        return {
            "rowid":self.rowid,
            "Date":self.Date,
            "France":self.France,
            "Canada":self.Canada,
            "Mexico":self.Mexico,
            "Germany":self.Germany,
            "Brazil":self.Brazil
        }          

class deaths(db.Model):
    __bind_key__ = 'deaths'
    rowid = db.Column(db.Integer, primary_key=True)
    Date = db.Column(db.Date)
    France = db.Column(db.Integer)
    Canada = db.Column(db.Integer)
    Mexico = db.Column(db.Integer)
    Germany = db.Column(db.Integer)
    Brazil = db.Column(db.Integer)

    def __str__(self):
        return '''\nDate: {}. 
        \nFrance: {}. 
        \nCanada: {}. 
        \nMexico: {}
        \nGermany: {}
        \nBrazil: {}
        '''.format(
            self.Date,
            self.France,
            self.Canada,
            self.Mexico,
            self.Germany,
            self.Brazil
        )

    def serialize(self):
        return {
            "rowid":self.rowid,
            "Date":self.Date,
            "France":self.France,
            "Canada":self.Canada,
            "Mexico":self.Mexico,
            "Germany":self.Germany,
            "Brazil":self.Brazil
        }          