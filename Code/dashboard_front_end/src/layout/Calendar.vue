<template>
    <b-container fluid>
        <b-row>
            <b-col>
                <div class="mt-3">
                    <b-card-group deck class="mb-3">
                        <b-card border-variant="light" class="text-center">
                            <b-calendar v-model="value" locale="fr-EU" :date-format-options="{ year: 'numeric', month: 'numeric', day: 'numeric' }"></b-calendar>                        </b-card>

                            <Batch_from_date :value="value"/>
                    </b-card-group>
                </div>
            </b-col>
        </b-row>
    </b-container>
</template>

<script>
    import Batch_from_date from "@/components/data/Batch_from_date";

    export default {
        name: "Calendar",
        components: {
          Batch_from_date
        },
        data() {
            return {
                value: '',
            };
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