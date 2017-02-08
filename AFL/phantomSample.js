/**
 * http://usejsdoc.org/
 */
function rendToHTML(PageObj,url,name)
{
//	console.log("execute");
//	console.log('before before')
	
//	console.log('before')
	PageObj.onLoadFinished = function(status) 
	{
	  console.log("page load finished");
	  //page.render('export.png');
	  htmlName = name.concat('.html');
	  console.log(htmlName);
	  fs.write(htmlName, PageObj.content, 'w');
	  console.log(htmlName);
	  PageObj.close();
	  //phantom.exit();
	};
//	console.log('after')
	PageObj.open(url, function() {
	  PageObj.evaluate(function() {
	  });
//	  console.log('after after');
	});

};
var page = [];
/*page.open(address, function (status) {
    if (status !== 'success') {
        console.log('Unable to load the address!');
        phantom.exit();
    } else {
        window.setTimeout(function () {
            page.render(output);
            phantom.exit();
        }, 1000); // Change timeout as required to allow sufficient time 
    }
});*/

var fs = require('fs');
var websites = ['http://www.afl.com.au/stats/player-ratings/overall-standings#club/CD_T10','http://www.afl.com.au/stats/player-ratings/overall-standings#club/CD_T10/page/2','http://www.afl.com.au/stats/player-ratings/overall-standings#club/CD_T20','http://www.afl.com.au/stats/player-ratings/overall-standings#club/CD_T20/page/2','http://www.afl.com.au/stats/player-ratings/overall-standings#club/CD_T30','http://www.afl.com.au/stats/player-ratings/overall-standings#club/CD_T30/page/2','http://www.afl.com.au/stats/player-ratings/overall-standings#club/CD_T40','http://www.afl.com.au/stats/player-ratings/overall-standings#club/CD_T40/page/2','http://www.afl.com.au/stats/player-ratings/overall-standings#club/CD_T50','http://www.afl.com.au/stats/player-ratings/overall-standings#club/CD_T50/page/2','http://www.afl.com.au/stats/player-ratings/overall-standings#club/CD_T60','http://www.afl.com.au/stats/player-ratings/overall-standings#club/CD_T60/page/2','http://www.afl.com.au/stats/player-ratings/overall-standings#club/CD_T1010','http://www.afl.com.au/stats/player-ratings/overall-standings#club/CD_T1010/page/2','http://www.afl.com.au/stats/player-ratings/overall-standings#club/CD_T70','http://www.afl.com.au/stats/player-ratings/overall-standings#club/CD_T70/page/2','http://www.afl.com.au/stats/player-ratings/overall-standings#club/CD_T1000','http://www.afl.com.au/stats/player-ratings/overall-standings#club/CD_T1000/page/2','http://www.afl.com.au/stats/player-ratings/overall-standings#club/CD_T80','http://www.afl.com.au/stats/player-ratings/overall-standings#club/CD_T80/page/2','http://www.afl.com.au/stats/player-ratings/overall-standings#club/CD_T90','http://www.afl.com.au/stats/player-ratings/overall-standings#club/CD_T90/page/2','http://www.afl.com.au/stats/player-ratings/overall-standings#club/CD_T100','http://www.afl.com.au/stats/player-ratings/overall-standings#club/CD_T100/page/2','http://www.afl.com.au/stats/player-ratings/overall-standings#club/CD_T110','http://www.afl.com.au/stats/player-ratings/overall-standings#club/CD_T110/page/2','http://www.afl.com.au/stats/player-ratings/overall-standings#club/CD_T120','http://www.afl.com.au/stats/player-ratings/overall-standings#club/CD_T120/page/2','http://www.afl.com.au/stats/player-ratings/overall-standings#club/CD_T130','http://www.afl.com.au/stats/player-ratings/overall-standings#club/CD_T130/page/2','http://www.afl.com.au/stats/player-ratings/overall-standings#club/CD_T160','http://www.afl.com.au/stats/player-ratings/overall-standings#club/CD_T160/page/2','http://www.afl.com.au/stats/player-ratings/overall-standings#club/CD_T150','http://www.afl.com.au/stats/player-ratings/overall-standings#club/CD_T150/page/2','http://www.afl.com.au/stats/player-ratings/overall-standings#club/CD_T140','http://www.afl.com.au/stats/player-ratings/overall-standings#club/CD_T140/page/2']
var htmlNames = ['Adelaide1','Adelaide2','Brisbane1','Brisbane2','Carlton1','Carlton2','Collingwood1','Collingwood2','Essendon1','Essendon2','Fremantle1','Fremantle2','Geelong1','Geelong2','GoldCoast1','GoldCoast2','GWS1','GWS2','Hawthorn1','Hawthorn2','Melbourne1','Melbourne2','NorthMelbourne1','NorthMelbourne2','PortAdelaide1','PortAdelaide2','Richmond1','Richmond2','StKilda1','StKilda2','SydneySwans1','SydneySwans2','WestCoast1','WestCoast2','WesternBulldogs1','WesternBulldogs2']
//console.log(htmlNames.length);
i= 0;
var int = setInterval(function(){doOperations()},8000);

/*page[0] = new WebPage();
//console.log(websites[i]);
rendToHTML(page[0],websites[0],htmlNames[0]);
*/
function doOperations()
{
	page[i] = new WebPage();
	rendToHTML(page[i],websites[i],htmlNames[i]);
//	page[i] = null;
	i++;
	console.log(i);
	if(i == 15 || i == 30 || i == 36)
		{
			setTimeout(function(){doNothing()},8000);
		}
	if (i>36)
		{
			console.log("done");
			clearInterval(int);
//			setTimeout(function(){doNothing()},30000);
			phantom.exit();
		}
	
}
function doNothing()
{
}
