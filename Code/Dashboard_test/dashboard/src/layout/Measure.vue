<template>
    <b-container fluid>
        <Navbar/>
        <b-row>
            <b-col class="col-auto sidebar"><Sidebar/></b-col>
            <b-col>
                <b-card-group deck class="mb-3">
                    <Temperature_lht65/>
                    <Humidity_lht65/>
                    <Temperature_amg883/>
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

</style>