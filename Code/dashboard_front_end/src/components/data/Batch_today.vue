<template>
  <b-card border-variant="light" header="Today" class="text-center">
    <h3>Feeding:</h3>
    <li class="list-group-item"
        v-for="(batch, index) in feeding_today"
        :key="index"
    >
      Batch: {{ batch.name }}
    </li>
    <h3>Harvest:</h3>
    <li class="list-group-item"
        v-for="(batch, index) in harvest_today"
        :key="index"
    >
      Batch: {{ batch.name }}
    </li>
  </b-card>
</template>

<script>
  import BatchDataService from "@/services/BatchDataService";

  export default {
    name: "Batch_today",
    data() {
      return {
        batchs: [],
        feeding_today: [],
        harvest_today: [],
        name: ""
      };
    },
    methods: {
      retrieveBatchs() {
        BatchDataService.getAll()
            .then(response => {
              this.batchs = response.data;
              //console.log(response.data);
              this.retrieveTodayBatchs()
            })
            .catch(e => {
              console.log(e);
            });
      },
      retrieveTodayBatchs() {
        this.feeding_today=[];
        this.harvest_today=[];
        var now = new Date();
        var day_to_ms = 8.64*Math.pow(10, 7);
        // console.log(new Date(now));
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

          for(let index=date_start; index<date_end_laying;index = new Date(index.getTime()+this.batchs[i].reproduction_humidity_freq*day_to_ms))
          {
            //console.log(index.getTime());
            if(index.getFullYear() == now.getFullYear() &&
                index.getMonth() == now.getMonth() &&
                index.getDate() == now.getDate())
            {
              this.feeding_today.push(this.batchs[i])
            }
          }

          //console.log("Start growth " + new Date(date_start_growth));
          //console.log("End growth " + new Date(date_end_growth));
          for(let index=date_start_growth; index<date_end_growth;index = new Date(index.getTime() + this.batchs[i].growth_humidity_freq * day_to_ms))
          {
            //console.log("index " + new Date(index));
            if(index.getFullYear() == now.getFullYear() &&
                index.getMonth() == now.getMonth() &&
                index.getDate() == now.getDate())
            {
              this.feeding_today.push(this.batchs[i])
            }
          }
          if(date_end_growth.getFullYear() == now.getFullYear() &&
              date_end_growth.getMonth() == now.getMonth() &&
              date_end_growth.getDate() == now.getDate())
          {
            this.harvest_today.push(this.batchs[i])
          }
        }
        //console.log(this.feeding_today)
      }

    },
    mounted() {
      this.retrieveBatchs();
      setInterval(function(){
        this.retrieveTodayBatchs()
      }.bind(this), 300000)
    }
  }
</script>

<style scoped>
.card-header{
  background-color: lightcoral;
  text-align: left;
}
</style>