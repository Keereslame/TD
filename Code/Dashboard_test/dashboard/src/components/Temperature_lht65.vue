<template>
    <div class="mt-3">
        <b-card border-variant="light" header="Température de la chambre" class="text-center">
            <Temp_line_highcharts :temperature-series="temp_series"/>
        </b-card>
    </div>
</template>

<script>
    //import moment from 'moment';
    import Influx from "influx";
    import Temp_line_highcharts from "./Temp_line_highcharts";

    export default {
        name: "Temp_lht65",
        components: {
            Temp_line_highcharts
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
                let temperature_Serie1;
                let temperature_Serie2;
                let query_tempSerie1 = 'SELECT TempC_SHT FROM ttn_lht65 WHERE time > now() - 7h';
                let query_tempSerie2 = 'SELECT TempC_DS FROM ttn_lht65 WHERE time > now() - 7h';
                //console.log("Query:" + query_tempSerie1)
                Promise.all([
                    this.client.query(query_tempSerie1),
                ]).then(results => {
                    //console.log("Result")
                    //console.log(results)
                    //console.log(results[0].length)
                    temperature_Serie1 = results[0].map(a => {
                        //var date = new Date((moment(a.time).unix()) * 1000)
                        //console.log(a.time)
                        return {
                            x: a.time,//(moment(a.time).unix())*1000,
                            y: parseFloat(a.TempC_SHT)
                        };
                    });
                    Promise.all([
                        this.client.query(query_tempSerie2),
                    ]).then(results => {
                        temperature_Serie2 = results[0].map(a => {
                            // var date = new Date((moment(a.time).unix()) * 1000)
                            return {
                                x:a.time,//(moment(a.time).unix())*1000,
                                y: parseFloat(a.TempC_DS)
                            };
                        });

                        //console.log("Temperature serie 1")
                        //console.log(temperature_Serie1)
                        let finale_series = [{
                            name: 'Température du boîtier',
                            data: temperature_Serie1,
                            showNavigator: true,
                        }, {
                            name: 'Température de la sonde',
                            data: temperature_Serie2,
                            showNavigator: true,
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