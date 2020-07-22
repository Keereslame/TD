<template>
    <div>
        <b-card-group class="mt3">
            <b-card>
                <Data_graph :data-series="data_series"></Data_graph>
            </b-card>
        </b-card-group>
    </div>
</template>

<script>
    import Data_graph from "./Data_graph";
    //import Batch from '../models/Batch';
    //import Template from '../models/Template';

    export default {
        name: "Data_query",
        components: {Data_graph},
        data(){
            return{
                //batch: require('../models/Batch').BatchModel,
                data_series:[],
            }
        },
        created() {

        },
        mounted() {

        },
        methods:{

        }
    }
</script>

<style scoped>

</style>