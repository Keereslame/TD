<template>
    <b-container fluid>
        <!--<Navbar/>-->
        <b-row>
            <!--<b-col class="col-auto sidebar"><Sidebar/></b-col>-->
            <b-col>
                <div class="mt-3">
                    <b-card-group deck class="mb-3">
                        <b-card border-variant="light" header="Stock" class="text-center">
                            <b-row id="date">
                                <div>
                                    <b-form-datepicker
                                            id="datepicker-dateformat2"
                                            :date-format-options="{ year: 'numeric', month: 'numeric', day: 'numeric' }"
                                            locale="en"
                                    ></b-form-datepicker>
                                </div>
                            </b-row>
                            <b-row>
                                <b-col cols="2" style="text-decoration: underline"><h3>Substrat</h3></b-col>
                                <b-col>
                                    <b-card border-variant="light" title="Drèche"></b-card>
                                </b-col>
                                <b-col>
                                    <b-card border-variant="light" title="Carottes fraîches"></b-card>
                                </b-col>
                                <b-col>
                                    <b-card border-variant="light" title="Poires"></b-card>
                                </b-col>
                            </b-row>
                            <b-row>
                                <b-col cols="2"></b-col>
                                <b-col>
                                    <b-card border-variant="light" title="Pommes"></b-card>
                                </b-col>
                                <b-col>
                                    <b-card border-variant="light" title="Carottes sechées"></b-card>
                                </b-col>
                                <b-col>
                                    <b-card border-variant="light" title="Raisins"></b-card>
                                </b-col>
                            </b-row>
                            <b-row>
                                <b-col cols="2" style="text-decoration: underline"><h3>Matériel</h3></b-col>
                                <b-col>
                                    <b-card border-variant="light" title="Bacs"></b-card>
                                </b-col>
                                <b-col>
                                    <b-card border-variant="light" title="Emballages"></b-card>
                                </b-col>
                                <b-col>
                                </b-col>
                            </b-row>
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
    export default {
        name: "Stock",
        components: {
      //      Sidebar,
        //    Navbar,
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
    #date{
        margin-bottom: 10px;
    }

</style>