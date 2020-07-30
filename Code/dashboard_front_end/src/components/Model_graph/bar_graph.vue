<template>
    <highcharts class="stock" :constructor-typ="'stockChart'" :options="stockOptions"></highcharts>
</template>

<script>
    export default {
        name: "bar_graph",
        props:[
            'dataSeries'
        ],
        data(){
            return{
                stockOptions:{
                    chart: {
                        alignTicks: false
                    },

                    rangeSelector: {
                        selected: 1
                    },

                    /*title: {
                        text: ''
                    },*/

                    series: [{
                        type: 'column',
                        name: 'AAPL Stock Volume',
                        data: this.dataSeries,
                        dataGrouping: {
                            units: [[
                                'week', // unit name
                                [1] // allowed multiples
                            ], [
                                'month',
                                [1, 2, 3, 4, 6]
                            ]]
                        }
                    }]
                }
            }
        },
        watch:{
            dataSeries(newSeries){
                this.stockOptions.series = newSeries
    }
        }
    }
</script>

<style scoped>

</style>