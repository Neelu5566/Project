$("#like-button").click(function() {
    var currentCount = parseInt($("#like-count").text());
    $("#like-count").text(currentCount + 1);
  });
  $("#dislike-button").click(function() {
    var currentCount = parseInt($("#dislike-count").text());
    $("#dislike-count").text(currentCount + 1);
  });
  $("#like-button").on("click", function(){
    $.get("/increment_likes/", function(data){
      $("#like-count").html(data.likes);
    });
  });
  
  $("#dislike-button").on("click", function(){
    $.get("/increment_dislikes/", function(data){
      $("#dislike-count").html(data.dislikes);
    });
  });
   