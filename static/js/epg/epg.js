$(".itemTabContent").find("li").eq(0).addClass('active')
var selectList=[];
function modeConfirm(turn, list){
     var isturn="";
    (turn=="turn_on")?isturn="开启":isturn="关停";
    window.wxc.xcConfirm("确定执行全省EPG一键"+isturn+"操作？", window.wxc.xcConfirm.typeEnum.warning, {
        onOk: function(v) {
            turnFn(turn, list)
        }
    })
}
function turnFn(turn, list) {
    var isturn="";
    (turn=="turn_on")?isturn="开启":isturn="关停";
    var List = [];
    if (type == 0) {
        List.push(list)
    } else {
        List = list;
    }
    $.ajax({
        url: "/program_change",
        type: "Post",
        data: {
            mode: turn,
        },
        dataType:'json',
       /* processData: false,
        contentType: false,*/
        "success": function (resp) {
            if(resp.code=="200"){
                window.wxc.xcConfirm("EPG一键"+isturn+"操作已提交审核！", window.wxc.xcConfirm.typeEnum.success);
            }
         },
        "error": function (response) {
        }
    })
}
$("#title").click(function () {
     modeConfirm('turn_off', ["all"])
});