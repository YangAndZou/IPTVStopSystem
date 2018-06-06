$(".itemTabContent").find("li").eq(3).addClass('active');
var oTable = null;
$(function () {
    initTable();
});
var selectList = [];
var initTable = function () {
    if (oTable != null) {
        oTable.fnClearTable(0);
        oTable.fnDraw(); //重新加载数据
        oTable.fnDestroy();
    }
    oTable = $('#dataTableList').dataTable({
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
//            "sAjaxSource": "/asset/hard/select/",
        "dom": 'Bfrtip',
        /*'columnDefs': [{
         targets:0,
         data: null,
         defaultContent:"<input type ='checkbox' name='test' class='icheckbox_minimal' value=''>",
         }],*/

        "buttons": [
            'pageLength',
            'colvis',
            /* {
             text: '大区关停',
             className: 'btn btn-sm btn-warning ',
             action: function (e, dt, node, config) {
             $("#regionDialog").modal('show')
             }
             },
             {
             text: '大区关停列表',
             className: 'btn btn-sm btn-warning ',
             action: function (e, dt, node, config) {
             }
             },
             {
             text: '操作日志',
             className: 'btn btn-sm btn-violet',
             action: function (e, dt, node, config) {
             }
             },*/
            /*{
             text: '区域边缘关停',
             className: 'btn btn-sm btn-warning ',
             action: function (e, dt, node, config) {
             }
             },
             {
             text: '区域边缘关停列表',
             className: 'btn btn-sm btn-warning ',
             action: function (e, dt, node, config) {
             }
             },
             {
             text: '操作日志',
             className: 'btn btn-sm btn-success',
             action: function (e, dt, node, config) {
             }
             },*/
            {
                text: '关停',
                className: 'btn btn-sm btn-danger btnClose',
                action: function (e, dt, node, config) {
                    console.log(selectList)
                    modeConfirm('turn_off', selectList, 1)
                }
            },
            {
                text: '开启',
                className: 'btn btn-sm btn-success btnOpen',
                action: function (e, dt, node, config) {
                    console.log(selectList)
                    modeConfirm('turn_on', selectList, 1)

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
            if(ischeckAll){
                $(settings.nTable).find(".icheckbox_minimal").prop("checked", ischeckAll).attr("disabled",true);
            }else{
                $(settings.nTable).find(".icheckbox_minimal").prop("checked", ischeckAll).attr("disabled",false);
            }
            // var ischeckAll = $("#all_checked").prop('checked');
            // $(":checkbox").prop("checked", ischeckAll);
            for (var index = 0; index < $(settings.nTBody).find("tr").length; index++) {
                if (selectList.length > 0 && selectList[0] != "all") {
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
        // $(":checkbox").prop("checked", ischeckAll);
        if(ischeckAll){
            $("#dataTableList").find(".icheckbox_minimal").prop("checked", ischeckAll).attr("disabled",true);
        }else{
            $("#dataTableList").find(".icheckbox_minimal").prop("checked", ischeckAll).attr("disabled",false);
        }
        if (ischeckAll) {
            selectList = ["all"]
        } else {
            selectList = []
        }
    });
    $('#dataTableList_wrapper').on("change", ".icheckbox_minimal", function () {
        //选择复选框按钮事件
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

function logout() {
    $.ajax({
        url: "/logout",
        type: "Post",
        dataType: "json",
        cache: false,
        processData: false,
        contentType: false,
        "success": function (resp) {
            window.wxc.xcConfirm("登出成功", window.wxc.xcConfirm.typeEnum.info);
        },
        "error": function (response) {

        }
    })
}

function sumbitQuery() {
    var programName = 0;
    var programIp = 0;
    var status = 0;
    var programStartNum = 0;
    var programEndNum = 0;
    var programNameDom=$("#program_name").val();
    var programIpDom=$("#program_ip").val();
    var programNumStartDom=$("#program_num_start").val();
    var programNumEndDom=$("#program_num_end").val();
    var statusDom=$("#status").val();
    if(parseInt(programNumStartDom) >parseInt(programNumEndDom) ){
        window.wxc.xcConfirm("请填写正确的频道号范围！", window.wxc.xcConfirm.typeEnum.warning);
        return false
    }
    programNameDom == ''|| programNameDom== null||programNameDom == undefined? programName = 0 : programName = programNameDom;
    programIpDom == '' || programIpDom == null||programIpDom== undefined? programIp = 0 : programIp = programIpDom;
    programNumStartDom == '' || programNumStartDom == null||programNumStartDom== undefined? programStartNum = 0 : programStartNum = programNumStartDom;
    programNumEndDom == '' || programNumEndDom == null||programNumEndDom== undefined? programEndNum = 0 : programEndNum = programNumEndDom;
    statusDom == ''||statusDom == null||statusDom == undefined ? status = 0 : status =statusDom;
     var url = '/program/' + programName + "/" + programIp + "/" + programStartNum +"-"+ programNumEndDom+ "/" + status;
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
            turnFn(turn, list,v, type, name)
        }
    })
}

function turnFn(turn, list,code, type, name) {
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
        url: "/program_change",
        type: "Post",
        data: {
            mode: turn,
            program_names: JSON.stringify(List),
            code:code,
            csrfmiddlewaretoken: token
        },
        dataType: 'json',
        /* processData: false,
         contentType: false,*/
        "success": function (resp) {
            if (resp.code == "200") {
                window.wxc.xcConfirm(title + "频道一键" + isturn + "操作成功！", window.wxc.xcConfirm.typeEnum.success);
                location.href="/program/0/0/0/0"
            }else if(resp.code=="201"){
                window.wxc.xcConfirm(resp.error, window.wxc.xcConfirm.typeEnum.warning);
            }
        },
        "error": function (response) {
        }
    })
}
function reset() {
    location.href="/program/0/0/0/0"
}
$(document).keyup(function (event) {
    if (event.keyCode == 13) {
        $("#submitprogram").trigger("click");
    }
});
$("#title").click(function () {
    modeConfirm('turn_off', ["all"], 2)
});
