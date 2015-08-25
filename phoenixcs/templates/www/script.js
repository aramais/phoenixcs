var referenceScreenWidth = 1920; //вся вёрстка была под эту ширину экрана

var scalingCoefficient;

var stripeWidth;
var stripeCenter;

var iH = window.innerHeight; //innerHeight

// ------------ правила поведения страницы -----------
window.onload = function () {
	figureElementsSizes();
	fixAllElements();
}

window.onresize = function() {
	moveStripe();
}
// -------------------------------------------------

function figureElementsSizes(){
	//var sW = screen.availWidth; //innerWidth
	var sW = 1920;
	scalingCoefficient = sW / referenceScreenWidth;
	stripeWidth = Math.round(sW * 0.68);
	stripeCenter = stripeWidth/2;
	
	$("#longWayDown").css("width", stripeWidth + 'px');
	$("#longWayDown").css("height", "6000px");
	
	//--------- Экран 1 -----------
	resizeImageByIdDesiredWidth("screen1bg", stripeWidth);
	resizeImageByIdCoef("logo", scalingCoefficient);
	//-----------------------------
	
	//--------- Экран 2 -----------
	resizeImageByIdDesiredWidth("screen2bg", stripeWidth);
	//-----------------------------
	
	//--------- Экран 3 -----------
	resizeImageByIdDesiredWidth("screen3bg", stripeWidth);
	//scaleSummary();
	scaleSummary();
	//-----------------------------
}

function fixAllElements(){
	moveStripe();
	//---------------- Экран 1 ----------------
	repositionTextBlockGivenXY("dayCounter", stripeCenter, 520*scalingCoefficient, scalingCoefficient);
	repositionTextBlockGivenXY("signUpForTest", stripeCenter, 620*scalingCoefficient, scalingCoefficient);
	
	repositionImageByIdCoef("logo", scalingCoefficient);
	//-----------------------------------------
	
	//---------------- Экран 2 ----------------
	repositionImageByIdCoef("screen2", scalingCoefficient);
	
	repositionTextBlockGivenXY("drawAttetionToEvents", stripeCenter, (150) * scalingCoefficient, scalingCoefficient);
	
	orderAdverts();
	//-----------------------------------------
	
	//---------------- Экран 3 ----------------
	repositionImageByIdCoef("screen3", scalingCoefficient);
	
	repositionTextBlockGivenXY("PhoenixCaseSchoolExplained", stripeCenter, (120) * scalingCoefficient, scalingCoefficient);
	//-----------------------------------------
	
}