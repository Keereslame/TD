<template>
    <b-container fluid>
        <Navbar/>
        <b-row>
            <b-col class="col-auto sidebar"><Sidebar/></b-col>
            <b-col>
                <div class="mt-3">
                    <b-card-group deck class="mb-3">
                        <b-card border-variant="light" class="text-center">
                            <b-calendar v-model="value" locale="fr-EU"></b-calendar>                        </b-card>

                        <b-card border-variant="light" header="Task" class="text-center">
                            <b-row>
                                <p>Date: <b>{{ value }}</b></p>
                            </b-row>
                            <b-row>
                                <h4>Feeding</h4>
                            </b-row>
                            <b-row>
                                <p>Batch:</p>
                            </b-row>
                            <b-row>
                                <p>Amount:</p>
                            </b-row>
                            <b-row>
                                <h4>Harvest</h4>
                            </b-row>
                            <b-row>
                                <p>Batch:</p>
                            </b-row>
                        </b-card>
                    </b-card-group>
                </div>
            </b-col>
        </b-row>
    </b-container>
</template>

<script>
    import Navbar from "../components/Navbar";
    import Sidebar from "../components/Sidebar";

    export default {
        name: "Calendar",
        components: {
            Sidebar,
            Navbar,
        },
        data(){
            return{
                value:'',

            }
        },
        methods:{

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