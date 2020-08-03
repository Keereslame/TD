<template>
    <b-container fluid>
        <!--<Navbar/>-->
        <b-row>
            <!--<b-col class="col-auto sidebar"><Sidebar/></b-col>-->
            <b-col>
                <div class="mt-3">
                    <b-card-group deck class="mb-3">
                        <b-card border-variant="light" header="Quantité de vers" class="text-center">
                            <Quantity_harvest/>
                        </b-card>

                        <b-card border-variant="light" header="Nombre de batchs" class="text-center">
                            <Quantity_boxes/>
                        </b-card>
                    </b-card-group>
                </div>
            </b-col>
        </b-row>
    </b-container>
</template>

<script>
   // import Navbar from "../components/Navbar";
    //import Sidebar from "../components/Sidebar";
    import Quantity_boxes from "../components/data/Quantity_boxes";
   import Quantity_harvest from "../components/data/Quantity_harvest";
   export default {
        name: "Data",
        components: {
            Quantity_harvest,
            Quantity_boxes
        //    Data_query,
      //      Sidebar,
       //     Navbar,
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