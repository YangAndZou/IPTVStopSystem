$(".itemTabContent").find("li").eq(0).addClass('active');
$(function () {
    $("#code").focus()
});
function getCode() {
    var code=$("#code").val();
    var reg =/^(?!([a-zA-Z]+|\d+)$)[a-zA-Z\d]{8}$/;
    // var reg=/^[A-Za-z0-9]{8}$/g;
    var flag=reg.test(code);
    if(code.length<8||code.length>8){
        window.wxc.xcConfirm("审核码必须是八位", window.wxc.xcConfirm.typeEnum.error)
    }else{
        if(flag){
            window.wxc.xcConfirm("确定要更改审核码？", window.wxc.xcConfirm.typeEnum.confirm, {
                onOk: function (v) {
                    $.ajax({
                        url: "/set_code",
                        type: "Post",
                        data: {
                            code:code,
                            csrfmiddlewaretoken: token
                        },
                        dataType: 'json',

                        "success": function (resp) {
                            if(resp.msg=="ok"){
                                location.reload()
                            }
                        },
                        "error": function (response) {
                        }
                    })
                }
            });
        }else{
            window.wxc.xcConfirm("审核码格式必须是八位数字和字母的组合", window.wxc.xcConfirm.typeEnum.error)
        }
    }



}
function reset() {
    location.reload()
}