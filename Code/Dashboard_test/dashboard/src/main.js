import Vue from 'vue'
import App from './App.vue'
import router from "./routes/routes";
import {BootstrapVue, BootstrapVueIcons} from 'bootstrap-vue'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
import HighchartsVue from 'highcharts-vue'

Vue.config.productionTip = false
Vue.use(BootstrapVue)
Vue.use(BootstrapVueIcons)
Vue.use(HighchartsVue)

new Vue({
  router: router,
  render: h => h(App),
}).$mount('#app')

var mongoose = require('mongoose')
mongoose.connection('mongodb://localhost/lowimpact_food').then(res => console.log(res))