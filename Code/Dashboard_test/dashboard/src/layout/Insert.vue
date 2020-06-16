<template>
    <b-container fluid>
        <Navbar/>
        <b-row>
            <b-col class="col-auto sidebar"><Sidebar/></b-col>
            <b-col>
            </b-col>
        </b-row>
    </b-container>
</template>

<script>
    import Navbar from "../components/Navbar";
    import Sidebar from "../components/Sidebar";

    export default {
        name: "Insert",
        components: {
            Sidebar,
            Navbar,
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