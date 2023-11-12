
import { createApp } from 'vue'
import { createPinia } from 'pinia'
import { useStore } from './stores/store'
import App from './App.vue'
import router from './router'

const app = createApp(App)

app.use(createPinia())


async function setup(){
    await useStore().restoreState()
}

app.use(router)
app.mount('#app')

setup()