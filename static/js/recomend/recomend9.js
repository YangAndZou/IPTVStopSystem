/*
* 模块分为两个部分，固定部分和动态加载部分
* 固定部分为header，按照视频有两种布局方式，第一种九张，第二种十一张
* 动态部分为row，分为两种加载方式:
*   1.行：随着滚动条滑动到某个位置而加载一行，数据良多，这里不适合全部返回数据
*   2.列：每行的列数是一次性加载的，因为某行对应的列数不多
*  点击下一页：每点击下一页就新增一行,数组切割方式(0,5),(1,6),(2,7),(3,8),(4,9)
*  点击上一页：每点击上一页就减一行,数组切割方式(4,9),(3,8),(2,7),(1,6),(0,5)
* */
var rowCount = 1;//动态部分默认调用一次，第一列为1
var activeRow = 0;//鼠标移动到某列会记录当前的那一列
var loadToolBarFn = function () {
    var data = ["全部", "电视", "应用", "精选", "会员", "电视剧", "电影", "少儿", "综艺", "学堂", "电竞", "游戏", "教育", "商城", "4k影院"]
    var temp = '<li><a onclick="titleTap(this)">{{ title }}</a></li>';
    var str = '';
    var total = data.length;
    for (var $index = 0; $index < data.length; $index++) {
        str += temp.replace(/{{ title }}/g, data[$index])
    }
    $("#toolbarList").append(str).width(90 * total);
    $("#toolbarList").find("a").eq(0).addClass("active");
    var width = $("#toolbarList").width();
    var listWidth = $("#toolbarList").parent().width();
    if (width < listWidth) {
        $(".toRight").hide()
    }

};
var titleTap = function (op) {
    $("#toolbarList").find("a").removeClass("active");
    $(op).addClass("active")
};

//点击上一页
var _prevTap = function (op,rowCount,data) {
    $(op).nextAll().show();//点击上一下
    var start = parseInt($(op).next().find(".box").first().attr("name"));//获取dom元素当前行的第一列
    var end = parseInt($(op).next().find(".box").last().attr("name"));//获取dom元素当前行的最后一列
    if (start > 0) { //开头为0，则是第一列
        if (parseInt($(op).attr("name")) > 0) {//该dom，name属性绑定的是点击次数，点击下一行则加1,点击上一行则减1
            //而该界面需求，为每点击一次下一页则加一列的情况下，恰好 开始列 =点击次数
            $(op).attr("name", parseInt($(op).attr("name")) - 1);//点击上一行则减1
            $(op).next().next().attr("name", parseInt($(op).attr("name")));//同时下一行的属性name的值也要保持一致
            var count = parseInt($(op).attr("name"));//重新获取点击的次数
            if (count <= 0) { //注意，如果次数为0的话，就不能点击上一页了
                $(op).hide()
            }
            _loadChangeCol(op, rowCount, count, parseInt(count + 5), data)//根据参数重新渲染该行的dom
        }
    }


};
//点击下一页
var _nextTap = function (op, rowCount,data) {
    var data=[
    {
      "src": "1.png"
    },
    {
      "src": "2.png"
    },
    {
      "src": "3.png"
    },
    {
      "src": "4.png"
    },
    {
      "src": "5.png"
    },
    {
      "src": "1.png"
    },
    {
      "src": "2.png"
    },
    {
      "src": "3.png"
    },
    {
      "src": "4.png"
    },
    {
      "src": "5.png"
    },
    {
      "src": "1.png"
    },
    {
      "src": "2.png"
    },
    {
      "src": "3.png"
    },
    {
      "src": "4.png"
    },
    {
      "src": "5.png"
    },
    {
      "src": "1.png"
    }
  ]
    $(op).prevAll().show();
    var start = parseInt($(op).prev().find(".box").first().attr("name"));//开始索引
    var end = parseInt($(op).prev().find(".box").last().attr("name")) + 1;//获取每列中的最后一个数，+1截取字符串的索引
    if (end >=data.length) {//end加了1则为数据截取的索引
        $(op).hide()
    } else {
        $(op).attr("name", parseInt($(op).attr("name")) + 1);//点击下一行则加1
        $(op).prev().prev().attr("name", parseInt($(op).attr("name")));
        var count = parseInt($(op).attr("name"));
        _loadChangeCol(op, rowCount, count, parseInt(count + 5), data)
    }


};
//点击上一页或者下一页，获取某行的数据渲染dom
var _loadChangeCol = function (op, rowCount, start, end, data) {
    // var start = 5 * count;//这里屏蔽的逻辑是每5列替换
    // var end = 5 * count + 5;
    // console.log(parseInt(start + 1), parseInt(end + 2))
    // var start =parseInt(start+1) ;
    // var end = parseInt(end+1);
    var data = data.slice(start, end);//通过调用的开始索引和结束索引来截取数据
    var str = '';
    if ($(op).attr("class") == "next") {//清空
        $(op).prev().empty();
    } else {
        $(op).next().empty();
    }
    var templ = '<li class="box" name="{{colCount}}" onmouseover="boxmouse(this,{{rowCount}},{{colCount}})"><div class="pic"><img src="/static/image/{{src}}" /><p>图文信息图文信息图文信息图文信息图文信息图文信息</p><div class="mask"><button onclick="boxTap(this,{{rowCount}},{{colCount}})"><i class="glyphicon glyphicon-off"></i></button></div></div></li>';
    for (var $index = 0; $index < data.length; $index++) {
        str += templ
            .replace(/{{src}}/g, data[$index].src)
            .replace(/{{colCount}}/g, start + $index)
            .replace(/{{rowCount}}/g, rowCount)
    }
    if ($(op).attr("class") == "next") {//dom绑定
        $(op).prev().append(str);
    } else {
        $(op).next().append(str);
    }
    /*if (data.length < 5) {
        $(op).hide()
    }*///每行没有五个数据则隐藏，每五个加载会有该情况
};

