
$(document).ready(function(){
    $('.topleftli1').click(function(){
        $('.topleftli1 p').show();
        $('.topleftli2 p').hide();
        $('.topleftli3 p').hide();
        $('.topleftli4 p').hide();
        $('.topright1').show();
        $('.topright2').hide();
        $('.topright3').hide();
        $('.topright4').hide();
    })
    $('.topleftli2').click(function(){
        $('.topleftli1 p').hide();
        $('.topleftli2 p').show();
        $('.topleftli3 p').hide();
        $('.topleftli4 p').hide();
        $('.topright1').hide();
        $('.topright2').show();
        $('.topright3').hide();
        $('.topright4').hide();
    })
    $('.topleftli3').click(function(){
        $('.topleftli1 p').hide();
        $('.topleftli2 p').hide();
        $('.topleftli3 p').show();
        $('.topleftli4 p').hide();
        $('.topright1').hide();
        $('.topright2').hide();
        $('.topright3').show();
        $('.topright4').hide();
    })
    $('.topleftli4').click(function(){
        $('.topleftli1 p').hide();
        $('.topleftli2 p').hide();
        $('.topleftli3 p').hide();
        $('.topleftli4 p').show();
        $('.topright1').hide();
        $('.topright2').hide();
        $('.topright3').hide();
        $('.topright4').show();
    })
})


// 添加
$('.topright2').on('click',function(){
    var addTds = $('.addlist input')
    dict_data = {}
    for (var i = 0; i < (addTds.length - 1); i++){
        if (i == 0){
            dict_data.btitle = addTds.eq(i).val()
        } else if (i ==1){
            dict_data.btitle = addTds.eq(i).val()
        }
        else if (i ==2){
            dict_data.btitle = addTds.eq(i).val()
        }
        else if (i ==3){
            dict_data.btitle = addTds.eq(i).val()
        }
        else if (i ==4){
            dict_data.btitle = addTds.eq(i).val()
        }
        else if (i ==5){
            dict_data.btitle = addTds.eq(i).val()
        }else if (i ==6){
            dict_data.btitle = addTds.eq(i).val()
        }else if (i ==7){
            dict_data.btitle = addTds.eq(i).val()
        }
    }
    if (dict_data.usename == "" | dict_data.age == "" | dict_data.sex == "" | dict_data.passwrod1 == "" | dict_data.phone1 == "" | dict_data.sites == "" | dict_data.mailbox == "" | dict_data.Date == "" ){
        alert('输入内容不能为空')
        return
    }
    $.post({
        url: "/books/",
        dataType:"json",
        data:dict_data,
        success: function (dat){
            alert(dat.data)
            fnLoadHomeData('add')
            window.location.reload()

            for (var i =0; i <(addTds.length - 1); i++){
                console.log(i)
                addTds.eq(i).val("")
            }
        }
    })
})
// 删除

$('.del').on('click',function(){
    result = $(this).siblings().eq(0).children('input').val()
    $.ajax({
        url: "/books/",
        dataType: 'json',
        type:'delete',
        data: JSON.stringify({id: result}),
        success: function (dat){
            $(this).parent().remove()
            console.log($(this))
            fnLoadHomeData('del')
            window.location.reload()
        }
    })
})