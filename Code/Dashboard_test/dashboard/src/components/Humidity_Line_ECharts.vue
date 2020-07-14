<template>
    <v-chart :options="humidityLine"></v-chart>
</template>

<script>
    import ECharts from "vue-echarts";
    import "echarts/lib/chart/line";

    export default {
        components: {
            "v-chart": ECharts
        },
        props: [
            'humiditySeries',
        ],
        data() {

            return {
                humidityLine : {
                    tooltip: {
                        trigger: 'axis',
                        formatter: (params => {
                            params = params[0];
                            var date = new Date(params.name);
                            return date.getDate() + '/' + (date.getMonth() + 1) + '/' + date.getFullYear() + ' : ' + params.value[1];
                        }),
                        axisPointer: {
                            animation: false
                        }
                    },
                    xAxis: {
                        type: 'time',
                    },
                    yAxis: {
                        type: 'value',
                    },
                    series: this.humiditySeries,
                    legend: {
                        data:[]
                    }
                },
            }
        },
        watch: {
            humiditySeries(newSeries){
                this.humidityLine.series = newSeries
            },
        },

    }

</script>

<style scoped>
    .echarts{
        max-width: 100%;
        height: 400px;
    }
</style>
