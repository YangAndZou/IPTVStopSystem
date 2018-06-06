$(".itemTabContent").find("li").hide().eq(3).show().addClass('active');
var oTable1 = null;
var oTable2 = null;
$(function () {
    initTable1();
    initTable2();
});
var selectList1 = [];
var selectList2 = [];
var initTable1 = function () {
    if (oTable1 != null) {
        oTable1.fnClearTable(0);
        oTable1.fnDraw(); //重新加载数据
        oTable1.fnDestroy();
    }
    oTable1 = $('#auditAccountList').dataTable({
        "aLengthMenu": [10, 20, 50, 100], //更改显示记录数选项
        "bProcessing": true,
        "bJQueryUI": false,
        "bFilter": false,
        "bLengthChange": true,
        "bSort": false,
        "bStateSave": false,
        //"bServerSide": true,
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
                text: '审核',
                className: 'btn btn-sm btn-violet',
                action: function (e, dt, node, config) {
                    console.log(selectList1)
                }
            },
            {
                text: '回退',
                className: 'btn btn-sm btn-info',
                action: function (e, dt, node, config) {


                }
            },
            {
                text: '操作日志',
                className: 'btn btn-sm btn-warning',
                action: function (e, dt, node, config) {
                    location.href = "/program_logs"
                }
            }
        ],
        "drawCallback": function (settings) {
            var ischeckAll = $(settings.nTable).find(".icheckbox_all").prop('checked');
            if (ischeckAll) {
                $(settings.nTable).find(".icheckbox_minimal").prop("checked", ischeckAll).attr("disabled", true);
            } else {
                $(settings.nTable).find(".icheckbox_minimal").prop("checked", ischeckAll).attr("disabled", false);
            }
            for (var index = 0; index < $(settings.nTBody).find("tr").length; index++) {
                if (selectList1.length > 0 && selectList1[0] != "all") {
                    for (var i = 0; i < selectList1.length; i++) {
                        var dom = $($(settings.nTBody).find("tr")[index]).find("td");
                        var text = dom.parents('tr').find('td').eq(3).text();
                        var data = selectList1[i];
                        if (text == data) {
                            dom.eq(0).find(":checkbox").prop("checked", true);
                        }
                    }
                }
            }
        },

    });

    $('#auditAccountList_wrapper').on("change", ".icheckbox_all", function () {
        //选择全选复选框按钮
        var ischeckAll = $(this).prop('checked');
        if (ischeckAll) {
            $("#auditAccountList").find(".icheckbox_minimal").prop("checked", ischeckAll).attr("disabled", true);
        } else {
            $("#auditAccountList").find(".icheckbox_minimal").prop("checked", ischeckAll).attr("disabled", false);
        }
        if (ischeckAll) {
            selectList1 = ["all"]
        } else {
            selectList1 = []
        }
    });
    $('#auditAccountList_wrapper').on("change", ".icheckbox_minimal", function () {
        //选择复选框按钮事件
        var ischeck = $(this).prop('checked');
        if (ischeck) {
            selectList1.push($(this).parents('tr').find('td').eq(3).text())
        } else {
            for (var index = 0; index < selectList1.length; index++) {
                var filed = $(this).parents('tr').find('td').eq(3).text();
                if (selectList1[index] == filed) {
                    selectList1.splice(index, 1)
                }
            }
        }
    });
};
var initTable2 = function () {
    if (oTable2 != null) {
        oTable2.fnClearTable(0);
        oTable2.fnDraw(); //重新加载数据
        oTable2.fnDestroy();
    }
    oTable2 = $('#confirmAccountList').dataTable({
        "aLengthMenu": [10, 20, 50, 100], //更改显示记录数选项
        "bProcessing": true,
        "bJQueryUI": false,
        "bFilter": false,
        "bLengthChange": true,
        "bSort": false,
        "bStateSave": false,
        //"bServerSide": true,
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
                text: '审核',
                className: 'btn btn-sm btn-violet',
                action: function (e, dt, node, config) {
                    console.log(selectList2)
                }
            },
            {
                text: '回退',
                className: 'btn btn-sm btn-info',
                action: function (e, dt, node, config) {
                    console.log(selectList2)

                }
            },
            {
                text: '操作日志',
                className: 'btn btn-sm btn-warning',
                action: function (e, dt, node, config) {
                    location.href = "/program_logs"
                }
            }
        ],
        "drawCallback": function (settings) {
            var ischeckAll = $(settings.nTable).find(".icheckbox_all").prop('checked');
            if (ischeckAll) {
                $(settings.nTable).find(".icheckbox_minimal").prop("checked", ischeckAll).attr("disabled", true);
            } else {
                $(settings.nTable).find(".icheckbox_minimal").prop("checked", ischeckAll).attr("disabled", false);
            }

            for (var index = 0; index < $(settings.nTBody).find("tr").length; index++) {
                if (selectList2.length > 0 && selectList2[0] != "all") {
                    for (var i = 0; i < selectList2.length; i++) {
                        var dom = $($(settings.nTBody).find("tr")[index]).find("td");
                        var text = dom.parents('tr').find('td').eq(3).text();
                        var data = selectList2[i];
                        if (text == data) {
                            dom.eq(0).find(":checkbox").prop("checked", true);
                        }
                    }
                }
            }
        },

    });

    $('#confirmAccountList_wrapper').on("change", ".icheckbox_all", function () {
        //选择全选复选框按钮
        var ischeckAll = $(this).prop('checked');
        if (ischeckAll) {
            $("#confirmAccountList").find(".icheckbox_minimal").prop("checked", ischeckAll).attr("disabled", true);
        } else {
            $("#confirmAccountList").find(".icheckbox_minimal").prop("checked", ischeckAll).attr("disabled", false);
        }
        if (ischeckAll) {
            selectList2 = ["all"]
        } else {
            selectList2 = []
        }
    });
    $('#confirmAccountList_wrapper').on("change", ".icheckbox_minimal", function () {
        //选择复选框按钮事件

        var ischeck = $(this).prop('checked');
        if (ischeck) {
            selectList2.push($(this).parents('tr').find('td').eq(3).text())
        } else {
            for (var index = 0; index < selectList2.length; index++) {
                var filed = $(this).parents('tr').find('td').eq(3).text();
                if (selectList2[index] == filed) {
                    selectList2.splice(index, 1)
                }
            }
        }


    });
};

