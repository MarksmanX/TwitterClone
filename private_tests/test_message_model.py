"""Message model tests."""

# run these tests like:
#
#    python -m unittest test_message_model.py


from app import app
import os
from unittest import TestCase
from sqlalchemy import exc

from models import db, User, Message, Follows, Likes

# BEFORE we import our app, let's set an environmental variable
# to use a different database for tests (we need to do this
# before we import our app, since that will have already
# connected to the database

os.environ['DATABASE_URL'] = "postgresql:///warbler-test"


# Now we can import app


# Create our tables (we do this here, so we only create the tables
# once for all tests --- in each test, we'll delete the data
# and create fresh new clean test data

class MessageModelTestCase(TestCase):
    """Test views for messages."""

    def setUp(self):
        """Create test client, add sample data."""
        self.client = app.test_client()

        # Establish an application context
        self.app_context = app.app_context()
        self.app_context.push()

        # Initialize the database within the application context
        db.drop_all()
        db.create_all()

        self.uid = 94566
        u = User.signup("testing", "testing@test.com", "password", None)
        u.id = self.uid
        db.session.commit()

        self.u = User.query.get(self.uid)

    def tearDown(self):
        """Tear down test client and application context."""
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_message_model(self):
        """Does basic model work?"""
        m = Message(
            text="a warble",
            user_id=self.uid
        )

        db.session.add(m)
        db.session.commit()

        # User should have 1 message
        self.assertEqual(len(self.u.messages), 1)
        self.assertEqual(self.u.messages[0].text, "a warble")

    def test_message_likes(self):
        """Can a user like a message?"""
        m1 = Message(
            text="a warble",
            user_id=self.uid
        )

        m2 = Message(
            text="a very interesting warble",
            user_id=self.uid
        )

        u = User.signup("yetanothertest", "t@email.com", "password", None)
        uid = 888
        u.id = uid
        db.session.add_all([m1, m2, u])
        db.session.commit()

        u.likes.append(m1)
        db.session.commit()

        l = Likes.query.filter(Likes.user_id == uid).all()
        self.assertEqual(len(l), 1)
        self.assertEqual(l[0].message_id, m1.id)
        