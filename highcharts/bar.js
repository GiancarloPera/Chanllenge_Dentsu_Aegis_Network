document.addEventListener('DOMContentLoaded', function () {
    var options = {
        chart: {
            type: 'spline'
        },
        series: [{}]
    };
    Highcharts.ajax({  
        url: './Data/json_data_for_charts/data.json',  
        success: function(data) {
            options.series[0].data = data;
            Highcharts.Chart('container', options);
        }  
    });
});
