$(function () {

});

var submitCheck=function () {
    var username=$("#username").val();
    var password=$("#password").val();
    if(username==""){
        window.wxc.xcConfirm("请输入正确用户名", window.wxc.xcConfirm.typeEnum.info);
        return false
    }else if(password==""){
        window.wxc.xcConfirm("请输入正确用户密码", window.wxc.xcConfirm.typeEnum.info);
        return false
    }
    return true

}