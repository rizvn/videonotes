NotesController = {
  mUser : 'Riz',
  mDate : "01/01/2012",

  mNoteSequence : -1,
  mNotesTemplate : null,

  $mEditNote : null,


  mDom : {
    notesInput     : "#notesInput",
    notesContainer : "#notes",
    addNoteButton  : "#addNoteButton",

    commentsDialog : "#commentsDialog",

    editNoteDialog   : "#editNoteDialog",
    saveNoteChanges  : "#saveNoteChanges",
    deleteNoteButton : "#deleteNoteButton",
    timeCodeSlider   : "#timeCodeSlider",

    emptyNotesMessage : '.emptyNotes',

    $notesInput       : "#notesInput",
    $notesContainer   : "#notes",
    $addNoteButton    : "#addNoteButton",
    $cancelNoteButton : "#cancelNoteButton",
    $commentsDialog   : "#commentsDialog",
    $editNoteDialog   : "#editNoteDialog",
    $saveNoteChanges  : "#saveNoteChanges",
    $deleteNoteButton : "#deleteNoteButton",
    $timeCodeSlider   : "#timeCodeSlider",
    $emptyNotesMessage: '.emptyNotes',
  },

  onAddNote : function() {
      var self = this;
	  var model = this.genNewNoteModel();
      model.vidId = Storage.vidId;


      $.ajax({
    	  data: model,
    	  dataType: "json",
    	  type: 'POST',
    	  url: "/note"
      })
      .done(function(aRes){
    	  if(aRes.ack == "success"){
	    	  self.addNote(aRes);
	    	  $(self.mDom.notesInput).val("");
	    	  VideoController.play();
    	  }
      });
  },

  onDeleteNote : function() {
	  var noteId = this.$mEditNote.attr("data-noteId");
	  var self = this;

	  $.ajax({
		 url: "/note/" + noteId + "/delete",
		 type: 'GET',
	     dataType: 'json'
	  })
	  .done(function(aRes){
		if(aRes.ack =='deleted')
	    {
		  self.$mEditNote.remove();
		  self.closeEditNoteDialog();
	    }
	  });
  },

  addNote : function(aModel) {
      this.mDom.$emptyNotesMessage.hide();
      var renderedNote = $(this.mNotesTemplate(aModel));
      this.mDom.$notesContainer.append(renderedNote);
  },

  saveNoteChanges : function() {
	  var self = this;
      var html = $("#notesArea", this.mDom.$editNoteDialog).val();
      var noteId = this.$mEditNote.attr('data-noteId');
      $.ajax({
    	  url: '/note/' + noteId + "/update",
    	  type: 'POST',
    	  data: {body: html},
    	  dataType: 'json'
      })
      .done(function(aRes){
    	 if(aRes.ack=='success'){
    	   self.$mEditNote.replaceWith( $(self.mNotesTemplate(aRes)));
    	   self.closeEditNoteDialog();
    	 }
      });
  },


  seekVideo : function(aUi) {
      var pos = $(aUi).closest(".note").attr("data-timecode");
      VideoController.seek(pos);
  },

  genNewNoteModel : function() {
      var thisClass = this;
      var position = VideoController.getPosition();
      var model = {
        "timeCode" : position,
        "body"     : $(this.mDom.notesInput).val(),
        "vidId"    : Storage.vidId
      };
      return model;
  },

  genNoteModel: function($aNoteEl){
      return {
        pos:      $aNoteEl.attr("data-timecode"),
        timecode: $(".timeCodeLink", $aNoteEl).text(),
        noteId:   $aNoteEl.attr("data-noteId"),
        text:     $(".noteText", $aNoteEl).html(),
        user:     $aNoteEl.attr("data-user"),
        date:     $aNoteEl.attr("data-date")
      }
  },

  showComments : function() {
      $(this.mDom.commentsDialog).dialog("open");
  },

  showEditNoteDialog : function($aNoteDiv) {
      var dialog = this.mDom.$editNoteDialog;
      var model = this.genNoteModel($aNoteDiv);

      $("#notesArea", dialog).val(model.text);
      $("#editNoteId", dialog).val(model.noteId);

      this.$mEditNote = $aNoteDiv;

      dialog.dialog("open");
  },

  closeEditNoteDialog : function() {
      this.mDom.$editNoteDialog.dialog("close");
  },

  init : function() {
      this.resolve();
      this.register();
      this.listen();
      this.effects();
  },


  //wire events to methods
  listen : function() {
      var thisClass = this;

      $(this.mDom.addNoteButton).click(function() {
        thisClass.onAddNote();
      });

      $(this.mDom.saveNoteChanges).click(function() {
        thisClass.saveNoteChanges();
      });

      $(thisClass.mDom.notesContainer).on("click", ".commentLink", function() {
        thisClass.showComments();
      });

      $(thisClass.mDom.notesContainer).on("click", ".editLink", function() {
        var noteDiv = $(this).closest('.note');
        thisClass.showEditNoteDialog(noteDiv);
      });

      $(thisClass.mDom.notesContainer).on("click", ".timecodeLink", function() {
        thisClass.seekVideo(this);

      });

      $(this.mDom.deleteNoteButton).click(function() {
        thisClass.onDeleteNote();
      });
  },

  //register or init dependencies
  register : function() {
      var thisClass = this;
      // Register dialogs
      $(this.mDom.commentsDialog).dialog({
          dialogClass : "vnDialog",
          autoOpen : false,
      });

      $(this.mDom.editNoteDialog).dialog({
          dialogClass : "vnDialog",
          autoOpen : false,
      });

      this.mNotesTemplate = Handlebars.compile($("#vn_noteTemplate").html());
  },

  //resolve dom elements with selectors and cache
  resolve : function(){
      this.mDom.$notesContainer     = $(this.mDom.$notesContainer );
      this.mDom.$emptyNotesMessage  = $(this.mDom.$emptyNotesMessage );
      this.mDom.$editNoteDialog     = $(this.mDom.$editNoteDialog );
      this.mDom.$notesInput         = $(this.mDom.$notesInput );
  },

  //ui effects that are not necessary for core functionality
  effects: function(){
      this.mDom.$notesInput.click(function(){
        VideoController.pause();
      });

  },

}