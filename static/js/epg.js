$(".itemTabContent").find("li").eq(0).addClass('active')
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
                text: '操作日志',
                className: 'btn btn-sm btn-warning',
                action: function (e, dt, node, config) {
                    location.href="/epg_logs"
                }
            }
        ],
       /* "drawCallback" : function(settings) {
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
        },*/

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
    var systemName=0;
    var routerIp=0;
    var routerGroup=0;
    $("#system_name").val()==''?systemName=0:systemName=$("#system_name").val();
    $("#router_ip").val()==''?routerIp=0:routerIp=$("#router_ip").val();
    $("#router_group").val()==''?routerGroup=0:routerGroup=$("#router_group").val();
    var url='/epg/'+systemName+"/"+routerIp+"/"+routerGroup;
    location.href=url
}
$(document).keyup(function(event){
    if(event.keyCode ==13){
        $("#submitEpg").trigger("click");
    }
});
