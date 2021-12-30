import Vue from 'vue'
import Vuex from 'vuex'
import {getAPI} from "@/axios-api";

Vue.use(Vuex)

export default new Vuex.Store({
    state: {
        access: '',
        refresh: '',
    },
    mutations: {
       initializeStore(state) {
           if (localStorage.getItem('access')) {
               state.access = localStorage.getItem('access')
               state.refresh = localStorage.getItem('refresh')
           } else {
               state.access = ''
               state.refresh = ''
           }
       },

        setAccess(state, access) {
           state.access = access;
        },

        setRefresh(state, refresh) {
           state.refresh = refresh
        }

    },
    actions: {
        // userLogout(context) {
        //     if (context.getters.loggedIn) {
        //         context.commit('destroyToken')
        //     }
        // },
        userLogin(context, credentials) {
            return new Promise((resolve, reject) => {
                getAPI.post('/api-token/', {
                    email: credentials.email,
                    password: credentials.password
                })
                    .then(response => {
                        context.commit('updateStorage', {access: response.data.access, refresh: response.data.refresh})
                        console.log('Getting token succeeded with: ', response.data.access)
                        resolve()
                    })
                    .catch(err => {
                        console.log('Getting token failed with: ', err)
                        reject(err)
                    })
            })
        }
    },
    modules: {},
    getters: {
        loggedIn(state) {
            return state.accessToken != null
        }
    }
})
