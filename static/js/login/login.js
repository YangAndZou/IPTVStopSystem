$(function () {

});

function login(form) {
    var username=form.username.value;
    var password=form.password.value;
    var token=form.csrfmiddlewaretoken.value;
    if(username==""){
        window.wxc.xcConfirm("请输入正确用户名", window.wxc.xcConfirm.typeEnum.warning);
        return false
    }else if(password==""){
        window.wxc.xcConfirm("请输入正确用户密码", window.wxc.xcConfirm.typeEnum.warning);
        return false
    }
    $.ajax({
        url: "/login",
        type: "Post",
        data:{
            username:username,
            password:password,
            csrfmiddlewaretoken:token
        },
        dataType:'json',
        "success": function (resp) {
            if(resp.status=="ok"){
                window.wxc.xcConfirm("登入成功", window.wxc.xcConfirm.typeEnum.success);
                location.href="/index"
            }else{
                window.wxc.xcConfirm(resp.status, window.wxc.xcConfirm.typeEnum.error);
            }
        },
        "error": function (response) {
            window.wxc.xcConfirm(response.status+'&nbsp;'+response.statusText, window.wxc.xcConfirm.typeEnum.error);

        }
    });
}
