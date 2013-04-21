NotesController = {
  //elements cache see resolve
  el : {},
  //resolve dom elements with selectors and cache
  resolve : function(){
    this.el.notesInput       = $("#notesInput");
    this.el.notesContainer   = $("#notes");
    this.el.addNoteButton    = $("#addNoteButton");
    this.el.cancelNoteButton = $("#cancelNoteButton");
    this.el.saveNoteChanges  = $("#saveNoteChanges");
    this.el.deleteNoteButton = $("#deleteNoteButton");

    this.el.editNotesDialog =
      $("#editNoteDialog").dialog({
        dialogClass : "vnDialog",
        autoOpen : false
      });

    this.el.notesTemplate = Handlebars.compile(" \
      <div class='note' data-id='{{id}}' data-time='{{time}}'>      \
        <div class='ctxMenu'>                                       \
          <a class='editLink'>Edit</a>                              \
          <a class='delLink'>Delete</a>                             \
        </div>                                                      \
        <p class='timeLink anchor'>{{time}}</p>                     \
        <p class='text'>{{text}}</p>                                \
        <p class='desc'>                                            \
            by {{user}}                                                  \
        </p>                                                        \
      </div>                                                        \
      ");
  },

  //element selectors
  sel : {
    emptyNotesMessage: '.emptyNotes'
  },

  addNote : function() {
    var self = this;
    var model = {};
    model.vid_id = Data.vidId;
    model.user = Data.user;
    model.time = VideoController.getPosition();
    model.text = self.el.notesInput.val();

    $.ajax({
      data: model,
      type: 'POST',
      url: "/note"
    })
    .done(function(res){
      if(res.ack == 1){
        var new_note = self.el.notesTemplate({
                        id: res.id,
                        time: model.time,
                        user : Data.user,
                        text: model.text})
        self.el.notesContainer.append(new_note);
        self.el.notesInput.val("");
	$('.emptyNotes', self.el.notesContainer).hide();
        VideoController.play();
      }
      else{
        alert('Failed to add note');
      }
    });
  },

  deleteNote : function(link) {
    var self = this;
    var note_el = $(link).closest('.note');
    var note_id = note_el.attr('data-id');

    if(confirm('Delete note?')){
      $.ajax({
        url: "/note/" + note_id + "/delete",
        type: 'GET',
        dataType: 'json'
      })
      .done(function(res){
        if(res.ack == 1){
          $(note_el).remove();
	  if ($('.note', self.el.notesContainer).length==1) {
	    $('.emptyNotes', self.el.notesContainer).show();
	  }
        }
      });
    }
  },

  editNote : function(editLink) {
    var noteEl = $(editLink).closest('.note');
    this.el.currentNote = noteEl;
    var dlg = this.el.editNotesDialog;
    var text = $(".text", noteEl).html();
    $("#notesArea", dlg).val(text);
    dlg.dialog("open");
  },

  updateNote : function() {
    var self = this;
    var html = $("#notesArea", this.el.editNoteDialog).val();
    var note = this.el.currentNote;

    var model = {};
    model.vid_id = Data.vidId;
    model.user = Data.user;
    model.id = note.attr('data-id');
    model.time = note.attr('data-time');
    model.text = $("#notesArea", this.el.editNotesDialog).val();

    $.ajax({
      url: '/note/' + model.id + "/update",
      type: 'POST',
      data: model,
      dataType: 'json'
    })
    .done(function(res){
      if(res.ack == 1){
        var new_note = self.el.notesTemplate({
                        id: model.id,
                        time: model.time,
                        user: Data.user,
                        text: model.text})
        note.replaceWith(new_note);
        self.el.editNotesDialog.dialog('close')
      }
    });
  },

  seekVideo : function(aUi) {
    var pos = $(aUi).closest(".note").attr("data-time");
    VideoController.seek(pos);
  },

  init : function() {
    this.resolve();
    this.register();
    this.listen();
    this.effects();
  },


  //wire events to methods
  listen : function() {
    var self = this;

    self.el.addNoteButton.click(function() {
      self.addNote();
    });

    self.el.saveNoteChanges.click(function() {
      self.updateNote();
    });

    self.el.notesContainer.on("click", ".editLink", function() {
      self.editNote(this);
    });

    self.el.notesContainer.on("click", ".timeLink", function() {
      self.seekVideo(this);
    });

    self.el.notesContainer.on("click", ".delLink", function() {
        self.deleteNote(this);
    });

    $('#cancelNoteButton').click(function(){
      self.el.notesInput.val('');
      VideoController.play();
    });

  },

  //register or init dependencies
  register : function() {
    var self = this;
    // Register dialogs


    this.mNotesTemplate = Handlebars.compile($("#vn_noteTemplate").html());
  },



  //ui effects that are not necessary for core functionality
  effects: function(){
    this.el.notesInput.click(function(){
      VideoController.pause();
    });

  }

}