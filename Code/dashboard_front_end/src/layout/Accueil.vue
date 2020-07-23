<template>
    <b-container fluid>
        <!--<Navbar/>-->
        <b-row>
            <!--<b-col class="col-auto sidebar"><Sidebar/></b-col>-->
            <b-col>
                <div class="mt-3">
                    <b-card-group deck class="mb-3">
                        <b-card border-variant="light" header="Today" class="text-center">

                        </b-card>

                        <b-card border-variant="light" header="Stock" class="text-center">
                            <b-card-group class="mb-3">
                                <b-card border-variant="light" header="Drèches"></b-card>
                                <b-card border-variant="light" header="Carottes"></b-card>
                                <b-card border-variant="light" header="Fruits"></b-card>
                            </b-card-group>                        </b-card>
                    </b-card-group>
                </div>
                <div>
                    <b-card border-variant="light">
                        <template v-slot:header>
                            <b-nav card-header tabs>
                                <b-nav-item>Quantité de vers</b-nav-item>
                                <b-nav-item>Nombre de bacs</b-nav-item>
                                <b-nav-item>Feed / Substrat</b-nav-item>
                                <b-nav-item>Stock de vers</b-nav-item>
                            </b-nav>
                        </template>
                    </b-card>
                </div>
            </b-col>
        </b-row>
    </b-container>
</template>
<script>
    //import Navbar from "../components/Navbar";
    //import Sidebar from "../components/Sidebar";
    import BatchDataService from "../services/BatchDataService";

    export default {
        name: "Accueil",
        components: {
            //Sidebar,
            //Navbar,
        },
        data() {
            return {
                batchs: [],
                feeding_today: [],
                currentBatch: null,
                currentIndex: -1,
                name: ""
            };
        },
        methods: {
            retrieveBatchs() {
                BatchDataService.getAll()
                    .then(response => {
                        this.batchs = response.data;
                        //console.log(response.data);
                        this.retrieveTodayBatchs()
                    })
                    .catch(e => {
                        console.log(e);
                    });
            },
            retrieveTodayBatchs() {
                var now = new Date().getTime();
                var day_to_ms = 8.64*Math.pow(10, 7);
                console.log(new Date(now));
                for(var i in this.batchs){
                    //console.log("Batch: " + this.batchs[i].name);
                    var date_start = new Date(this.batchs[i].date_start);
                    //console.log("Date start: " + date_start);
                    var date_end_laying = new Date(date_start.getTime()+this.batchs[i].nb_laying_day*day_to_ms);
                    //console.log("Date end laying: " + date_end_laying);
                    var date_start_growth = date_end_laying;
                    //console.log("Date start growth: ");
                    //console.log(new Date(date_start_growth));
                    //var date_end_growth = new Date(date_start_growth.getTime() + this.batchs[i].growth_day*day_to_ms);
                    //console.log(this.batchs[i].growth_day)
                    //console.log("Date end growth: ");
                    //console.log(new Date(date_end_growth));
                    if(date_end_laying > now)
                    {
                        for(let index=date_start; index<date_end_laying;index+=this.batchs[i].reproduction_humidity_freq)
                        {
                            //console.log(index.getTime());
                            if(index.getTime() == now)
                            {
                                this.feeding_today.push(this.batchs[i])
                            }
                        }
                    }
                    else if(date_start_growth < now)
                    {
                        //console.log("Start growth " + new Date(date_start_growth));
                        //console.log("End growth " + new Date(date_end_growth));
                        for(let index=date_start_growth.getTime(); index<now;index+=this.batchs[i].growth_humidity_freq*day_to_ms)
                        {
                            console.log("index " + new Date(index));
                            if(index == now)
                            {
                                this.feeding_today.push(this.batchs[i])
                            }
                        }
                    }
                }
                console.log(this.feeding_today)
            }

        },
        mounted() {
            this.retrieveBatchs();
        }
    }
</script>

<style scoped>
    .col-auto{
        background-color: #96d2d4;
        padding-right: 0px;
    }
    .card-header{
        background-color: lightcoral;
        text-align: left;
    }
    .container-fluid{
        padding-right: 0px;
        padding-left: 0px;
    }
    .nav-link{
        color: #2c3e50;
    }

</style>