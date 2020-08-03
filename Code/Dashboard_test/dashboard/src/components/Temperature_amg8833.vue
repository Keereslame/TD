<template>
    <div class="mt-3">
        <b-card border-variant="light" header="Température des bacs" class="text-center">
            <Temp_line_highcharts_offset :temperature-series="temp_series"/>
        </b-card>
    </div>
</template>
<script>
    //  import moment from 'moment';
    import Influx from "influx";
    import Temp_line_highcharts_offset from "./Temp_line_HighCharts_offset";

    export default {
        name: "Temperature_amg883",
        components: {
            Temp_line_highcharts_offset
        },
        data() {
            return {
                client: new Influx.InfluxDB({
                    host: '192.168.1.70', // maison
                    //host: '153.109.7.30',   //école
                    database: 'lowimpact_food',
                    port:8086
                }),
                temp_series: [],
            }
        },
        methods: {
            loadDataChart: function () {
                //console.log("update temperature box charts")
                let temperature_Serie1;
                let temperature_Serie2;
                let query_tempSerie1 = 'SELECT temp_max FROM amg8833 WHERE time > now() - 7h';
                let query_tempSerie2 = 'SELECT temp_min FROM amg8833 WHERE time > now() - 7h';
                //console.log("Query:" + query_tempSerie1)
                Promise.all([
                    this.client.query(query_tempSerie1),
                ]).then(results => {
                    //console.log("Result")
                    //console.log(results)
                    //console.log(results[0].length)
                    temperature_Serie1 = results[0].map(a => {
                        //console.log(a.time)
                        //var date = new Date(+(moment(a.time).unix()) * 1000)
                        return {
                            x:  a.time,//(moment(a.time).unix())*1000,
                            y: parseFloat(a.temp_max)
                        };
                    });
                    Promise.all([
                        this.client.query(query_tempSerie2),
                    ]).then(results => {
                        temperature_Serie2 = results[0].map(a => {
                            //var date = new Date(+(moment(a.time).unix()) * 1000)
                            return {
                                x: a.time-7200,//(moment(a.time).unix())*1000,
                                y: parseFloat(a.temp_min)
                            };
                        });

                        //console.log("Temperature serie 1")
                        //console.log(temperature_Serie1)
                        let finale_series = [{
                            name: 'Température maximal des bacs',
                            type: 'line',
                            data: temperature_Serie1
                        }, {
                            name: 'Température minimal des bacs',
                            type: 'line',
                            data: temperature_Serie2
                        }]
                        //console.log("Serie finale")
                        //console.log(finale_series)
                        this.temp_series = finale_series
                    }).catch(error => console.log(error))
                }).catch(error => console.log(error))
            }
        },
        created() {
            this.loadDataChart()
        },
        mounted() {
            setInterval(function(){
                this.loadDataChart()
            }.bind(this), 300000) //refresh query toutes les 5min
        }
    }
</script>

<style scoped>
    .card-header{
        background-color: lightcoral;
        text-align: left;
    }

</style>