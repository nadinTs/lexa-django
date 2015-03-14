$(function(){
    $('.spoiler').hide();
    $('<span class="revealer">Подробнее...</span>').insertBefore('.spoiler');
    $('.revealer').click(function(){
        $(this).hide();
        $(this).next().fadeIn();
    });
});

