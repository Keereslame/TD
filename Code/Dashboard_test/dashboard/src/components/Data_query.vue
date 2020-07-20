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
    //import mongoose from "../../node_modules/mongoose"

    export default {
        name: "Data_query",
        components: {Data_graph},
        data(){

            return{

                data_series:[]
            }
        },
        created() {
            const mongoose = require("mongoose");
            mongoose.connect('mongodb://localhost/test', {useNewUrlParser: true});
            const db = mongoose.connection;
            db.on('error', console.error.bind(console, 'connection error:'));
            db.once('open', function() {
                console.log("we're connected!");
            });
        },
        methods:{

        }
    }
</script>

<style scoped>

</style>