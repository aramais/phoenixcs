var empiricalColumnWidth = Number();

function putOnYLine( id ){
	objW = $("#" + id).width();
	
	$("#" + id).css("left", (empiricalColumnWidth/2 - objW/2).toString() + "px");
}

function scaleAndArrangeSingleColumn( id, coef ){// id = column1	
	resizeImageByIdCoef(id + "Icon", coef);
	
	simpleScaleTextBlock(id + "Title", coef);
	simpleScaleTextBlock(id + "Description", coef);
	
	repositionImageByIdCoef(id + "Illustration", coef);
	repositionImageByIdCoef(id + "Title", coef);
	repositionImageByIdCoef(id + "Description", coef);

	putOnYLine(id + "Illustration" );
	putOnYLine(id + "Title");
	putOnYLine(id + "Description");
}

function scaleSummary(){
	shiftFromTop = 220*scalingCoefficient;
	empiricalColumnWidth = stripeWidth/4;
	
	for(i=1; i<=4; i++){
		id = "column" + i;
		shiftFromLeft = empiricalColumnWidth * (i-1);
		
		$("#" + id).css("top", Number(shiftFromTop).toString() + "px");
		$("#" + id).css("left", Number(shiftFromLeft).toString() + "px");
		
		scaleAndArrangeSingleColumn(id, scalingCoefficient);
	}
}