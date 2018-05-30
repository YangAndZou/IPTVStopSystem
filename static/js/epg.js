$(".itemTabContent").find("li").eq(0).addClass('active')
alert("gyt")
var oTable=null;
$(function(){
    initTable();
});
var selectList=[];
var initTable = function () {
    if (oTable != null) {
        oTable.fnClearTable(0);
        oTable.fnDraw(); //重新加载数据
        oTable.fnDestroy();
    }
    oTable = $('#dataTableList').dataTable({
        "aLengthMenu": [10,20, 50, 100], //更改显示记录数选项
        "bProcessing": true,
        "bJQueryUI": false,
        "bFilter": false,
        "bLengthChange": true,
        "bSort": false,
        "bStateSave": false,
        //"bServerSide": true,
        "iDisplayStart": 0,
        "iDisplayLength":10,
        "paging": true,
        "bScrollCollapse": true,
        "bAutoWidth": false,
        "infoCallback":function (oSettings) {
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
                className: 'btn btn-sm btn-danger',
                action: function (e, dt, node, config) {
                    turnFn('turn_off',selectList,1)
                }
            },
            {
                text: '开启',
                className: 'btn btn-sm btn-success',
                action: function (e, dt, node, config) {
                    turnFn('turn_on',selectList,1)
                }
            },
            {
                text: '操作日志',
                className: 'btn btn-sm btn-warning',
                action: function (e, dt, node, config) {
                    location.href="/program_logs"
                }
            }
        ],
        "drawCallback" : function(settings) {
            var ischeckAll=$("#all_checked").prop('checked');
            $(":checkbox").prop("checked",ischeckAll);
            for(var index=0;index<$(settings.nTBody).find("tr").length;index++){
                if(selectList.length>0&&selectList[0]!="all"){
                    for(var i=0;i<selectList.length;i++){
                        var dom=$($(settings.nTBody).find("tr")[index]).find("td");
                        var text=dom.parents('tr').find('td').eq(4).text();
                        var data=selectList[i];
                        if(text==data){
                            dom.eq(0).find(":checkbox").prop("checked",true);
                        }
                    }
                }
            }
        },

    });

    $('#dataTableList_wrapper').on("change", ".icheckbox_all", function() {
        //选择全选复选框按钮
        var ischeckAll=$(this).prop('checked');
        $(":checkbox").prop("checked",ischeckAll);
        if(ischeckAll){
            selectList=["all"]
        }else{
            selectList=[]
        }
    });
    $('#dataTableList_wrapper').on("change", ".icheckbox_minimal", function() {
        //选择复选框按钮事件
        var ischeck=$(this).prop('checked');
        if(ischeck){
            selectList.push($(this).parents('tr').find('td').eq(4).text())
        }else{
            for(var index=0;index<selectList.length;index++){
                var filed=$(this).parents('tr').find('td').eq(4).text();
                if(selectList[index]==filed){
                    selectList.splice(index,1)
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
function sumbitQuery(){
    var programName=0;
    var programIp=0;
    var status=0;
    $("#program_name").val()==''?programName=0:programName=$("#program_name").val();
    $("#program_ip").val()==''?programIp=0:programIp=$("#program_ip").val();
    $("#status").val()==''?status=0:status=$("#status").val();
    var url='/'+programName+"/"+programIp+"/"+status;
    location.href=url
}
function turnFn(turn,list,type) {
    var List=[];
    if(type==0){
        List.push(list)
    }else{
        List=list;
    }
    var formData = new FormData();
    formData.append("mode",turn);
    formData.append("program_ips",JSON.stringify(List));
    formData.append("csrfmiddlewaretoken",token);
    console.log(List)
    $.ajax({
        url: "/program_change",
        type: "Post",
        data:{
            mode:turn,
            program_ips:List,
            csrfmiddlewaretoken:token
        },
        dataType:'json',
        /* processData: false,
         contentType: false,*/
        "success": function (resp) {
            location.reload()
        },
        "error": function (response) {}
    })
}

$(document).keyup(function(event){
    var active=0;
    var panel=$('#myTabContent').find(".tab-pane");
    panel.each(function (index,obj) {
        if($(obj).hasClass('active')){
            active=index;
        }
    });

    if(event.keyCode ==13){
        if(active==0){
            $("#submitprogram").trigger("click");
        }else{
            $("#submitprogram").trigger("click");
        }

    }
});
