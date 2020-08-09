<template>
    <div class="container-fluid">
        <b-card-group deck>
          <Batch_today/>
        </b-card-group>
        <b-card border-variant="light">
          <Card_last_value/>
        </b-card>
    </div>
</template>
<script>
    import Card_last_value from "../components/Sensors/Card_last_value";
    import Batch_today from "@/components/data/Batch_today";

    export default {
        name: "Accueil",
        components: {
          Batch_today,
          Card_last_value
        },

    }
</script>

<style scoped>
    .col-auto{
        background-color: #96d2d4;
        padding-right: 0px;
    }
    .container-fluid{
        margin-left: auto;
        margin-right: auto;

    }
    .nav-link{
        color: #2c3e50;
    }

</style>