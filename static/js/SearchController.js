SearchController = {
  mDom : {
    mSearchField : "#searchField",
    mSearchButton : "#searchButton",
    mClearSearchButton : "#clearSearchButton"
  },

  doSearch : function() {
      var thisClass = this;
      $("#notes .note").each(function() {
        var noteText = $(this).text().toLowerCase();
        var searchCrit = $(thisClass.mDom.mSearchField).val().toLowerCase();
        if (noteText.indexOf(searchCrit) < 0) {
          $(this).addClass("hidden");
        }
      });

      //show clear button
      $("#clearSearchButton").css("display", "inline");
  },

  undoSearch : function() {
      $("#notes .hidden").each(function() {
        $(this).removeClass("hidden");
      });

      $("#clearSearchButton").css("display", "none");
  },

  init : function() {
      this.connectDom();
  },

  connectDom : function() {
      var thisClass = this;
      $(this.mDom.mSearchButton).click(function() {
        thisClass.doSearch();
      });

      $(this.mDom.mClearSearchButton).click(function() {
        thisClass.undoSearch();
      })
  },

  disconnectDom : function() {

  }

}