var oTable = null;
var selectList = [];
$(function () {
    $(".itemTabContent").find("li").eq(3).addClass('active');
    initTable();
    //初始化查询
    var pathnameList = location.pathname.split("/");
    var getPathnameList = getPathnameListFn(pathnameList);
    queryLoad(getPathnameList)
});

function initTable() {
    if (oTable != null) {
        oTable.fnClearTable(0);
        oTable.fnDraw(); //重新加载数据
        oTable.fnDestroy();
    }
    oTable = $('#dataTableList').dataTable({
        "aLengthMenu": [10, 20, 20, 50, 100], //更改显示记录数选项
        "bProcessing": true,
        "bJQueryUI": false,
        "bFilter": false,
        "bLengthChange": true,
        "bSort": false,
        "bStateSave": false,
        "iDisplayStart": 0,
        "iDisplayLength": 10,
        "paging": true,
        "bScrollCollapse": true,
        "bAutoWidth": false,
        "infoCallback": function (oSettings) {
            ellipsisText(oSettings);
        },
        "fnInitComplete": function (oSettings, json) {
            ellipsisText(oSettings);
        },
        "oLanguage": {
            "sLengthMenu": "每页显示 _MENU_条",
            "sZeroRecords": "没有找到符合条件的数据",
            "sProcessing": " 数据加载中， 请稍候......",
            "sInfo": "当前第 _START_ - _END_ 条　共计 _TOTAL_ 条",
            "sInfoEmpty": "没有记录",
            "sInfoFiltered": "(从 _MAX_ 条记录中过滤)",
            "sSearch": "",
            "oPaginate": {
                "sFirst": "首页",
                "sPrevious": "前一页",
                "sNext": "后一页",
                "sLast": "尾页"
            }
        },
        "dom": 'Bfrtip',
        "buttons": [
            'pageLength',
            'colvis',
            {
                text: '关停',
                className: 'btn btn-sm btn-danger btnClose',
                action: function (e, dt, node, config) {
                    modeConfirm('turn_off', selectList, 1)
                }
            },
            {
                text: '开启',
                className: 'btn btn-sm btn-success btnOpen',
                action: function (e, dt, node, config) {
                    modeConfirm('turn_on', selectList, 1)

                }
            },
            {
                text: '操作日志',
                className: 'btn btn-sm btn-warning',
                action: function (e, dt, node, config) {
                    location.href = "/program_logs/0/0"
                }
            }
        ],
        "drawCallback": function (settings) {
            var ischeckAll = $(settings.nTable).find(".icheckbox_all").prop('checked');
            //if(ischeckAll){
            //$(settings.nTable).find(".icheckbox_minimal").prop("checked", ischeckAll).attr("disabled",true);
            //}else{
            // $(settings.nTable).find(".icheckbox_minimal").prop("checked", ischeckAll).attr("disabled",false);
            // }
            $(settings.nTable).find(".icheckbox_minimal").prop("checked", ischeckAll);
            // var ischeckAll = $("#all_checked").prop('checked');
            // $(":checkbox").prop("checked", ischeckAll);
            for (var index = 0; index < $(settings.nTBody).find("tr").length; index++) {
                if (selectList.length > 0) {
                    for (var i = 0; i < selectList.length; i++) {
                        var dom = $($(settings.nTBody).find("tr")[index]).find("td");
                        var text = dom.parents('tr').find('td').eq(1).text();
                        var data = selectList[i];
                        if (text == data) {
                            dom.eq(0).find(":checkbox").prop("checked", true);
                        }
                    }
                }
            }
        },

    });

    $('#dataTableList_wrapper').on("change", ".icheckbox_all", function () {
        //选择全选复选框按钮
        var ischeckAll = $(this).prop('checked');

        if (ischeckAll == true) {
            $("#dataTableList").find(".icheckbox_minimal").prop("checked", true);
            selectList = selectListAllFn()
        } else {
            $("#dataTableList").find(".icheckbox_minimal").prop("checked", false);
            selectList = []
        }
        // $(":checkbox").prop("checked", ischeckAll);
        /* if(ischeckAll){
             $("#dataTableList").find(".icheckbox_minimal").prop("checked", ischeckAll).attr("disabled",true);
         }else{
             $("#dataTableList").find(".icheckbox_minimal").prop("checked", ischeckAll).attr("disabled",false);
         }*/
        // $("#dataTableList").find(".icheckbox_minimal").prop("checked", ischeckAll);
        // if ($("#dataTableList").find(".icheckbox_minimal").prop("checked")==true) {
        //     selectList = selectListAllFn()
        // } else {
        //     selectList = []
        // }
        //  console.log(ischeckAll,selectList)
    });
    $('#dataTableList_wrapper').on("change", ".icheckbox_minimal", function () {
        //选择复选框按钮事件
        var allcheck = $('#dataTableList_wrapper').find('.icheckbox_all');
        var isallcheck = allcheck.prop("checked");
        if (isallcheck) {
            allcheck.prop("checked", false)
        }
        var ischeck = $(this).prop('checked');
        if (ischeck) {
            selectList.push($(this).parents('tr').find('td').eq(1).text())
        } else {
            for (var index = 0; index < selectList.length; index++) {
                var filed = $(this).parents('tr').find('td').eq(1).text();
                if (selectList[index] == filed) {
                    selectList.splice(index, 1)
                }
            }
        }
    });
};

