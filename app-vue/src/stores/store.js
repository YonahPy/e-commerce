import {defineStore} from 'pinia'

const STORAGE_KEY = 'app-vue';

export const useStore = defineStore({
    id: 'main',
    state: () => ({
        currentCategory: '',
        idCurrentCategory: null
    }),
    actions:{
        setCategory(name, id){
            this.currentCategory = name;
            this.idCurrentCategory = id;
            this.persistState();
        },
        persistState(){
            localStorage.setItem(STORAGE_KEY, JSON.stringify(this.$state));
        },
        restoreState(){
            const savedState = localStorage.getItem(STORAGE_KEY);
            if(savedState){
                Object.assign(this.$state, JSON.parse(savedState));
            }
        },
    },
   
});