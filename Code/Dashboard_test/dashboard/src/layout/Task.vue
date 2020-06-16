<template>
    <b-container fluid>
        <Navbar/>
        <b-row>
            <b-col class="col-auto sidebar"><Sidebar/></b-col>
            <b-col>
                <div class="mt-3">
                    <b-card-group deck class="mb-3">
                        <b-card border-variant="light" header="Task of the day" class="text-center">
                            <b-card-group class="mb-3">
                                <b-card border-variant="light" title="Feed">
                                    <div>
                                        <b-table striped hover :items="items_tab1"></b-table>
                                    </div>
                                </b-card>
                                <b-card border-variant="light" title="Reproduction">
                                    <b-table striped hover :items="items_tab2_1"></b-table>
                                    <b-table striped hover :items="items_tab2_2"></b-table>
                                </b-card>
                                <b-card border-variant="light" title="Harvest">
                                    Quantity:
                                    <div>
                                        <b-input-group class="mt-3">
                                            <b-form-input></b-form-input>
                                            <b-input-group-append>
                                                <b-button variant="secondary">Add</b-button>
                                            </b-input-group-append>
                                        </b-input-group>
                                    </div>
                                </b-card>
                            </b-card-group>
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
        name: "Task",
        components: {
            Sidebar,
            Navbar,
        },
        data() {
            return {
                items_tab1: [
                    { Batch: 'G2.A', Carottes : '0.3'},
                    { Batch: 'G2.B', Carottes: '0.3'},
                    { Batch: 'G2.C', Carottes: '0.3'},
                    { Batch: 'G2.D', Carottes: '0.3'}
                ],
                items_tab2_1: [
                    { Substrat: 30, Type: 'Drèche'},
                    { Substrat: 25, Type: 'Pomme'},
                    { Substrat: 25, Type: 'Poire'},
                    { Substrat: 20, Type: '...'}
                ],
                items_tab2_2: [
                    { Batch: 'G2.A', Substrat: '3', Adult: '1700' },
                    { Batch: 'G2.B', Substrat: '3', Adult: '1700' },
                    { Batch: 'G2.C', Substrat: '3', Adult: '1700' },
                    { Batch: 'G2.D', Substrat: '3', Adult: '...' }
                ]
            }
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