function auditTap(turn, list, type, name, process_id) {
    var title = "";
    if (type == 1) {
        title = "所选"
    } else if (type == 2) {
        title = "所有"
    } else {
        title = name
    }
    window.wxc.xcConfirm("确定提交一键关停操作？", window.wxc.xcConfirm.typeEnum.warning, {
        onOk: function (v) {
            auditFn(turn, list, type, name, process_id)
        }
    })
}

function auditFn(turn, list, type, name, process_id) {
    var title = "";
    if (type == 1) {
        title = "所选"
    } else if (type == 2) {
        title = "所有"
    } else {
        title = name
    }
    var List = [];
    if (type == 0) {
        List.push(list)
    } else {
        List = list;
    }
    var formData = new FormData();
    formData.append("mode", turn);
    formData.append("program_ips", JSON.stringify(List));
    formData.append("csrfmiddlewaretoken", token);
    $.ajax({
        url: "/process_verify_change",
        type: "Post",
        data: {
            mode: turn,
            process_id:
            program_ips
:
    JSON.stringify(List),
        csrfmiddlewaretoken
:
    token
},
    dataType:'json',
        /* processData: false,
         contentType: false,*/
        "success"
:

    function (resp) {
        if (resp.code == "200") {
            window.wxc.xcConfirm("提交成功！", window.wxc.xcConfirm.typeEnum.success);
        }
    }

,
    "error"
:

    function (response) {
    }
})
}

function retroveTap(turn, list, type, name) {
    var title = "";
    if (type == 1) {
        title = "所选"
    } else if (type == 2) {
        title = "所有"
    } else {
        title = name
    }
    window.wxc.xcConfirm("回退意见输入框:", window.wxc.xcConfirm.typeEnum.input, {
        onOk: function (v) {
            retroveFn(turn, list, type, name, v)
        }
    })
}

function retroveFn(turn, list, type, name, v) {
    var title = "";
    if (type == 1) {
        title = "所选"
    } else if (type == 2) {
        title = "所有"
    } else {
        title = name
    }
    var List = [];
    if (type == 0) {
        List.push(list)
    } else {
        List = list;
    }
    var formData = new FormData();
    formData.append("mode", turn);
    formData.append("retroveTxt", v);
    formData.append("program_ips", JSON.stringify(List));
    formData.append("csrfmiddlewaretoken", token);
    $.ajax({
        url: "/program_change",
        type: "Post",
        data: {
            mode: turn,
            program_ips: JSON.stringify(List),
            csrfmiddlewaretoken: token
        },
        dataType: 'json',
        /* processData: false,
         contentType: false,*/
        "success": function (resp) {
            if (resp.code == "200") {
                window.wxc.xcConfirm("提交成功！", window.wxc.xcConfirm.typeEnum.success);
            }
        },
        "error": function (response) {
        }
    })
}