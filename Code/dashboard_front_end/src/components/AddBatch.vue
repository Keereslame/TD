<template>
    <div class="submit-form">
        <div v-if="!submitted">
            <div class="form-group">
                <label for="name">Batch name</label>
                <input
                        type="text"
                        class="form-control"
                        id="name"
                        required
                        v-model="batch.name"
                        name="name"
                />
            </div>

            <div class="form-group">
                <label for="nb_bac">Number of boxes</label>
                <input
                        class="form-control"
                        id="nb_bac"
                        required
                        v-model="batch.nb_bac"
                        name="nb_bac"
                />
            </div>

            <div class="form-group">
                <label for="template">Template</label>
                <input
                        class="form-control"
                        id="template"
                        required
                        v-model="batch.template"
                        name="template"
                />
            </div>

            <div class="form-group">
                <label for="date_start">Start day</label>
                <input
                        class="form-control"
                        id="date_start"
                        required
                        v-model="batch.date_start"
                        name="date_start"
                />
            </div>

            <div class="form-group">
                <label for="nb_adult">Number of adults</label>
                <input
                        class="form-control"
                        id="nb_adult"
                        required
                        v-model="batch.nb_adult"
                        name="nb_adult"
                />
            </div>

            <div class="form-group">
                <label for="nb_laying_day">Number of laying days</label>
                <input
                        class="form-control"
                        id="nb_laying_day"
                        required
                        v-model="batch.nb_laying_day"
                        name="nb_laying_day"
                />
            </div>

            <div class="form-group">
                <label for="reproduction_humidity_mass">Humidity mass for reproduction</label>
                <input
                        class="form-control"
                        id="reproduction_humidity_mass"
                        required
                        v-model="batch.reproduction_humidity_mass"
                        name="reproduction_humidity_mass"
                />
            </div>

            <div class="form-group">
                <label for="reproduction_humidity_freq">Humidity frequency for reproduction</label>
                <input
                        class="form-control"
                        id="reproduction_humidity_freq"
                        required
                        v-model="batch.reproduction_humidity_freq"
                        name="reproduction_humidity_freq"
                />
            </div>

            <div class="form-group">
                <label for="reproduction_humidity_type">Humidity type for reproduction</label>
                <input
                        class="form-control"
                        id="reproduction_humidity_type"
                        required
                        v-model="batch.reproduction_humidity_type"
                        name="reproduction_humidity_type"
                />
            </div>

            <div class="form-group">
                <label for="substrat_initial_mass">Initial mass of substrate</label>
                <input
                        class="form-control"
                        id="substrat_initial_mass"
                        required
                        v-model="batch.substrat_initial_mass"
                        name="substrat_initial_mass"
                />
            </div>

            <div class="form-group">
                <label for="substrat_add_mass">Additional mass of substrate</label>
                <input
                        class="form-control"
                        id="substrat_add_mass"
                        required
                        v-model="batch.substrat_add_mass"
                        name="substrat_add_mass"
                />
            </div>

            <div class="form-group">
                <label for="substrat_BSG">Brewery grains</label>
                <input
                        class="form-control"
                        id="substrat_BSG"
                        required
                        v-model="batch.substrat_BSG"
                        name="substrat_BSG"
                />
            </div>

            <div class="form-group">
                <label for="substrat_carrot">Carrot</label>
                <input
                        class="form-control"
                        id="substrat_carrot"
                        required
                        v-model="batch.substrat_carrot"
                        name="substrat_carrot"
                />
            </div>

            <div class="form-group">
                <label for="substrat_apple">Apple</label>
                <input
                        class="form-control"
                        id="substrat_apple"
                        required
                        v-model="batch.substrat_apple"
                        name="substrat_apple"
                />
            </div>

            <div class="form-group">
                <label for="substrat_pear">Pear</label>
                <input
                        class="form-control"
                        id="substrat_pear"
                        required
                        v-model="batch.substrat_pear"
                        name="substrat_pear"
                />
            </div>

            <div class="form-group">
                <label for="substrat_initial_mass">Initial mass of substrate</label>
                <input
                        class="form-control"
                        id="substrat_initial_mass"
                        required
                        v-model="batch.substrat_initial_mass"
                        name="substrat_initial_mass"
                />
            </div>

            <button @click="saveBatch" class="btn btn-success">Submit</button>
        </div>

        <div v-else>
            <h4>You submitted successfully!</h4>
            <button class="btn btn-success" @click="newBatch">Add</button>
        </div>
    </div>
