<template>
  <v-hover v-slot="{ hover }" open-delay="200">
    <v-card color="orange-light" :elevation="hover ? 16 : 2">
      <v-row>
        <v-col cols="12" sm="12">
          <v-list-item three-line>
            <v-list-item-content class="text-center">
              <v-list-item-title class="headline mb-1 purple--text">
                <h3>{{ total.toLocaleString() }} Rwf</h3>
              </v-list-item-title>
              <v-list-item-subtitle class="grey--text">
                <div>
                  <span>{{ currentDateTime() }} - Now</span> <br>
                </div>
              </v-list-item-subtitle>
            </v-list-item-content>
          </v-list-item>
        </v-col>
      </v-row>
    </v-card>
  </v-hover>
</template>

<script>
import axios from "axios";

export default {
  name: "IncomeVsExpense",
  data() {
    return {
      total_income: [],
      total: null,
    }
  },

  mounted() {
    axios.get("/auth/users/me")
        .then(response => {
          console.log('CurrentUser Data.', response)
          this.user_data = response.data
          this.getIncomeByUser(this.user_data['id'])
        })
        .catch(error => {
          console.log("Couldn't get current user: ", error)
        })
  },

  computed: {},
  methods: {
    getIncomeByUser(userId) {
      axios.get(`/api/income/by/${userId}`)
          .then(response => {
            this.total_income = response.data
            let total = 0
            for (let i = 0; i <= this.total_income.length; i++) {
              total += this.total_income[i].amount
              console.log("Income of user ( " + userId + ")", total)
              this.total = total
            }
          }).catch(error => {
        console.log("Couldn't get this user's Income", error)
      })
    },
    currentDateTime() {
      const current = new Date();
      const date = current.getFullYear()+'-'+(current.getMonth()+1)+'-'+current.getDate();
      // const time = current.getHours() + ":" + current.getMinutes() + ":" + current.getSeconds();
      return date
    },
  }
}
</script>

<style scoped>

</style>