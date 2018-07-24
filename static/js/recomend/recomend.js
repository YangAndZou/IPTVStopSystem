var oTable = null;
var selectList = [];
$(function () {
    $(".itemTabContent").find("li").eq(4).addClass('active');
    recomendTap("#recomBtn", 'recom', 10)
});

function recomendTap(op, moduleID, num) {
    $(op).parent().find("button").removeClass("active");
    $(op).addClass("active");
    var title="";
    switch (moduleID){
        case "recom":
           title="热门质询";
            break;
        case "live":
            title="电视节目";
            break;
        case "rank":
            title="排行榜";
            break;
        case "hotapp":
            title="热门应用";
            break;
    }

    $("#title").text(title);
    loadImage(moduleID, num);
}

function loadImage(moduleID, num) {
    $(".recomend-body").attr('id', moduleID);
    $('#' + moduleID).empty();
    var str = '';
    if (moduleID == "live") {
        str = liveFn(moduleID, num)
    } else if (moduleID == "hotapp") {
        str = hotappFn(moduleID, num)
    } else {
        str = elseFn(moduleID, num)
    }
    $('#' + moduleID).append(str);
    onSize()
}

function liveFn(moduleID, num) {
    var str = '';
    for (var $index = 0; $index < num; $index++) {
        var $status = 1;
        if ($index == 0) {
            str = '<div style="float:left;display:inline-block">' + str
        } else if ($index == 4) {
            str = str + '</div>';
            $status = 0;
        }
        var $statusBox = '';
        if ($status == 1) {
            $statusBox = '<img src = "/static/image/1.png"> <div class="mask"> <h5>标题页</h5> <div class="recomendBtn"><button class="closed" onclick="picTap(this,' + parseInt($index + 1) + ',\'' + moduleID + '\',1)"><i class="glyphicon glyphicon-off"></i></button></div> </div>';
        } else {
            $statusBox = '<img src = "/static/image/1.png"> <div class="mask"> <h5>标题页</h5> <div class="recomendBtn"><button class="open" onclick="picTap(this,' + parseInt($index + 1) + ',\'' + moduleID + '\',0)"><i class="glyphicon glyphicon-open"></i></button></div> </div>';
        }
        str += '<div class = "box">' + $statusBox + '</div>'
    }
    return str
}

function hotappFn(moduleID, num) {
    var str = '';

    for (var $index = 0; $index < num; $index++) {
         var $status = 1;
        if ($index == 0) {
            str = '<div style="float:left;display:inline-block">' + str
        } else if ($index == 3 || $index == 5 || $index == 8 || $index == 11) {
            str = str + '</div><div style="float:left;display:inline-block">'
                 $status = 0;
        } else if ($index == 11) {
            str = str + '</div>'

        }
        var $statusBox = '';
        if ($status == 1) {
            $statusBox = '<img src = "/static/image/1.png"> <div class="mask"> <h5>标题页</h5> <div class="recomendBtn"><button class="closed" onclick="picTap(this,' + parseInt($index + 1) + ',\'' + moduleID + '\',1)"><i class="glyphicon glyphicon-off"></i></button></div> </div>';
        } else {
            $statusBox = '<img src = "/static/image/1.png"> <div class="mask"> <h5>标题页</h5> <div class="recomendBtn"><button class="open" onclick="picTap(this,' + parseInt($index + 1) + ',\'' + moduleID + '\',0)"><i class="glyphicon glyphicon-open"></i></button></div> </div>';
        }
        str += '<div class = "box"  >' + $statusBox + '</div>'
    }
    return str
}

function elseFn(moduleID, num) {
    var str = '';

    for (var $index = 0; $index < num; $index++) {
         var $status = 1;
         if($index==2){
            $status = 0;
         }
        var $statusBox = '';
        if ($status == 1) {
            $statusBox = '<img src = "/static/image/1.png"> <div class="mask"> <h5>标题页</h5> <div class="recomendBtn"><button class="closed" onclick="picTap(this,' + parseInt($index + 1) + ',\'' + moduleID + '\',1)"><i class="glyphicon glyphicon-off"></i></button></div> </div>';
        } else {
            $statusBox = '<img src = "/static/image/1.png"> <div class="mask"> <h5>标题页</h5> <div class="recomendBtn"><button class="open" onclick="picTap(this,' + parseInt($index + 1) + ',\'' + moduleID + '\',0)"><i class="glyphicon glyphicon-open"></i></button></div> </div>';
        }
        str += '<div class = "box"  >' + $statusBox + '</div>'
    }
    return str
}

function picTap(op, pos, moduleID, status) {
    var statusStr="";
    status==0?statusStr="开启":statusStr="关停";
    window.wxc.xcConfirm("确定要"+statusStr+"该频道吗？", window.wxc.xcConfirm.typeEnum.warning, {
        onOk: function (v) {
            $.ajax({
                url: "/recommend_change_8",
                type: "Post",
                data: {
                    position_head: moduleID,
                    position: pos,
                    status:status,
                    csrfmiddlewaretoken: token
                },
                dataType: 'json',
                success: function (resp) {
                    loadClose();
                    if (resp.code == "200") {
                       location.reload()
                    } else if (resp.code == "201") {
                        window.wxc.xcConfirm(resp.msg, window.wxc.xcConfirm.typeEnum.success);
                    }
                },
                "error": function (response) {
                    loadClose();
                }
            })
        }
    });

}