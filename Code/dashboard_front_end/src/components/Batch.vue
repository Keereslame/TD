<template>
    <div v-if="currentBatch" class="edit-form">
        <h4>Batch</h4>
        <form>
            <div class="form-group">
                <label for="name">Name</label>
                <input type="text" class="form-control" id="name"
                       v-model="currentBatch.name"
                />
            </div>
            <div class="form-group">
                <label for="template">Template</label>
                <input type="text" class="form-control" id="template"
                       v-model="currentBatch.template"
                />
            </div>

            <div class="form-group">
                <label for="nb_bac">Number of boxes</label>
                <input type="text" class="form-control" id="nb_bac"
                       v-model="currentBatch.nb_bac"
                />
            </div>
            <div class="form-group">
                <label for="date_start">Start date</label>
                <input type="text" class="form-control" id="date_start"
                       v-model="currentBatch.date_start"
                />
            </div>
            <div class="form-group">
                <label for="nb_adult">Number of adults</label>
                <input type="text" class="form-control" id="nb_adult"
                       v-model="currentBatch.nb_adult"
                />
            </div>
            <div class="form-group">
                <label for="nb_laying_day">Number of laying day</label>
                <input type="text" class="form-control" id="nb_laying_day"
                       v-model="currentBatch.nb_laying_day"
                />
            </div>
            <div class="form-group">
                <label for="reproduction_humidity_mass">Humidity mass for reproduction</label>
                <input type="text" class="form-control" id="reproduction_humidity_mass"
                       v-model="currentBatch.reproduction_humidity_mass"
                />
            </div>
            <div class="form-group">
                <label for="reproduction_humidity_freq">Humidity frequency for reproduction</label>
                <input type="text" class="form-control" id="reproduction_humidity_freq"
                       v-model="currentBatch.reproduction_humidity_freq"
                />
            </div>
            <div class="form-group">
                <label for="reproduction_humidity_type">Humidity type for reproduction</label>
                <input type="text" class="form-control" id="reproduction_humidity_type"
                       v-model="currentBatch.reproduction_humidity_type"
                />
            </div>
            <div class="form-group">
                <label for="substrat_initial_mass">Initial mass of substrate</label>
                <input type="text" class="form-control" id="substrat_initial_mass"
                       v-model="currentBatch.substrat_initial_mass"
                />
            </div>
            <div class="form-group">
                <label for="substrat_add_mass">Additional mass of substrate</label>
                <input type="text" class="form-control" id="substrat_add_mass"
                       v-model="currentBatch.substrat_add_mass"
                />
            </div>
            <div class="form-group">
                <label for="substrat_BSG">Brewer grains mass of substrate</label>
                <input type="text" class="form-control" id="substrat_BSG"
                       v-model="currentBatch.substrat_BSG"
                />
            </div>
            <div class="form-group">
                <label for="substrat_carrot">Carrot mass of substrate</label>
                <input type="text" class="form-control" id="substrat_carrot"
                       v-model="currentBatch.substrat_carrot"
                />
            </div>
            <div class="form-group">
                <label for="substrat_apple">Apple mass of substrate</label>
                <input type="text" class="form-control" id="substrat_apple"
                       v-model="currentBatch.substrat_apple"
                />
            </div>
            <div class="form-group">
                <label for="substrat_pear">Pear mass of substrate</label>
                <input type="text" class="form-control" id="substrat_pear"
                       v-model="currentBatch.substrat_pear"
                />
            </div>
            <div class="form-group">
                <label for="substrat_other">Other mass of substrate</label>
                <input type="text" class="form-control" id="substrat_other"
                       v-model="currentBatch.substrat_other"
                />
            </div>
            <div class="form-group">
                <label for="other_type">Other type in substrate</label>
                <input type="text" class="form-control" id="other_type"
                       v-model="currentBatch.other_type"
                />
            </div>
            <div class="form-group">
                <label for="growth_humidity_mass">Humidity mass during growth</label>
                <input type="text" class="form-control" id="growth_humidity_mass"
                       v-model="currentBatch.growth_humidity_mass"
                />
            </div>
            <div class="form-group">
                <label for="growth_humidity_freq">Humidity frequency during growth</label>
                <input type="text" class="form-control" id="growth_humidity_freq"
                       v-model="currentBatch.growth_humidity_freq"
                />
            </div>
            <div class="form-group">
                <label for="growth_humidity_type">Humidity type during growth</label>
                <input type="text" class="form-control" id="growth_humidity_type"
                       v-model="currentBatch.growth_humidity_type"
                />
            </div>
            <div class="form-group">
                <label for="humidity_delay">Humidity delay</label>
                <input type="text" class="form-control" id="humidity_delay"
                       v-model="currentBatch.humidity_delay"
                />
            </div>
            <div class="form-group">
                <label for="humidity_total_mass">Humidity total mass</label>
                <input type="text" class="form-control" id="humidity_total_mass"
                       v-model="currentBatch.humidity_total_mass"
                />
            </div>
            <div class="form-group">
                <label for="growth_day">Growth day</label>
                <input type="text" class="form-control" id="growth_day"
                       v-model="currentBatch.growth_day"
                />
            </div>
            <div class="form-group">
                <label for="harvest_mealworm_mass">Harvest mealworm mass</label>
                <input type="text" class="form-control" id="harvest_mealworm_mass"
                       v-model="currentBatch.harvest_mealworm_mass"
                />
            </div>
            <div class="form-group">
                <label for="harvest_pupa_nb">Harvest pupa number</label>
                <input type="text" class="form-control" id="harvest_pupa_nb"
                       v-model="currentBatch.harvest_pupa_nb"
                />
            </div>
            <div class="form-group">
                <label for="harvest_frass_pure">Harvest frass pure</label>
                <input type="text" class="form-control" id="harvest_frass_pure"
                       v-model="currentBatch.harvest_frass_pure"
                />
            </div>
            <div class="form-group">
                <label for="harvest_frass_filtered">Harvest frass filtered</label>
                <input type="text" class="form-control" id="harvest_frass_filtered"
                       v-model="currentBatch.harvest_frass_filtered"
                />
            </div>
        </form>


        <button class="badge badge-danger mr-2"
                @click="deleteBatch"
        >
            Delete
        </button>

        <button type="submit" class="badge badge-success"
                @click="updateBatch"
        >
            Update
        </button>
        <p>{{ message }}</p>
    </div>

    <div v-else>
        <br />
        <p>Please click on a Batch...</p>
    </div>
</template>

<script>
    import BatchDataService from "../services/BatchDataService";

    export default {
        name: "Batch",
        data() {
            return {
                currentBatch: null,
                message: ''
            };
        },
        methods: {
            getBatch(id) {
                BatchDataService.get(id)
                    .then(response => {
                        this.currentBatch = response.data;
                        console.log(response.data);
                    })
                    .catch(e => {
                        console.log(e);
                    });
            },

            updateBatch() {
                BatchDataService.update(this.currentBatch.id, this.currentBatch)
                    .then(response => {
                        console.log(response.data);
                        this.message = 'The Batch was updated successfully!';
                    })
                    .catch(e => {
                        console.log(e);
                    });
            },

            deleteBatch() {
                BatchDataService.delete(this.currentBatch.id)
                    .then(response => {
                        console.log(response.data);
                        this.$router.push({ name: "Batchs" });
                    })
                    .catch(e => {
                        console.log(e);
                    });
            }
        },
        mounted() {
            this.message = '';
            this.getBatch(this.$route.params.id);
        }
    };
</script>

<style>
    .edit-form {
        max-width: 300px;
        margin: auto;
    }
</style>
