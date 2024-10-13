import pandas as pd
from app import create_app
from models import db, Guest, Episode, Appearance

app = create_app()

def seed_data():
    with app.app_context():
        # Load the CSV file
        data = pd.read_csv('data/appearances.csv')

        for _, row in data.iterrows():
            # Create or get guest
            guest = Guest.query.filter_by(name=row['Raw_Guest_List'], occupation=row['GoogleKnowlege_Occupation']).first()
            if not guest:
                guest = Guest(name=row['Raw_Guest_List'], occupation=row['GoogleKnowlege_Occupation'])
                db.session.add(guest)

            # Create episode
            episode = Episode(date=row['Show'])
            db.session.add(episode)

            # Create appearance
            appearance = Appearance(rating=row['YEAR'], episode=episode, guest=guest)
            db.session.add(appearance)

        db.session.commit()

if __name__ == '__main__':
    seed_data()
