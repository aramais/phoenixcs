$(function() {
    $('#login').click(function(e) {
        var $message = $('#login_block');
        
        if ($message.css('display') != 'block') {
            $message.show();
            
            var firstClick = true;
            $(document).bind('click.myEvent', function(e) {
                if (!firstClick && $(e.target).closest('#login_block').length == 0) {
                    $message.hide();
                    $(document).unbind('click.myEvent');
                }
                firstClick = false;
            });
        }
        
        e.preventDefault();
    });
});

//СКРИПТЫ ВЫЗЫВАЮЩИЙ ПЛАШКУ "НАПИСАТЬ СООБЩЕНИЕ ПОЛЬЗОВАТЕЛЮ"

$(function() {
    $('#write_message').click(function(e) {
        var $message = $('#message_block_back');
        
        if ($message.css('display') != 'block') {
            $message.show();
            
            var firstClick = true;
           /* $(document).bind('click.myEvent', function(e) {
                if (!firstClick && $().closest('#message_block_back').length == 0) { // НАДО ПОЧИНИТЬ ОБРАТНО - ВЗЯТЬ СВЕРХУ
                    $message.hide();
                    $(document).unbind('click.myEvent');
                }
                firstClick = false;
            });*/
        }
        
        e.preventDefault();
    });
});

//ВЫЗЫВАЕМ МЕНЮ ПРОФИЛЯ ИЗ ШАПКИ

$(function() {
    $('#profile_settings').click(function(e) {
        var $menu = $('#profile_menu_block');
        
        if ($menu.css('display') != 'block') {
            $menu.show();
            
            var firstClick = true;
            $(document).bind('click.myEvent', function(e) {
                if (!firstClick && $(e.target).closest('#profile_menu_block').length == 0) {
                    $menu.hide();
                    $(document).unbind('click.myEvent');
                }
                firstClick = false;
            });
        }
        
        e.preventDefault();
    });
});

//СКРОЛЛ К ЭЛЕМЕНТУ

$(document).ready(function(){
    $('a[href^="#"], a[href^="."]').click( function(){
        var scroll_el = $(this).attr('href');
        if ($(scroll_el).length != 0) {
        $('html, body').animate({ scrollTop: $(scroll_el).offset().top-115 }, 700);
        }
        return false;
    });
});

//ДОБАВЛЕНИЕ НОВЫХ БЛОКОВ ОТ ДАВИДА

function cloneLastFormInFormset(selector, type) {
	//alert($(selector).html())
    var newElement = $(selector).clone(true);
    var total = $(selector).parent().parent().find('#id_' + type + '-TOTAL_FORMS').val()
    //alert(total)
    //var total = $('#id_' + type + '-TOTAL_FORMS').val();
    newElement.find(':input').each(function() {
        var name = $(this).attr('name').replace('-' + (total-1) + '-','-' + total + '-');
        var id = 'id_' + name;
        $(this).attr({'name': name, 'id': id}).val('').removeAttr('checked');
    });
    newElement.find('label').each(function() {
        var newFor = $(this).attr('for').replace('-' + (total-1) + '-','-' + total + '-');
        $(this).attr('for', newFor);
    });
    total++;
    $(selector).parent().parent().find('#id_' + type + '-TOTAL_FORMS').val(total);
    $(selector).after(newElement);
}

function cloneLastFormInFormsetSimple(selector, type) {
    var newElement = $(selector).clone(true);
    var total = $('#id_' + type + '-TOTAL_FORMS').val();
    newElement.find(':input').each(function() {
        var name = $(this).attr('name').replace('-' + (total-1) + '-','-' + total + '-');
        var id = 'id_' + name;
        $(this).attr({'name': name, 'id': id}).val('').removeAttr('checked');
    });
    newElement.find('label').each(function() {
        var newFor = $(this).attr('for').replace('-' + (total-1) + '-','-' + total + '-');
        $(this).attr('for', newFor);
    });
    total++;
    $('#id_' + type + '-TOTAL_FORMS').val(total);
    $(selector).after(newElement);
}