</template>

<script>
    import BatchDataService from "../services/BatchDataService";

    export default {
        name: "add-batch",
        data() {
            return {
                batch: {
                    id: null,
                    name: "",
                    template: "",
                    nb_bac: 0,
                    date_start : "",
                    nb_adult: 0,
                    nb_laying_day: 0,
                    reproduction_humidity_mass: 0,
                    reproduction_humidity_freq: 0,
                    reproduction_humidity_type: "",
                    substrat_initial_mass: 0,
                    substrat_add_mass: 0,
                    substrat_BSG: 0,
                    substrat_carrot: 0,
                    substrat_apple: 0,
                    substrat_pear: 0,
                    substrat_other: 0,
                    other_type: "",
                    growth_humidity_mass: 0,
                    growth_humidity_freq: 0,
                    growth_humidity_type: "",
                    humidity_delay: 0,
                    humidity_total_mass: 0,
                    growth_day: 0,
                    harvest_mealworm_mass: 0,
                    harvest_pupa_nb: 0,
                    harvest_frass_pure: 0,
                    harvest_frass_filtered: ""
                },
                submitted: false
            };
        },
        methods: {
            saveBatch() {
                var data = {
                    name: this.batch.name,
                    template: this.batch.template,
                    nb_bac: this.batch.nb_bac,
                    date_start : this.batch.date_start,
                    nb_adult: this.batch.nb_adult,
                    nb_laying_day: this.batch.nb_laying_day,
                    reproduction_humidity_mass: this.batch.reproduction_humidity_mass,
                    reproduction_humidity_freq: this.batch.reproduction_humidity_freq,
                    reproduction_humidity_type: this.batch.reproduction_humidity_type,
                    substrat_initial_mass: this.batch.substrat_initial_mass,
                    substrat_add_mass: this.batch.substrat_add_mass,
                    substrat_BSG: this.batch.substrat_BSG,
                    substrat_carrot: this.batch.substrat_carrot,
                    substrat_apple: this.batch.substrat_apple,
                    substrat_pear: this.batch.substrat_pear,
                    substrat_other: this.batch.substrat_other,
                    other_type: this.batch.other_type,
                    growth_humidity_mass: this.batch.growth_humidity_mass,
                    growth_humidity_freq: this.batch.growth_humidity_freq,
                    growth_humidity_type: this.batch.growth_humidity_type,
                    humidity_delay: this.batch.humidity_delay,
                    humidity_total_mass: this.batch.humidity_total_mass,
                    growth_day: this.batch.growth_day,
                    harvest_mealworm_mass: this.batch.harvest_mealworm_mass,
                    harvest_pupa_nb: this.batch.harvest_pupa_nb,
                    harvest_frass_pure: this.batch.harvest_frass_pure,
                    harvest_frass_filtered: this.batch.harvest_frass_filtered
                };

                BatchDataService.create(data)
                    .then(response => {
                        this.batch.id = response.data.id;
                        console.log(response.data);
                        this.submitted = true;
                    })
                    .catch(e => {
                        console.log(e);
                    });
            },

            newBatch() {
                this.submitted = false;
                this.batch = {};
            }
        }
    };
</script>

<style>
    .submit-form {
        max-width: 300px;
        margin: auto;
    }
</style>
