<template>
    <b-container fluid>
        <Navbar/>
        <b-row>
            <b-col class="col-auto sidebar"><Sidebar/></b-col>
            <b-col>
                <div>
                    <b-card-group>
                        <b-card border-variant="light" header="Create template" class="text-left">
                            <b-form-input v-model="template" placeholder="Name of template"></b-form-input>
                            <h2>During reproduction</h2>
                            <label>Adult mass</label>
                            <b-form-input v-model="adult_mass" :type="'number'"></b-form-input>
                            <label>Number of laying days</label>
                            <b-form-input v-model="nb_laying_days" :type="'number'"></b-form-input>
                            <label>Humidity input frequency</label>
                            <b-form-input v-model="reproduction_hum_input_frequency" :type="'number'"></b-form-input>
                            <label>Humidity input type</label>
                            <b-form-input v-model="reproduction_hum_input_type" placeholder="Humidity input type"></b-form-input>
                            <label>Humidity input amount</label>
                            <b-form-input v-model="reproduction_hum_input_amount" :type="'number'"></b-form-input>
                            <h2>During the growth</h2>
                            <label>Number of growing days</label>
                            <b-form-input v-model="nb_growing_days" :type="'number'"></b-form-input>
                            <label>Delay to give humidity</label>
                            <b-form-input v-model="delay_hum_days" :type="'number'"></b-form-input>
                            <label>Humidity input frequency</label>
                            <b-form-input v-model="reproduction_hum_input_frequency" :type="'number'"></b-form-input>
                            <label>Humidity input type</label>
                            <b-form-input v-model="reproduction_hum_input_type" placeholder="Humidity input type"></b-form-input>
                            <label>Humidity input amount</label>
                            <b-form-input v-model="reproduction_hum_input_amount" :type="'number'"></b-form-input>
                            <h2>Substrat</h2>
                            <label>Spent brewery grains</label>
                            <b-form-input v-model="spent_brewery_grains" :type="'number'"></b-form-input>
                            <label>Apples</label>
                            <b-form-input v-model="apples" :type="'number'"></b-form-input>
                            <label>Pears</label>
                            <b-form-input v-model="pears" :type="'number'"></b-form-input>
                            <label>Carrots</label>
                            <b-form-input v-model="carrots" :type="'number'"></b-form-input>
                            <label>Other</label>
                            <b-form-input v-model="other" :type="'number'"></b-form-input>
                            <label>Other type</label>
                            <b-form-input v-model="other_type" placeholder="Other type"></b-form-input>
                            <button type="submit" class="btn btn-primary">Submit</button>
                        </b-card>
                        <b-card border-variant="light" header="Create batch" class="text-left">
                            <b-form-input v-model="batchName" placeholder="Name of the batch"></b-form-input>
                            <label>Choose template</label>
                            <b-form-select v-model="templateName" :options="options_template"></b-form-select>
                            <label>Number of bins</label>
                            <b-form-input v-model="nb_box" :type="'number'" placeholder="Number of bins"></b-form-input>
                            <label>Date of creation</label>
                            <b-form-input v-model="date_init" :type="'date'" ></b-form-input>
                            <label>Date of harvest</label>
                            <b-form-input v-model="date_end" :type="'date'" ></b-form-input>
                            <button type="submit" class="btn btn-primary">Submit</button>
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
        name: "Insert",
        components: {
            Sidebar,
            Navbar,
        },
        data(){
            return {
                template:'',
                spent_brewery_grains:0,
                apples:0,
                pears:0,
                carrots:0,
                other:0,
                other_type:'',
                adult_mass:0,
                nb_laying_days:0,
                nb_box: 0,
                date_init:null,
                date_end:null,
                reproduction_hum_input_frequency: 0,
                reproduction_hum_input_type: '',
                reproduction_hum_input_amount: 0,
                nb_growing_days:0,
                delay_hum_days:0,
                batchName: '',
                templateName: null,
                options_template:[
                    {value: null, text: 'Please select an option'},
                    {value: 'a', text: 'Production template'},
                    {value: 'b', text: 'R&D template'}
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