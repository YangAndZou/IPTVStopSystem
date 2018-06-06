$(".itemTabContent").find("li").eq(0).addClass('active');
$(function () {
    $("#code").focus()
});
function getCode() {
    window.wxc.xcConfirm("确定要更改审核码？", window.wxc.xcConfirm.typeEnum.confirm, {
        onOk: function (v) {
            $.ajax({
                url: "/set_code",
                type: "Post",
                data: {
                    code:$("#code").val(),
                    csrfmiddlewaretoken: token
                },
                dataType: 'json',

                "success": function (resp) {
                    /*if(resp.msg=="ok"){
                     location.reload()
                     }*/
                },
                "error": function (response) {
                }
            })
        }
    });

}
function reset() {
    location.reload()
}