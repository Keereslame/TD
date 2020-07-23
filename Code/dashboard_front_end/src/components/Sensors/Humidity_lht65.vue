<template>
    <div class="mt-3">
        <b-card border-variant="light" header="Humidité de la chambre" class="text-center">
            <Humidity_line_highcharts :humidity-series="hum_series"/>
        </b-card>
    </div>
</template>

<script>
    //import moment from 'moment';
    import Influx from "influx";
    import Humidity_line_highcharts from "../Model_graph/Humidity_line_highcharts";

    export default {
        name: "Humidity_lht65",
        components: {
            Humidity_line_highcharts,
        },
        data() {
            return {
                client: new Influx.InfluxDB({
                    //host: '192.168.1.70', // maison
                    host: '153.109.7.30',   //école
                    database: 'lowimpact_food',
                    port:8086
                }),
                hum_series: [],
            }
        },
        methods: {
            loadDataChart: function () {
                let humidity_Serie1;
                let query_humSerie1 = 'SELECT Hum_SHT FROM ttn_lht65 WHERE time > now() - 7h';
                //console.log("Query:" + query_humSerie1)
                Promise.all([
                    this.client.query(query_humSerie1),
                ]).then(results => {
                    //console.log("Result")
                    //console.log(results)
                    //console.log(results[0].length)
                    humidity_Serie1 = results[0].map(a => {
                        //var date = new Date(+(moment(a.time).unix()) * 1000)
                        return {
                            x: a.time,
                            y: parseFloat(a.Hum_SHT)
                        };
                    });


                    //console.log("Humidity serie 1")
                    //console.log(humidity_Serie1)
                    let finale_series = {
                        name: 'Humidité du boîtier',
                        data: humidity_Serie1
                    }
                    //console.log("Serie finale")
                    //console.log(finale_series)
                    this.hum_series = finale_series
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