//点击关停函数
var boxTap = function (op, rowCount, colCount) {
    window.wxc.xcConfirm("确定要关停该频道吗？", window.wxc.xcConfirm.typeEnum.warning, {
        onOk: function (v) {
            console.log(op, rowCount, colCount)
        }
    });
};
//鼠标选中函数
var boxmouse = function (op, rowCount, colCount) {
    $(".box").removeClass("active");
    $(op).addClass("active");
    if (activeRow == rowCount) {
        $(op).parents(".row").prev().find(".colActive").text(parseInt(colCount) + 1);
    } else {
        $(".row").prev().find(".colActive").text(1);
    }
    activeRow = rowCount
};
//每行dom加载，参数 数据，数据开始和结束索引
var _loadImage = function (data, start, end) {
    /*
    * 渲染row通过name属性绑定了对应的行数、列数和点击次数
    *
    * */
    var str = "";
    var count = 0;
    var dataLength = data.length;
    var rowLoadData = data.slice(start, end);
    var title = "电视剧";
    var templ = '<li class="box" name="{{colCount}}"  onmouseover="boxmouse(this,{{rowCount}},{{colCount}})"><div class="pic"><img src="/static/image/{{src}}" /><p>图文信息图文信息图文信息图文信息图文信息图文信息</p><div class="mask"><button onclick="boxTap(this,{{rowCount}},{{colCount}})"><i class="glyphicon glyphicon-off"></i></button></div></div> </li>';
    for (var i = 0; i < rowLoadData.length; i++) {
        str += templ
            .replace(/{{src}}/g, data[i].src)
            .replace(/{{rowCount}}/g, rowCount)
            .replace(/{{colCount}}/g, i);
    }//boxdom渲染，box的name属性表示该行某列
    //上一页dom渲染，的name属性表示点击的次数，点击下一行则加1,点击上一行则减1
    var prevDom = '<div class="prev" name="{{count}}"  onclick="_loadChangeColResponse(this,{{rowCount}},{{_prevTap}})"><i class="glyphicon glyphicon-chevron-left"></i></div><ul class="boxrow" name="{{rowCount}}">';

    prevDom = prevDom
        .replace(/{{count}}/g, count)
        .replace(/{{rowCount}}/g, rowCount)
        .replace(/{{_prevTap}}/g,0);
    //下一页dom渲染，的name属性表示点击的次数，点击下一行则加1,点击上一行则减1
    var nextDom = '</ul><div class="next" name="{{count}}" onclick="_loadChangeColResponse(this,{{rowCount}},{{_nextTap}})"><i class="glyphicon glyphicon-chevron-right"></i></div> ';

    nextDom = nextDom
        .replace(/{{count}}/g, count)
        .replace(/{{rowCount}}/g, rowCount)
        .replace(/{{_nextTap}}/g,1);
    //该行的标题，总列数，选中某列
    var titleTempl = '<div class="rowTitle">{{title}}&nbsp;<span class="colActive">1</span>/{{colTotal}}</div>';

    titleTempl = titleTempl
        .replace(/{{title}}/g, title)
        .replace(/{{colTotal}}/g, data.length);
    //渲染该行
    str = titleTempl + '<div class="row" style="opacity:0;filter:alpha(opacity=0);">' + prevDom + str + nextDom + '</div>';
    $(str).appendTo($("#cardCxt"));
    if (dataLength <= 5) {
        $("#cardCxt").find(".row").last().find(".next").hide()
    }
    //每调用一次该行就加1
    rowCount++
};
//渲染头部固定部分
var _loadHeader1 = function (data) {
    var str = '';
    for (var $index = 0; $index < 9; $index++) {
        var $status = 1;
        if ($index == 1) {
            str = '<div style="float:left;display:inline-block">' + str
        } else if ($index == 5) {
            str = str + "</div>"
        }
        var $statusBox = '';
        if ($status == 1) {
            $statusBox = '<img src = "/static/image/1.png"> <div class="mask"> <h5>标题页</h5> <div class="recomendBtn"><button class="closed"><i class="glyphicon glyphicon-off"></i></button></div> </div>';
        } else {
            $statusBox = '<img src = "/static/image/1.png"> <div class="mask"> <h5>标题页</h5> <div class="recomendBtn"><button class="open" ><i class="glyphicon glyphicon-open"></i></button></div> </div>';
        }
        str += '<div class = "box" onmouseover="boxmouse(this,0,' + ($index + 1) + ')">' + $statusBox + '</div>'
    }
    $("#header").append('<div class="row"><div class="boxrow" name="0"> ' + str + '</div></div>');
    //该函数，设置了每个box宽高，按照比例进行计算
    onSize()
};
var _loadChangeColResponse=function(op,rowCount,tap){
     $.ajax({
        url: "static\\js\\recomend\\recomend9_data.json",
        type: "get",
        /*data: {
           row:rowCount,
           csrfmiddlewaretoken: token
        },*/
        dataType: 'json',
        "success": function (resp) {
            if(tap==undefined){
                  _loadImage(resp.data, 0, 5);
             }else{
                (tap==0)? _prevTap(op,rowCount,resp.data):_nextTap(op,rowCount,resp.data)
            }
         },
        "error": function (response) {
        }
    });
};
$(function () {
    $(".itemTabContent").find("li").eq(4).addClass('active');
    var $window = $(window),
        pluginName = 'waterfall',
        defaults = {
            itemClass: "waterfall-item", // the brick element class
            resizeable: false, // trigger positionAll() when browser window is resized
            isFadeIn: true, // fadeIn effect on loading
            ajaxCallback: null // callback when ajax loaded, two parameters ( success, end )
        };

    function Waterfall(element, options) {
        this.$element = $(element);
        this.options = $.extend(true, {}, defaults, options);
        this.ajaxLoading = false;
        this._loadRows();
        this._init();

    }

    Waterfall.prototype = {
        constructor: Waterfall,
        _init: function () {
            var $this = this;
            $window.on("load", function () {
                $this._positionAll();
            });
            if (this.options.resizeable) {
                $window.on("resize", function () {
                    $this._positionAll();
                });
            }
            this._doScroll();
        },
        _loadRows: function () {
            var $this = this;
            loadToolBarFn();
            _loadHeader1();
            _loadChangeColResponse()

        },
        _positionAll: function () {
            var $this = this,
                $item = $(this.options.itemClass);
            $item.each(function (index) {
                if ($this.options.isFadeIn) {
                    $(this).animate({"opacity": 1}, 500);
                }
            });
        },
        _doScroll: function () {
            var $this = this,
                scrollTimer;
            $window.on("scroll", function () {
                if (scrollTimer) {
                    clearTimeout(scrollTimer);
                }
                scrollTimer = setTimeout(function () {
                    var $last = $($this.options.itemClass).last(),
                        scrollTop = $window.scrollTop() + $window.height();
                    if (!$this.ajaxLoading && scrollTop > $last.offset().top + $last.outerHeight() / 2) {
                        $this.ajaxLoading = true;
                        $this.options.ajaxCallback && $this.options.ajaxCallback(
                            function () {
                              _loadChangeColResponse()
                            },
                            function () {
                                $this._positionAll();
                            },
                            function () {
                                $this.ajaxLoading = false;
                            }
                        );
                    }
                }, 100);
            });
        }

    };
    $.fn[pluginName] = function (options) {
        new Waterfall(this, options)
    };

    $("#cardCxt").waterfall({
        itemClass: ".row",
        resizeable: true,
        ajaxCallback: function (loadImage, success, end) {
            loadImage();
            success();
            end();
        }
    });
    var left = 0;
    $(".toRight").click(function () {
        $(".toLeft").show();
        $(".toRight").show();
        var listDom = $("#toolbarList");
        var toLeft = listDom.css("marginLeft");
        var toLeftAr = -parseFloat(toLeft.substring(0, toLeft.length - 2));
        var listW = listDom.width();
        var tabBoxWidth = listDom.parent().width();
        var sum = parseFloat(toLeftAr + tabBoxWidth);
        var leftW = 270;
        if (sum <= listW) {
            if (sum + leftW >= listW) {
                $(this).hide()
            }
            left = left - leftW;
            $(this).prev().find(".toolbarList").animate({
                marginLeft: left + "px"
            })
        }
    });
    $(".toLeft").click(function () {
        $(".toLeft").show();
        $(".toRight").show();
        var listDom = $("#toolbarList");
        var toLeft = listDom.css("marginLeft");
        var toLeftAr = parseFloat(toLeft.substring(0, toLeft.length - 2));
        var leftW = 270;
        if (toLeftAr < 0) {
            if (toLeftAr + leftW >= 0) {
                $(this).hide()
            }
            left = left + leftW;
            $(this).next().find(".toolbarList").animate({
                marginLeft: left
            })
        }

    });
    $(document).keyup(function (event) {
        var row = parseInt($(".box.active").parent(".boxrow").attr("name"));
        var col = parseInt($(".box.active").attr("name"));
        if (event.keyCode == 37) {
            if (col != undefined) {
                boxmouse($($(".row")[row]).find(".box")[col - 1], row, col)

            }
        }
        if (event.keyCode == 38) {
            if (row != undefined) {
                boxmouse($($(".row")[row - 1]).find(".box")[col], row, col)
            }
        }
        if (event.keyCode == 39) {
            if (col != undefined) {
                boxmouse($($(".row")[row]).find(".box")[col + 1], row, col)
            }
        }
        if (event.keyCode == 40) {
            if (row != undefined) {
                boxmouse($($(".row")[row + 1]).find(".box")[col], row, col)
            }
        }
    });
});
