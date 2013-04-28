import app.db_sqlite as db
import unittest

class DbTest(unittest.TestCase):
    def test_verify_getAllVideos(self):
        result = db.getAllVideos()
        assert result

    def test_getNotesForVideo(self):
        result = db.getNotesForVideo(1)
        assert True

    def test_getNotesForVideoByUser(self):
        result = db.getNotes(1, 'riz');
        assert True

    def test_getVideoByPk(self):
        result = db.getVideo(1)
        assert result

    def test_verify_getUserByName(self):
        result = db.getUserByName('riz')
        assert result

    def test_verify_authquery(self):
        result = db.authUser('riz', 'password')
        assert result

    def test_insert_note(self):
        db.addNote(1, 130, 'Test note', 'Riz')
        assert True

    def test_verify_delete_note(self):
        db.deleteNote(2)
        assert True

    def test_updateNote(self):
        db.updateNote(20, 'hello', 'world')
        assert True

    def test_isAuthor(self):
        db.isAuthor(1, 'riz')
        assert True
