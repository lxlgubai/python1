$(
    function () {
        var chart = echarts.init(document.getElementById('bar'), 'pink', {renderer: 'canvas'});
        $.ajax({
            type: "GET",
            url: "http://127.0.0.1:5000/barChart",
            dataType: 'json',
            success: function (result) {
                chart.setOption(result);
            }
        });
    }
)
$(
    function () {
        var chart = echarts.init(document.getElementById('bar1'), 'pink', {renderer: 'canvas'});
        $.ajax({
            type: "GET",
            url: "http://127.0.0.1:5000/barChart1",
            dataType: 'json',
            success: function (result) {
                chart.setOption(result);
            }
        });
    }
)
$(
    function () {
        var chart = echarts.init(document.getElementById('bar2'), 'pink', {renderer: 'canvas'});
        $.ajax({
            type: "GET",
            url: "http://127.0.0.1:5000/barChart2",
            dataType: 'json',
            success: function (result) {
                chart.setOption(result);
            }
        });
    }
)
$(
    function () {
        var chart = echarts.init(document.getElementById('bar3'), 'pink', {renderer: 'canvas'});
        $.ajax({
            type: "GET",
            url: "http://127.0.0.1:5000/barChart3",
            dataType: 'json',
            success: function (result) {
                chart.setOption(result);
            }
        });
    }
)
$(
    function () {
        var chart = echarts.init(document.getElementById('bar4'), 'pink', {renderer: 'canvas'});
        $.ajax({
            type: "GET",
            url: "http://127.0.0.1:5000/barChart4",
            dataType: 'json',
            success: function (result) {
                chart.setOption(result);
            }
        });
    }
)