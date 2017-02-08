/**
 * http://usejsdoc.org/
 */
/*var page = require('webpage').create();
page.open('http://www.afl.com.au/stats/player-ratings/overall-standings#club/CD_T10', function(status) {
  console.log("Status: " + status);
  if(status === "success") {
    page.render('example.png');
  }
  phantom.exit();
});*/

var page = new WebPage()
var fs = require('fs');
var string = ''
page.onLoadFinished = function() {
  console.log("page load finished");
  page.render('export'.concat(htmlNames[i].concat('.png')));
  string = htmlNames[i].concat('.html')
  console.log("here")
  fs.write(string, page.content, 'w');
  console.log("further")
  phantom.exit();
};
var websites = ['http://www.afl.com.au/stats/player-ratings/overall-standings#club/CD_T10','http://www.afl.com.au/stats/player-ratings/overall-standings#club/CD_T10/page/2','http://www.afl.com.au/stats/player-ratings/overall-standings#club/CD_T20','http://www.afl.com.au/stats/player-ratings/overall-standings#club/CD_T20/page/2','http://www.afl.com.au/stats/player-ratings/overall-standings#club/CD_T30','http://www.afl.com.au/stats/player-ratings/overall-standings#club/CD_T30/page/2','http://www.afl.com.au/stats/player-ratings/overall-standings#club/CD_T40','http://www.afl.com.au/stats/player-ratings/overall-standings#club/CD_T40/page/2','http://www.afl.com.au/stats/player-ratings/overall-standings#club/CD_T50','http://www.afl.com.au/stats/player-ratings/overall-standings#club/CD_T50/page/2','http://www.afl.com.au/stats/player-ratings/overall-standings#club/CD_T60','http://www.afl.com.au/stats/player-ratings/overall-standings#club/CD_T60/page/2','http://www.afl.com.au/stats/player-ratings/overall-standings#club/CD_T1010','http://www.afl.com.au/stats/player-ratings/overall-standings#club/CD_T1010/page/2','http://www.afl.com.au/stats/player-ratings/overall-standings#club/CD_T70','http://www.afl.com.au/stats/player-ratings/overall-standings#club/CD_T70/page/2','http://www.afl.com.au/stats/player-ratings/overall-standings#club/CD_T1000','http://www.afl.com.au/stats/player-ratings/overall-standings#club/CD_T1000/page/2','http://www.afl.com.au/stats/player-ratings/overall-standings#club/CD_T80','http://www.afl.com.au/stats/player-ratings/overall-standings#club/CD_T80/page/2','http://www.afl.com.au/stats/player-ratings/overall-standings#club/CD_T90','http://www.afl.com.au/stats/player-ratings/overall-standings#club/CD_T90/page/2','http://www.afl.com.au/stats/player-ratings/overall-standings#club/CD_T100','http://www.afl.com.au/stats/player-ratings/overall-standings#club/CD_T100/page/2','http://www.afl.com.au/stats/player-ratings/overall-standings#club/CD_T110','http://www.afl.com.au/stats/player-ratings/overall-standings#club/CD_T110/page/2','http://www.afl.com.au/stats/player-ratings/overall-standings#club/CD_T120','http://www.afl.com.au/stats/player-ratings/overall-standings#club/CD_T120/page/2','http://www.afl.com.au/stats/player-ratings/overall-standings#club/CD_T130','http://www.afl.com.au/stats/player-ratings/overall-standings#club/CD_T130/page/2','http://www.afl.com.au/stats/player-ratings/overall-standings#club/CD_T160','http://www.afl.com.au/stats/player-ratings/overall-standings#club/CD_T160/page/2','http://www.afl.com.au/stats/player-ratings/overall-standings#club/CD_T150','http://www.afl.com.au/stats/player-ratings/overall-standings#club/CD_T150/page/2','http://www.afl.com.au/stats/player-ratings/overall-standings#club/CD_T140','http://www.afl.com.au/stats/player-ratings/overall-standings#club/CD_T140/page/2']
var htmlNames = ['Adelaide1','Adelaide2','Brisbane1','Brisbane2','Carlton1','Carlton2','Collingwood1','Collingwood2','Essendon1','Essendon2','Fremantle1','Fremantle2','Geelong1','Geelong2','GoldCoast1','GoldCoast2','GWS1','GWS2','Hawthorn1','Hawthorn2','Melbourne1','Melbourne2','NorthMelbourne1','NorthMelbourne2','PortAdelaide1','PortAdelaide2','Richmond1','Richmond2','StKilda1','StKilda2','SydneySwans1','SydneySwans2','WestCoast1','WestCoast2','WesternBulldogs1','WesternBulldogs2']
//console.log(htmlNames.length);

for (i = 0; i < htmlNames.length; i++)
	{
		//console.log(websites[i]);
		page.open(websites[i], function() {
			page.evaluate(function() {
			});
			});
	}
//phantom.exit();

/*    var page = new WebPage()
var fs = require('fs');

page.onLoadFinished = function() {
  console.log("page load finished");
  page.render('export.png');
  fs.write('1.html', page.content, 'w');
  phantom.exit();
};

page.open("http://www.google.com", function() {
  page.evaluate(function() {
  });
});*/