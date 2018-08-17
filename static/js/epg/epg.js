var selectList = [];
$(function () {
    $(".itemTabContent").find("li").eq(1).addClass('active');
     $(".versionTip").find("span").text("5期以前版本");
    $(".version input").click(function () {
        var index=$(this).index();
        var version="5期以前版本";
        switch (index){
            case 0:
                version="5期以前版本";
                break;
            case 1:
                version="6-8期版本";
                break;
            case 2:
                version="9期以上版本";
                break;
            default:
                break;
        }
        $(".version input").removeClass("active");
        $(this).addClass("active");
        $(".versionTip").find("span").text(version)

    })
});

function modeConfirm(index) {
    var turn = '';
    if (index == 1) {
        turn = "turn_on"
    } else if (index == 2) {
        turn = "turn_off"
    }
    var isturn = "";
    (turn == "turn_on") ? isturn = "开启" : isturn = "关停";
    window.wxc.xcConfirm("确定输入全省EPG一键" + isturn + "操作的审核码:", window.wxc.xcConfirm.typeEnum.input, {
        onOk: function (v) {
            var reg = /^(?!([a-zA-Z]+|\d+)$)[a-zA-Z\d]{8,16}$/;
            var flag = reg.test(v);
            if (v.length < 8 || v.length > 16) {
                window.wxc.xcConfirm("审核码长度为8-16", window.wxc.xcConfirm.typeEnum.error)
            } else {
                if (flag) {
                    turnFn(turn, isturn, v)
                } else {
                    window.wxc.xcConfirm("审核码格式必须是8-16位的数字和字母组合", window.wxc.xcConfirm.typeEnum.error)
                }
            }

        }
    })
}

function turnFn(turn, isturn, code) {
    loadOpen();
    $.ajax({
        url: "/epg_one_key",
        type: "Post",
        data: {
            mode: turn,
            code: code,
            csrfmiddlewaretoken: token
        },
        dataType: 'json',
        "success": function (resp) {
            loadClose();
            window.wxc.xcConfirm("EPG一键" + isturn + "操作成功", window.wxc.xcConfirm.typeEnum.success);
            location.reload()
        },
        "error": function (response) {
            loadClose();
            window.wxc.xcConfirm("EPG一键" + isturn + "操作成功", window.wxc.xcConfirm.typeEnum.error);
        }
    })
}

$(document).keyup(function (event) {
    if (event.keyCode == 13) {
        $(".sgBtn").trigger("click");
    }

});
