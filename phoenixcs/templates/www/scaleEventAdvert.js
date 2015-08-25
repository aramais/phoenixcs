function scaleEventAdvert( id, coef ){//id "advert1"
	resizeImageByIdCoef(id + "ProjectorScreen", coef);
	resizeImageByIdCoef(id + "LectorPhoto", coef);
	
	repositionImageByIdCoef(id + "Photo", coef);
	resizeImageByIdCoef(id + "Photo", coef);
	
	repositionImageByIdCoef(id + "WhiteBg", coef);
	resizeImageByIdCoef(id + "WhiteBg", coef);
	
	repositionImageByIdCoef(id + "Info", coef);
	
	simpleScaleTextBlock(id + "Date", coef);
	simpleScaleTextBlock(id + "EventType", coef);
	simpleScaleTextBlock(id + "EventName", coef);
	simpleScaleTextBlock(id + "LectorName", coef);
	
	resizeImageByIdCoef(id + "LocationMark", coef);
	simpleScaleTextBlock(id + "Location", coef);
	
	simpleScaleTextBlock(id + "registrationToEvent", coef);
}

function orderAdverts(){
	gap = 70*scalingCoefficient;
	shiftFromTop = 280*scalingCoefficient;
	
	dX = (stripeWidth - 3*gap) / 5;
	
	for(i=1; i<=4; i++){
		id = "advert" + i;
		
		scaleEventAdvert(id, 0.8 * scalingCoefficient);
		
		
		shiftFromLeft = 0.5*dX + dX*i + gap*(i-1) - 0.5*dX - $("#" + id + "ProjectorScreen").width()/2;
		
		
		$("#" + id).css("left", shiftFromLeft.toString() + "px");
		$("#" + id).css("top", shiftFromTop.toString() + "px");
	}
}