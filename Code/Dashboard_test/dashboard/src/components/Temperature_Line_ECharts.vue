<template>
    <v-chart :options="temperatureLine"></v-chart>
</template>

<script>
    import ECharts from "vue-echarts";
    import "echarts/lib/chart/line";

    export default {
        components: {
            "v-chart": ECharts
        },
        props: [
            'temperatureSeries'
        ],
        data() {
            return {
                temperatureLine : {
                    tooltip: {
                        show: true,
                        trigger: 'axis',
                        axisPointer: {
                            type:'',
                            label: {
                                formatter: (params => {
                                    params = params[0];
                                    var date = new Date(params.name);
                                    return date.getDate() + '/' + (date.getMonth() + 1) + '/' + date.getFullYear() + ' : ' + params.value[1];
                                })
                            }
                        },
                    },
                    toolbox: {
                        feature: {
                            saveAsImage: {}
                        }
                    },
                    xAxis: {
                        type: 'time',
                    },
                    yAxis: [{
                        type: 'value',
                    },{
                        type: 'value',
                    }],
                    series: this.temperatureSeries,
                    legend: {
                        data:[]
                    }
                },

            }
        },
        watch: {
            temperatureSeries(newSeries){
                this.temperatureLine.series = newSeries
            }
        },
    }

</script>

<style scoped>
    .echarts{
        max-width: 100%;
        height: 400px;
    }
</style>
