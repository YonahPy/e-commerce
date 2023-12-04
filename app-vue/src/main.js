
import { createApp } from 'vue'
import { createPinia } from 'pinia'
import { useStore } from './stores/store'
import App from './App.vue'
import router from './router'
import VueAwesomePaginate from "vue-awesome-paginate";
import "vue-awesome-paginate/dist/style.css";


const app = createApp(App)

app.use(createPinia())


async function setup(){
    await useStore().restoreState()
}

app.use(router)
app.use(VueAwesomePaginate)

app.mount('#app')

setup()