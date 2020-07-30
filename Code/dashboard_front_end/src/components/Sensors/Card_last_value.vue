<template>
    <b-card-group deck>
        <b-card border-variant="light" header="Humidity" class="text-center">
            {{last_hum_lht65_sht}}
        </b-card>
        <b-card border-variant="light" header="Temperature" class="text-center">
            {{last_temp_lht65_ds}}
        </b-card>
        <b-card border-variant="light" header="Temperature" class="text-center">
            {{last_temp_lht65_sht}}
        </b-card>

        <b-card border-variant="light" header="Temperature" class="text-center">
            {{last_temp_amg8833_max}}
        </b-card>
        <b-card border-variant="light" header="Temperature" class="text-center">
            {{last_temp_amg8833_min}}
        </b-card>
    </b-card-group>
</template>

<script>
    import Influx from "influx";
    export default {
        name: "Card_last_value",
        data() {
            return {
                client: new Influx.InfluxDB({
                    host: '192.168.1.70', // maison
                    //host: '153.109.7.30',   //école
                    database: 'lowimpact_food',
                    port: 8086
                }),
                last_temp_lht65_sht: 0,
                last_temp_lht65_ds: 0,
                last_hum_lht65_sht: 0,
                last_temp_amg8833_max: 0,
                last_temp_amg8833_min: 0
            }
        },
        methods: {
            loadDataChart: function () {
                let humidity;// temp_sht, temp_ds, temp_amg_max, temp_amg_min;
                let query_hum = 'SELECT Hum_SHT FROM ttn_lht65 WHERE time > now() - 5m';
                //console.log("Query:" + query_humSerie1)
                //let query_temp_sht = 'SELECT Temp_SHT FROM ttn_lht65 WHERE time > now() -5m';
                //let query_temp_ds ='SELECT Temp_DS FROM ttn_lht65 WHERE time > now() -5m';
                //let query_temp_amg_max ='SELECT temp_max FROM amg8833 WHERE time > now() -5m';
                //let query_temp_amg_min ='SELECT temp_min FROM amg8833 WHERE time > now() -5m';
                Promise.all([
                    this.client.query(query_hum),
                ]).then(results => {
                    //console.log("Result")
                    //console.log(results)
                    //console.log(results[0].length)
                    humidity = results[0].map(a => {
                        //var date = new Date(+(moment(a.time).unix()) * 1000)
                        return {
                            y: parseFloat(a.Hum_SHT)
                        };
                    });

                    this.last_hum_lht65_sht = humidity
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

</style>