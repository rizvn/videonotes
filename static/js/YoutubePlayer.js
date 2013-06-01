ytPlayer = {
  mPlayer : "videoPlayer",

  play : function() {
    this.mPlayer.playVideo();
  },

  pause : function() {
    this.mPlayer.pauseVideo();
  },

  playPause : function() {
    
  },

  seek : function(aSecs) {
    this.mPlayer.seekTo(aSecs, true);
  },

  getPosition : function() {
      return this.mPlayer.getCurrentTime();
  },

  init : function(aVideoId){
    var params = { allowScriptAccess: "always" };
    var atts = { id: "videoPlayer"};
    swfobject.embedSWF("http://www.youtube.com/v/"+ aVideoId +"?enablejsapi=1&playerapiid=ytplayer&version=3&autoplay=1",
                       this.mPlayer, "420", "320", "8", null, null, params, atts);
  }
}


VideoController = ytPlayer;

function onYouTubePlayerReady(playerId) {
    VideoController.mPlayer = document.getElementById('videoPlayer');
}