function sumbitQuery() {
    var programName = 0;
    var programType = 0;
    var programPlatform = 0;
    // var programIp = 0;
    var status = 0;
    var programIpType = 0;
    var programNameDom = $("#program_name").val();
    var programTypeDom = $("#program_type").val();
    var programPlatformDom = $("#program_platform").val();

    // var programIpDom=$("#program_ip").val();
    var statusDom = $("#status").val();
    var programIpTypeDom = $("#ip_type").val();
    programNameDom == '' || programNameDom == null || programNameDom == undefined ? programName = 0 : programName = programNameDom;
    programTypeDom == '' || programTypeDom == null || programTypeDom == undefined ? programType = 0 : programType = programTypeDom;
    programPlatformDom == '' || programPlatformDom == null || programPlatformDom == undefined ? programPlatform = 0 : programPlatform = programPlatformDom;
    // programIpDom == '' || programIpDom == null||programIpDom== undefined? programIp = 0 : programIp = programIpDom;
    statusDom == '' || statusDom == null || statusDom == undefined ? status = 0 : status = statusDom;
    programIpTypeDom == '' || programIpTypeDom == null || programIpTypeDom == undefined ? programIpType = 0 : programIpType = programIpTypeDom;
    var url = '/program/' + programName + "/" + programType + "/" + programPlatform + "/" + status + "/" + programIpTypeDom;
    location.href = url
}

function modeConfirm(turn, list, type, name) {
    var title = "";
    if (type == 1) {
        title = "所选"
    } else if (type == 2) {
        title = "所有"
    } else {
        title = name
    }
    var isturn = "";
    (turn == "turn_on") ? isturn = "开启" : isturn = "关停";
    // window.wxc.xcConfirm("确定执行" + title + "频道一键" + isturn + "操作？", window.wxc.xcConfirm.typeEnum.warning, {
    //     onOk: function (v) {
    //         turnFn(turn, list,v, type, name)
    //     }
    // })
    window.wxc.xcConfirm("请输入" + title + "频道一键" + isturn + "操作的审核码：", window.wxc.xcConfirm.typeEnum.input, {
        onOk: function (v) {
            var reg = /^(?!([a-zA-Z]+|\d+)$)[a-zA-Z\d]{8,16}$/;
            var flag = reg.test(v);
            if (v.length < 8 || v.length > 16) {
                window.wxc.xcConfirm("审核码长度为8-16", window.wxc.xcConfirm.typeEnum.error)
            } else {
                if (flag) {
                    turnFn(turn, list, v, type, name)
                } else {
                    window.wxc.xcConfirm("审核码格式必须是8-16位的数字和字母组合", window.wxc.xcConfirm.typeEnum.error)
                }
            }

        }
    })
}

