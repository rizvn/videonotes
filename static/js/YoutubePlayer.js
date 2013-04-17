ytPlayer = {
  mPlayer : "videoPlayer",

  mConfig : {
      flashplayer : '/static/js/lib/jwplayer/player.swf',
      width : '100%',
      height : '100%',
      autoplay : 'true',
      skin : '/static/js/lib/jwplayer/skins/glow/glow.xml',
      file : '/static/testVideos/paradox_of_choice.mp4'
  },

  play : function() {
      jwplayer(this.mPlayer).play(true);
  },

  pause : function() {
      jwplayer(this.mPlayer).pause(true);
  },

  playPause : function() {
      jwplayer(this.mPlayer).play();
  },

  seek : function(aSecs) {
      jwplayer(this.mPlayer).seek(aSecs);
  },

  getPosition : function() {
      return parseInt(jwplayer(this.mPlayer).getPosition(), 10);
  },

  init : function(aVideoId) {
    var params = { allowScriptAccess: "always" };
    var atts = { id: "videoPlayer" };
    swfobject.embedSWF("http://www.youtube.com/v/"+ aVideoId +"?enablejsapi=1&playerapiid=ytplayer&version=3",
                       this.mPlayer, "425", "356", "8", null, null, params, atts);
  }
}


VideoController = ytPlayer;


