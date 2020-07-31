<template>
    <highcharts class="stock" :constructor-typ="'stockChart'" :options="stockOptions"></highcharts>
</template>

<script src="https://code.highcharts.com/modules/exporting.js"></script>
<script src="https://code.highcharts.com/modules/export-data.js"></script>
<script>
    export default {
        props: [
            'humiditySeries',
        ],
        data() {
            return {
                stockOptions : {
                    chart: {
                        high: 300,
                        zoomType: 'x'
                    },
                    xAxis:{
                        scrollbar: {
                            enable: true
                        },
                        type: 'datetime'
                    },
                    scrollbar: {
                        enable: true,
                        barBackgroundColor: 'gray',
                        barBorderRadius: 7,
                        barBorderWidth: 0,
                        buttonBackgroundColor: 'gray',
                        buttonBorderWidth: 0,
                        buttonBorderRadius: 7,
                        trackBackgroundColor: 'none',
                        trackBorderWidth: 1,
                        trackBorderRadius: 8,
                        trackBorderColor: '#CCC'
                    },
                    navigator: {
                        enabled: true
                    },
                    yAxis: {
                        title: {
                            text: 'Humidity (%)'
                        },
                        labels: {
                            format: '{value} %'
                        }
                    },
                    time: {
                        useUTC: false
                    },
                    rangeSelector: {
                        selected: 'all',
                        buttons: [{
                            type: 'hour',
                            count: 12,
                            text: '12 h',
                            //could be perhaps used to set the group by
                            //events:{
                            //  click : function(){
                            //    alert('12 h clicked')
                            //  }
                            //}
                        }, {
                            type: 'hour',
                            count: 24,
                            text: '24 h'
                        }, {
                            type: 'day',
                            count: 5,
                            text: '5 j'
                        },/* {
            type: 'month',
            count: 3,
            text: '3m'
          }, */{
                            type: 'all',
                            text: 'Tous'
                        }]
                    },
                    exporting: {
                        enabled:true,
                        buttons: {
                            exportButton: {
                                enabled: true
                            }
                        }
                    },
                    title: {
                        text: ''
                    },
                    tooltip: {
                        pointFormat: '{series.name}: <b>{point.y:.1f}%</b><br/>'
                    },
                    series: this.temperatureSeries
                    ,
                },

            }
        },
        watch: {
            humiditySeries(newSeries){
                this.stockOptions.series = newSeries
            },
        },

    }

</script>

<style scoped>

</style>
