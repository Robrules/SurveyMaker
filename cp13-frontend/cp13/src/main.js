// import Vue from 'vue'
// import App from './App.vue'
// import router from './router'
// import i18n from './i18n'

// Vue.config.productionTip = false
// document.documentElement.lang = i18n.locale

// new Vue({
//   i18n,
//   router,
//   render: h => h(App)
// }).$mount('#app')

import Vue from 'vue'
import App from './App.vue'
import axios from 'axios'
import vueRouter from 'vue-router'
import router from './router'
import i18n from './i18n'
import VueSweetalert2 from 'vue-sweetalert2';
import 'sweetalert2/dist/sweetalert2.min.css';
import { library } from '@fortawesome/fontawesome-svg-core'
import { fas } from '@fortawesome/free-solid-svg-icons'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'

Vue.config.productionTip = false
Vue.prototype.$axios = axios
Vue.use(vueRouter)
Vue.use(VueSweetalert2);
library.add(fas)
Vue.component('font-awesome-icon', FontAwesomeIcon)

// axios.defaults.baseURL = 'http://35.220.143.92:8888/';
// axios.defaults.baseURL = 'http://localhost:8000/';
axios.defaults.baseURL = 'https://cp13demoapi.piran.xyz/';
const lang = localStorage.getItem('lang') || 'en';
axios.defaults.headers['Accept-Language'] = lang;

new Vue({
  i18n,
  render: h => h(App),
  router:router,
  beforeCreate() {
    Vue.prototype.$bus = this
  }
}).$mount('#app')
