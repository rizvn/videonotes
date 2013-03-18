Utility = {
  timecodeFormat : function(aSecs) {
      var int = parseInt(aSecs);
      var seconds = this.doubleDigitPad(parseInt(aSecs % 60));
      var minutes = this.doubleDigitPad(parseInt(aSecs / 60));
      return minutes + ":" + seconds;
  },

  doubleDigitPad : function(aDigit) {
      if (aDigit < 10) {
        return "0" + aDigit;
      } else {
        return "" + aDigit;
      }
  },

  init : function() {
      return this;
  },

  registerPrototypes : function() {

  }
}.init();