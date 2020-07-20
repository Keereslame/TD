<template>
    <b-container fluid>
        <Navbar/>
        <b-row>
            <b-col class="col-auto sidebar"><Sidebar/></b-col>
            <b-col>
                <b-card-group deck class="mb-3">
                    <b-card>
                        <Temperature_lht65/>
                    </b-card>
                    <b-card>
                        <Humidity_lht65/>
                    </b-card>
                </b-card-group>
                <b-card-group deck class="mb-3">
                    <b-card>
                        <Temperature_amg883/>
                    </b-card>
                    <b-card>
                    </b-card>
                </b-card-group>
            </b-col>
        </b-row>
    </b-container>
</template>

<script>
    import Navbar from "../components/Navbar";
    import Sidebar from "../components/Sidebar";
    import Temperature_lht65 from "../components/Temperature_lht65";
    import Humidity_lht65 from "../components/Humidity_lht65";
    import Temperature_amg883 from "../components/Temperature_amg8833";

    export default {
        name: "Measure",
        components: {
            Temperature_amg883,
            Humidity_lht65,
            Sidebar,
            Navbar,
            Temperature_lht65,
        },
    }
</script>

<style scoped>
    .col-auto{
        background-color: #95ca91;
        padding-right: 0px;
    }

    .container-fluid{
        padding-right: 0px;
        padding-left: 0px;
    }
    .nav-link{
        color: #2c3e50;
    }

    #temp_lht65{
        max-width: 100%;
        height: 300px;
    }

</style>