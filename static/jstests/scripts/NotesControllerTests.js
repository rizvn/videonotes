function runNotesControllerTests(){
    module("Notes Controller Tests");

    test("Initialisation", function(){
        NotesController.init();
        ok(true);
    });


    test("Test NoteController GenNoteModel", function(){
      var note = $('\
          <div class="note" type="t" noteId="123" pos="456" user="riz" date="01/01/1989">\
            <div class="ctxMenu">\
              <a class="editLink">Edit/Delete</a>\
              <a class="commentLink">Comments</a>\
            </div>\
            <p class="timecodeLink anchor">11.33</p>\
            <p class="noteText">Note 1</p>\
            <p class="desc">\
              by riz on  01/01/2012\
            </p>\
          </div>\
          </div>');


      var noteModel = NotesController.genNoteModel(note);

      deepEqual( noteModel,
                 {
                  "date": "01/01/1989",
                  "noteId": "123",
                  "pos": "456",
                  "text": "Note 1",
                  "timecode": "11.33",
                  "type": "t",
                  "user": "riz"
                 },
                "should be the same" );
      ok(true);
    });


}