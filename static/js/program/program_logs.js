var oTable=null;
$(".itemTabContent").find("li").eq(2).addClass('active');
$(function(){
    initTable();
    $(".back").click(function () {
        location.href="/program/0/0/0/0/0"
    })
});
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
            'colvis'
        ]

    });
};


