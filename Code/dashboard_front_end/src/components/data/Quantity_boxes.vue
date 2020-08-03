<template>
    <div class="mt-3">
        <Column_graph :data-series="data_series"/>
    </div>
</template>

<script>
    import Column_graph from "../Model_graph/column_graph";
    import BatchDataService from "../../services/BatchDataService";
    export default {
        components: {Column_graph},
        data(){
            return{
                batchs: [],
                data_series: [],
            }
        },
        methods: {
            retrieveBatchs() {
                BatchDataService.getAll()
                    .then(response => {
                        this.batchs = response.data;
                        //console.log(response.data);
                        this.retrieveMonthlyBatchs()
                    })
                    .catch(e => {
                        console.log(e);
                    });
            },
            retrieveMonthlyBatchs(){
                let month = [0,0,0,0,0,0]
                let nb_box_month = [0,0,0,0,0,0];
                var day_to_ms = 8.64*Math.pow(10, 7);
                //getMonth return value between [0,11] according [January, December]
                month[0] = new Date().getMonth();
                month[1] = month[0]-1;
                month[2] = month[1]-1;
                month[3] = month[2]-1;
                month[4] = month[3]-1;
                month[5] = month[4]-1;

                for(var i in this.batchs){
                    var date_start = new Date(this.batchs[i].date_start);
                    var date_end_growth = new Date(date_start.getTime() +
                        this.batchs[i].nb_laying_day*day_to_ms +
                        this.batchs[i].humidity_delay*day_to_ms +
                        this.batchs[i].growth_day*day_to_ms);
                    let nbBox = this.batchs[i].nb_bac;
                    for(let index=date_start.getMonth(); index<=date_end_growth.getMonth(); index++)
                    {

                        //console.log(index)
                        switch(index){
                            case month[5]:
                                nb_box_month[5] = nb_box_month[5]+nbBox;
                                console.log("Add box month5")
                                break;
                            case month[4]:
                                nb_box_month[4] = nb_box_month[4]+nbBox;
                                console.log("Add box month4")
                                break;
                            case month[3]:
                                nb_box_month[3] = nb_box_month[3] + nbBox;
                                console.log("Add box month3")
                                break;
                            case month[2]:
                                nb_box_month[2] = nb_box_month[2] + nbBox;
                                console.log("Add box month2")
                                break;
                            case month[1]:
                                nb_box_month[1] = nb_box_month[1] + nbBox;
                                console.log("Add box month1")
                                break;
                            case month[0]:
                                nb_box_month[0] = nb_box_month[0] + nbBox;
                                console.log("Add box month")
                                break;
                        }
                        //console.log(nb_box_month[5], nb_box_month[4], nb_box_month[3], nb_box_month[2], nb_box_month[1], nb_box_month[0])
                    }
                }

                this.data_series = [{
                    name: "Number of boxes",
                    data: [nb_box_month[5], nb_box_month[4], nb_box_month[3], nb_box_month[2], nb_box_month[1], nb_box_month[0]]
                }]
            }
        },
        mounted() {
            this.retrieveBatchs();
        }
    }
</script>

<style scoped>

</style>