function turnFn(turn, list, code, type, name) {
    var title = "";
    if (type == 1) {
        title = "所选"
    } else if (type == 2) {
        title = "所有"
    } else {
        title = name
    }
    var isturn = "";
    (turn == "turn_on") ? isturn = "开启" : isturn = "关停";
    var listStr = [];
    if (type == 0) {
        listStr.push(list)
    } else {
        listStr = list;
    }
    var listNum = [];
    for (var i = 0; i < listStr.length; i++) {
        listNum.push(parseInt(listStr[i]))
    }
    loadOpen();
    $.ajax({
        url: "/program_change",
        type: "Post",
        data: {
            mode: turn,
            program_ids: JSON.stringify(listNum),
            code: code,
            csrfmiddlewaretoken: token
        },
        dataType: 'json',
        "success": function (resp) {
            loadClose();
            if (resp.msg == 'ok') {
                window.wxc.xcConfirm(title + "频道一键" + isturn + "操作成功！", window.wxc.xcConfirm.typeEnum.success);
                location.reload()
            } else {
                window.wxc.xcConfirm(resp.error, window.wxc.xcConfirm.typeEnum.error);
            }
            /* if (resp.code == "200") {
                 window.wxc.xcConfirm(title + "频道一键" + isturn + "操作成功！", window.wxc.xcConfirm.typeEnum.success);
                 location.href="/program/0/0/0/0/0"
             }else if(resp.code=="201"){
                 window.wxc.xcConfirm(resp.error, window.wxc.xcConfirm.typeEnum.warning);
             }*/
        },
        "error": function (response) {
            loadClose();
        }
    })
}

function reset() {
    location.href = "/program/0/0/0/0/0"
}

function selectListAllFn() {
    //一定要注意这里不能直接复制，否则会改变原来初始的值（关与引用类型和基本类型的概念）
    var allList = [];
    for (var index = 0; index < programIds.length; index++) {
        allList.push(programIds[index])
    }
    return allList
}

function programData(op) {
    var value = op.value;
    var list = "";
    $(op).next().remove();
    $.ajax({
        url: "/approximate",
        type: "Post",
        data: {
            program_name: value,
            csrfmiddlewaretoken: token
        },
        dataType: 'json',
        "success": function (resp) {
            var list = "";
            var data = resp.search_names;
            if (data != "undefined") {
                for (var index = 0; index < data.length; index++) {
                    if (data[index] == value) {
                        list += '<li onclick="activeTap(this)" class="active">' + data[index] + '</li>'
                    } else {
                        list += '<li onclick="activeTap(this)">' + data[index] + '</li>'
                    }

                }
                var menu = '<div class="programCard"> <ul class="programCard-menu">' + list + '</ul> </div>';
                $(op).after(menu);
            }


        },
        "error": function (response) {
        }
    });
}

function activeTap(op) {
    $(op).parent().find("li").removeClass("active");
    $(op).hasClass("active") ? $(op).removeClass("active") : $(op).addClass("active");
    var value = $("#program_name").val();
    $("#program_name").val($(op).text())
}

function queryLoad(getPathnameList) {
    for (var index = 0; index < getPathnameList.length; index++) {
        var active = getPathnameList[index];
        var query = $(".query").children().children('div').not(".querySubmit")[index];
        if (index == 0) {
            var inputType = $(query).find('input');

            if (active == "0") {
                $(inputType).val("")
            } else {
                $(inputType).val(decodeURI(active))
            }
        } else {
            var selectType = $(query).find('select');
            if (active == "0") {
                $(selectType).selectpicker('val', 0)
            } else {
                $(selectType).selectpicker('val', decodeURI(active))
            }
        }
    }
}

$(document).click(function () {
    $(".programCard").remove()
});
$(document).keyup(function (event) {
    if (event.keyCode == 13) {
        $("#submitprogram").trigger("click");
    }
});
$("#title").click(function () {
    modeConfirm('turn_off', selectListAllFn(), 2)
});
