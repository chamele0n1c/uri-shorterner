 // JavaScript Document

 $(document).ready(function() {
     var wherenav = $("#ngh");
     var div1 = $("<div id='nav'></div>");
     var navel1 = $('<div id="custom-bootstrap-menu" class="navbar navbar-default " role="navigation"><div class="container-fluid"><div class="navbar-header"><a class="navbar-brand" href="#"><img src="/smf.png" width="30" height="30" /></a><button type="button" class="navbar-toggle" data-toggle="collapse" data-target=".navbar-menubuilder"><span class="sr-only">Toggle navigation</span><span class="icon-bar"></span><span class="icon-bar"></span><span class="icon-bar"></span></button></div><div class="collapse navbar-collapse navbar-menubuilder"><ul class="nav navbar-nav navbar-left"><li><a href="https://smfree.cf/"><h4>Short Me Free</h4></a></li></ul></div></div></div>')
     div1.append(navel1);
     wherenav.append(div1);
     head = $("head");
     headdata ="</script><link href='https://fonts.googleapis.com/css?family=Poiret+One' rel='stylesheet' type='text/css'><link rel='stylesheet' href='https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap.min.css' integrity='sha384-1q8mTJOASx8j1Au+a5WDVnPi2lkFfwwEAa8hDDdjZlpLegxhjVME1fgjWPGmkzs7' crossorigin='anonymous'><link rel='stylesheet' href='https://smfree.cf/css/main.css' />"
     head.append(headdata);
     var green = $(".green > p");
     var blue = $(".blue > p");
     var red = $(".red > p");
     var yellow = $(".yellow > p");
     $("h4").tooltip({title: "<h3>Drag me to your Bookmarks!</h3>", placement: "bottom", html: true});
     $("h1 a").tooltip({title: "<h3>Drag me to your Bookmarks!</h3>", placement: "bottom", html: true}); 
     green.wrap("<h4></h4>");
     blue.wrap("<h4></h4>");
     red.wrap("<h4></h4>");
     yellow.wrap("<h4></h4>");
     wherenav.after("<br /><br /><br />");
 });

function ResMe() {
}

var doit;
window.onresize = function(){
  clearTimeout(doit);
  doit = setTimeout(ResMe, 100);
};
