<template>
  <b-card border-variant="light" header="Task" class="text-center">
    <b-row>
      <p>Date: <b>{{ date }}</b></p>
    </b-row>
    <b-row>
      <h4>Feeding during reproduction</h4>
    </b-row>
    <b-row>
      <li class="list-group-item"
          v-for="(batch, index) in reproduction_feeding_today"
          :key="index"
      >
        Batch:{{ batch.name }},
        quantity:{{ batch.reproduction_humidity_mass }},
        type: {{ batch.reproduction_humidity_type }}
      </li>
    </b-row>
    <b-row>
      <h4>Feeding during growth</h4>
    </b-row>
    <b-row>
      <li class="list-group-item"
          v-for="(batch, index) in growth_feeding_today"
          :key="index"
      >
        Batch:{{ batch.name }},
        quantity:{{ batch.growth_humidity_mass }},
        type: {{ batch.growth_humidity_type }}
      </li>
    </b-row>
    <b-row>
      <h4>Harvest</h4>
    </b-row>
    <b-row>
      <li class="list-group-item"
          v-for="(batch, index) in harvest_today"
          :key="index"
      >
        {{ batch.name }}
      </li>
    </b-row>
  </b-card>

</template>

<script>
  import BatchDataService from "@/services/BatchDataService";

  export default {
    name: "batch_from_date",
    props: [
        'value'
    ],
    data(){
      return {
        date: this.value,
        batchs: [],
        reproduction_feeding_today: [],
        growth_feeding_today: [],
        harvest_today: [],
        name: ""
      }
    },
    methods: {
      retrieveBatchs() {
        BatchDataService.getAll()
            .then(response => {
              this.batchs = response.data;
              //console.log(response.data);
            })
            .catch(e => {
              console.log(e);
            });
      },
      retrieveTodayBatchs() {
        this.reproduction_feeding_today = [];
        this.growth_feeding_today = [];
        this.harvest_today = [];
        //console.log(new Date(this.value))
        var day_to_ms = 8.64*Math.pow(10, 7);
        for(var i in this.batchs){
          //console.log("Batch: " + this.batchs[i].name);
          var date_start = new Date(this.batchs[i].date_start);
          //console.log("Date start: " + date_start);
          var date_end_laying = new Date(date_start.getTime()+this.batchs[i].nb_laying_day*day_to_ms);
          //console.log("Date end laying: " + date_end_laying);
          var date_start_growth = new Date(date_end_laying.getTime()+this.batchs[i].humidity_delay*day_to_ms);
          //console.log("Date start growth: ");
          //console.log(new Date(date_start_growth));
          var date_end_growth = new Date(date_start_growth.getTime() + this.batchs[i].growth_day*day_to_ms);
          //console.log(this.batchs[i].growth_day)
          //console.log("Date end growth: ");
          //console.log(new Date(date_end_growth));

          for(let index=date_start; index<date_end_laying;index = new Date(index.getTime()+this.batchs[i].reproduction_humidity_freq*day_to_ms))//index+=this.batchs[i].reproduction_humidity_freq)
          {
            //console.log(index.getTime());
            //console.log(new Date(this.value).getTime())
            if(index.getTime() == new Date(this.value).getTime())
            {
              this.reproduction_feeding_today.push(this.batchs[i])
              //console.log("Reproduction feeding date")
            }
          }


          //console.log("Start growth " + new Date(date_start_growth));
          //console.log("End growth " + new Date(date_end_growth));
          for(let index=date_start_growth; index<date_end_growth;index = new Date(index.getTime() + this.batchs[i].growth_humidity_freq * day_to_ms))//index+=this.batchs[i].growth_humidity_freq)
          {
            if(date_end_growth>new Date()) {
              //console.log("index " + new Date(index));
              if (index.getTime() == new Date(this.value).getTime()) {
                this.growth_feeding_today.push(this.batchs[i])
                //console.log("Growth feeding date")
              }
            }
          }
          //console.log(date_end_growth)
          if(date_end_growth.getTime() == new Date(this.value).getTime())
          {
            this.harvest_today.push(this.batchs[i])
            //console.log("Harvest date")
          }
        }
        //console.log(this.feeding_today)
      }

    },
    mounted() {
      this.retrieveBatchs();
    },
    watch: {
      value(newValue){
        this.date = newValue
        this.retrieveTodayBatchs()
      }
    },
  }
</script>

<style scoped>
.card-header{
  background-color: lightcoral;
  text-align: left;
}

</style>