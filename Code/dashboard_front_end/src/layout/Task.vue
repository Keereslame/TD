<template>
    <b-container fluid>
        <!--<Navbar/>-->
        <b-row>
            <!--<b-col class="col-auto sidebar"><Sidebar/></b-col>-->
            <b-col>
                <div class="mt-3">
                    <b-card-group deck class="mb-3">
                        <b-card border-variant="light" header="Task of the day" class="text-center">
                            <b-card-group class="mb-3">
                                <b-card border-variant="light" title="Feed">
                                    <div>
                                        <h6>Growth:</h6>
                                        <b-table striped hover :items="items_tab1_1"></b-table>
                                        <h6>Reproduction:</h6>
                                        <b-table striped hover :items="items_tab1_2"></b-table>
                                    </div>
                                </b-card>
                                <b-card border-variant="light" title="Reproduction">
                                    <b-table striped hover :items="items_tab2_1"></b-table>
                                    <b-table striped hover :items="items_tab2_2"></b-table>
                                </b-card>
                                <b-card border-variant="light" title="Harvest">
                                    <div>
                                        <b-input-group class="mt-3">
                                            <b-table striped hover :items="items_tab3"></b-table>
                                        </b-input-group>
                                    </div>
                                </b-card>
                            </b-card-group>
                        </b-card>
                    </b-card-group>
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
        name: "Task",
        components: {
      //      Sidebar,
       //     Navbar,
        },
        data() {
            return {
                reproduction_feeding_today: [],
                growth_feeding_today: [],
                harvest_today: [],
                items_tab1_1: [],
                items_tab1_2: [],
                items_tab2_1: [],
                items_tab2_2: [],
                items_tab3:[]
            }
        },
        methods: {
            retrieveBatchs() {
                BatchDataService.getAll()
                    .then(response => {
                        this.batchs = response.data;
                        //console.log(response.data);
                        this.retrieveTodayBatchs();
                    })
                    .catch(e => {
                        console.log(e);
                    });
            },
            retrieveTodayBatchs() {
                this.reproduction_feeding_today = [];
                this.growth_feeding_today = [];
                this.harvest_today = [];
                var now = new Date();
                //console.log(now)
                var day_to_ms = 8.64*Math.pow(10, 7);
                for(var i in this.batchs){
                    //console.log("Batch: " + this.batchs[i].name);
                    var date_start = new Date(this.batchs[i].date_start);
                    //console.log("Date start: " + date_start);
                    var date_end_laying = new Date(date_start.getTime()+this.batchs[i].nb_laying_day*day_to_ms);
                    //console.log("Date end laying: " + date_end_laying);
                    var date_start_growth = new Date(date_end_laying.getTime()+this.batchs[i].humidity_delay*day_to_ms);
                    //console.log("Date start growth: ");
                    //console.log(new Date(date_start_growth));
                    var date_end_growth = new Date(date_start_growth.getTime() + this.batchs[i].growth_day*day_to_ms);
                    //console.log(this.batchs[i].growth_day)
                    //console.log("Date end growth: ");
                    //console.log(new Date(date_end_growth));

                    for(let index=date_start; index<date_end_laying;index = new Date(index.getTime()+this.batchs[i].reproduction_humidity_freq*day_to_ms))//index+=this.batchs[i].reproduction_humidity_freq)
                    {

                        if(index.getFullYear() == now.getFullYear() &&
                            index.getMonth() == now.getMonth() &&
                            index.getDate() == now.getDate())
                        {
                            this.reproduction_feeding_today.push(this.batchs[i])
                            console.log("Reproduction feeding date")
                        }
                    }


                    //console.log("Start growth " + new Date(date_start_growth));
                    //console.log("End growth " + new Date(date_end_growth));
                    for(let index=date_start_growth; index<date_end_growth;index = new Date(index.getTime() + this.batchs[i].growth_humidity_freq * day_to_ms))//index+=this.batchs[i].growth_humidity_freq)
                    {
                        if(date_end_growth>new Date()) {
                            //console.log("index " + new Date(index));
                            if(index.getFullYear() == now.getFullYear() &&
                                index.getMonth() == now.getMonth() &&
                                index.getDate() == now.getDate())
                            {
                                this.growth_feeding_today.push(this.batchs[i])
                                console.log("Growth feeding date")
                            }
                        }
                    }
                    //console.log(date_end_growth)
                    if(date_end_growth.getTime() == now.getFullYear() &&
                        date_end_growth.getTime() == now.getMonth() &&
                        date_end_growth.getTime() == now.getDay())
                    {
                        this.harvest_today.push(this.batchs[i])
                        console.log("Harvest date")
                    }
                }
                for(let index=0;index < this.growth_feeding_today.length; index++)
                {
                    this.items_tab1_1[index] = {Batch: '', Quantity: '', Type: ''};
                }
                for(let index=0;index < this.reproduction_feeding_today.length; index++)
                {
                    this.items_tab1_2[index] = {Batch: '', Quantity: '', Type: ''}
                }
                for(let index=0;index < this.reproduction_feeding_today.length; index++)
                {
                    this.items_tab3[index] = {Batch: ''}
                }
                //console.log(this.feeding_today)
                this.putItem()
            },
            putItem(){
                for(let index = 0; index < this.growth_feeding_today.length; index++){
                    this.items_tab1_1[index].Batch  = this.growth_feeding_today[index].name;
                    this.items_tab1_1[index].Quantity = this.growth_feeding_today[index].growth_humidity_mass;
                    this.items_tab1_1[index].Type = this.growth_feeding_today[index].growth_humidity_type;
                }
                for(let index = 0; index < this.reproduction_feeding_today.length; index++){
                    this.items_tab2_1[index].Batch  = this.reproduction_feeding_today[index].name;
                    this.items_tab2_1[index].Quantity = this.reproduction_feeding_today[index].growth_humidity_mass;
                    this.items_tab2_1[index].Type = this.reproduction_feeding_today[index].growth_humidity_type;
                }
                for(let index=0; index<this.harvest_today.length; index++){
                    this.items_tab3[index].Batch = this.harvest_today[index].name;
                }

            }
        },
        mounted() {
            this.retrieveBatchs();
        }
    }
</script>

<style scoped>
    .col-auto{
        background-color: #95ca91;
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