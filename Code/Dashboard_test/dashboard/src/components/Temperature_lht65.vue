<template>
    <div class="mt-3">
            <b-card border-variant="light" header="Température de la chambre" class="text-center">
                <Temperature_Line_ECharts :temperature-series="temp_series"/>
            </b-card>
    </div>
</template>

<script>
    import Temperature_Line_ECharts from "../components/Temperature_Line_ECharts";
    import moment from 'moment';
    import Influx from "influx";

    export default {
        name: "Temperature_lht65",
        components: {
            Temperature_Line_ECharts
        },
        data() {
            return {
                client: new Influx.InfluxDB({
                    host: 'localhost',
                    database: 'ttn_lowimpact_food',
                    port:8086
                }),
                temp_series: [],
            }
        },
        methods: {
            loadDataChart: function () {
                let temperature_Serie1;
                let temperature_Serie2;
                let query_tempSerie1 = 'SELECT TempC_SHT FROM ttn_lht65 '; //WHERE time > now() - 7d';
                let query_tempSerie2 = 'SELECT TempC_DS FROM ttn_lht65';// AND time > now() - 7d';
                //console.log("Query:" + query_tempSerie1)
                Promise.all([
                    this.client.query(query_tempSerie1),
                ]).then(results => {
                    //console.log("Result")
                    //console.log(results)
                    //console.log(results[0].length)
                    temperature_Serie1 = results[0].map(a => {
                        var date = new Date(+(moment(a.time).unix()) * 1000)
                        return {
                            name: date.toString(),
                            value: [
                                [date.getFullYear(), date.getMonth(), date.getDate()].join('/'),
                                a.TempC_SHT
                            ]
                        };
                    });
                    Promise.all([
                        this.client.query(query_tempSerie2),
                    ]).then(results => {
                        temperature_Serie2 = results[0].map(a => {
                            var date = new Date(+(moment(a.time).unix()) * 1000)
                            return {
                                name: date.toString(),
                                value: [
                                    [date.getFullYear(), date.getMonth(), date.getDate()].join('/'),
                                    a.TempC_DS
                                ]
                            };
                        });

                        //console.log("Temperature serie 1")
                        //console.log(temperature_Serie1)
                        let finale_series = [{
                            name: 'Température du boîtier',
                            type: 'line',
                            data: temperature_Serie1
                        }, {
                            name: 'Température de la sonde',
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
        mounted() {
            this.loadDataChart()
        }
    }
</script>

<style scoped>
    .card-header{
        background-color: lightcoral;
        text-align: left;
    }

</style>