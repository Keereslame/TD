<template>
    <div class="list row">
        <div class="col-md-8">
            <div class="input-group mb-3">
                <input type="text" class="form-control" placeholder="Search by name"
                       v-model="name"/>
                <div class="input-group-append">
                    <button class="btn btn-outline-secondary" type="button"
                            @click="searchName"
                    >
                        Search
                    </button>
                </div>
            </div>
        </div>
        <div class="col-md-6">
            <h4>Batchs List</h4>
            <ul class="list-group">
                <li class="list-group-item"
                    :class="{ active: index == currentIndex }"
                    v-for="(batch, index) in batchs"
                    :key="index"
                    @click="setActiveBatch(batch, index)"
                >
                    {{ batch.name }}
                </li>
            </ul>

            <button class="m-3 btn btn-sm btn-danger" @click="removeAllBatchs">
                Remove All
            </button>
        </div>
        <div class="col-md-6">
            <div v-if="currentBatch">
                <h4>Batch</h4>
                <div>
                    <label><strong>Name:</strong></label> {{ currentBatch.name }}
                </div>
                <div>
                    <label><strong>Number of boxes:</strong></label> {{ currentBatch.nb_bac }}
                </div>
                <div>
                    <label><strong>Template:</strong></label> {{ currentBatch.template }}
                </div>
                <div>
                    <label><strong>Start date:</strong></label> {{ currentBatch.date_start }}
                </div>
                <div>
                    <label><strong>Number of adults:</strong></label> {{ currentBatch.nb_adult }}
                </div>
                <div>
                    <label><strong>Number of laying days:</strong></label> {{ currentBatch.nb_laying_day }}
                </div>
                <div>
                    <label><strong>Humidity mass in reproduction:</strong></label> {{ currentBatch.reproduction_humidity_mass }}
                </div>
                <div>
                    <label><strong>Humidity frequency in reproduction:</strong></label> {{ currentBatch.reproduction_humidity_freq }}
                </div>
                <div>
                    <label><strong>Humidity type in reproduction:</strong></label> {{ currentBatch.reproduction_humidity_type }}
                </div>
                <div>
                    <label><strong>Initial mass of substrate:</strong></label> {{ currentBatch.substrat_initial_mass }}
                </div>
                <div>
                    <label><strong>Additional mass of substrate:</strong></label> {{ currentBatch.substrat_add_mass }}
                </div>
                <div>
                    <label><strong>Quantity of brewery grains in substrate:</strong></label> {{ currentBatch.substrat_BSG }}
                </div>
                <div>
                    <label><strong>Quantity of carrot in substrate:</strong></label> {{ currentBatch.substrat_carrot }}
                </div>
                <div>
                    <label><strong>Quantity of apple in substrate:</strong></label> {{ currentBatch.substrat_apple }}
                </div>
                <div>
                    <label><strong>Quantity of pear in substrate:</strong></label> {{ currentBatch.substrat_pear }}
                </div>
                <div>
                    <label><strong>Quantity of other in substrate:</strong></label> {{ currentBatch.substrat_other }}
                </div>
                <div>
                    <label><strong>Type of other in substrate:</strong></label> {{ currentBatch.other_type }}
                </div>
                <div>
                    <label><strong>Humidity mass during growth:</strong></label> {{ currentBatch.growth_humidity_mass }}
                </div>
                <div>
                    <label><strong>Humidity frequency during growth:</strong></label> {{ currentBatch.growth_humidity_freq }}
                </div>
                <div>
                    <label><strong>Humidity type during growth:</strong></label> {{ currentBatch.growth_humidity_type }}
                </div>
                <div>
                    <label><strong>Humidity delay during growth:</strong></label> {{ currentBatch.humidity_delay }}
                </div>
                <div>
                    <label><strong>Humidity total mass:</strong></label> {{ currentBatch.humidity_total_mass }}
                </div>
                <div>
                    <label><strong>Growth day:</strong></label> {{ currentBatch.growth_day }}
                </div>
                <div>
                    <label><strong>Harvest mealworm mass:</strong></label> {{ currentBatch.harvest_mealworm_mass }}
                </div>
                <div>
                    <label><strong>Harvest pupa number:</strong></label> {{ currentBatch.harvest_pupa_nb }}
                </div>
                <div>
                    <label><strong>Harvest frass pure:</strong></label> {{ currentBatch.harvest_frass_pure }}
                </div>
                <div>
                    <label><strong>Harvest frass filtered:</strong></label> {{ currentBatch.harvest_frass_filtered }}
                </div>
                <a class="badge badge-warning"
                   :href="'/batchs/' + currentBatch.id"
                >
                    Edit
                </a>
            </div>
            <div v-else>
                <br />
                <p>Please click on a Batch...</p>
            </div>
        </div>
    </div>
</template>

<script>
    import BatchDataService from "../services/BatchDataService";

    export default {
        name: "batchs-list",
        data() {
            return {
                batchs: [],
                currentBatch: null,
                currentIndex: -1,
                name: ""
            };
        },
        methods: {
            retrieveBatchs() {
                BatchDataService.getAll()
                    .then(response => {
                        this.batchs = response.data;
                        console.log(response.data);
                    })
                    .catch(e => {
                        console.log(e);
                    });
            },

            refreshList() {
                this.retrieveBatchs();
                this.currentBatch = null;
                this.currentIndex = -1;
            },

            setActiveBatch(batch, index) {
                this.currentBatch = batch;
                this.currentIndex = index;
            },

            removeAllBatchs() {
                BatchDataService.deleteAll()
                    .then(response => {
                        console.log(response.data);
                        this.refreshList();
                    })
                    .catch(e => {
                        console.log(e);
                    });
            },

            searchName() {
                BatchDataService.findByName(this.name)
                    .then(response => {
                        this.batchs = response.data;
                        console.log(response.data);
                    })
                    .catch(e => {
                        console.log(e);
                    });
            }
        },
        mounted() {
            this.retrieveBatchs();
        }
    };
</script>

<style>
    .list {
        text-align: left;
        max-width: 750px;
        margin: auto;
    }
</style>
