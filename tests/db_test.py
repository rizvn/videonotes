import app.db as db

def test_verify_getAllVideos():
    result = db.getAllVideos()
    assert result
    
def test_getNotesForVideo():
    result = db.getNotesForVideo(1)
    assert True
    
def test_getVideoByPk():
    result = db.getVideo(1)
    assert result

def test_verify_getUserByName():
    result = db.getUserByName('riz')
    assert result

def test_verify_authquery():
    result = db.authUser('riz', 'password')
    assert result
    
def test_insert_note():
    db.addNote(1, 130, 'Test note', 'Riz')
    assert True

def test_verify_delete_note():
    db.deleteNote(2)
    assert True

def test_updateNote():
    db.updateNote(20, 'hello', 'world')
    assert True
