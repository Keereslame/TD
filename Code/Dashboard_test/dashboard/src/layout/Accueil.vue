<template>
    <b-container fluid>
        <Navbar/>
        <b-row>
            <b-col class="col-auto sidebar"><Sidebar/></b-col>
            <b-col>
                <div class="mt-3">
                    <b-card-group deck class="mb-3">
                        <b-card border-variant="light" header="Today" class="text-center">

                        </b-card>

                        <b-card border-variant="light" header="Stock" class="text-center">
                            <b-card-group class="mb-3">
                                <b-card border-variant="light" header="Drèches"></b-card>
                                <b-card border-variant="light" header="Carottes"></b-card>
                                <b-card border-variant="light" header="Fruits"></b-card>
                            </b-card-group>                        </b-card>
                    </b-card-group>
                </div>
                <div>
                    <b-card border-variant="light">
                        <template v-slot:header>
                            <b-nav card-header tabs>
                                <b-nav-item>Quantité de vers</b-nav-item>
                                <b-nav-item>Nombre de bacs</b-nav-item>
                                <b-nav-item>Feed / Substrat</b-nav-item>
                                <b-nav-item>Stock de vers</b-nav-item>
                            </b-nav>
                        </template>
                    </b-card>
                </div>
            </b-col>
        </b-row>
    </b-container>
</template>
<script>
    import Navbar from "../components/Navbar";
    import Sidebar from "../components/Sidebar";
    export default {
        name: "Accueil",
        components: {
            Sidebar,
            Navbar,
        }
    }
</script>

<style scoped>
    .col-auto{
        background-color: #96d2d4;
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