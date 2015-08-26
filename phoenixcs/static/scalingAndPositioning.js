function moveStripe(){
	var iW = window.innerWidth; //innerWidth
	
	$("#longWayDown").css("top", "0px");
	$("#longWayDown").css("left", Math.round( (iW - stripeWidth)/2 ) + 'px');
}

function repositionImageByIdCoef ( id, coef ){//затрагивает отступы слева и сверху, для равномерного масштабирования
	imgTop = Number(String($("#" + id).css("top")).replace("px",""));
	imgLeft = Number(String($("#" + id).css("left")).replace("px",""));
	
	$("#" + id).css("top", (Math.round(imgTop * coef)).toString() + "px");
	$("#" + id).css("left", (Math.round(imgLeft * coef)).toString() + "px");
}

function resizeImageByIdCoef( id, coef){
	imgW = $("#" + id).width();
	imgH = $("#" + id).height();
	
	imgDesiredWidth = imgW * coef;
	
	$("#" + id).css("width", Math.round(imgDesiredWidth) + "px");
	$("#" + id).css("height", imgDesiredWidth * imgH / imgW + "px");
}

function resizeImageByIdDesiredWidth( id, imgDesiredWidth){
	imgW = $("#" + id).width();
	imgH = $("#" + id).height();
	
	$("#" + id).css("width", Math.round(imgDesiredWidth) + "px");
	$("#" + id).css("height", imgDesiredWidth * imgH / imgW + "px");
}

function simpleScaleTextBlock ( id, coef ){//уменьшить размер блока и шрифт в нём
	txtSize = Number(String($("#" + id).css("font-size")).replace("px",""));
	$("#" + id).css("font-size", (Math.round(txtSize * coef)).toString() + "px");
	
	$("#" + id).width( $("#" + id).width() * coef );
	$("#" + id).height( $("#" + id).height() * coef );
}

function repositionTextBlockGivenXY ( id, x, y, coef){//
	simpleScaleTextBlock ( id, coef );
	
	//вернуть центр на место
	objW = $("#" + id).width();
	objH = $("#" + id).height();
	
	$("#" + id).css("top", (y - objH/2).toString() + "px");
	$("#" + id).css("left", (x - objW/2).toString() + "px");
}