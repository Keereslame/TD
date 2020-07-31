<template>
    <highcharts class="stock" :constructor-typ="'stockChart'" :options="stockOptions"></highcharts>
</template>

<script>
    export default {
        name: "column_graph",
        props:[
            'dataSeries'
        ],
        data(){
            return{
                categoriesXAxis: [],
                stockOptions:{
                    chart: {
                        type: 'column',
                        alignTicks: false
                    },
                    rangeSelector: {
                        selected: 1
                    },
                    title:{
                      text: ''
                    },
                    xAxis: {
                        categories: this.updateCategories(),
                        crosshair: true
                    },
                    series: this.dataSeries
                }
            }
        },
        methods:{
          getMonthValue(value){
              switch(value){
                  case 0:
                      return 'January'
                  case 1:
                      return 'February'
                  case 2:
                      return 'March'
                  case 3:
                      return 'April'
                  case 4:
                      return 'May'
                  case 5:
                      return 'June'
                  case 6:
                      return 'July'
                  case 7:
                      return 'August'
                  case 8:
                      return 'September'
                  case 9:
                      return 'October'
                  case 10:
                      return 'November'
                  case 11:
                      return 'December'
              }
          } ,
          updateCategories(){
              return [this.getMonthValue(new Date().getMonth()-5),
                  this.getMonthValue(new Date().getMonth()-4),
                  this.getMonthValue(new Date().getMonth()-3),
                  this.getMonthValue(new Date().getMonth()-2),
                  this.getMonthValue(new Date().getMonth()-1),
                  this.getMonthValue(new Date().getMonth())]
          }
        },
        watch:{
            dataSeries(newSeries){
                this.stockOptions.series = newSeries
    }
        }
    }
</script>

<style scoped>

</style>