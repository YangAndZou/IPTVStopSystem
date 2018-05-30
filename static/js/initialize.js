//初始化函数
$(function () {
    var layoutClass= {
        container: {
            name: '.login',
            width: 1,
            height: 1
        },
        loginTitle: {
            name: '.login-title',
            width: 1,
            height:0.25,
            lineHeight:1
        },
        loginbody: {
            name: '.login-body',
            width: 1,
            height:0.6,
            lineHeight:1
        }
    };
    layout(layoutClass);
    $(window).resize(function () {
        layout(layoutClass);
    });
});


function layout(option) {
    var height=$(window).height();
    var width=$(window).width();
    for(var key in option){
        var name=option[key].name;
        var ratioW=option[key].width;
        var ratioH=option[key].height;
        //$(name).width(ratioW*width-1);
        $(name).css({
            height:ratioH*height-1
        });
        //$(name).height(ratioH*height-1);
        var lineHeight=option[key].lineHeight;
        if(lineHeight!=undefined){
            $(name).css({
                lineHeight:$(name).height()*lineHeight+"px"
            })
        }
    }
    $(".panel").css({
        minHeight:(height-150)+'px'
    });
    var panelH=$(".panel").height();
    /*$(".table tr td").css({
        height:(panelH-200)/10+"px",
        lineHeight:(panelH-200)/10+"px",
        minHeight:'40px',
        maxHeight:'60px'
    })*/

}

/*
function autoInputFn() {
    var autoinput = $("input.auto-input");

    autoinput.each(function (index,obj) {
        $(obj).attr('size', $(obj).val().length > 4 ? $(obj).val().length+1:4);
        var placeholder=$(obj).attr("placeholder");
        placeholder==undefined||placeholder==''?$(obj).attr('size', 4):$(obj).attr('size',$(obj).attr("placeholder").length+2);
    });
    autoinput.keyup(function () {
        $(this).attr('size', $(this).val().length > 4 ? $(this).val().length:4);
    });
    autoinput.keydown(function () {
        $(this).keyup()
    });
    $(".radio").click(function () {
        $(this).parent().parent().find(".radio").removeClass('checked');
        $(this).addClass('checked')
    });
}
var ellipsisText=function(){
    var dom=$("table").find("tbody");
    var html=dom.html();
    dom.find('td').find("div").css("display",'inline-block');
    dom.find('td').each(function (index,obj) {
        //将每个td里添加一个div
        var code=$(obj).find('code').length;
        var child=$(obj).find('code').eq(0);
        if(code==0){
            return
        }
        var tdWidth=$(obj).width();
        var textWidth=child.width();
        if(tdWidth<textWidth){
            var textlen=child.find('a').length;
            //每个字体的平均宽度=文本宽度/字体个数
            var fontSize=textWidth/child.text().length;
            //表格长度能容纳字体的个数=表格宽度/每个字体的平均宽度
            var tableFontNum=Math.floor(tdWidth/fontSize)-1;
            if(textlen>0){
                child.find('a').attr("title",child.text()).text(child.text().substr(0,tableFontNum)+"...")
            }else{
                child.attr("title",child.text()).text(child.text().substr(0,tableFontNum)+"...")
            }
        }

    });
};
function initialize() {
    var currentW = window.innerWidth;//当前窗口内大小

    var defaultW =$(window).width();
    var defaultH =$(window).height();
    var defaultF =Math.round($(window).width()/100) 
    var rat = currentW / defaultW; //比率
    var currentF = defaultF * rat ;//当前需要的fonsize值

    var parentElement = document.getElementById('html'); //根节点
    var styleString = '' + currentF + 'px';//样式字符串
    // console.log('styleString', styleString)
    //  parentElement.style.overflowY = 'hidden';

    if (currentW > 1000) { //窗口大于1000
        //窗口调整大小
        // parentElement.style.overflowX = 'hidden'
        parentElement.style.fontSize = styleString
    } else {

        // parentElement.style.overflowX = 'auto'
    }
    var topOffset =180;
    var height =$(window).height();
    height = height - topOffset;
    if (height > topOffset) {
        $("#region_table").height(height+"px");

        $("#region_table td").css({
            height:($("#region_table").height()-150)/10+"px"
        });
        $("#region_table th").css({
            height:($("#region_table").height()-150)/10+"px"
        });
        $(".region_card").css({
            height:($("#region_table").height()-80)+"px"
        })
    }
}
*/

//表格里溢出的数据打省略号
var ellipsisText=function(oSettings){
    var dom=$(oSettings.nTBody);
    var html=dom.html();
    dom.find('td').find("div").css("display",'inline-block');
    dom.find('td').each(function (index,obj) {
        //将每个td里添加一个div
        var len=$(obj).find('div').length;

        // var code=$(obj).find('code').length;
        if(len==0){
            //if(code>0){
            $(obj).html('<div style="display:inline-block">'+$(obj).html()+'</div>')
            //}
        }
        var child=$(obj).find('div').eq(0);
        var tdWidth=$(obj).width();
        var textWidth=child.width();
        if(tdWidth<textWidth){
            var textlen=child.find('a').length;
            //每个字体的平均宽度=文本宽度/字体个数
            var fontSize=textWidth/child.text().length;
            //表格长度能容纳字体的个数=表格宽度/每个字体的平均宽度
            var tableFontNum=Math.floor(tdWidth/fontSize)-1;
            if(textlen>0){
                child.find('a').attr("title",child.text()).text(child.text().substr(0,tableFontNum)+"...")
            }else{
                child.attr("title",child.text()).text(child.text().substr(0,tableFontNum)+"...")
            }
        }

    });
};