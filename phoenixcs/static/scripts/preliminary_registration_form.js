// чтобы закрыть форму и растемнить страницу. Надо сделать окошко "всё получилось!"
function close_reg_form() {
	$('#theform_popup').css({'visibility':'hidden'});
	//$('#theform_mask').css({'visibility':'hidden'});
	$('#theform_popup_after').css({'visibility':'visible'});
}
function return_from_registration_dialogue() {
	$('#theform_popup').css({'visibility':'hidden'});
	$('#theform_mask').css({'visibility':'hidden'});
	$('#theform_popup_after').css({'visibility':'hidden'});
}

// функция, чтобы затемнить страницу и подгрузить форму
function theform_popup_show(qualifier, title){
	$('#theform_title').html(title);
	$.ajax({
		type: 'GET',
		url: 'registration/reg_form_event',
		data: '',
		success: function(response) {
			// здесь затемняем страницу и делаем прочие приятные изменения. В данном случае я просто заполняю innerHtml
			//$('#theform_container').dialog({ modal: true });
			var maskHeight = $(document).height();
			var maskWidth = $(window).width();
			//Set heigth and width to mask to fill up the whole screen
			$('#theform_mask').css({'opacity':0.6, 'background-color':'black', 'visibility':'visible'});

			//transition effect     
			//$('#mask').fadeIn(1000);    
			//$('#mask').fadeTo("slow",0.5);

			$('#theform_popup').css({'visibility':'visible'});
			$('#theform_container').html(response);
			$('#id_qualifier').val(qualifier);
		},
		error:  function(xhr, str){
			alert(str)
			$('#theform_container').html("Произошла ошибка загрузки формы: " + str);
		}
	});
}

// функция, чтобы попробовать отправить содержимое формы на сервер
function try_to_submit() {
	var msg   = $('#theform').serialize();
	$.ajax({
		type: 'POST',
		url: 'registration/reg_form_event',
		data: msg,
		success: function(response) {
			if (response == 'OKEY') {
				close_reg_form();
				// растемнить страницу назад
			} else {
				// джанго выплюнул форму - она ему не понравилась, надо дозаполнить
				$('#theform_container').html(response);
				$('#theform_required_fields').html("Пожалуйста, заполните все обязательные поля!");
			}
		},
		error:  function(xhr, str){
			$('#theform_container').html("Произошла ошибка отправки формы: " + str);
		}
	});
}

// навешиваем функции на кнопки; квалификатор может быть любым.

$(document).ready(function(){
	$('#signUpForTest').click(function(){
		theform_popup_show('main', 'Регистрация на отбор в Школу');
	});
	$('#advert1registrationToEvent').click(function(){
		theform_popup_show('m1', 'Регистрация на открытую лекцию "Философия кейс-чемпионата"');
	});
	$('#advert2registrationToEvent').click(function(){
		theform_popup_show('m2', 'Регистрация на бизнес-игру');
	});
	$('#advert3registrationToEvent').click(function(){
		theform_popup_show('m3', 'Регистрация на открытую лекцию "Школа 2.0"');
	});
	$('#advert4registrationToEvent').click(function(){
		theform_popup_show('m4', 'Регистрация на открытую лекцию "Семь доказательств"');
	});
	$('#signUpForOnline1').click(function(){
		theform_popup_show('z1', 'Регистрация на удалённое обучение');
	});
	$('#signUpForOnline2').click(function(){
		theform_popup_show('z2', 'Регистрация на онлайн-обучение');
	});
});

