var selectList=[];
$(function () {
    $(".itemTabContent").find("li").eq(1).addClass('active');
});
function modeConfirm(turn){
     var isturn="";
    (turn=="turn_on")?isturn="开启":isturn="关停";
     window.wxc.xcConfirm("确定输入全省EPG一键"+isturn+"操作的审核码:", window.wxc.xcConfirm.typeEnum.input, {
        onOk: function(v) {
            var reg = /^(?!([a-zA-Z]+|\d+)$)[a-zA-Z\d]{8,16}$/;
            var flag = reg.test(v);
            if (v.length < 8 || v.length > 16) {
                window.wxc.xcConfirm("审核码长度为8-16", window.wxc.xcConfirm.typeEnum.error)
            } else {
                if (flag) {
                     turnFn(turn,v)
                } else {
                    window.wxc.xcConfirm("审核码格式必须是8-16位的数字和字母组合", window.wxc.xcConfirm.typeEnum.error)
                }
            }

        }
    })
}
function turnFn(turn,code) {
    var isturn="";
    (turn=="turn_on")?isturn="开启":isturn="关停";
    var List = [];
    $.ajax({
        url: "/epg_change",
        type: "Post",
        data: {
            mode: turn,
            code:code
        },
        dataType:'json',
        "success": function (resp) {
            if(resp.code=="200"){
                window.wxc.xcConfirm("EPG一键"+isturn+"操作成功", window.wxc.xcConfirm.typeEnum.success);
            }
         },
        "error": function (response) {
        }
    })
}
$("#title").click(function () {
     modeConfirm('turn_off')
});