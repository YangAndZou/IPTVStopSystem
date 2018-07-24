var oTable = null;
var selectList = [];
$(function () {
    $(".itemTabContent").find("li").eq(4).addClass('active');
    recomendTap("#recomBtn",'hotapp',12)
});

function recomendTap(op,moduleID,num) {
    $(op).parent().find("button").removeClass("active");
    $(op).addClass("active");
    loadImage(moduleID,num);
}
function loadImage(moduleID,num){
    $(".recomend-body").attr('id',moduleID);
    $('#'+moduleID).empty();
    var str='';
    if(moduleID=="live"){
       for(var $index=0;$index<num;$index++){
           if($index==0){
               str='<div style="float:left;display:inline-block">'+str
           }else if($index==4){
               str=str+'</div>'
           }
        str+='<div class = "box"> <img src = "/static/image/1.png"> <div class="mask"> <h5>标题页</h5> <div class="recomendBtn"> <button onclick="picTap(this,'+parseInt($index+1) +',\''+moduleID+'\')"><i class="glyphicon glyphicon-off"></i></button> </div> </div> </div>'
       }

    }  else if (moduleID=="hotapp"){
       for(var $index=0;$index<num;$index++){
           if($index==0){
               str='<div style="float:left;display:inline-block">'+str
           }else if($index==3||$index==5||$index==8||$index==11){
               str=str+'</div><div style="float:left;display:inline-block">'
           }else if($index==12){
               str=str+'</div>'
           }
           str+='<div class = "box"  > <img src = "/static/image/1.png"> <div class="mask"> <h5>标题页</h5> <div class="recomendBtn"> <button onclick="picTap(this,'+parseInt($index+1)+',\''+moduleID+'\')"><i class="glyphicon glyphicon-off"></i></button> </div> </div> </div>'

       }
    }else{
       for(var $index=0;$index<num;$index++){
        str+='<div class = "box" onclick="picTap(this,'+parseInt($index+1)+',\''+moduleID+'\')"> <img src = "/static/image/1.png"> <div class="mask"> <h5>标题页</h5> <div class="recomendBtn"> <button onclick="picTap(this,'+parseInt($index+1)+',\''+moduleID+'\')"><i class="glyphicon glyphicon-off"></i></button> </div> </div> </div>'
       }
    }

    $('#'+moduleID).append(str);
    onSize()
}
function picTap(op,pos,moduleID) {
    window.wxc.xcConfirm("确定要关停该频道吗？", window.wxc.xcConfirm.typeEnum.warning, {
        onOk: function (v) {
               console.log(op,pos,moduleID)
        }
    });

}