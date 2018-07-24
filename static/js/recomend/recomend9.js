var rowCount = 0;
var data = {
    "data": [
        {"src": "1.png"}, {"src": "2.png"}, {"src": "3.png"}, {"src": "4.png"}, {"src": "5.png"}, {"src": "1.png"}, {"src": "2.png"}, {"src": "3.png"},
        {"src": "4.png"}, {"src": "5.png"}, {"src": "1.png"}, {"src": "2.png"}, {"src": "3.png"}, {"src": "4.png"}, {"src": "5.png"}, {"src": "1.png"}
    ]
};
var _prevTap = function (op, rowCount, count) {
    $(op).nextAll().show();
    var data = {
        "data": [
            {"src": "1.png"}, {"src": "2.png"}, {"src": "3.png"}, {"src": "4.png"}, {"src": "5.png"}, {"src": "1.png"}, {"src": "2.png"}, {"src": "3.png"},
            {"src": "4.png"}, {"src": "5.png"}, {"src": "1.png"}, {"src": "2.png"}, {"src": "3.png"}, {"src": "4.png"}, {"src": "5.png"}, {"src": "1.png"}
        ]
    };
    if (parseInt($(op).attr("name")) > 0) {
        $(op).attr("name", parseInt($(op).attr("name")) - 1);
        $(op).next().next().attr("name", parseInt($(op).attr("name")));
        var count = parseInt($(op).attr("name"));
        loadLeave(op, rowCount, count, data)
    } else {
        $(op).hide()
    }


};
var _nextTap = function (op, rowCount) {
    $(op).prevAll().show();
    var data = {
        "data": [
            {"src": "1.png"}, {"src": "2.png"}, {"src": "3.png"}, {"src": "4.png"}, {"src": "5.png"}, {"src": "1.png"}, {"src": "2.png"}, {"src": "3.png"},
            {"src": "4.png"}, {"src": "5.png"}, {"src": "1.png"}, {"src": "2.png"}, {"src": "3.png"}, {"src": "4.png"}, {"src": "5.png"}, {"src": "1.png"}
        ]
    };
    $(op).attr("name", parseInt($(op).attr("name")) + 1);
    $(op).prev().prev().attr("name", parseInt($(op).attr("name")));
    var count = parseInt($(op).attr("name"));
    loadLeave(op, rowCount, count, data)


};
var loadLeave = function (op, rowCount, count, data) {

    var start = 5 * count;
    var end = 5 * count + 5;
    var data = data.data.slice(start, end);
    var str = '';
    if ($(op).attr("class") == "next") {
        $(op).prev().empty();
    } else {
        $(op).next().empty();
    }
    var templ = '<li class="box" name="{{title}}" ><div class="pic"><img src="/static/image/{{src}}" /><p>图文信息图文信息图文信息图文信息图文信息图文信息</p><div class="mask"><button onclick="boxTap(this,{{rowCount}},{{colCount}})"><i class="glyphicon glyphicon-off"></i></button></div></div></li>';
    for (var $index = 0; $index < data.length; $index++) {
        str += templ
            .replace("{{src}}", data[$index].src)
            .replace("{{title}}", $index + count * 5)
            .replace("{{rowCount}}", rowCount)
            .replace("{{colCount}}", $index + count * 5);
    }
    if ($(op).attr("class") == "next") {
        $(op).prev().append(str);
    } else {
        $(op).next().append(str);
    }
    if (data.length < 5) {
        $(op).hide()
    }
};
var boxTap = function (op, rowCount, colCount) {
    window.wxc.xcConfirm("确定要关停该频道吗？", window.wxc.xcConfirm.typeEnum.warning, {
        onOk: function (v) {
               console.log(op, rowCount, colCount)
        }
    });

};
var _loadImage = function (data, start, end) {
    var str = "";
    var count = 0;
    var rowLoadData = data.data.slice(start, end);
    var templ = '<li class="box" name="{{title}}"  ><div class="pic"><img src="/static/image/{{src}}" /><p>图文信息图文信息图文信息图文信息图文信息图文信息</p><div class="mask"><button onclick="boxTap(this,{{rowCount}},{{colCount}})"><i class="glyphicon glyphicon-off"></i></button></div></div> </li>';
    for (var i = 0; i < rowLoadData.length; i++) {
        str += templ
            .replace("{{src}}", data.data[i].src)
            .replace("{{title}}", i)
            .replace("{{rowCount}}", rowCount)
            .replace("{{colCount}}", i);
    }
    var left = '<div class="prev" name="' + count + '" id="prev' + rowCount + '" onclick="_prevTap(this,' + rowCount + ' )"><i class="glyphicon glyphicon-chevron-left"></i></div><ul class="boxrow">';
    var right = '</ul><div class="next" name="' + count + '" id="next' + rowCount + '" onclick="_nextTap(this,' + rowCount + ')"><i class="glyphicon glyphicon-chevron-right"></i></div> ';
    str = '<div class="row" style="opacity:0;filter:alpha(opacity=0);">' + left + str + right + '</div>';
    $(str).appendTo($("#div1"));
    rowCount++
}
$(function () {

    var $window = $(window),
        pluginName = 'waterfall',
        defaults = {
            itemClass: "waterfall-item", // the brick element class
            resizeable: false, // trigger positionAll() when browser window is resized
            isFadeIn: true, // fadeIn effect on loading
            ajaxCallback: null // callback when ajax loaded, two parameters ( success, end )
        };

    function Waterfall(element, options, aa) {
        this.$element = $(element);
        this.options = $.extend(true, {}, defaults, options);
        this.ajaxLoading = false;
        this._loadRows();
        this._init();

    }

    Waterfall.prototype = {
        constructor: Waterfall,
        _prevTap: function (rowCount) {
            console.log(rowCount)
        },
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
            _loadImage(data, 0, 5);
            _loadImage(data, 0, 5);
            _loadImage(data, 0, 5);
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
                                _loadImage(data, 0, 5);
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

    $("#div1").waterfall({
        itemClass: ".row",
        resizeable: true,
        ajaxCallback: function (loadImage, success, end) {
            loadImage();
            success();
            end();
        }
    });

})
